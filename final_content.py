"""Final Perspective argument. Analysis results remain unchanged."""
ABSTRACT = (
'''Motor learning transfers between planned actions and corrective responses, yet also separates across sensory channels and contexts. We argue that these findings describe coupling at different stages of learning. Integrating evidence across sensory inputs, control outputs and timescales explains how separable memories can support shared behaviour. Two worked cases show how temporal mixing and perceptual reporting change the measurements needed to distinguish explanations. Public-data reanalyses support richer temporal responses while exposing unstable architecture rankings. An experiment-level evidence map translates this synthesis into competing predictions, essential controls and targeted measurements for motor neuroscience and embodied control.''',
'''运动学习能够在计划动作与纠错响应之间迁移，也会随感觉通道和情境表现出分离。本文认为，这些发现反映了学习不同环节的耦合。沿感觉输入、控制输出和时间尺度整合证据，可以解释可分离记忆如何支持共同的行为输出。两个具体案例展示时间混合及感知报告如何改变区分竞争解释所需的测量。公开数据重分析支持更丰富的时间响应，同时揭示架构排序对分析设定的依赖。逐实验证据地图将这一综合转化为竞争预测、必要对照及针对性测量，为运动神经科学与具身控制提供实验选择依据。''')

INTRO = (r'''
Learning a sideways force field changes both the forces prepared before a reach and the corrections made during it. Other experiments selectively alter one response or reveal memories specific to vision and proprioception. Together, these findings ask how learning can be shared across actions while remaining separable across inputs and conditions. Force-field adaptation makes this question concrete: channel trials measure anticipatory compensation, perturbations reveal feedback responses, and muscle activity constrains the contribution of body mechanics. \cite{wagner2008,maeda2018,yousif2012,hayashi2020}

We argue that sharing is a relation that must be specified across sensory inputs, control outputs and timescales. Distinct sensory learning processes can contribute to both planned and corrective actions. Their relative contributions depend on error attribution, retention and the context in which a memory is expressed. This organization explains why transfer and dissociation can coexist: the same learning system can couple outputs under one comparison and separate them under another.

The practical consequence is a change in what experiments compare. A transfer result motivates a crossed training--test-context comparison; a changing output ratio motivates paired temporal responses; a localization shift motivates independent calibration of what the report measures. We develop these consequences through the force-field case, connect them to a 29-entry evidence map, and use worked constructions and public-data reanalyses to establish which distinctions each measurement can resolve. The resulting contribution is an explicit route from an apparent contradiction to a competing prediction and an experimental choice.
''',r'''
学习侧向力场会同时改变到达运动前准备的力与运动中的纠错响应。另一些实验能够选择性地改变其中一种响应，或揭示视觉、本体感觉特异的记忆。这些发现共同提出一个问题：学习如何在动作之间共享，同时又在输入和条件之间保持可分离性？力场适应使问题具体可测：通道试次测量预期补偿，扰动揭示反馈响应，肌肉活动约束身体力学的贡献。\cite{wagner2008,maeda2018,yousif2012,hayashi2020}

本文提出，共享是一种需要沿感觉输入、控制输出和时间尺度明确界定的关系。不同感觉学习过程能够共同影响计划动作与纠错响应，各自的贡献取决于误差归因、保持过程及记忆表达的情境。这一组织方式解释了迁移与分离为何能够并存：同一学习系统可以在一种比较下表现出输出耦合，在另一种比较下表现出分离。

这一观点直接改变实验应当比较的对象。迁移结果引出训练与测试情境的交叉比较，变化的输出比例引出配对时间响应，定位偏移引出对报告测量对象的独立校准。本文以力场案例展开这些后果，将其连接到29项逐实验证据，并通过构造案例和公开数据重分析确立不同测量能够解决的区分。由此形成的贡献，是将表面矛盾连接到竞争预测和实验选择的明确路径。
''')

