from pathlib import Path
import json,re,shutil,hashlib
import formatting as f
from evidence import ROWS
from rules import RULES
from manuscript import TITLE,ABSTRACT,SECTIONS
from current_render import render as render_acceptance
from acceptance import CLAIMS,REMOVALS
R=Path(__file__).parent
def tex(x):return f.esc(x).replace('×',r'$\times$').replace('→',r'$\rightarrow$').replace('–','--')
def para(t):return t.strip()+'\n\n'
def heading(t):return '\\section{'+t+'}\n'
def figure(name,caption):
 return '\n\\begin{figure}[!htbp]\\centering\n\\includegraphics[width=\\textwidth]{'+name+'}\n\\caption{'+caption.replace('%',r'\%')+'}\n\\end{figure}\n'
def tablesynth(z):
 cap=('Evidence supports different levels of explanation. IDs resolve to the detailed atlas.','证据支持不同解释层级；编号对应详细图谱。')[z]
 heads=[('Evidence','证据'),('Established inference','已支持推断'),('Integrative prediction','整合预测')]
 data=[(('Transfer (E01–E03, E08)','迁移（E01–E03、E08）'),('Dynamics knowledge affects multiple outputs.','动力学知识影响多个输出。'),('Measure cross-output transfer under crossed training/test contexts.','交叉训练/测试情境测量跨输出迁移。')),
 (('Dissociation (E04–E07, E11)','分离（E04–E07、E11）'),('Coupling depends on exposure and timing.','耦合依赖暴露与时序。'),('Pair full correction and learning waveforms at matched delays.','匹配延迟，配对完整纠错与学习波形。')),
 (('Attribution (E13–E16, E19)','归因（E13–E16、E19）'),('Source and context affect specific learning/readout components.','来源与情境影响特定学习/读出成分。'),('Cross source with persistence and independently calibrate perception.','交叉来源与持续性，独立校准感知。')),
 (('Sensory specificity (E12, E17–E18)','感觉特异性（E12、E17–E18）'),('Sensory inputs can have distinct learning consequences.','不同感觉输入可产生不同学习后果。'),('Test distinct input dynamics alongside transfer into both control outputs.','同时检验不同输入动态及向两个控制输出的迁移。'))]
 s='\\begin{table}[!htbp]\\small\\caption{'+cap+'}\\label{tab:synthesis}\n'+r'\begin{tabularx}{\textwidth}{>{\raggedright\arraybackslash}X>{\raggedright\arraybackslash}X>{\raggedright\arraybackslash}X}\toprule'+'\n'
 s+=' & '.join(r'\textbf{'+h[z]+'}' for h in heads)+r'\\\midrule'+'\n'
 for row in data:s+=' & '.join(tex(t[z]) for t in row)+r'\\[5pt]'+'\n'
 return s+r'\bottomrule\end{tabularx}\end{table}'+'\n'
def rulestable(z):
 cap=('Evidence-derived choices of additional measurements. Full controls and simulation boundaries appear in the atlas.','由证据导出的追加测量选择；完整对照与模拟边界见图谱。')[z]
 s=r'\small\begin{longtable}{p{.20\textwidth}p{.34\textwidth}p{.36\textwidth}}'+'\n'+r'\caption{'+cap+r'}\label{tab:rules}\\\toprule'+'\n'
 h=('Dispute & Minimal addition & Outcome interpretation','争议 & 最小追加测量 & 结果解释')[z]+r'\\\midrule'
 s+=h+r'\endfirsthead\toprule'+'\n'+h+r'\endhead\bottomrule\endfoot'+'\n'
 for row in RULES:s+=tex(row[0]+' '+row[2][z])+' & '+tex(row[3][z])+' & '+tex(row[4][z])+r'\\[9pt]'+'\n'
 return s+r'\end{longtable}\normalsize'+'\n'
