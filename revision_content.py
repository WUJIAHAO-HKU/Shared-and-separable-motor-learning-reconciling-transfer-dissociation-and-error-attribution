"""Current scientific interpretation; numerical text loaded from completed analyses."""
from pathlib import Path
import json
R=Path(__file__).parent
def section(h,en,zh):return (h,(en,zh))
WORKED=section(('Temporal mixtures resolve the apparent contradiction','时间尺度混合如何解释表面矛盾'),r'''
Sensory-specific learning and cross-output transfer constrain different axes of the learning system. Hayashi et al. already proposed separate visual and proprioceptive memories whose outputs are integrated; Smith et al. established interacting fast and slow adaptive processes. Combining these precedents with transfer experiments yields an experimentally useful account: each input can excite several temporal modes, and each output can read a different mixture of them. The resulting impulse response is
\begin{equation}B_{ij}(k)=\sum_{r=1}^{m}h_{ir}a_r^k u_{rj}.\label{eq:worked}\end{equation}
Here $k$ indexes error-free retention steps, $a_r$ is a retention factor, $u_{rj}$ is input access to mode $r$, and $h_{ir}$ is its readout into output $i$. This construction explains how distinct sensory learning dynamics coexist with transfer into planned and corrective responses. It extends the comparison across experimental axes; the constituent memory architecture comes from the earlier studies. \cite{hayashi2020,smith2006,wagner2008,maeda2020}

Fixed readout can produce changing output ratios. For example, take $H=\left(\begin{smallmatrix}1&0.4\\0.6&1\end{smallmatrix}\right)$, $A=\operatorname{diag}(0.9,0.7)$ and $U=\left(\begin{smallmatrix}0.3&0.1\\0.15&0.5\end{smallmatrix}\right)$. With $B(k)=HA^kU$, the first input's output ratio changes from 1.091 at $k=0$ to 1.371 at $k=4$; the second changes from 0.536 to 0.713. All input and readout weights remain fixed. Each input excites both modes, whose different decay rates change the mixture over time. Constant ratios require an effectively one-dimensional trajectory for that input, for example one excited mode or proportional output loadings. Therefore a ratio change rejects that one-dimensional restriction and leaves fixed multi-mode readout viable.

The discriminating object is the complete temporal response. A two-mode common-dynamics model imposes the same characteristic roots on both outputs, while allowing arbitrary output amplitudes. An output-specific model allows different roots. For error-free measurements the former satisfies $B_{ij}(k+2)-(a_1+a_2)B_{ij}(k+1)+a_1a_2B_{ij}(k)=0$ for every measured input--output entry. Fit the common recurrence and output-specific alternatives to several training delays and predict additional delays and perturbation histories. Use independent first probes, signed errors, zero-error controls and matched sensory exposure; a ratio near a zero denominator is replaced by the joint response likelihood. Probe-driven learning enters the state transition explicitly. Two delays alone give a weak test of a flexible multi-mode account. \cite{unlearning2016}

Common temporal modes can be implemented by a shared state or duplicated, separately updated states driven by the same error. The accompanying construction reproduces all measured responses with output-specific copies. Behavioural discrimination consequently targets restrictions on temporal response families. A claim about physical sharing requires an additional intervention whose effect on one state or pathway has been independently measured. This separates a useful functional prediction from a neural implementation claim through an explicit equivalence construction.
''',r'''
感觉特异学习与跨输出迁移约束学习系统的不同维度。Hayashi等已提出分别的视觉和本体感觉记忆在输出端整合；Smith等确立了快慢适应过程的交互。将这些先例与迁移实验结合，可得到有实验价值的解释：每个输入能够激发多个时间模式，每个输出读取这些模式的不同比例。相应的脉冲响应为
\begin{equation}B_{ij}(k)=\sum_{r=1}^{m}h_{ir}a_r^k u_{rj}.\label{eq:worked}\end{equation}
其中$k$表示无误差保持步数，$a_r$为保持系数，$u_{rj}$表示输入对模式$r$的作用，$h_{ir}$表示该模式对输出$i$的贡献。这一构造解释了不同感觉学习动态如何与向预期运动、纠错响应的迁移并存。本文将比较扩展到多个实验轴；记忆架构的组成来自前人研究。\cite{hayashi2020,smith2006,wagner2008,maeda2020}

固定读出能够产生变化的输出比例。例如，令$H=\left(\begin{smallmatrix}1&0.4\\0.6&1\end{smallmatrix}\right)$、$A=\operatorname{diag}(0.9,0.7)$、$U=\left(\begin{smallmatrix}0.3&0.1\\0.15&0.5\end{smallmatrix}\right)$。在$B(k)=HA^kU$中，第一个输入的输出比例从$k=0$时的1.091变为$k=4$时的1.371；第二个从0.536变为0.713。输入和读出权重始终固定。每个输入激发两种模式，不同衰减率改变其随时间的混合比例。比例恒定要求该输入形成有效一维轨迹，例如只激发一种模式或输出载荷成比例。因此，比例变化排除这一维度限制，并保留固定多模式读出的解释。

判别对象应是完整时间响应。双模式共同动力学模型要求两个输出具有相同特征根，同时允许任意输出幅度；输出特异模型允许不同特征根。在无误差测量中，前者要求所有输入—输出条目满足$B_{ij}(k+2)-(a_1+a_2)B_{ij}(k+1)+a_1a_2B_{ij}(k)=0$。使用多个训练延迟拟合共同递推与输出特异竞争模型，再预测额外延迟及扰动历史。采用独立首次探针、有符号误差、零误差对照及匹配感觉暴露；分母接近零时使用联合响应似然。探针诱发学习须显式进入状态转移。两个延迟对灵活多模式解释的约束较弱。\cite{unlearning2016}

共同时间模式既可由共享状态实现，也可由接收同一误差、分别更新的复制状态实现。随附构造使用输出特异的状态副本复现全部测量响应。因此，行为判别检验的是时间响应家族的限制。物理共享主张需要增加对某个状态或通路作用已被独立测量的干预。显式等价构造据此区分可检验的功能预测与神经实现主张。
''')
CALIBRATION=section(('Perceptual calibration is itself a measurement model','感觉校准本身也是测量模型'),r'''
Localization supplies an additional outcome with its own learning dependence. Gastrock et al. measured active and passive localization separately: active movement combines afferent information with movement-related predictions. Their design provides a direct reason to include both input-related and update-related contributions to a report. In local contrast coordinates, write
\begin{align}\delta y&=I+U, &\delta\ell&=C I+L U.\label{eq:calibration}\end{align}
The symbols denote condition contrasts after physical error has been specified; $C$ and $L$ are report loadings. A single report cannot identify both contrasts when these loadings are unknown. Even with known loadings, $C=L$ makes the two measurements redundant. Setting $C=1,L=0$ assigns every report change to input recalibration and therefore builds selectivity into the observation model. \cite{external2020,hayashi2020}

The consequence is quantitative. If true updating changes by $D$ and the report has loading $L=1$, then $(\delta y,\delta\ell)=(D,D)$. The selective-report model fits these data exactly with an input change $I=D$ and no update change. Our stress test samples pure and mixed contrasts under graded cross-loading; fitting the wrong observation model produces this false attribution even with precise measurements. Measuring $C$ and $L$ independently restores separation when the resulting observation matrix has adequate singular values. As the two loadings approach equality, uncertainty in the factor estimates grows. Additional repetitions cannot remove the exact rank deficiency at equality.

We downloaded the public localization archive and reanalysed the authors' spatially interpolated participant estimates. Averaging the three reported directions, the active-minus-passive adaptation shift in the control group was $-1.54^\circ$ (participant-bootstrap 95\% interval $[-2.91,-0.12]$, $n=20$); in the hand-view group it was $-0.02^\circ$ ($[-0.86,0.81]$, $n=29$). The direct between-group contrast was $1.52^\circ$ ($[-0.14,3.13]$). The within-group contrast establishes that the two report procedures can yield different adaptation shifts; the between-group interval leaves the size of the hand-view effect uncertain. These estimates retain the deposited angular sign convention. Active--passive subtraction measures a report contrast whose attribution to a single neural component depends on the observation model. \cite{external2020}

For an input-versus-update dispute, calibrate reports using sensory discrepancies during passive exposure, active movements with matched kinematics, and error-free cue switches. Fit their joint observation model and predict reports in an untrained context before transferring the calibration to learning. Passive exposure can itself recalibrate perception; its contribution must be measured through pre/post reports and motor aftereffects. Cross-loading remains a free parameter unless an independent manipulation constrains it. The experiment supports factor-specific inference when those constraints yield separated held-out predictions; otherwise its resolved quantity is the joint input-to-report-and-motor response.
''',r'''
定位提供具有自身学习依赖性的额外结果。Gastrock等分别测量主动和被动定位：主动运动将传入信息与运动相关预测结合。这一设计直接支持在报告模型中同时纳入输入和更新相关贡献。在局部差异坐标下，可写为
\begin{align}\delta y&=I+U, &\delta\ell&=C I+L U.\label{eq:calibration}\end{align}
各符号表示物理误差已确定后的条件差异，$C$与$L$为报告载荷。载荷未知时，单项报告无法辨识两种差异；即使载荷已知，$C=L$也使两项测量冗余。设定$C=1,L=0$会把所有报告变化归为输入重校准，从而在观测模型中预置选择性。\cite{external2020,hayashi2020}

其后果可以定量展示。若真实更新变化为$D$、报告载荷$L=1$，则$(\delta y,\delta\ell)=(D,D)$；选择性报告模型用输入变化$I=D$及零更新变化即可精确拟合。新增压力测试在不同交叉载荷下抽取纯机制与混合差异；错误观测模型在测量精确时仍产生这种误判。独立测量$C$和$L$，并使相应观测矩阵具有足够大的奇异值，才可恢复分离。两种载荷趋近时，因子估计的不确定性增长；增加重复无法消除载荷相等时的精确秩亏。

我们下载公开定位档案，重新分析作者按空间插值得到的参与者估计。平均三个报告方向后，对照组主动减被动的适应变化为$-1.54^\circ$（参与者自助法95\%区间$[-2.91,-0.12]$，$n=20$）；手可见组为$-0.02^\circ$（$[-0.86,0.81]$，$n=29$）。直接组间差异为$1.52^\circ$（$[-0.14,3.13]$）。组内对比确立两种报告程序能够产生不同适应变化；组间区间保留手可见效应幅度的不确定性。估计保留档案的角度符号约定。主动减被动得到报告层差异，将其归于单一神经成分依赖观测模型。\cite{external2020}

针对输入与更新争议，应结合被动暴露中的感觉偏差、运动学匹配的主动运动及无误差线索切换校准报告。拟合联合观测模型，先预测未训练情境中的报告，再将校准迁移至学习。被动暴露本身能够重校准感知，其贡献须通过前后报告及运动后效测量。交叉载荷应作为自由参数，直至独立操纵提供约束。约束使留出预测分离时，实验支持因子特异推断；否则，已解析的量是输入到报告及运动的联合响应。
''')
EXPERIMENT=section(('Choosing an experiment by the restriction it tests','按所检验的限制选择实验'),r'''
Each experiment-selection rule starts from an explicit restriction on competing models (Table~\ref{tab:rules}). For the delay dispute, compare a one-mode response, two common temporal modes with mixed readout, and output-specific temporal modes. Measure both outputs at enough independent delays to fit the candidate order and reserve further delays or histories for prediction. Common dynamics predict shared characteristic roots; separate dynamics can deviate from that recurrence. Removing a delay reduces temporal constraints, while removing an output eliminates the cross-output comparison. A shared fit remains compatible with duplicated states. Consequently the design targets common temporal dynamics, and its sample size must follow the predictive separation observed in pilot data.

For the input-versus-update dispute, add active and passive reports with an independently tested cross-loading model. The relevant contrast is a held-out report-and-motor prediction after calibration uncertainty is propagated. A report-only fit with freely interchangeable input and update contributions returns a compatible set. Removing the independent loading constraints restores an exact continuum of decompositions, even when both reports remain. Adding a report is informative when its loading supplies a distinct, measured direction in observation space.

For acquisition versus expression, cross training and test cues and read the first probe before new error. Maintain matched sensory exposure, delay, speed, background EMG and probe compliance. Test-cue effects provide an expression contrast; retained training effects can include both learned state and persistent sensory change. For mechanics versus neural control, add latency-resolved force, EMG and independent impedance probes. These measurements have different inferential jobs, so the complete matrix battery is reserved for claims involving both sensory inputs and both control outputs. \cite{coin2021,franklin2003,unlearning2016}

Minimum size is determined for a defined model pair, detectable effect and validated observation model. Our cross-study and recovery analyses below assess a specific two-output temporal comparison. The broader delay-by-input and cross-loaded perceptual design is an experiment to be tested with matching data; the existing human archives measure complementary parts of it. A proposal advances to human sampling when the candidate predictive intervals separate under empirical repeatability, the planned ablation removes that separation, and all source-locked models have been optimized on the same training observations.
''',r'''
每项实验选择规则都从竞争模型的明确限制出发（表\ref{tab:rules}）。针对延迟争议，比较单模式响应、混合读出的双共同时间模式及输出特异时间模式。在足够多的独立延迟测量两个输出，以拟合候选阶数，并留出额外延迟或历史用于预测。共同动力学预测共享特征根，分别动力学能够偏离该递推关系。删除延迟会减少时间约束，删除输出会消除跨输出比较。共同拟合仍兼容复制状态。因此，该设计检验共同时间动力学，样本量由先导数据中的预测分离程度决定。

针对输入与更新争议，增加主动、被动报告，并独立检验交叉载荷模型。关键对比是在传播校准不确定性后，预测留出的报告与运动响应。若仅拟合报告且输入、更新贡献能够自由互换，则得到兼容集合。删除独立载荷约束，即使保留两项报告，也会恢复连续的等价分解。额外报告的价值来自其载荷提供了一个不同且经过测量的观测方向。

针对获得与表达，交叉训练及测试线索，在新误差之前读取首次探针。匹配感觉暴露、延迟、速度、背景肌电和探针柔顺性。测试线索效应提供表达对比；保留的训练效应能够包含已学习状态与持续感觉变化。针对力学与神经控制，增加按潜伏期分解的力、肌电及独立阻抗探针。各测量承担不同推断任务，涉及两个感觉输入及两个控制输出的主张才采用完整矩阵测量。\cite{coin2021,franklin2003,unlearning2016}

最小规模相对于明确模型对、可检出效应及已验证观测模型确定。下文跨研究预测和恢复分析检验一个具体的双输出时间比较。更广的延迟乘输入及交叉载荷感觉设计，需要对应数据检验；已有公开人体档案测量其中互补的部分。当候选预测区间在实测重复精度下分离、计划消融会消除该分离，并且所有模型均在相同训练观测上完成优化时，方案具备推进人体采样的依据。
''')
def empirical():
 d=json.loads((R/'analysis/crossstudy_summary.json').read_text());rec=json.loads((R/'analysis/recovery.json').read_text())
 conf=rec['confusion'];accuracy=sum(conf[i][i] for i in range(4))/rec['n']*100
 def c(s,a,b):return next(x for x in d['contrasts'] if x['source']==s and x['window']=='180_230' and x['variant']=='source_cv_ridge' and x['a']==a and x['b']==b)
 def v(x):return f"{x['delta_b_minus_a']:.3f} [{x['ci95'][0]:.3f}, {x['ci95'][1]:.3f}]"
 x=c('visual_errors','shared_two_mixed','separate_two');y=c('visual_clamp','shared_two_mixed','separate_two');a=c('visual_errors','shared_one','shared_two_mixed');b=c('visual_clamp','shared_one','shared_two_mixed')
 en=r'''
We tested temporal-response transport using two public force-field studies with visual error information available or removed during adaptation (12 participants per study). Both contain abrupt and gradual field schedules, channel compensation and visually evoked force. We reconstructed the archived block observations and used each entire study as the source for predicting the other. Source-participant cross-validation selects regularization; all dynamic parameters and output coefficients are frozen before target scoring. Target pre-exposure means supply baseline calibration, with source-baseline-only prediction reported as a sensitivity analysis. The primary response window is 180--230 ms; 230--300 ms is reported separately. The two conditions are drawn from separate cohorts, so transport evaluates study change together with sensory change. \cite{franklin2021,franklin2023}

Four candidates compare one common mode (three parameters), one mode per output (four), two common modes with mixed readout (six), and two modes per output (eight). In block coordinates, $z_{r,t+1}=p_rz_{r,t}+(1-p_r)f_t$ and $y_{i,t}=\sum_r c_{ir}(z_{r,t}+z_{r,t+1})/2$. All candidates use the same field schedule, initialization, stable-pole range, observation timing and source-derived output scales. The poles describe effective closed-loop block persistence; their neural retention and error-sensitivity factors are not separately measured. Two close poles use a divided-difference basis with its derivative limit, avoiding cancellation by huge opposing coefficients. Linear coefficients are solved exactly conditional on poles; final fits use 64 starts. Ridge strength is chosen from the same five values by six source-participant folds, and unpenalized predictions are retained. A pre-exposure baseline and a source phase-mean template provide simple comparators.

In the primary window, adding a second common mode changed standardized prediction MSE by @A@ for visual-error to visual-clamp transport and @B@ in the reverse direction. The separate-two minus common-two differences were @X@ and @Y@, respectively. Brackets give paired target-participant bootstrap 95\% intervals conditional on the trained source. In visual-error to visual-clamp transport, the regularized comparison favours separate modes in the primary window; the direction reverses in the secondary window, and the unpenalized comparisons overlap zero. The reverse-study primary comparison also overlaps zero. Architecture ranking therefore depends on the observation window and penalty. The joint improvement from temporal complexity is concentrated in compensation; feedback-force RMSE remains approximately 1.8--2.0 N, and the phase template performs competitively for that output. Thus the measurable predictive gain concerns temporal response richness, while this comparison resolves little about shared versus separate modes. Full endpoint scores, the second window, baseline transport and unpenalized fits accompany the atlas.

Fresh-instance recovery used the source-fitted families, perturbed parameters, and paired five-block resampling of human residual trajectories. Each synthetic group averages twelve participant residual draws; both channels retain their pairing and short temporal dependence. Candidates fit abrupt exposure and predict gradual exposure. Forced family assignment recovered @ACC@\% across 80 instances (20 per family; balanced chance reference 25\%). The confusion matrix is reported without converting near-equivalent predictions into a shared-storage claim. Exact output-specific copies of common modes remain observationally equivalent independently of noise or optimizer accuracy. This recovery exercise measures practical discrimination among effective kernel families in this protocol.
'''
 zh=r'''
我们用两项公开力场研究检验时间响应的跨研究迁移：适应中保留或移除视觉误差信息，每项研究12人。两项均包含突然及渐变力场、通道补偿与视觉诱发力。我们重建存档块级观测，依次用完整一项研究训练并预测另一项。正则化由来源研究的参与者交叉验证选择；目标评分前冻结全部动力学参数及输出系数。目标暴露前均值用于基线校准，同时报告完全沿用来源基线的敏感性分析。主要响应窗为180--230 ms，另行报告230--300 ms。两种条件来自不同队列，迁移同时检验研究变化及感觉变化。\cite{franklin2021,franklin2023}

四个候选分别为单共同模式（三参数）、每输出单模式（四参数）、混合读出的双共同模式（六参数）及每输出双模式（八参数）。块级方程为$z_{r,t+1}=p_rz_{r,t}+(1-p_r)f_t$及$y_{i,t}=\sum_r c_{ir}(z_{r,t}+z_{r,t+1})/2$。全部候选使用相同力场序列、初始状态、稳定极点范围、观测时序及来源数据输出尺度。极点表示有效闭环块级持续性，其神经保持与误差敏感性因子未被分别测量。接近的双极点采用差商基底及其导数极限，避免巨大正负系数抵消。给定极点时精确求解线性系数；最终拟合采用64个初值。正则强度通过来源参与者六折验证从相同五值中选择，同时保留无正则预测。暴露前基线与来源研究的阶段均值模板提供简单比较对象。

主要时间窗中，增加第二共同模式使标准化预测MSE在视觉误差研究预测视觉钳制研究时改变@A@，反方向改变@B@。双分别模式减双共同模式的差异依次为@X@及@Y@。括号为固定已训练来源模型、按目标参与者配对自助法得到的95\%区间。从视觉误差研究预测视觉钳制研究时，正则比较在主要时间窗支持分别模式，第二时间窗方向反转，无正则比较则跨越零；反方向研究的主要时间窗差异也跨越零。因此，架构排序依赖观测时间窗及正则设定。时间复杂性带来的联合改善主要集中于补偿；反馈力RMSE约为1.8--2.0 N，阶段模板在该输出上也具有竞争力。因此，实测预测收益涉及时间响应的丰富性，这一比较对共享与分别模式的分辨较弱。图谱附完整分输出评分、第二时间窗、基线迁移及无正则拟合。

新增实例恢复使用来源拟合家族、扰动后的参数及人体残差轨迹的配对五块重采样。每个合成组平均十二份参与者残差抽样，保留双通道配对及短时依赖。候选拟合突然暴露并预测渐变暴露。80个实例（每家族20个，平衡机会参照25\%）的强制家族分类恢复率为@ACC@\%。混淆矩阵完整报告，近等价预测不被转换为共享存储结论。共同模式的输出特异副本在任何噪声或优化精度下均保持观测等价。这一恢复实验测量该方案中有效时间核家族的实际可分性。
'''
 for key,val in [('@A@',v(a)),('@B@',v(b)),('@X@',v(x)),('@Y@',v(y)),('@ACC@',f'{accuracy:.1f}')]:en=en.replace(key,val);zh=zh.replace(key,val)
 return section(('Frozen predictions across public human studies','公开人体研究之间的冻结参数预测'),en,zh)