INCREMENT = (r'''
The synthesis links three established advances. Hayashi et al. showed how sensory-specific memories can combine at output; Smith et al. established interacting adaptation processes with different timescales; Heald et al. explained how contextual inference changes memory updating and expression. Transfer experiments constrain a further axis: learned dynamics influence both anticipatory and corrective control. Each contribution identifies a different relation within learning. Their conjunction yields a specific account of the apparent contradiction: sensory-specific acquisition can coexist with cross-output access, while temporal mixtures and context determine the expression of that access. \cite{hayashi2020,smith2006,coin2021,wagner2008,maeda2020}

The increment is the connection from this joint account to observations that adjudicate among explanations. Consider an early transfer effect followed by a later dissociation. Separate discussion of the studies leaves both shared and separate learning accounts available. The integrated account first asks whether the two studies changed input, test context or measurement delay. At a common input and context, it then asks whether fixed mixtures of fast and slow components reproduce the dissociation. If they do, the decisive comparison becomes a prediction of paired responses at new delays. If the dissociation instead follows the test cue on the first error-free probe, expression becomes the relevant experimental contrast. This progression gives the same observed dissociation different, testable meanings according to the intervention that produced it.

Three changes in experimental inference follow (Table~\ref{tab:synthesis}). An output ratio is replaced by a joint temporal response when multiple timescales are plausible. A perceptual report constrains input-versus-update accounts through measured report loadings. A transfer measurement is interpreted through the separation of training and test contexts. The following sections work through the first two cases and connect all three to experiment-selection rules. The framework's added value is the choice of the next informative comparison, grounded in the controls and observations of the original studies.
''',r'''
这一综合连接了三项已确立的进展。Hayashi等展示了感觉特异记忆如何在输出端整合；Smith等确立了不同时间尺度适应过程的交互；Heald等解释了情境推断如何改变记忆更新与表达。迁移实验进一步约束另一维度：已学动力学同时影响预期控制与纠错控制。每项进展分别揭示学习内部的一种关系，将它们结合便得到对表面矛盾的具体解释：感觉特异的获得过程可以与跨输出调用并存，时间混合和情境共同决定这种调用如何表现。\cite{hayashi2020,smith2006,coin2021,wagner2008,maeda2020}

本文的增量在于，将这一联合解释连接到能够裁决竞争解释的观测。以早期迁移、晚期分离为例，逐篇讨论仍会同时保留共享学习和分别学习。整合解释首先检查两项研究是否改变了输入、测试情境或测量延迟。在输入与情境相同的条件下，进一步检验快慢成分的固定混合能否复现分离。若能够复现，关键比较就转为对新延迟下配对响应的预测。若分离在首次无误差探针中随测试线索改变，表达过程就成为相应实验的比较对象。这样，同一项分离观察会根据产生它的干预，获得不同且可检验的含义。

由此得到三项实验推断上的改变（表~\ref{tab:synthesis}）：存在多个时间尺度时，使用联合时间响应替代单个输出比例；通过独立测得的报告载荷，用感知报告约束输入与更新解释；通过区分训练和测试情境，解释迁移测量。后文详细展开前两个案例，并将三项改变共同连接到实验选择规则。这一框架增加的价值，是依据原研究的对照与观测，明确选择下一项有判别力的比较。
''')