def header(z,atlas=False):
 s=f.pre(z).replace('ADAPTIVE FEEDBACK','EVIDENCE TO EXPERIMENT').replace('November 2026','17 November 2026')
 if not atlas:
  s=s.replace(r'\begin{document}',r'\usepackage[mathlines]{lineno}'+ '\n'+r'\setlength{\linenumbersep}{8pt}'+ '\n'+r'\renewcommand\linenumberfont{\normalfont\tiny\sffamily}'+ '\n'+r'\begin{document}\runninglinenumbers')
 s+=r'{\small\sffamily\color{navy} '+(('SUPPLEMENTARY EVIDENCE ATLAS' if atlas else 'PERSPECTIVE | EVIDENCE SYNTHESIS') if not z else ('补充证据图谱' if atlas else 'PERSPECTIVE | 证据综合'))+r'}\par\medskip'+'\n'
 s+=r'{\LARGE\bfseries\raggedright '+( ('Evidence map and experiment-selection rules','证据地图与实验选择规则')[z] if atlas else TITLE[z])+r'\par}\bigskip'+'\n'
 s+=r'{\normalsize '+('JiaHao Wu and Long Zeng' if not z else 'JiaHao Wu、曾龙（Long Zeng）')+r'\par}'+'\n'
 s+=r'{\small '+('Tsinghua Shenzhen International Graduate School, Tsinghua University, Shenzhen, China' if not z else '清华大学深圳国际研究生院，中国深圳')+r'\par}\medskip'+'\n'
 s+=r'\hypersetup{pdfauthor={JiaHao Wu; Long Zeng}}'+'\n'
 s+=r'{\small '+('Correspondence: Long Zeng, ' if not z else '通讯作者：曾龙（Long Zeng），')+r'\href{mailto:zenglong@sz.tsinghua.edu.cn}{zenglong@sz.tsinghua.edu.cn}\par}\medskip'+'\n'
 return s
