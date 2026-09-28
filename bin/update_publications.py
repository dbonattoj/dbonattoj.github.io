#!/usr/bin/env python3
"""Sync the Google Scholar profile into _bibliography/papers.bib and _data/citations.yml.

- Fetches every page of the profile's publication list (HTML, no API key).
- Merges into the existing papers.bib:
    * new papers are appended (as @misc entries with a google_scholar_id field)
    * papers already in the file are only updated when fetched data changed
      (year, venue, authors, or a missing/changed google_scholar_id); all other
      fields (doi, url, selected, comments, ...) are preserved untouched
    * entries present only in the file are never removed
- Writes _data/citations.yml (format expected by al-folio's al_citations badge
  lookup: papers keyed by scholar paper id with title/year/citations).
- Re-running with nothing changed leaves both files byte-identical.

Usage:
    python3 bin/update_publications.py            # update files in place
    python3 bin/update_publications.py --dry-run  # show what would change
"""

import difflib
import re
import sys
import time
import urllib.request
from datetime import date
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

REPO = Path(__file__).resolve().parent.parent
BIB_PATH = REPO / "_bibliography" / "papers.bib"
CITATIONS_PATH = REPO / "_data" / "citations.yml"
SOCIALS_PATH = REPO / "_data" / "socials.yml"

PROFILE_URL = (
    "https://scholar.google.com/citations?user={uid}&hl=en"
    "&sortby=year&view_doc=list&cstart={start}"
)
PAGE_SIZE = 20
REQUEST_DELAY_S = 1.5
TIMEOUT_S = 30
USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"
)
TITLE_MIN_LEN = 15  # shorter anchor texts are "all versions" links, not titles

STOPWORDS = {
    "a", "an", "the", "and", "or", "of", "on", "in", "for", "to", "from",
    "with", "via", "towards", "using", "based", "toward", "study", "part",
}


def load_scholar_userid() -> str:
    config = yaml.safe_load(SOCIALS_PATH.read_text())
    uid = config.get("scholar_userid")
    if not uid:
        sys.exit(f"error: scholar_userid missing from {SOCIALS_PATH}")
    return uid


def fetch(url: str) -> str:
    last_err = None
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=TIMEOUT_S) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:  # noqa: BLE001 - report and retry
            last_err = e
            time.sleep(2 * (attempt + 1))
    sys.exit(f"error: failed to fetch {url}: {last_err}")


def parse_page(html: str):
    """Return (papers, row_count) from one profile-listing page.

    row_count is the number of paper rows Scholar served (20 per page); the
    fetched list may be shorter if some rows are filtered, so pagination must
    stop on row_count, not on len(papers).
    """
    if "unusual traffic" in html.lower() or "detected unusual" in html.lower():
        sys.exit(
            "error: Google returned a CAPTCHA/blocked page.\n"
            "        Try again later, or run this script from a residential "
            "connection (see README)."
        )
    soup = BeautifulSoup(html, "html.parser")
    papers = []
    seen = set()
    rows = 0
    for tr in soup.find_all("tr", class_="gsc_a_tr"):
        rows += 1
        anchor = tr.select_one("a.gsc_a_at")
        if anchor is None:
            continue
        title = anchor.get_text(" ", strip=True).replace("\xa0", " ")
        if len(title) < TITLE_MIN_LEN:
            continue
        m = re.search(r"citation_for_view=[^:]*:([^&]+)", anchor.get("href") or "")
        scholar_id = m.group(1) if m else None
        grays = tr.select("td.gsc_a_t > div.gs_gray")
        authors = grays[0].get_text(" ", strip=True).replace("\xa0", " ") if len(grays) > 0 else ""
        venue = ""
        if len(grays) > 1:
            venue_el = grays[1]
            span = venue_el.select_one("span.gs_oph")
            if span:
                span.extract()
            venue = venue_el.get_text(" ", strip=True).replace("\xa0", " ")
        cites_el = tr.select_one("td.gsc_a_c a")
        cites_raw = cites_el.get_text(strip=True) if cites_el else "0"
        year_el = tr.select_one("td.gsc_a_y span")
        year = year_el.get_text(strip=True) if year_el else ""
        year_m = re.search(r"(19|20)\d{2}", year)
        year = year_m.group(0) if year_m else ""
        if scholar_id and scholar_id in seen:
            continue
        if scholar_id:
            seen.add(scholar_id)
        papers.append(
            {
                "title": title,
                "authors": authors,
                "venue": venue,
                "year": year,
                "citations": int(re.sub(r"\D", "", cites_raw) or 0),
                "scholar_id": scholar_id,
            }
        )
    return papers, rows


def fetch_all(uid: str):
    papers = []
    start = 0
    while True:
        print(f"fetching page cstart={start} ...")
        html = fetch(PROFILE_URL.format(uid=uid, start=start))
        page, rows = parse_page(html)
        papers.extend(page)
        if rows < PAGE_SIZE:
            break
        start += PAGE_SIZE
        time.sleep(REQUEST_DELAY_S)
    print(f"fetched {len(papers)} papers from Google Scholar")
    return papers