WORKED = (r'''
Distinct sensory memories can contribute to both anticipatory compensation and feedback correction. Each contribution can contain fast and slow components. Consequently, a component that dominates early transfer may decay before a later probe, changing the relationship between outputs while every readout weight remains fixed. This is a concrete mechanism by which transfer and dissociation arise within one architecture. \cite{hayashi2020,smith2006}

In a two-mode worked example, both sensory inputs excite both modes, and the outputs read fixed mixtures. One input's output ratio changes from 1.091 immediately after learning to 1.371 after four error-free retention steps; the other changes from 0.536 to 0.713. The complete matrices and calculation appear in Supplementary Methods SM1. The changing ratio identifies a departure from an effectively one-dimensional response. A fixed mixture of multiple temporal components remains compatible with the observation.

The next experiment therefore measures both outputs at several independent delays and predicts reserved delays or perturbation histories. A model with common temporal modes requires the same decay factors to explain both outputs, with different amplitudes allowed; output-specific modes permit different decay factors. Their predictions should be evaluated at matched sensory exposure, context and mechanics, using independent first probes to measure retention before probe-induced learning. The common recurrence and its measurement requirements are given in SM1. \cite{unlearning2016}

This comparison assigns a precise meaning to temporal coupling. A successful common-mode prediction establishes a common description of measured dynamics. Independently targeted pathway interventions are required to localize the states implementing those dynamics, because shared states and synchronized output-specific copies can reproduce the same response. The experimental decision follows the intended claim: temporal measurements constrain response dynamics; selective interventions constrain neural implementation.
''',r'''
不同感觉记忆可以共同贡献于预期补偿和反馈纠错，每项贡献又可以包含快慢成分。因此，主导早期迁移的成分可能在较晚探针前衰减，在所有读出权重保持固定时改变两个输出的关系。这提供了同一架构中同时产生迁移与分离的具体机制。\cite{hayashi2020,smith2006}

在双模式构造案例中，两个感觉输入均激发两种模式，两个输出读取固定混合。一个输入的输出比例从学习后即刻的1.091变为四个无误差保持步后的1.371，另一个从0.536变为0.713。完整矩阵及计算见补充方法SM1。比例变化表明响应偏离有效一维形式，多种时间成分的固定混合仍与观察相容。

因此，下一步实验应在多个独立延迟测量两个输出，并预测留出的延迟或扰动历史。共同时间模式模型要求同一组衰减因子解释两个输出，同时允许不同幅度；输出特异模式允许不同衰减因子。在匹配感觉暴露、情境和力学的条件下评价预测，并使用独立首次探针，在探针诱发学习前测量保持。共同递推关系及其测量要求见SM1。\cite{unlearning2016}

这一比较为时间耦合赋予明确含义。共同模式的成功预测确立了对测得动态的共同描述。定位实现这些动态的状态，需要独立靶向的通路干预，因为共享状态与同步的输出特异副本可以复现相同响应。实验选择由目标主张决定：时间测量约束响应动态，选择性干预约束神经实现。
''')