def end():return f.end(clear=False)
def make_main(z):
 s=header(z)+heading(('Abstract','摘要')[z])+ABSTRACT[z]+'\n\n'
 for i,(h,t) in enumerate(SECTIONS):
  s+=heading(h[z])+para(t[z])
  if i==0:s+=figure(('figure1_en.pdf','figure1_zh.pdf')[z],('Evidence streams and proposed integration. The four observations constrain different stages of learning and three independent dimensions: sensory channels, control outputs and timescales. The pathway organizes experimental comparisons. Native PowerPoint text, shapes and connectors depict conceptual relationships to be tested.','证据线索与拟议整合。四类观察约束不同学习环节，以及感觉通道、控制输出和时间尺度三个独立维度。流程组织实验比较。文字、图形与连线由PowerPoint原生对象组成，表示待检验的概念关系。')[z])
  if h[0]=='A joint explanation with explicit observables':s+=tablesynth(z)
  if h[0]=='Choosing an experiment by the restriction it tests':
   s+=figure(('figure2_en.pdf','figure2_zh.pdf')[z],('Testing temporal mixtures, report loadings and external prediction. Fixed mixed readout can change delay ratios. Solid arrows connect temporal modes to the two measured outputs; dashed arrows denote candidate contributions to localization reports. Independent calibration constrains the report loadings. Passive movement denotes robot-guided human-arm movement. Source-fitted parameters are frozen before target-study scoring. The diagram is composed of native PowerPoint objects.','检验时间混合、报告载荷及外部预测。固定混合读出能够改变延迟比例；实线连接时间成分与两项测量输出；虚线表示定位报告的候选贡献，报告载荷由独立校准约束。被动运动指机器人引导人体手臂运动。来源拟合参数在目标研究评分前冻结。本图由PowerPoint原生对象组成。')[z])+r'\FloatBarrier'+'\n'+rulestable(z)
  if h[0]=='Frozen predictions across public human studies':
   s+=figure('empirical_validation.png',('Public-data predictions and calibration checks. a,b: target-study mean changes (points, participant SEM) and frozen source predictions, shown for abrupt exposure; complete schedule scores are supplied. c: paired difference in joint standardized MSE, separate-two minus common-two, with target-participant bootstrap 95% intervals. d: active-minus-passive localization shifts with participant-bootstrap 95% intervals. Curves and points are computed from deposited human data; no image generation was used.','公开数据预测与校准检查。a、b：突然暴露中目标研究均值变化（点及参与者SEM）与冻结来源预测；附完整序列评分。c：双分别减双共同模式的联合标准化MSE配对差异及目标参与者自助法95%区间。d：主动减被动定位变化及参与者自助法95%区间。点与曲线由公开人体数据计算，未使用图像生成。')[z])
 s+=heading(('Transparency and reproducibility','透明性与可复核材料')[z])
 s+=(r'The paired evidence records, frozen predictions, participant scores, model fits, exact counterexamples and executable scripts accompany this Perspective. Public data are secondary analyses of the cited studies. Target post-exposure observations were excluded from fitting and penalty selection. The analysis was developed after inspection of the broader archives and is retrospective. The accompanying recovery test uses newly drawn synthetic instances. Figures 1--2 were reconstructed in Microsoft PowerPoint as editable text and vector shapes with AI-assisted layout code; earlier drafts used OpenAI-generated conceptual images. The current figures contain no generated-image pixels. The quantitative figure is generated directly from analysis outputs. Language-model assistance supported literature organization, bilingual drafting and code preparation.' if not z else '随附配对证据、冻结预测、参与者评分、模型拟合、精确反例及可执行脚本。公开数据分析为所引研究的二次分析；目标暴露后观测未用于拟合及正则选择。分析在先前查阅广泛档案后开发，属于回顾性研究。恢复检验使用新抽取合成实例。图1--2通过AI辅助布局代码在Microsoft PowerPoint中重建为可编辑文字与矢量图形；早期草稿使用过OpenAI生成的概念图。当前图中不含生成图像像素。定量图直接由分析输出生成。语言模型辅助用于文献组织、双语撰写及代码准备。')+'\n'
 s+=heading(('Data availability','数据可用性')[z])
 s+=(r'This secondary analysis uses public human data from Franklin and Franklin (2021, 2023) and Gastrock et al. (2020). Source records and dataset identifiers are provided in the accompanying public\_data metadata. Processed block observations, participant localization estimates, model predictions and analysis summaries are included in the accompanying reproducibility package. \cite{franklin2021,franklin2023,external2020}' if not z else r'本研究二次分析Franklin与Franklin（2021、2023）及Gastrock等（2020）的公开人体数据。来源记录和数据集标识符见随附public\_data元数据。处理后的块级观测、参与者定位估计、模型预测及分析摘要包含于随附复现材料包。\cite{franklin2021,franklin2023,external2020}')+'\n'
 s+=heading(('Code availability','代码可用性')[z])
 s+=('The code and reproducibility package are available in the \\href{https://github.com/WUJIAHAO-HKU/Shared-and-separable-motor-learning-reconciling-transfer-dissociation-and-error-attribution}{project repository}. The package contains the Python scripts for data extraction checks, temporal-model fitting, cross-study prediction, model recovery, calibration examples and quantitative figures. The README describes the workflow and dependencies; the release manifest records file hashes.' if not z else '代码与复现材料见\\href{https://github.com/WUJIAHAO-HKU/Shared-and-separable-motor-learning-reconciling-transfer-dissociation-and-error-attribution}{项目仓库}。材料包提供用于数据提取核查、时间模型拟合、跨研究预测、模型恢复、校准案例及定量图的Python脚本。README说明运行流程与依赖，发布清单记录文件哈希。')+'\n'
 s+=heading(('Author contributions','作者贡献')[z])
 s+=('J.W. conceived the Perspective, organized the literature, performed the analyses, developed the code and wrote the manuscript. L.Z. provided supervision.' if not z else 'JiaHao Wu负责构思、文献整理、分析、代码开发及论文写作。曾龙提供指导。')+'\n'
 s+=heading(('Competing interests','利益冲突')[z])
 s+=('The authors declare no competing interests.' if not z else '作者声明不存在利益冲突。')+'\n'
 s+=heading(('Funding','资助')[z])
 s+=('No specific funding was received for this work.' if not z else '本工作未获得专项资助。')+'\n'
 return s+end()
