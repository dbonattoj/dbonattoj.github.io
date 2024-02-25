---
layout: post
title: Nicer way of formatting acronyms in LaTeX papers
date: 2024-02-25 19:00:00
description: Papers just miss this kind of interactivity.
tags: formatting latex
categories: publications
---

For my manuscript, I was not happy with the handling of acronyms, in particular, when I read paper in other fields than mine, often it is cumbersome to find some acronym I overlooked.

To improve that, discovered the `acronym` package, but, it does not do exactly what I want, it merely expands acronyms at their first usage and provides the generation of a table of acronyms, which is fine for printed material, even if it requires to go back and forth between the table and the text, but as I digest mainly electronic material, I thought I can do better.

Finally, I found someone else that struggled before me with something similar of what I wanted in [stackexchange](https://tex.stackexchange.com/questions/199084/tooltip-with-glossary-items). I promplty modified it and used it. The result is perfect, now, when the acronym is shown for the first time, it is expanded, as usual, and I can have a table of acronyms, but, in pdf files, when I see an acronym that I don’t know, I can over it with the mouse, and a small tooltip appears with the full definition of it !

Now I think every research papers should include this utility, and this blogpost is to encourage researchers to do so.

It is super easy, in the **main text file header**, just add:
```Latex
\input{acronyms}
```

And when you need to use an acronym, let’s say Reference View Synthesizer (RVS), you just need to write:

```Latex
Visual comparison between \tip{rvs} (4 and 8 input views) on zoomed details of [...]
```

If you need to have the acronym in plural form, you can use `\tips`, and if you need a capital letter `\Tip{s}` is working as well.

Now, you can have an `acronyms.tex` file that you copy paste between all your papers which contains the acronyms you find useful in your field and at the same time all the cool code that allows LaTeX to properly display them.

```Latex
\usepackage[printonlyused]{acronym}
\usepackage[draft, author={}]{pdfcomment}

\usepackage[hyperfirst=false,%sort=none,
acronym,nomain,shortcuts,toc,nogroupskip]{glossaries}
% https://tex.stackexchange.com/questions/199084/tooltip-with-glossary-items

\usepackage{xcolor} % used for colored acronyms

\renewcommand{\acs}[1]{\pdftooltip{\acrshort*{#1}}{\glsentrylong{#1}}}
\renewcommand{\acsp}[1]{\pdftooltip{\acrshortpl*{#1}}{\glsentrylongpl{#1}}}

\glsdisablehyper % disable hyperlinks on all acronyms

% Change list of acronyms name:
%\renewcommand*{\acronymname}{List of Abbreviations}

% Funky colors:
%\definecolor{myBlue}{RGB}{73, 142, 41}
%\definecolor{myViolet}{RGB}{17, 138, 178}
% Black:
\definecolor{myBlue}{RGB}{0, 0, 0}
\definecolor{myViolet}{RGB}{0, 0, 0}

\newcommand{\accolor}[1]{\textcolor{myBlue}{#1}}
% use to make first definition special format:
\newcommand*{\glossfirstformat}[1]{\accolor{#1}}

%https://tex.stackexchange.com/questions/232707/modify-appearance-of-first-acronym
\newcommand*{\acfirstformat}[1]{\textcolor{myViolet}{{#1}}}
\newcommand*{\acplfirstformat}[1]{\textcolor{myViolet}{{#1}}}
\newacronymstyle{myacro}
{%
  \GlsUseAcrEntryDispStyle{long-short}%
}%
{%
  \GlsUseAcrStyleDefs{long-short}%
  \renewcommand*{\genacrfullformat}[1]{%
   \glossfirstformat{\glsentrylong{##1}}\space
   (\acfirstformat{\glsentryshort{##1}})%
  }%
  \renewcommand*{\Genacrfullformat}[2]{%
   \glossfirstformat{\Glsentrylong{##1}}\space
   (\glsentryshort{##1})%
  }%
  \renewcommand*{\genplacrfullformat}[2]{%
   \glossfirstformat{\glsentrylongpl{##1}}\space
   (\acplfirstformat{\glsentryshort{##1}})%
  }%
  \renewcommand*{\Genplacrfullformat}[2]{%
   \glossfirstformat{\Glsentrylongpl{##1}}\space
   (\glsentryshortpl{##1})%
  }%
}

\setacronymstyle{myacro}

% use for normal acronyms, gives them a PDF tooltip popup
\newcommand*{\tip}[1]{%  define our acronym command,  make it short since we use it a lot, use * for so that it is only a 'short' command
    \ifglsused{#1}{% if we used it already, then put pdftooltip
      {\pdftooltip{\accolor{\glsentryshort{#1}}}{\glsentrydesc{#1}}}%
    }{%
      \gls{#1}% otherwise put the normal gls
    }%
}%

% Capital first letter
\newcommand*{\Tip}[1]{
    \ifglsused{#1}{%
      {\pdftooltip{\accolor{\Glsentryshort{#1}}}{\glsentrydesc{#1}}}%
    }{%
      \Gls{#1}%
    }%
}%

% Plural acronyms
\newcommand*{\tips}[1]{%
    \ifglsused{#1}{%
      {\pdftooltip{\accolor{\glsentryshortpl{#1}}}{\glsentrydesc{#1}}}%
    }{%
      \glspl{#1}%
    }%
}%

% Capital letter and plural
\newcommand*{\Tips}[1]{%
    \ifglsused{#1}{%
      {\pdftooltip{\accolor{\Glsentryshortpl{#1}}}{\glsentrydesc{#1}}}%
    }{%
      \Glspl{#1}%
    }%
}%

\newacronym{mla}{MLA}{micro-lens array}
\newacronym{rvs}{RVS}{Reference View Synthesizer}
[...]
```