CALIBRATION = (r'''
A change in sensory reliability can alter the error represented by the learner, the update made from that error, or the perceptual report used to estimate it. Gastrock et al. measured active and passive localization separately, providing a way to compare reports with different access to afferent and movement-related information. For a local contrast, let the motor change be the sum of an input contribution $I$ and an update contribution $U$, and let the report contain measured loadings $C$ and $L$:
\begin{align}\delta y&=I+U, &\delta\ell&=CI+LU.\label{eq:calibration}\end{align}
The loadings determine which component the additional report can resolve. Equal loadings make it redundant with the motor measurement; distinct, independently measured loadings permit separation. \cite{external2020,hayashi2020}

This distinction changes the inference even with precise data. When an update changes both action and report equally, assigning every report change to sensory recalibration produces an exact fit with the wrong factor attribution. The worked cross-loading examples in SM2 demonstrate this ambiguity and propagate it into parameter estimates. The useful addition is therefore a report with a calibrated contribution from each candidate process.

Public localization data illustrate why report composition matters (Fig.~3d). The active-minus-passive adaptation shift was $-1.54^\circ$ in the control group (participant-bootstrap 95\% interval $[-2.91,-0.12]$, $n=20$) and $-0.02^\circ$ in the hand-view group ($[-0.86,0.81]$, $n=29$). The direct group contrast was $1.52^\circ$ ($[-0.14,3.13]$). These observations establish a difference between report procedures within the control group; the group contrast includes zero. The appropriate next comparison measures how each procedure combines sensory and movement-related information. \cite{external2020}

Calibrate reports using passive sensory discrepancies, active movements with matched kinematics and error-free cue switches, then predict reports in an untrained context. Measure perceptual and motor changes induced by calibration itself. Propagating the resulting loading uncertainty into held-out report-and-motor predictions tests whether input and update accounts are distinguishable. With free or collinear loadings, the resolved quantity is the joint response rather than its individual factors. This measurement requirement gives sensory-specific learning and error-attribution experiments a common interpretive test.
''',r'''
感觉可靠性变化可以改变学习者表征的误差、由误差产生的更新，或用于估计误差的感知报告。Gastrock等分别测量主动与被动定位，由此可以比较对传入信息和运动相关信息具有不同访问方式的报告。对局部条件差异，令运动变化为输入贡献$I$与更新贡献$U$之和，并令报告具有经测量确定的载荷$C$与$L$：
\begin{align}\delta y&=I+U, &\delta\ell&=CI+LU.\label{eq:calibration}\end{align}
载荷决定追加报告能够分辨哪个成分。相同载荷使报告与运动测量冗余，独立测得且不同的载荷允许分离两个成分。\cite{external2020,hayashi2020}

即使数据精确，这一区别也会改变推断。当更新同等改变动作和报告时，把全部报告变化归为感觉重校准，会以错误的因子归因精确拟合数据。SM2中的交叉载荷案例展示了这一歧义及其对参数估计的影响。因此，有用的追加测量是对各候选过程贡献经过校准的报告。

公开定位数据说明报告组成为何重要（图3d）。对照组主动减被动的适应偏移为$-1.54^\circ$（参与者自助法95\%区间$[-2.91,-0.12]$，$n=20$），手部可见组为$-0.02^\circ$（$[-0.86,0.81]$，$n=29$）。直接组间对比为$1.52^\circ$（$[-0.14,3.13]$）。这些观察确立了对照组内两种报告程序的差异；组间对比区间包含零。相应的下一步比较，应测量每种程序如何结合感觉与运动相关信息。\cite{external2020}

通过被动感觉差异、运动学匹配的主动运动及无误差线索切换校准报告，再预测未训练情境中的报告。同时测量校准本身诱发的感知与运动变化，将载荷不确定性传递到报告与运动的联合留出预测，检验输入和更新解释能否分离。载荷自由变化或共线时，可以确定的是联合响应。该测量要求为感觉特异学习和误差归因实验提供了共同的解释检验。
''')