def field(label,text):return r'\textbf{'+label+r'} '+text+r'\par'+'\n'
def make_atlas(z):
 s=header(z,True)
 s+=('The 29 entries distinguish published observations from our interpretive synthesis and proposed tests. Each entry cites the source and a figure, experiment or section locator. The eight decision cards specify controls and computational boundaries. Coverage is centered on human upper-limb adaptation; the 2026 reviewed preprint and computational contributions are explicitly labelled. The full paired records are also supplied as JSON.\n' if not z else '29个条目分别记录已发表观察、本文综合推断和拟议测试；每项给出文献及原文图、实验或节定位。八张决策卡说明对照与计算边界。覆盖以人类上肢适应为中心，2026年已评审预印本及计算贡献均单独标示；完整双语条目另以JSON提供。\n')
 s+=tablesynth(z)
 s+=heading(('Reading the evidence levels','证据层级的阅读方式')[z])
 s+=('Observed result: what the experiment measured. Supported inference: the mechanism level constrained by its controls. Residual explanation: a specific alternative that can produce the observation. Proposed test: our next comparison and its predicted interpretive value. A surviving alternative is retained without changing the original result.\n' if not z else '观察结果：实验实际测得什么。支持推断：原实验对照约束到的机制层级。残余解释：能产生该观察的具体竞争解释。拟议测试：本文提出的下一对比及其解释价值。保留竞争解释，同时保留原研究已确立的结果。\n')
 for ix,row in enumerate(ROWS):
  s+=(r'\clearpage' if ix%2==0 else r'\bigskip\hrule\medskip')+heading(row['id']+' | '+f.refs[row['key']]['title'])
  s+=r'{\small\sffamily\color{navy} '+tex(row['group'].split(' / ')[z])+r'}\par'+'\n'
  s+=field(('Source','来源')[z],r'\cite{'+row['key']+'}; '+tex(row['locator']))
  status=row['status'].split(' / ')
  if z and status==['Published primary study']:status=['Published primary study','已发表原始研究']
  s+=field(('Study type / status','研究类型/状态')[z],tex(status[min(z,len(status)-1)]))
  for key,labels in [('design',('Manipulation and comparison','操纵与比较')),('measure',('Measured outcome','测量指标')),('finding',('Observed finding','观察结果')),('inference',('Supported inference','支持的推断')),('alternative',('Residual explanation','残余解释')),('test',('Discriminating prediction / proposed addition','可区分预测/拟议追加测量'))]:
   s+=field(labels[z],tex(row[key][z]))
  applicable=[rr[0] for rr in RULES if row['id'] in rr[6]]
  # Range references remain in decision cards to avoid inaccurate expansion here.
  s+=r'\vfill'+field(('Evidence locator','证据定位'),r'\url{https://doi.org/'+f.refs[row['key']]['doi']+'}') if False else ''
 for ix,row in enumerate(RULES):
  s+=(r'\clearpage' if ix%2==0 else r'\bigskip\hrule\medskip')+heading(row[0]+' | '+row[1][z])
  for labels,val in [(('Competing explanations','竞争解释'),row[2][z]),(('Minimal additional measurement','最小追加测量'),row[3][z]),(('Different outcomes mean','不同结果的含义'),row[4][z]),(('Required controls','关键对照'),row[5][z]),(('Evidence anchor','证据依据'),row[6]),(('Simulation boundary','模拟适用边界'),row[7+z])]:s+=r'\medskip'+field(labels[z],tex(val))
 s+=r'\clearpage'+heading(('Computational provenance','计算结果来源')[z])
 s+=('The accompanying simulation_snapshot contains summaries and a hash manifest copied from identifiability-interventions-20261117. Recovery values refer to overlapping effective-map families, not neural architectures. Noise is transported from processed human residual blocks, while intervention effects and calibration precision are design assumptions. The current synthesis verifies and reuses the stored results.\n' if not z else '随附simulation_snapshot含从identifiability-interventions-20261117复制的摘要与哈希清单。恢复率针对相互重叠的有效映射家族，噪声来自已处理人体残差块的迁移；干预效应和校准精度为设计假设。本次综合核对并复用存档结果。\n')
 summary=json.loads((R/'simulation_snapshot/summary.json').read_text())
 s+=r'\begin{center}\small\begin{tabular}{lrr}\toprule'+'\n'+('Condition & Datasets & Recovery','条件 & 数据集数 & 恢复率')[z]+r'\\\midrule'+'\n'
 for row in summary:s+=tex(row['run'])+' & '+str(row['datasets'])+' & '+f"{row['recovery']*100:.2f}"+r'\%\\'+'\n'
 s+=r'\bottomrule\end{tabular}\end{center}'+'\n'
 s+=tex('The first four rows use five balanced generating families (20% chance reference); the last three use four (25% chance reference).' if not z else '前四行使用五个平衡生成家族（机会参照20%）；后三行使用四个（机会参照25%）。')+'\n'
 s+=heading(('Source-check notes','来源核查说明')[z])
 s+=('The preceding edition checked 25 local full texts; this revision adds the Smith et al. full text and the Franklin et al. primary study and repository records. Cluff and Scott (2013) and Makino et al. (2026) were checked through the primary-source web text. The Albert and Shadmehr correction concerns the purple displacement traces for Error 2 in Figure 2A; those traces were not digitized or used for new quantitative inference. Bibliographic titles and DOIs were reconciled against publisher/Crossref records. No percentages of alleged overclaiming were computed.\n' if not z else '前版核查25篇本地全文；本版补充Smith等全文及Franklin等原始研究与档案记录。Cluff和Scott（2013）、Makino等（2026）通过原始来源网页正文核查。Albert和Shadmehr的更正涉及图2A中Error 2的紫色位移曲线，本稿未数字化该曲线或用其进行新增定量推断。书目信息按出版社/Crossref记录校对，未计算所谓过度归因文献比例。\n')
 s+=heading(('AI disclosure','AI披露')[z])+('Language-model assistance supported extraction organization, paired drafting and document production. Observations are paraphrased with source locators; proposed tests are labelled as synthesis.\n' if not z else '语言模型辅助用于提取结果组织、双语撰写及文档制作。观察结果按原文定位转述；拟议测试标为本文综合。\n')
 s+=render_acceptance(z)
 return s.replace('simulation_snapshot',r'simulation\_snapshot')+end()