ABSTRACT=('Similar adaptive movements can arise from different learning mechanisms. This Perspective integrates evidence on transfer, dissociation, error attribution and sensory specificity across inputs, outputs and timescales. Worked examples show how temporal mixing and perceptual measurements shape mechanistic inference. Public-data reanalyses illustrate cross-study prediction and its limits: additional temporal components improve compensation prediction, while common-versus-separate model rankings vary with analysis settings. An evidence map connects competing explanations to targeted measurements, controls and predictions. The framework guides experimental choices in motor neuroscience and offers a prospective approach to evaluating embodied controllers with similar task performance.',
'相似的适应动作可以由不同学习机制产生。本文沿输入、输出和时间尺度整合迁移、分离、误差归因及感觉特异性证据。具体案例展示时间混合与感知测量如何影响机制推断。公开数据重分析说明跨研究预测及其边界：增加时间成分改善补偿预测，共同与分别模型的排序随分析设定变化。证据地图将竞争解释连接到针对性测量、对照和预测。该框架指导运动神经科学中的实验选择，并为评估任务表现相似的具身控制器提供前瞻性方法。')

def revise(sections):
 out=[]
 for h,t in sections:
  if h[0]=='A resolved contradiction and its new prediction':out.append(WORKED)
  elif h[0]=='What each measurement makes identifiable':out.append(CALIBRATION)
  elif h[0]=='Selecting the smallest informative experiment':out.append(EXPERIMENT)
  elif h[0]=='Simulation calibration defines the reach of the rules':out.append(empirical())
  else:out.append((h,t))
 # Introduce the observation model before the rules that rely on it.
 cal=next(x for x in out if x[0][0]=='Perceptual calibration is itself a measurement model')
 out.remove(cal);ix=next(i for i,x in enumerate(out) if x[0][0]=='Choosing an experiment by the restriction it tests');out.insert(ix,cal)
 return out