PUBLIC = (r'''
Two public force-field studies provide a test of how much temporal structure transports between experiments: one retained visual error information during adaptation and the other removed it (12 participants each). Both measured channel compensation and visually evoked force during abrupt and gradual field schedules. We compared one or two temporal modes, either common to both outputs or fitted separately. All models used the same source observations; parameter fitting and penalty selection preceded scoring on the other study's post-exposure data. These are retrospective predictions across studies. Supplementary Methods SM3 reports observation windows, baseline calibration, fitting, uncertainty and recovery procedures. \cite{franklin2021,franklin2023}

The strongest transported feature was temporal complexity (Fig.~3a,b). Adding a second common mode reduced joint standardized prediction MSE by 0.850 (95\% interval 0.472--1.296) from visual-error to visual-clamp training and by 0.459 (0.292--0.627) in the reverse direction. The gain was concentrated in anticipatory compensation. Feedback-force RMSE remained approximately 1.8--2.0 N, with a source phase template performing competitively. The result directs attention to the output carrying the predictive information: an improved joint score can be driven by the compensation trajectory.

Architecture ranking depended on how feedback was observed and models were regularized (Fig.~3c). In the primary window, separate-two minus common-two MSE was $-0.040$ (95\% interval $[-0.075,-0.002]$) in one transport direction and $-0.009$ ($[-0.027,0.008]$) in the reverse. The first direction changed sign in the secondary window, and unpenalized contrasts included zero. Thus the stable empirical finding is a richer compensation response; selecting a shared or output-specific organization requires predictions that remain separated across measurement choices. Complete endpoint scores and all comparisons remain in the Supplementary Evidence Atlas.

Fresh-instance recovery further localizes the available information. Under human residual noise, fitting abrupt exposure and predicting gradual exposure recovered 41 of 80 generating labels (51.2\%; four balanced families). Recovery was 7/20 and 4/20 for the one-mode common and separate families, respectively, and 15/20 for each two-mode family. This pattern supports a protocol-specific distinction in response complexity while showing uneven architecture discrimination. In addition, exact duplicated states can reproduce a common-state response. Together, prediction and recovery motivate the same experimental priority: measure joint responses under interventions that make the surviving explanations diverge.
''',r'''
两项公开力场研究可用于检验时间结构在实验之间的可迁移性：一项在适应中保留视觉误差信息，另一项移除该信息，每项12名参与者。两项均在突然和渐变力场序列中测量通道补偿及视觉诱发力。我们比较单个或两个时间模式，并分别设为两输出共同或各自拟合。全部模型使用相同来源观测，在另一研究暴露后数据评分之前完成参数拟合和惩罚项选择。这些比较属于回顾性的跨研究预测。补充方法SM3说明测量窗口、基线校准、拟合、不确定性及恢复程序。\cite{franklin2021,franklin2023}

迁移最稳定的特征是时间复杂度（图3a、b）。从视觉误差训练预测视觉钳制训练时，增加第二个共同模式使联合标准化预测MSE下降0.850（95\%区间0.472--1.296）；反向预测下降0.459（0.292--0.627）。改善集中于预期补偿。反馈力RMSE约为1.8--2.0 N，来源阶段均值模板具有相近的预测表现。结果将注意力定位到实际提供预测信息的输出：联合评分的改善可以由补偿轨迹驱动。

架构排序取决于反馈测量方式和模型正则化（图3c）。主窗口中，一个迁移方向的双分别减双共同模式MSE为$-0.040$（95\%区间$[-0.075,-0.002]$），反向为$-0.009$（$[-0.027,0.008]$）。前一方向在第二窗口改变符号，无正则对比区间均包含零。因此，稳定的经验发现是更丰富的补偿响应；选择共享或输出特异的组织方式，需要在不同测量选择下仍然分离的预测。补充证据图谱保留全部分输出评分和对比。

新实例恢复进一步定位了现有信息。在人体残差噪声下，拟合突然暴露、预测渐变暴露，共恢复80个生成标签中的41个（51.2\%；四个平衡家族）。单共同与单分别家族分别恢复7/20和4/20，两个双模式家族各恢复15/20。这一模式支持特定方案中的响应复杂度区分，同时显示架构判别能力并不均衡。此外，精确复制状态可以复现共同状态响应。预测与恢复共同指向同一实验优先项：在使剩余解释产生分歧的干预下，测量联合响应。
''')

OUTLOOK = (r'''
The synthesis yields a focused research agenda: locate the coupling that allows sensory-specific learning to influence planned and corrective actions. Three comparisons carry this agenda. Crossed training and test contexts identify when transfer depends on memory expression. Paired responses across delays test whether a changing transfer pattern follows common temporal components. Independently calibrated perceptual reports test whether sensory changes account for altered learning. Each comparison connects a particular uncertainty in the literature to a predicted consequence and a necessary measurement.

The strongest next biological test would combine distinct visual and proprioceptive errors with both anticipatory and corrective readouts, sampled under a common test context at reserved delays. Distinct input learning profiles together with cross-output transfer would support sensory-specific acquisition with convergent control consequences. Predicting those joint responses with fixed mixed readout would explain a delay-dependent dissociation within that architecture. Systematic held-out deviations would identify the input, context or temporal condition requiring a different account. Independent report calibration, mechanics measurements and matched probe exposure constrain the corresponding alternatives (Table~\ref{tab:rules}).

Embodied systems offer a prospective test of the measurement procedure. A microassembly controller can undergo separately documented changes in camera calibration, contact mechanics or memory, while placement accuracy is matched across implementations. Paired vision, contact-force and release measurements can then be tested for recovery of the changed component on a held-out part or surface. This experiment would establish whether the diagnostic transfers to a system with known interventions; comparable human measurements are needed to evaluate biological transfer.

Sharing becomes scientifically informative when its input, output, context and timescale are specified. Separability at acquisition and convergence at control can organize the same learning system. The evidence map and worked comparisons turn that integration into a practical question for each experiment: which additional observation would change the explanation of the joint response?
''',r'''
这一综合形成聚焦的研究议程：定位使感觉特异学习影响计划动作与纠错响应的耦合环节。三项比较承载这一议程。交叉训练与测试情境定位迁移何时依赖记忆表达；跨延迟配对响应检验迁移模式的变化是否遵循共同时间成分；独立校准的感知报告检验感觉变化能否解释学习改变。每项比较都将文献中的具体不确定性连接到预测后果和必要测量。

下一项关键生物学检验，是在共同测试情境中结合不同视觉、本体感觉误差与预期、纠错两类读出，并在留出延迟采样。不同输入学习曲线与跨输出迁移的共同出现，将支持感觉特异获得过程汇合到控制后果。用固定混合读出预测这些联合响应，可以在该架构内解释延迟依赖的分离；系统性留出偏差则定位需要其他解释的输入、情境或时间条件。独立报告校准、力学测量及匹配探针暴露约束相应的竞争解释（表~\ref{tab:rules}）。

具身系统提供测量程序的前瞻检验。在匹配不同实现的放置精度后，可分别改变并记录微装配控制器的相机校准、接触力学或记忆。随后配对视觉、接触力和释放测量，在留出零件或表面上检验能否恢复被改变的成分。该实验可确立诊断方法能否迁移到干预已知的系统；生物学迁移由具有对应测量的人体数据评价。

明确输入、输出、情境和时间尺度，使共享成为具有科学解释力的关系。获得环节的可分离性与控制环节的汇合能够组织同一学习系统。证据地图与具体比较将这一整合转化为每项实验中的实际问题：哪项追加观察能够改变对联合响应的解释？
''')