# --------------------------------------------------------------------------
# BibTeX parsing / writing (minimal, brace-aware)
# --------------------------------------------------------------------------

def split_entries(bib: str):
    """Yield (type, key, body) for each @entry; body is the raw field text."""
    for m in re.finditer(r"@(\w+)\s*\{", bib):
        start = m.end()
        depth = 1
        i = start
        in_str = False
        while i < len(bib) and depth:
            c = bib[i]
            if in_str:
                if c == "}":
                    in_str = False
            elif c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
            elif c == '"':
                in_str = True
            i += 1
        end = i - 1
        inner = bib[start:end]
        key_end = inner.find(",")
        if key_end == -1:
            continue
        yield m.group(1).lower(), inner[:key_end].strip(), inner[key_end + 1 :]


def parse_fields(body: str):
    """Parse 'field = {value}, field2 = "v2"' into an ordered list of (name, value)."""
    fields = []
    i, n = 0, len(body)
    while i < n:
        m = re.match(r"\s*([^,={]+?)\s*=", body[i:])
        if not m:
            break
        name = m.group(1).strip()
        i += m.end()
        while i < n and body[i] in " \t":
            i += 1
        # value: brace group, quoted string, or bare token
        if i < n and body[i] == "{":
            depth = 1
            j = i + 1
            while j < n and depth:
                if body[j] == "{":
                    depth += 1
                elif body[j] == "}":
                    depth -= 1
                j += 1
            value = body[i + 1 : j - 1]
            i = j
        elif i < n and body[i] == '"':
            j = i + 1
            while j < n and body[j] != '"':
                j += 1
            value = body[i + 1 : j]
            i = j + 1
        else:
            m2 = re.match(r"[^,]*", body[i:])
            value = m2.group(0).strip()
            i += m2.end()
        while i < n and body[i] in " \t\n":
            i += 1
        if i < n and body[i] == ",":
            i += 1
        fields.append((name, value.strip()))
    return fields


def field_value(fields, name):
    for n, v in fields:
        if n.lower() == name:
            return v
    return None


def render_entry(etype: str, key: str, fields) -> str:
    lines = [f"@{etype}{{{key},"]
    for n, v in fields:
        v = re.sub(r"\s+", " ", v).strip()
        lines.append(f"  {n} = {{{v}}},")
    lines.append("}")
    return "\n".join(lines)


