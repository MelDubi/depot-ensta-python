\ProvidesClass{styles/rapportEnsta}[04/09/2022]

\LoadClass[a4paper,11pt]{report}
\RequirePackage[top=2cm,bottom=2cm,left=2cm,right=2cm]{geometry}
\RequirePackage[utf8]{inputenc}
\RequirePackage[frenchb]{babel}
\RequirePackage[T1]{fontenc}

\RequirePackage{styles/pageGarde}

\RequirePackage{multirow}
\RequirePackage{makecell}
\RequirePackage{fancyhdr}
\RequirePackage{caption}
\RequirePackage[final]{pdfpages}
\RequirePackage{tikz,pgfplots,pgf}
\RequirePackage{subcaption}
\RequirePackage{siunitx}
\RequirePackage[toc,page]{appendix}
\renewcommand{\appendixtocname}{Annexes}
\renewcommand{\appendixpagename}{Annexes}
\RequirePackage{tcolorbox, listings} 
\RequirePackage{minted}
\usemintedstyle{friendly}
\RequirePackage{sectsty}
\RequirePackage[french]{minitoc} 
\RequirePackage{hyperref}
\RequirePackage{titlesec}
\RequirePackage{colortbl}
\RequirePackage{amsmath}
\RequirePackage{mwe}
\RequirePackage{lipsum}



\hypersetup{
	colorlinks=true, %colorise les liens
	breaklinks=true, %permet le retour à la ligne dans les liens trop longs
	urlcolor=blue,  %couleur des hyperliens
    citecolor=blue, %couleur des citations
	linkcolor=black, %couleur des liens internes
	plainpages=false  %pour palier à "Bookmark problems can occur when you have duplicate page numbers, for example, if you have a page i and a page 1."
}


% Define a custom style
\lstdefinestyle{myBash}{
    backgroundcolor=\color{backcolour},   
    commentstyle=\color{codegreen},
    otherkeywords={bash, &&, bt-device, bt-obex, bt-network, bt-agent, brctl, ifconfig, ip, readlink, dirname, 
                    sleep, hcitool, sudo},
    keywordstyle=\color{codeblue},
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codeorange},
    basicstyle=\ttfamily\footnotesize,
    breakatwhitespace=false,         
    breaklines=true,                 
    keepspaces=true,                 
    numbers=left,       
    numbersep=5pt,                  
    showspaces=false,                
    showstringspaces=false,
    showtabs=false,                  
    tabsize=2,
}

\lstdefinestyle{myPython}{
    backgroundcolor=\color{backcolour},   
    commentstyle=\color{codegreen},
    otherkeywords={threading, Thread},
    keywordstyle=\color{codeblue},
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codeorange},
    basicstyle=\ttfamily\footnotesize,
    breakatwhitespace=false,         
    breaklines=true,                 
    keepspaces=true,                 
    numbers=left,       
    numbersep=5pt,                  
    showspaces=false,                
    showstringspaces=false,
    showtabs=false,                  
    tabsize=2,
}


\lstdefinestyle{myC}{
    backgroundcolor=\color{backcolour},   
    commentstyle=\color{codegreen},
    otherkeywords={},
    keywordstyle=\color{codeblue},
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codeorange},
    basicstyle=\ttfamily\footnotesize,
    breakatwhitespace=false,         
    breaklines=true,                 
    keepspaces=true,                 
    numbers=left,       
    numbersep=5pt,                  
    showspaces=false,                
    showstringspaces=false,
    showtabs=false,                  
    tabsize=2,
}

\lstdefinestyle{myCpp}{
    backgroundcolor=\color{backcolour},   
    commentstyle=\color{codegreen},
    otherkeywords={},
    keywordstyle=\color{codeblue},
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codeorange},
    basicstyle=\ttfamily\footnotesize,
    breakatwhitespace=false,         
    breaklines=true,                 
    keepspaces=true,                 
    numbers=left,       
    numbersep=5pt,                  
    showspaces=false,                
    showstringspaces=false,
    showtabs=false,                  
    tabsize=2,
}

\chapterfont{\color{Pantone2377C}{}\fontfamily{pag}}
\sectionfont{\color{subtitlecolour}{}\fontfamily{pag}}
\subsectionfont{\color{subtitlecolour}{}\fontfamily{pag}}
\subsubsectionfont{\color{subtitlecolour}{}\fontfamily{pag}}

\definecolor{Pantone2377C}{HTML}{2C5574}
\definecolor{subtitlecolour}{HTML}{00A2A9}
\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codeblue}{HTML}{3E8BC0}
\definecolor{codeorange}{HTML}{ffa334}
\definecolor{backcolour}{HTML}{efefef}

