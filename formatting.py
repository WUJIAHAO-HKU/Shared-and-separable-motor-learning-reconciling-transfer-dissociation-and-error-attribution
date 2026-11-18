from pathlib import Path
import json,re
R=Path(__file__).parent
refs=json.loads((R/"references_verified.json").read_text(encoding="utf-8"))
def esc(s):return str(s).replace('&',r'\&').replace('%',r'\%').replace('_',r'\_').replace('#',r'\#').replace('–','--').replace('—','---')
def pair(x,z):
 s=x[z]
 if z:
  for c in re.findall(r'\\cite\{[^}]+\}',x[0]):
   if c not in s:s+=' '+c
 return s
def pre(z,short=False):
 s=r'''\documentclass[11pt,a4paper]{article}
\usepackage[margin=23mm,headheight=15pt]{geometry}
\usepackage{fontspec}
\setmainfont{Times New Roman}
\setsansfont{Arial}
\usepackage{amsmath,amssymb,graphicx,booktabs,array,tabularx,longtable,caption,xcolor,fancyhdr,enumitem,placeins}
\usepackage[numbers,sort&compress]{natbib}
\usepackage[colorlinks=true,linkcolor=teal!55!black,citecolor=teal!55!black,urlcolor=teal!55!black]{hyperref}
\definecolor{navy}{HTML}{193447}
\definecolor{pale}{HTML}{EDF4F5}
\usepackage{titlesec}
\titleformat{\section}{\large\sffamily\bfseries\color{navy}}{}{0em}{}
\setlength{\parindent}{0pt}
\setlength{\parskip}{6pt}
\raggedbottom
\setlength{\emergencystretch}{3em}
\widowpenalty=10000\clubpenalty=10000
\renewcommand{\topfraction}{.95}\renewcommand{\bottomfraction}{.85}\renewcommand{\textfraction}{.05}\renewcommand{\floatpagefraction}{.75}
\renewcommand{\arraystretch}{1.16}
\captionsetup{font=small,labelfont=bf,justification=raggedright,singlelinecheck=false}
\pagestyle{fancy}\fancyhf{}\fancyhead[L]{\small\sffamily ADAPTIVE FEEDBACK}\fancyhead[R]{\small\sffamily November 2026}\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.3pt}
\graphicspath{{figures/}}
\newcounter{boxnum}
\newcommand{\boxlabel}{Box}
'''
 if z:s+=r'''\usepackage{xeCJK}
\setCJKmainfont{SimSun}[BoldFont=SimHei,ItalicFont=KaiTi]
\setCJKsansfont{Microsoft YaHei}
\renewcommand{\figurename}{图}\renewcommand{\tablename}{表}\renewcommand{\refname}{参考文献}\renewcommand{\boxlabel}{框}
'''
 if short:s=s.replace('11pt,a4paper','10pt,a4paper')
 return s+r'\begin{document}'+'\n'
def title(z,syn=False):
 return (r'{\small\sffamily\color{navy} '+('投稿前咨询概要 | SYNOPSIS' if z else 'PRESUBMISSION SYNOPSIS')+r'}\par' if syn else r'{\small\sffamily\color{navy} NATURE COMMUNICATIONS | PROPOSED PERSPECTIVE}\par')+'\n'+r'{\LARGE\bfseries '+TITLE[z]+r'}\par\vspace{7pt}'+'\n'+(r'{\small 作者审阅稿；作者信息与声明待作者补充。}' if z else r'{\small Draft for author review; author details and declarations to be supplied by the authors.}')+r'\par\vspace{9pt}'+'\n'
def fig(k,z):
 f,en,zh=FIGURES[k]
 height='.43' if k=='workflow' else '.58'
 if k=='workflow':return r'\par\medskip\noindent\begin{minipage}{\textwidth}\centering\includegraphics[width=\textwidth,height='+height+r'\textheight,keepaspectratio]{'+f+'}\n\\captionof{figure}{'+(zh if z else en)+'}\\label{fig:'+k+'}\n'+r'\end{minipage}\par\medskip'+'\n'
 return r'\begin{figure}[!htbp]\centering\includegraphics[width=\textwidth,height='+height+r'\textheight,keepaspectratio]{'+f+'}\n\\caption{'+(zh if z else en)+'}\\label{fig:'+k+'}\n\\end{figure}\n'
def table(k,z):
 cap,heads,rows=TABLES[k]
 s='\n\\begin{table}[!htbp]\n\\caption{'+cap[z]+'}\\label{tab:'+k+'}\n\\small\n'
 s+=r'\begin{tabularx}{\textwidth}{>{\hsize=.85\hsize\linewidth=\hsize\raggedright\arraybackslash}X>{\hsize=.95\hsize\linewidth=\hsize\raggedright\arraybackslash}X>{\hsize=1.2\hsize\linewidth=\hsize\raggedright\arraybackslash}X}\toprule'+'\n'
 s+=' & '.join(r'\textbf{'+pair(x,z)+'}' for x in heads)+r'\\\midrule'+'\n'
 for row in rows:s+=' & '.join(pair(x,z) for x in row)+r'\\[7pt]'+'\n'
 return s+r'\bottomrule\end{tabularx}\end{table}'+'\n'
def box(z):
 s=r'\par\bigskip\noindent\begin{minipage}{\textwidth}\refstepcounter{boxnum}\label{box:protocol}'+'\n'+r'{\large\sffamily\bfseries\color{navy}\boxlabel~\theboxnum. '+BOX[z]+r'}\par\medskip'+'\n'+r'\begin{enumerate}[leftmargin=*,itemsep=7pt]'+'\n'
 s+='\n'.join(r'\item '+x[z] for x in BOX[2])+r'\end{enumerate}\end{minipage}\par\bigskip'+'\n'
 return s
def bibliography(keys):
 out=[]
 for k in sorted(keys):
  v=refs[k];assert 'error' not in v,(k,v)
  authors=' and '.join(a.get('family','')+', '+a.get('given','') for a in v['authors'])
  fields={'title':'{'+esc(v['title'])+'}','author':authors,'year':v['year'],'journal':esc(v.get('journal',''))}
  for x in ['volume','pages','doi','url']:
   if v.get(x):fields[x]=v[x]
  out.append('@article{'+k+',\n'+',\n'.join(' '+a+'={'+str(b)+'}' for a,b in fields.items())+'\n}')
 (R/'references.bib').write_text('\n\n'.join(out),'utf8')
def end(clear=False):return '\n'+(r'\clearpage' if clear else '')+r'\begingroup\fontsize{8.5}{9.6}\selectfont\setlength{\parskip}{0pt}\setlength{\bibsep}{0pt}\bibliographystyle{unsrtnat}\bibliography{references}\endgroup\end{document}'