def norm_title(t: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", t.lower())


def make_key(paper, taken) -> str:
    authors = [p.strip() for p in paper["authors"].split(",")]
    last = re.sub(r"[^a-z]", "", (authors[0].split()[-1] if authors else "unknown").lower()) or "unknown"
    year = paper["year"] or "nd"
    words = re.findall(r"[A-Za-z0-9]+", paper["title"].lower())
    first = next((w for w in words if w not in STOPWORDS), words[0] if words else "paper")
    key = f"{last}_{year}_{first}"
    base, n = key, 2
    while key in taken:
        key = f"{base}_{n}"
        n += 1
    taken.add(key)
    return key


def format_author_list(raw: str) -> str:
    # "S Fachada, D Bonatto, A Schenkel" -> "Fachada, S. and Bonatto, D. and Schenkel, A."
    # Scholar abbreviates long author lists with a trailing ellipsis token.
    out = []
    for p in (x.strip() for x in raw.split(",")):
        if p in ("\u2026", "..."):
            out.append("et al.")
            continue
        toks = p.replace("-", " ").split()
        if len(toks) >= 2:
            initials = " ".join(t[0].upper() + "." for t in toks[:-1])
            out.append(f"{toks[-1][0].upper()}{toks[-1][1:]}, {initials}")
        elif p:
            out.append(p)
    return " and ".join(out)


def bib_escape(s: str) -> str:
    return s.replace("{", r"\{").replace("}", r"\}")


def new_entry(paper, key) -> str:
    fields = [
        ("title", bib_escape(paper["title"])),
        ("author", format_author_list(paper["authors"]) if paper["authors"] else ""),
        ("year", paper["year"]),
    ]
    if paper["venue"]:
        fields.append(("note", bib_escape(paper["venue"])))
    if paper["scholar_id"]:
        fields.append(("google_scholar_id", paper["scholar_id"]))
    fields = [(n, v) for n, v in fields if v != ""]
    return render_entry("misc", key, fields)


def update_entry(etype, key, fields, paper):
    """Apply fetched data to an existing entry. Returns (new_fields, changed).

    Each field is compared against the FETChed raw value with a field-appropriate
    normalizer, so a re-run with unchanged data produces no edits.
    """
    changed = False
    names = {n.lower() for n, _ in fields}

    def replace_field(name, value):
        nonlocal changed
        for i, (n, _) in enumerate(fields):
            if n.lower() == name:
                fields[i] = (n, value)
                return
        fields.append((name, value))

    # year: exact string
    if paper["year"] and field_value(fields, "year") != paper["year"]:
        replace_field("year", paper["year"])
        changed = True

    # venue: stored as note or journal; compare normalized
    if paper["venue"]:
        venue_field = "note" if "note" in names else ("journal" if "journal" in names else "note")
        old = field_value(fields, venue_field)
        if old is None or norm_title(old) != norm_title(paper["venue"]):
            replace_field(venue_field, bib_escape(paper["venue"]))
            changed = True

    # authors: compare surname sets across formats
    if paper["authors"]:
        old = field_value(fields, "author")
        if old is None or _surnames_bib(old) != _surnames_scholar(paper["authors"]):
            replace_field("author", format_author_list(paper["authors"]))
            changed = True

    # scholar id: exact
    if paper["scholar_id"] and field_value(fields, "google_scholar_id") != paper["scholar_id"]:
        replace_field("google_scholar_id", paper["scholar_id"])
        changed = True

    return fields, changed


def _surnames_bib(a: str) -> set:
    # "Fachada, S. and Bonatto, D." -> {"fachada", "bonatto"}
    return {
        p.split(",")[0].strip().lower()
        for p in a.split(" and ")
        if p.strip() and p.strip()[0].isalnum() and p.strip().lower() != "et al."
    }


def _surnames_scholar(a: str) -> set:
    # "S Fachada, D Bonatto" -> {"fachada", "bonatto"} (drops Scholar's "…")
    out = set()
    for p in (x.strip() for x in a.split(",")):
        toks = p.replace("-", " ").split()
        if len(toks) >= 2 and toks[-1][0].isalnum():
            out.add(toks[-1].lower())
    return out


def merge_bib(bib_text: str, papers):
    """Merge fetched papers into the bib text. Returns (new_text, added, updated).

    Matching is bijective and keyed by Google Scholar paper id (the
    google_scholar_id field) when available; entries without an id match on
    normalized title (manual/legacy entries). Unmatched existing entries are
    rendered as-is; each fetched paper consumes at most one entry.
    """
    existing = list(split_entries(bib_text))
    parsed = [parse_fields(body) for _, _, body in existing]
    taken = {k for _, k, _ in existing}
    updated = 0
    entry_used = [False] * len(existing)
    paper_matched = set()

    def match_for(paper):
        if paper["scholar_id"]:
            for i, fields in enumerate(parsed):
                if not entry_used[i] and field_value(fields, "google_scholar_id") == paper["scholar_id"]:
                    return i
        for i, fields in enumerate(parsed):
            if entry_used[i] or field_value(fields, "google_scholar_id"):
                continue
            if norm_title(field_value(fields, "title") or "") == norm_title(paper["title"]):
                return i
        return None

    for pi, paper in enumerate(papers):
        i = match_for(paper)
        if i is None:
            continue
        entry_used[i] = True
        paper_matched.add(pi)
        etype, key, _ = existing[i]
        fields, changed = update_entry(etype, key, parsed[i], paper)
        parsed[i] = fields
        if changed:
            updated += 1

    entries = []  # (text, year, title)

    def entry_order(fields, title):
        m = re.search(r"(19|20)\d{2}", field_value(fields, "year") or "")
        return (-(int(m.group(0)) if m else 0), norm_title(title))

    for (etype, key, _), fields in zip(existing, parsed):
        title = field_value(fields, "title") or ""
        entries.append((render_entry(etype, key, fields), entry_order(fields, title)))

    for pi, paper in enumerate(papers):
        if pi in paper_matched:
            continue
        key = make_key(paper, taken)
        fields = [("title", paper["title"]), ("year", paper["year"])]
        entries.append((new_entry(paper, key), entry_order(fields, paper["title"])))

    entries.sort(key=lambda item: item[1])
    new_text = "\n\n".join(text for text, _ in entries) + "\n"
    added = len(papers) - len(paper_matched)
    return new_text, added, updated


def write_if_changed(path: Path, text: str, dry: bool) -> bool:
    old = path.read_text() if path.exists() else None
    if old == text:
        return False
    if dry:
        print(f"--- would update {path.relative_to(REPO)}")
        for line in list(difflib.unified_diff(
            (old or "").splitlines(), text.splitlines(), lineterm=""
        ))[:60]:
            print("    " + line)
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        print(f"wrote {path.relative_to(REPO)}")
    return True


def main():
    dry = "--dry-run" in sys.argv
    uid = load_scholar_userid()
    papers = fetch_all(uid)

    bib_text = BIB_PATH.read_text() if BIB_PATH.exists() else ""
    new_bib, added, updated = merge_bib(bib_text, papers)
    print(f"bib: {added} new entries, {updated} updated")

    citation_data = {
        "metadata": {"last_updated": date.today().isoformat()},
        "papers": {},
    }
    for p in papers:
        if p["scholar_id"]:
            citation_data["papers"][p["scholar_id"]] = {
                "title": p["title"],
                "year": p["year"],
                "citations": p["citations"],
            }
    citations_text = yaml.dump(citation_data, sort_keys=True, width=1000)

    b = write_if_changed(BIB_PATH, new_bib, dry)
    c = write_if_changed(CITATIONS_PATH, citations_text, dry)
    if not b and not c:
        print("no changes")


if __name__ == "__main__":
    main()