outputs={}
for z,lang in enumerate(['en','zh']):
 outputs['perspective_'+lang]=make_main(z)
 outputs['evidence_atlas_'+lang]=make_atlas(z)
keys=set()
for n,t in outputs.items():
 for c in re.findall(r'\\cite\{([^}]+)\}',t):keys.update(c.split(','))
 (R/(n+'.tex')).write_text(t,encoding='utf8')
f.bibliography(keys)
(R/'evidence_map_bilingual.json').write_text(json.dumps(ROWS,ensure_ascii=False,indent=2),encoding='utf8')
(R/'experiment_rules_bilingual.json').write_text(json.dumps(RULES,ensure_ascii=False,indent=2),encoding='utf8')
manifest={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'simulation_snapshot').glob('*.json') if p.name!='sha256.json'}
(R/'simulation_snapshot/sha256.json').write_text(json.dumps(manifest,indent=2),encoding='utf8')
(R/'claim_audit_bilingual.json').write_text(json.dumps(CLAIMS,ensure_ascii=False,indent=2),encoding='utf8')
(R/'measurement_removal_bilingual.json').write_text(json.dumps(REMOVALS,ensure_ascii=False,indent=2),encoding='utf8')
print('entries',len(ROWS),'rules',len(RULES),'references',len(keys))
print('English body words',len(re.findall(r'\b[\w-]+\b',' '.join(t[0] for h,t in SECTIONS))))