JOINT=(r'''
The integrated account connects a controlled error to its later consequences in planned and corrective actions. For small perturbations around a specified baseline, write
\begin{equation}\Delta\mathbf y_{t+k}=H(q_{\mathrm{test}})A^kU(q_{\mathrm{train}})E(s)\mathbf e_t+\boldsymbol\epsilon.\label{eq:factor}\end{equation}
The physical error $\mathbf e_t$ enters a sensory representation $E$, updates adaptive states through $U$, persists through $A$, and reaches the measured outputs through $H$. Sensory condition $s$, training context $q_{\mathrm{train}}$ and test context $q_{\mathrm{test}}$ can act at different stages. A visual-specific state and a proprioceptive-specific state may therefore learn differently while both contribute to compensation and correction. This local representation organizes the experimental contrasts; larger perturbations can require nonlinear input, state and output mappings.

The four competing explanations now have explicit locations. A source-dependent scalar gate changes the overall update amplitude. An input account changes the represented error in $E$. A routing account changes the pattern of updating in $U$. An expression account changes the contribution of retained states through $H$. Retention in $A$ determines how each consequence changes with delay. At a single condition, the experiment measures their product. Independently calibrated inputs, crossed contexts and paired time courses test whether the same factorization predicts new conditions.

This formulation organizes the strongest supported conclusion: sensory selectivity and cross-output access can coexist, with context and timescale determining their measured relationship. The joint tests locate changes in that relationship. Selective neural interventions can then ask which physical pathways implement the effective factors. In this way, the integrated account connects behavioural evidence to progressively more specific mechanistic claims.
''',r'''
整合解释将受控误差连接到它对计划动作和纠错动作的后续影响。在指定基线附近，对小扰动可写为
\begin{equation}\Delta\mathbf y_{t+k}=H(q_{\mathrm{test}})A^kU(q_{\mathrm{train}})E(s)\mathbf e_t+\boldsymbol\epsilon.\label{eq:factor}\end{equation}
物理误差$\mathbf e_t$进入感觉表征$E$，通过$U$更新适应状态，经$A$保持，再通过$H$贡献于测量输出。感觉条件$s$、训练情境$q_{\mathrm{train}}$和测试情境$q_{\mathrm{test}}$可以作用于不同环节。因此，视觉特异与本体感觉特异状态可以具有不同学习动态，同时共同影响补偿和纠错。该局部表示组织实验比较；较大扰动可能需要非线性的输入、状态和输出映射。

四类竞争解释由此获得明确位置。来源依赖的标量门控改变整体更新幅度，输入解释改变$E$中的误差表征，路由解释改变$U$中的更新模式，表达解释通过$H$改变保持状态对输出的贡献。$A$中的保持过程决定各项后果如何随延迟变化。在单个条件下，实验测得的是这些因子的乘积。独立校准输入、交叉情境和配对时间轨迹，检验同一分解能否预测新条件。

这一表示组织了证据支持最充分的结论：感觉选择性可以与跨输出调用并存，情境和时间尺度决定其测得关系。联合检验定位这种关系的改变，选择性神经干预再检验实现有效因子的物理通路。整合解释据此将行为证据连接到逐步具体化的机制主张。
''')

