---
layout: post
title: From Print to Pixel - Transforming Acronym Usage in Academic Writing
date: 2024-02-25 19:00:00
description: Papers just miss this kind of interactivity.
tags: formatting latex
categories: publications
---

In the world of academic manuscripts, grappling with acronyms can be a real headache, especially when diving into papers from different fields. I recently found myself facing this issue, and the standard solutions weren't quite cutting it.

To tackle this issue, I explored the [`glossaries`](https://fr.overleaf.com/learn/latex/Glossaries) package, hoping it would be the solution I needed. However, it fell short of my expectations. While it did expand acronyms at their initial usage and offered a table generation feature, it was more tailored for printed material. Having to navigate between the table and the text wasn't ideal, especially for someone like me who primarily engages with electronic materials. I was convinced there was room for improvement.

Fortunately, after some digging, I stumbled upon a gem on [Stack Exchange](https://tex.stackexchange.com/questions/199084/tooltip-with-glossary-items). Inspired by someone else's struggle, I tweaked the solution to fit my needs. The outcome? Perfect. Now, when I encounter an unfamiliar acronym in a PDF, a simple hover with the mouse reveals a tooltip with the full definition. Game-changer!

I believe every research paper could benefit from this nifty utility, and this post is my call to action for fellow researchers to hop on the bandwagon.

Implementation is a breeze – just add the following line to your **main text file header**:

{% highlight latex %}
{% raw %}
\input{acronyms}
{% endraw %}
{% endhighlight %}

When you're ready to use an acronym, like Reference View Synthesizer (RVS), simply write:

{% highlight latex %}
{% raw %}
Visual comparison between \tip{rvs} (4 and 8 input views) on zoomed details of [...] \tip{rvs} [...]
{% endraw %}
{% endhighlight %}

{% include figure.liquid path="assets/img/posts/tooltip.jpg" class="img-fluid rounded z-depth-1" %}

For plurals, try \tips, and for capital letters, go for \Tip\{s\}. Easy, right?

Now, create an `acronyms.tex` file, a versatile copy-paste companion for all your papers. It not only houses the acronyms relevant to your field but also contains the nifty LaTeX code for seamless display.

{% highlight latex %}
{% raw %}
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

% Acronyms in colors
%\definecolor{color1}{RGB}{73, 142, 41} % greenish
%\definecolor{color2}{RGB}{17, 138, 178} % blue
%\definecolor{color3}{RGB}{73, 142, 41} % greenish
% Acronyms in black
\definecolor{color1}{RGB}{0, 0, 0} % black
\definecolor{color2}{RGB}{0, 0, 0} % black
\definecolor{color3}{gray}{0.30} % gray
\newcommand{\mygray}[1]{\textcolor{color3}{#1}}
\newcommand{\mybold}[1]{\textbf{\mygray{#1}}}

\newcommand{\accolor}[1]{\textcolor{color1}{#1}}
\newcommand*{\glossfirstformat}[1]{\accolor{#1}} % use to make first definition special format

%https://tex.stackexchange.com/questions/232707/modify-appearance-of-first-acronym
\newcommand*{\acfirstformat}[1]{\textcolor{color2}{\textbf{#1}}}
\newcommand*{\acplfirstformat}[1]{\textcolor{color2}{\textbf{#1}}}
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
\newcommand*{\tip}[1]{% define our acronym command, make it short since we use it a lot,
  % use * for so that it is only a 'short' command
  \ifglsused{#1}{% if we used it already, then put pdftooltip
    {\pdftooltip{\accolor{\mybold{\glsentryshort{#1}}}}{\glsentrydesc{#1}}}%
  }{%
    {\gls{#1}}% otherwise put the normal gls
  }%
}%

\newcommand*{\Tip}[1]{%
  \ifglsused{#1}{%
    {\pdftooltip{\accolor{\mybold{\Glsentryshort{#1}}}}{\glsentrydesc{#1}}}%
  }{%
    {\Gls{#1}}%
  }%
}%

% use for plural acronyms
\newcommand*{\tips}[1]{%
  \ifglsused{#1}{%
    {\pdftooltip{\accolor{\mybold{\glsentryshortpl{#1}}}}{\glsentrydesc{#1}}}%
  }{%
    {\glspl{#1}}%
  }%
}%

\newcommand*{\Tips}[1]{%
  \ifglsused{#1}{%
    {\pdftooltip{\accolor{\mybold{\Glsentryshortpl{#1}}}}{\glsentrydesc{#1}}}%
  }{%
    {\Glspl{#1}}%
  }%
}%

% Forced short version in capital and without capital, for example to use in figure captions,
% where we do not want to define the term if it appears for the first time there,
% but we still want the tooltip.
\newcommand*{\Tipshort}[1]{%
  \ifglsused{#1}{%
    {\pdftooltip{\accolor{\mybold{\Glsentryshort{#1}}}}{\glsentrydesc{#1}}}%
  }{%
    \mybold{\acs{#1}}%
  }%
}%

\newcommand*{\tipshort}[1]{%
  \ifglsused{#1}{%
    {\pdftooltip{\accolor{\mybold{\glsentryshort{#1}}}}{\glsentrydesc{#1}}}%
  }{%
    \mybold{\acs{#1}}%
  }%
}%

\newacronym{rvs}{RVS}{Reference View Synthesizer}
{% endraw %}
{% endhighlight %}

Here is an [Overleaf link](https://www.overleaf.com/read/ftdtbqcrfgrd#11682c) with a **downloadable working example**.

Let's empower every research paper with this tool – simple, effective, and a game-changer for both writers and readers alike! 🚀
