% Graduation project coordinator, Applied Mathematics, FMS, UofK
% Don't change anything here

\NeedsTeXFormat{LaTeX2e}[1994/06/01]
\ProvidesClass{fms}[2020/04/01 Class for Applied and Pure Mathematics, FMS Dissertation]
\LoadClass[12pt,a4paper,oneside]{report}
%\usepackage{setspace}
%\onehalfspacing

% Formatting
\usepackage[text={6.5in,9in}]{geometry}
\topmargin=0in
\headheight=0in
\oddsidemargin=0in
\evensidemargin=0in
\parskip=0.5\baselineskip
\parindent=0pt
%\renewcommand{\familydefault}{\sfdefault}
\linespread{1.0}

% AMS packages.
\RequirePackage{amsmath}
\RequirePackage{amssymb}
\RequirePackage{amsfonts}
\RequirePackage{amsthm}
\RequirePackage{latexsym}

% An additional colour for citecolor= in the hyperref pacakage
\RequirePackage{color}
\definecolor{red}{rgb}{1,0.0,0.0}
\RequirePackage[pdftex,a4paper,%
    colorlinks=true,urlcolor=blue,citecolor=red]{hyperref}
\urlstyle{same}

% appendix command changes chapter headings to say "Appendix"
\def\appendix{\setcounter{chapter}{0}\setcounter{section}{0}\def\thechapter{\Alph{chapter}}\def\@chapapp{Appendix }}

% Undefine "\subsubsection", "\paragraph", "\subparagraph" in a nice way.
\newcommand{\aims@undefined@error}[1]{%
  \ClassError{fms}{The command \string#1 is disabled in FMS Dissertation}%
  {Please choose a less intricate structure for your Dissertation!}}
\renewcommand{\subsubsection}{\aims@undefined@error{\subsubsection}}
\renewcommand{\paragraph}    {\aims@undefined@error{\paragraph}}
\renewcommand{\subparagraph} {\aims@undefined@error{\subparagraph}}

% Produce an error when \\ is used in normal text 
\AtBeginDocument{\def\\{\ClassError{fms}{%
      You should not use \protect\\ in normal text. If you want
      \MessageBreak
      to separate two paragraphs, just leave an empty line
      \MessageBreak
      in your code. Otherwise, why would you want a new
      \MessageBreak
      line? Basically, only use \protect\\ in your title, in
      \MessageBreak
      tables, in matrices, and in aligned equations.}{}}}

%Do not show subsections and theorems in Table of Contents
\AtBeginDocument{\setcounter{tocdepth}{1}}

\definecolor{wine-stain}{rgb}{0,0,0.1}
\hypersetup{
  colorlinks,
  linkcolor=wine-stain, % custom color
  linktoc=all
}