def revise(sections):
    replacements = {
        'The problem revealed by a force field': INTRO,
        'Temporal mixtures resolve the apparent contradiction': WORKED,
        'Perceptual calibration is itself a measurement model': CALIBRATION,
        'Frozen predictions across public human studies': PUBLIC,
        'What would move the explanation forward': OUTLOOK,
        'A joint explanation with explicit observables': JOINT,
    }
    result=[]
    for h,t in sections:
        result.append((h,replacements.get(h[0],t)))
        if h[0]=='Sensory-specific learning can support shared control outputs':
            result.append((('What the integration adds','整合解释增加了什么'),INCREMENT))
    return result

def contribution_table(z):
    import formatting as f
    rows=[
      (('Sensory-specific memories combine at output (Hayashi et al.).','感觉特异记忆在输出端整合（Hayashi等）。'),
       ('Separate acquisition can support transfer into several control outputs.','分别获得的学习可以迁移到多个控制输出。'),
       ('Cross sensory error channels with anticipatory and corrective readouts.','交叉感觉误差通道与预期、纠错读出。')),
      (('Adaptation contains interacting timescales (Smith et al.).','适应包含相互作用的时间尺度（Smith等）。'),
       ('Fixed mixed readout can generate delay-dependent dissociation.','固定混合读出能够产生延迟依赖的分离。'),
       ('Predict both outputs at reserved delays; compare common and output-specific dynamics.','预测留出延迟的两个输出，比较共同及输出特异动态。')),
      (('Context affects updating and expression (Heald et al.).','情境影响更新与表达（Heald等）。'),
       ('Transfer depends on both the training condition and the condition of measurement.','迁移同时依赖训练条件和测量条件。'),
       ('Cross training and test cues; use the first error-free probe at matched delay.','交叉训练与测试线索，在匹配延迟使用首次无误差探针。')),
      (('Active and passive localization sample different information (Gastrock et al.).','主动、被动定位采样不同信息（Gastrock等）。'),
       ('A report constrains input versus updating through its component loadings.','报告通过各成分载荷约束输入与更新解释。'),
       ('Calibrate report loadings independently and predict joint report-and-motor outcomes.','独立校准报告载荷，预测报告与运动的联合结果。')),
    ]
    caption=('From established findings to the experimental increment of this synthesis. The first column credits prior contributions; the next columns state the joint interpretation and the comparison it motivates.','从已有发现到本文综合带来的实验增量。第一列标明前人贡献，后两列给出联合解释及其导出的比较。')[z]
    s='\\begin{table}[!htbp]\\small\\caption{'+caption+'}\\label{tab:synthesis}\n'
    s+=r'\begin{tabularx}{\textwidth}{>{\raggedright\arraybackslash}X>{\raggedright\arraybackslash}X>{\raggedright\arraybackslash}X}\toprule'+'\n'
    heads=[('Established contribution','已有贡献'),('Joint interpretation','联合解释'),('Experimental consequence','实验后果')]
    s+=' & '.join(r'\textbf{'+x[z]+'}' for x in heads)+r'\\\midrule'+'\n'
    for row in rows:s+=' & '.join(f.esc(x[z]) for x in row)+r'\\[6pt]'+'\n'
    return s+r'\bottomrule\end{tabularx}\end{table}'+'\n'
