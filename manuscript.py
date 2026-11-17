TITLE=('Shared and separable motor learning: reconciling transfer, dissociation and error attribution', '运动学习中的共享与分离：整合迁移、分离与误差归因证据')
ABSTRACT=(
'Adaptive movements depend on learning that can transfer between planned actions and rapid corrections, yet these outputs can also change independently. We integrate experiments on dynamic adaptation, sensory remapping, error attribution and contextual memory to explain how these findings constrain the organization of learning. The evidence supports coupling across control outputs, selective sensitivity to training experience, and modality-dependent learning dynamics. These observations occupy three distinct dimensions: sensory input, control output and timescale. Their joint interpretation requires separating error representation, memory updating and context-dependent expression. An evidence map of 27 experimental, modelling and conceptual entries connects manipulations and measurements to warranted conclusions, residual explanations and discriminating predictions. We derive experiment-selection rules that pair correction with subsequent learning, cross training and test contexts, and calibrate perception and mechanics. Existing simulations show that independent input calibration can control false routing inferences, while recovery among overlapping model families remains close to chance in difficult regimes. The resulting agenda targets changes in effective error-to-output coupling and specifies the additional evidence needed to connect those changes to neural implementation.',
'适应性运动依赖能够在预先准备的动作与快速纠错之间迁移的学习，同时，这两类输出也能独立变化。本文整合动力学适应、感觉重映射、误差归因与情境记忆实验，说明这些结果如何约束学习的组织方式。已有证据支持跨控制输出的耦合、对训练经验的选择性敏感，以及依赖感觉模态的学习动态。这些观察分属感觉输入、控制输出和时间尺度三个维度，联合解释需要分清误差表征、记忆更新与情境依赖表达。本文以27个实验、建模与概念条目的证据地图，将操纵和测量连接至支持的结论、残余解释及可区分预测；据此导出配对纠错与后续学习、交叉训练与测试情境、独立校准感知与力学的实验选择规则。既有模拟显示，独立输入校准能够控制错误的路由归因，而在困难条件下，重叠模型家族的恢复率仍接近机会水平。由此形成的研究议程以有效误差—输出耦合的变化为核心测量对象，并明确将其连接至神经实现所需的追加证据。')
SECTIONS=[]
def s(h,en,zh):SECTIONS.append((h,(en,zh)))
s(('The problem revealed by a force field','从力场实验提出问题'),r'''
Consider a person learning to reach through a sideways force field. The hand path gradually straightens. A mechanical pulse then reveals a changed corrective response, and a channel trial reveals anticipatory compensation. Together, these observations establish that training affects multiple components of control. The scientific question is where their relationship arises: in a common representation of dynamics, communication between learning processes, a common error signal, or the expression of stored knowledge through the current task. Force-field and altered-arm-dynamics experiments provide unusually direct access to this question because perturbations, forces and muscle activity can be measured within the same apparatus. \cite{wagner2008,maeda2018,maeda2020}

The literature also provides selective changes. The temporal consistency of force exposure affects feedforward and feedback structural learning differently; mirror-reversal training depends on whether online consequences are visible; and visual errors can influence immediate correction more strongly than subsequent adaptation. These findings give the field a productive constraint: an account must explain both transfer and selective change under the conditions that elicit them. \cite{yousif2012,kasuga2015,hoffmann2023}

Our organizing claim is that sharing must be specified by \emph{what is shared, between which outputs, and over what interval}. We place sensory channels, control outputs and timescales on separate axes. We then connect the axes through an explicit sequence of error representation, updating, retention and expression. This perspective produces concrete comparisons: a tested observation model for an input-level dispute, a crossed-context test for an expression-level dispute, and paired temporal responses for a teaching-signal dispute. Supplementary Evidence Atlas entries E01--E29 provide the experiment-level basis for these choices.
''',r'''
设想一个人在侧向力场中学习到达目标。手的轨迹逐渐变直；随后施加的机械脉冲揭示纠错响应发生变化，通道试次则显示预期性补偿。两类测量共同确立了训练影响多个控制成分。科学问题在于这些成分的联系产生于何处：共同的动力学表征、学习过程间的通信、共同误差信号，或已有知识在当前任务中的表达。力场与手臂动力学改变实验能够在同一装置内测量扰动、力和肌肉活动，为回答这一问题提供直接条件。\cite{wagner2008,maeda2018,maeda2020}

文献也记录了选择性变化。力场暴露的时间一致性对前馈与反馈结构学习产生不同影响；镜像反转学习依赖在线动作后果是否可见；视觉误差对即时纠错的影响可以强于对后续适应的影响。这些结果共同约束理论：解释必须同时覆盖迁移与选择性变化，并说明各自的发生条件。\cite{yousif2012,kasuga2015,hoffmann2023}

本文的组织观点是，共享需要说明\emph{共享什么、连接哪些输出，以及发生在哪个时间区间}。我们将感觉通道、控制输出和时间尺度放在独立轴上，再用误差表征、更新、保持和表达的过程连接它们。这一组织方式导出具体比较：输入层争议需要经过检验的观测模型，表达层争议需要交叉情境测试，教学信号争议需要配对的时间响应。补充证据图谱E01--E29提供这些选择的逐实验依据。
''')
s(('How the evidence map was constructed','证据地图的构建'),r'''
The map is a purposive critical synthesis of experiments that connect at least two relevant measurements, selectively manipulate a learning condition, or expose an alternative implementation. The updated map additionally searches for target-error, uncertainty, attention and perceptual-error findings that challenge its central claims. Eight claim cards record support, counterevidence to the stated or stronger proposition, scope and the resulting experimental choice. This adversarial audit is documented in the atlas and search log. Its core is human upper-limb adaptation; computational source-inference and recurrent-network studies establish explicit competitors. Entries record the manipulation, measurement, observed result, supported inference, residual account and proposed discriminating test. A source locator identifies the experiment, figure or results section supporting each entry. Original findings and our proposed tests occupy separate fields. The search and source check were updated through 17 November 2026; the 2026 eLife item is labelled as reviewed preprint version 1. \cite{makino2026}

The unit of synthesis is an experimental contrast with a defined readout. Results measured as a 50--100 ms muscle response, a 251--350 ms visually evoked force, or a next-trial aftereffect retain their original timing and meaning. We use study-specific controls to judge each inference. For example, Cluff and Scott controlled background activation through a probe target, making their evidence more informative than a correlation between two unconstrained outputs. The atlas preserves such design strengths alongside the remaining alternatives. It provides an auditable argument rather than a pooled effect estimate; heterogeneous outcomes are compared by their causal role in the experiment. \cite{cluff2013,maeda2018,kasuga2015}
''',r'''
证据地图采用目的性批判综合：纳入能够连接至少两项相关测量、选择性操纵学习条件或提供竞争实现的研究。更新版进一步检索目标误差、不确定性、注意及感知误差研究，检查它们对核心主张的挑战。八张结论卡记录支持、针对当前或更强主张的反证、范围及由此形成的实验选择；反证审计详见图谱和检索记录。核心领域为人类上肢适应，来源推断与循环网络计算研究用于明确竞争解释。每个条目记录操纵、测量、观察结果、支持的推断、残余解释与拟议判别测试，并给出原文实验、图或结果节定位。原始发现与本文提出的测试分别存放。检索及来源核查更新至2026年11月17日；2026年的eLife条目标明为已评审预印本第1版。\cite{makino2026}

综合单元是具有明确定义读出的实验对比。50--100 ms肌肉响应、251--350 ms视觉诱发力及下一试次后效均保留各自的时间定义与测量含义。推断强度按原研究的具体对照判断。例如，Cluff和Scott通过探针目标控制背景激活，使其证据比两个不受约束输出之间的相关更有信息量。图谱同时保留这些设计优势与残余解释。各类异质结果按实验中的因果作用比较，形成可审计的论证链。\cite{cluff2013,maeda2018,kasuga2015}
''')
s(('Transfer establishes cross-output access to learned dynamics','迁移确立跨输出利用已学习动力学'),r'''
Wagner and Smith showed that corrective responses incorporated learned force-field dynamics (E01). Maeda and colleagues provided a complementary manipulation of the arm itself: shoulder fixation reduced the shoulder commands required for voluntary elbow movements, and this learning transferred to long-latency responses measured with the shoulder free (E02). Training perturbation responses subsequently transferred in the reverse direction to voluntary reaching (E03). Cluff and Scott measured load-specific changes in long-latency responses while controlling muscle activation at a probe target (E08). These experiments support a robust common statement: experience acquired in one control setting changes how another setting responds to limb dynamics. \cite{wagner2008,maeda2018,maeda2020,cluff2013}

This common statement constrains candidate mechanisms. A shared dynamics estimate supplies both outputs with updated predictions. Distinct adaptive pathways can communicate an update or receive a common teaching signal. A recurrent controller can embed dynamics-sensitive responses in its policy. A feedback-trained recurrent implementation has reproduced several behavioural and neural learning features, providing a concrete alternative to explicit predictor architectures (E21). The critical comparison is therefore the joint prediction across outputs and interventions after their normal behaviour is matched. \cite{feulner2025}

Transfer also depends on the test. A cue can select a stored memory or change its gain at readout. The COIN framework and its evoked-recovery experiments demonstrate how contextual inference affects memory expression and updating (E19). A two-by-two crossing of training cue and test cue directly exposes this ambiguity: a test-cue effect on the first error-free probe identifies an expression contribution; a training-cue effect that survives a common test cue motivates comparison of acquisition, retention and persistent input recalibration. Such a design assigns different observations to different stages of the transfer process. \cite{coin2021}
''',r'''
Wagner和Smith发现，纠错响应能够利用已学到的力场动力学（E01）。Maeda及同事直接改变手臂动力学：肩关节固定减少了自主肘关节运动所需的肩部指令，这种学习迁移至肩关节释放时测得的长潜伏期响应（E02）；随后，训练扰动响应又在反方向迁移至自主到达（E03）。Cluff和Scott在控制探针目标处肌肉激活的同时，测得具有负载特异性的长潜伏期响应变化（E08）。这些实验共同支持：一种控制条件下获得的经验，会改变另一条件对肢体动力学的响应。\cite{wagner2008,maeda2018,maeda2020,cluff2013}

这一结论约束机制解释。共享动力学估计可以为两个输出提供更新后的预测；不同适应通路可以传递更新，或接收共同教学信号；循环控制器则可将动力学相关响应嵌入策略。反馈训练的循环实现已复现多项行为与神经学习特征，为显式预测器架构提供了具体竞争者（E21）。因此，关键比较应在匹配正常行为后，检验跨输出、跨干预的联合预测。\cite{feulner2025}

迁移也依赖测试条件。线索可以选择已存储记忆，或改变其读出增益。COIN框架及诱发恢复实验展示了情境推断如何影响记忆表达与更新（E19）。训练线索乘测试线索的二乘二交叉设计可以直接揭示这种歧义：首次无误差探针上的测试线索效应识别表达贡献；在共同测试线索下保留的训练线索效应，则推动对获得、保持与持续输入重校准的比较。由此，不同观察可归入迁移过程的不同阶段。\cite{coin2021}
''')
s(('Dissociation identifies the conditions of coupling','分离揭示耦合的发生条件'),r'''
Yousif and Diedrichsen manipulated temporal consistency while matching the counts of exposure-trial types. Consistent experience altered structural learning in both feedforward and feedback measurements; inconsistent experience altered feedback structure without the corresponding feedforward structural change (E04). This result makes disturbance history part of the mechanism. A model with a single unconditional update applied identically to both readouts must explain why temporal organization changes the relationship. Distinct timescales, context selection and selective updates offer explicit alternatives. \cite{yousif2012}

Kasuga and colleagues manipulated access to online visual consequences during mirror-reversed reaching (E05). Endpoint feedback supported better feedforward performance, while continuous feedback produced stronger attenuation of inappropriate corrective responses. The measured feedback response was a visually evoked force in a later window than the long-latency mechanical responses above. Mirror reversal also changes the required policy mapping. These differences specify a valuable contrast: knowledge transfer under altered dynamics and acquisition of a new feedback mapping place different demands on experience. Comparing them requires matched exposure, training duration and baseline performance. \cite{kasuga2015}

Timescale adds a further distinction. Crevecoeur and colleagues observed field-specific adjustment during ongoing movements exposed to unanticipated dynamics (E11). Such within-movement adaptation can improve an endpoint before a persistent next-trial change is established. A paired design therefore asks both whether the current correction changes and what survives into a subsequent probe. Delay-resolved tests then distinguish transient control adjustment from slower retention processes. \cite{crevecoeur2020}
''',r'''
Yousif和Diedrichsen在匹配各类暴露试次数量的条件下操纵时间一致性。一致经验同时改变前馈与反馈测量中的结构学习；不一致经验改变反馈结构，却未引起相应前馈结构变化（E04）。这一结果将扰动历史纳入机制解释：若模型对两个读出施加相同且无条件的更新，就必须解释时间组织为何改变二者关系。不同时间尺度、情境选择和选择性更新提供了明确的竞争解释。\cite{yousif2012}

Kasuga及同事操纵镜像反转到达训练中的在线视觉后果（E05）。终点反馈支持更好的前馈表现，连续反馈使不适当纠错响应更明显地衰减。该研究测量的是较晚时间窗的视觉诱发力，与前述机械长潜伏期响应有不同时间定义；镜像反转还改变了所需策略映射。由此形成有价值的比较：动力学改变下的知识迁移与新反馈映射的获得，对经验提出不同要求。比较需要匹配暴露、训练时长与基线表现。\cite{kasuga2015}

时间尺度还提供了另一层区分。Crevecoeur及同事在不可预期动力学下观察到进行中运动的力场特异调整（E11）。这种试次内适应可以在持续的下一试次改变形成之前改善终点表现。因此，配对设计应同时测量当前纠错的变化及其在后续探针中的保留，再用多延迟测试区分瞬时控制调整与较慢保持过程。\cite{crevecoeur2020}
''')
s(('Error attribution depends on the candidate cause','误差归因取决于候选原因'),r'''
The word ``external'' covers biologically different causes. A display displacement that can be discounted, an external force that will recur, and an unexpected object mass imply different useful responses. Likewise, ``internal'' can refer to random execution noise or a persistent change in limb dynamics. Berniker and Kording formalized the consequences: inferred body and world changes predict different generalization patterns (E13). Wei and Kording related nonlinear error sensitivity to inferred error relevance (E14). These studies motivate recording source, persistence and behavioural relevance separately. \cite{berniker2008,wei2009}

Gastrock and colleagues revealed a visuomotor rotation through cursor jumps or hand visibility (E15). Aftereffects decreased, while the hand-view active-minus-passive localization estimate was near zero and proprioceptive recalibration persisted; the direct control-versus-hand-view report contrast remained uncertain. This identifies component-selective consequences of revealing a display distortion. Hand visibility simultaneously changes available sensory information, so a cue-only manipulation with matched visibility supplies the next useful contrast. \cite{external2020}

Kim and colleagues compared externally imposed rotations with matched internally generated movement errors and found greater adaptation to the externally imposed errors (E16). Here the internal category was movement variability, and the proposed causal-inference model estimated whether an external perturbation had occurred. Together, these findings support a conditional synthesis: learning depends on which latent cause the evidence supports and which behavioural component is measured. The prediction ``external attribution reduces learning'' loses the distinctions needed to explain both experiments. A stronger test crosses source credibility with persistence while matching physical and perceived error, then measures perceptual and motor consequences separately. \cite{piece2025}
''',r'''
“外部”包含生物学意义不同的原因：可以忽略的显示位移、将再次出现的外力、意外的物体质量，对应不同的有效响应。“内部”也可指随机执行噪声，或肢体动力学的持续变化。Berniker和Kording形式化了这种差别：推断出的身体与世界变化产生不同泛化预测（E13）。Wei和Kording则将非线性误差敏感性与所推断的误差相关性联系起来（E14）。因此，来源、持续性与行为相关性需要分别记录。\cite{berniker2008,wei2009}

Gastrock及同事通过光标跳变或让手可见来揭示视运动旋转（E15）。后效减小；手可见组的主动减被动定位估计接近零，本体感觉重校准保留；对照与手可见组的直接报告差异仍有不确定性。该结果揭示显示失真信息对不同学习成分的选择性影响。手可见性同时改变感觉信息，因而保持可见性一致的纯线索操纵提供下一项有效对比。\cite{external2020}

Kim及同事比较外加旋转与匹配的自身生成运动误差，发现对外加误差的适应更强（E16）。这里的内部类别是运动变异，其因果推断模型估计外部扰动是否发生。结合两项结果，可形成条件化解释：学习取决于证据支持哪一种潜在原因，以及测量哪一个行为成分。“外部归因降低学习”这一预测缺少同时解释两项实验所需的区分。更有判别力的测试应交叉来源可信度与持续性，匹配物理和感知误差，再分别测量感觉与运动后果。\cite{piece2025}
''')
s(('Sensory-specific learning can support shared control outputs','感觉特异学习可以支持共享的控制输出'),r'''
Hayashi and colleagues independently varied visual and proprioceptive errors, including opposing-error conditions (E17). Nonlinear aftereffects and modality-dependent learning dynamics supported their account of distinct sensory memories with interacting error processing. This evidence constrains the input dimension of learning. Both sensory-specific states could still contribute to planned compensation and corrective control. A statement about separate visual and proprioceptive memories and a statement about transfer between feedforward and feedback control can therefore hold within one architecture. \cite{hayashi2020}

Hoffmann and colleagues brought the two dimensions into the same experiment (E18). Scaling visual displacement during force perturbations changed online corrections more consistently than subsequent aftereffects, and instructions to control the hidden hand removed a residual visual influence on adaptation. The task goal affects how sensory evidence relates to correction and learning. A crossed target-by-reliability experiment should therefore calibrate perceived displacement separately and evaluate the untrained combinations with fixed learned parameters. \cite{hoffmann2023}

Izawa and Shadmehr demonstrate why adding a sensory consequence is useful: sensory-error and reward-driven learning produced different sensory remapping (E12). Gastrock and colleagues extend this logic with active and passive localization. These measurements can reveal an input or prediction change that a reach endpoint misses. The subtraction between active and passive reports is itself a measurement model, requiring matched reporting demands and an assessment of localization reliability. \cite{izawa2011,external2020}
''',r'''
Hayashi及同事独立改变视觉与本体感觉误差，包括符号相反的误差条件（E17）。非线性后效与模态相关学习动态支持分别的感觉记忆及交互误差处理解释。这些证据约束学习的输入维度。两个感觉特异状态仍可同时参与预期补偿和纠错控制，因此，视觉与本体感觉记忆分别存在、前馈与反馈控制之间发生迁移，可以在同一架构内成立。\cite{hayashi2020}

Hoffmann及同事将两个维度纳入同一实验（E18）。力扰动中缩放视觉位移，对在线纠错的影响比对后续后效更一致；控制隐藏手的指示消除了视觉对适应的残余影响。任务目标会改变感觉证据与纠错、学习之间的关系。因此，目标乘可靠性的交叉实验应独立校准感知位移，并用固定的已学习参数预测未训练组合。\cite{hoffmann2023}

Izawa和Shadmehr说明了增加感觉后果测量的价值：感觉误差驱动与奖励驱动学习产生不同感觉重映射（E12）。Gastrock及同事通过主动与被动定位进一步展开这一逻辑。这些测量能够揭示到达终点遗漏的输入或预测变化。主动减被动报告本身也是一个测量模型，需要匹配报告要求并评估定位可靠性。\cite{izawa2011,external2020}
''')
s(('A joint explanation with explicit observables','具有明确观测量的联合解释'),r'''
The evidence supports three propositions: learned dynamics can influence multiple control outputs; the coupling depends on training statistics and sensory access; and sensory, contextual and mechanical processes can change the observed transfer. We integrate them as \emph{conditional coupling across partially separable processes}. The proposed synthesis predicts structured variation in transfer when input, training context, test context and delay are independently manipulated. Its empirical target is the effective mapping from a controlled error to a subsequent measured output.

For small perturbations around a specified baseline, write
\begin{equation}\Delta\mathbf y_{t+k}=H(q_{\mathrm{test}})A^kU(q_{\mathrm{train}})E(s)\mathbf e_t+\boldsymbol\epsilon.\label{eq:factor}\end{equation}
Here $\mathbf e_t$ contains physical visual and proprioceptive errors; $E$ maps them into effective sensory errors under sensory condition $s$; $U$ updates latent learning states; $A$ describes local retention; and $H$ maps those states to anticipatory compensation and a standardized feedback-probe response. Training and test contexts are separate arguments. The equation is a local bookkeeping model for experimental contrasts. Nonlinear saturation, changing policies and mechanical output maps require corresponding extensions. The factorization is a synthesis proposed here; the component phenomena are anchored in E01--E29.

This representation makes four accounts directly comparable. A scalar-gating account multiplies an otherwise fixed update by a source-dependent gain. An input account changes $E$. An expression account changes $H$. A routing account changes the pattern of $U$ across sensory inputs and control consequences. A pair of sensory-specific latent states can have distinct columns in $U$ and both contribute to each row of $H$. This explicitly reconciles sensory specificity with cross-output transfer.

The experiment identifies the product $B=HA^kUE$ at a given condition. A shared latent update and synchronized separate updates can generate the same product. Mechanistic inference therefore progresses by independently measuring factors and testing new conditions where competing factorizations predict different products. The central prediction is a change in the joint transfer response after independently validated observation and temporal constraints are imposed. Evidence for that prediction would establish conditional redistribution of effective learning. Neural storage and cellular update mechanisms then require interventions with independently demonstrated selectivity.
''',r'''
证据支持三个命题：已学习动力学能够影响多个控制输出；这种耦合依赖训练统计与感觉可用性；感觉、情境及力学过程都能改变所测迁移。本文将其整合为\emph{部分可分过程之间的条件性耦合}。这一综合预测：独立操纵输入、训练情境、测试情境和延迟，将产生具有结构的迁移变化。其经验目标是受控误差到后续所测输出的有效映射。

在指定基线附近的小扰动条件下，可写为
\begin{equation}\Delta\mathbf y_{t+k}=H(q_{\mathrm{test}})A^kU(q_{\mathrm{train}})E(s)\mathbf e_t+\boldsymbol\epsilon.\label{eq:factor}\end{equation}
其中，$\mathbf e_t$为物理视觉和本体感觉误差；$E$在感觉条件$s$下将其映射为有效感觉误差；$U$更新潜在学习状态；$A$描述局部保持；$H$将状态映射为预期补偿及标准反馈探针响应。训练情境与测试情境分别进入模型。该式为实验对比提供局部记账模型；非线性饱和、策略改变与机械输出映射需要相应扩展。因子分解是本文提出的综合表示，其组成现象由E01--E29支撑。

这一表示使四种解释可直接比较。标量门控解释用来源依赖增益乘以固定更新；输入解释改变$E$；表达解释改变$H$；路由解释改变$U$跨感觉输入与控制后果的结构。两个感觉特异潜状态可以在$U$中具有不同列，同时均参与$H$的每一行。由此，感觉特异性与跨输出迁移获得明确的联合实现。

实验在给定条件下辨识的是乘积$B=HA^kUE$。共享潜在更新与同步的分别更新能够产生相同乘积。因此，机制推断需要独立测量因子，并测试竞争分解在其中预测不同乘积的新条件。本文的核心预测是：施加独立验证的观测与时间约束后，联合迁移响应仍随条件变化。支持该预测的证据将确立有效学习的条件性重新分配；进一步定位神经存储与细胞更新机制，需要选择性得到独立验证的干预。
''')
s(('The temporal shape of a teaching signal is a decisive test','教学信号的时间形状提供关键检验'),r'''
Albert and Shadmehr paired perturbation-trial EMG with the next channel-trial change and found a scaled, temporally advanced relationship (E06). This supports a feedback-related teaching signal in their force-field task. Makino and colleagues subsequently manipulated the temporal profile of visual errors within a channel and observed that the learning response retained its relation to movement onset, while the tonic holding response predicted learning amplitude (E07; reviewed preprint). The task distinction is informative: the visual-error experiment tests timing flexibility that the original force-field relation left open. \cite{albert2016,makino2026}

A minimal next contrast uses the same participants and paired readouts with two onset timings and a late sign reversal, first for visual displacement and then for a mechanically matched perturbation. Fit a fixed-shift copying model and an integral/tonic-teacher model on one onset condition, using the same error representation and observation noise. Evaluate the other onset and reversal condition without refitting. A copied waveform predicts corresponding temporal displacement of the learned command; an integrated teacher predicts learning amplitude from the retained error summary even when the within-trial waveform changes. Shared upstream causes remain testable by varying the corrective demand at matched perceived error. This design concentrates the disagreement into a waveform prediction instead of a correlation coefficient.
''',r'''
Albert和Shadmehr配对扰动试次肌电与下一通道试次变化，发现缩放且时间提前的对应关系（E06），支持其力场任务中与反馈相关的教学信号。Makino及同事随后在通道内操纵视觉误差时间模式，观察到学习响应仍与运动开始对齐，而持续保持响应可预测学习幅度（E07；已评审预印本）。任务差异本身有信息价值：视觉误差实验检验了原力场对应关系尚未覆盖的时序灵活性。\cite{albert2016,makino2026}

最小追加对比可在同一批参与者中，以配对读出比较两个误差起始时点及一次晚期符号反转，先测试视觉位移，再测试机械上匹配的扰动。在一种起始条件下拟合固定平移复制模型与积分/持续教学模型，统一误差表征与观测噪声，再不重新拟合地预测另一时点及反转条件。复制模型预测学习指令发生相应时间位移；积分教学模型则预测，即使试次内波形变化，保留的误差摘要仍决定学习幅度。在匹配感知误差时改变纠错需求，可继续检验共同上游原因。该设计将分歧集中到波形预测。
''')
s(('Selecting the smallest informative experiment','选择最小且有信息量的实验'),r'''
Minimality is defined relative to a specific pair of explanations and a measurement model. Table~\ref{tab:rules} lists eight decisions. Each starts with an observed ambiguity, adds the measurement that targets it, and names the conclusion licensed by each outcome. The appropriate next experiment follows the first unresolved link in Equation~\ref{eq:factor}. When perception is uncalibrated, an extra motor probe cannot assign the effect to updating. When test context changes, a training-only comparison cannot isolate acquisition. When mechanics change, a matched endpoint leaves the force-generating process ambiguous.

Two controls are particularly consequential in force-field work. Stable and unstable dynamics can recruit different combinations of compensatory commands and coactivation, motivating independent impedance probes. Visual feedback during nominally error-free channel trials can accelerate unlearning, so the measurement sequence must be included in the learning model. Visual feedback gains also depend on sensory availability during training. These observations motivate the mechanics, probe-order and gain-calibration rules rather than treating every channel or perturbation response as a neutral readout. \cite{franklin2003,unlearning2016,franklin2023}

For the central source-dependent coupling question, a staged design is efficient. First establish two independently varying error directions with opposite-sign and zero-error controls. Pair an anticipatory channel-force measure with a standardized feedback probe on separate randomized readout trials to avoid one probe teaching the next. Then cross source cues at training with test cues, maintaining matched visual information, movement speed and background EMG. Independent active/passive localization, gain calibration and delay probes estimate the relevant nuisance factors. Hold out complete cue-by-input-by-output combinations, rather than randomly dividing repeated trials from the same condition.

The stopping rule is scientific: if calibrated candidate models predict the held-out observations within the same prespecified tolerance, report the compatible mechanism set and identify the intervention on which predictions next diverge. A failed recovery test directs the design toward an identifiable contrast. Equivalence margins should be based on measurement repeatability and the smallest change that alters a model's held-out prediction. Sample size follows simulated power for that contrast over a range of plausible effects and calibration errors, including the near-equivalent regime; it cannot be read from model count alone.
''',r'''
“最小”相对于具体的一对解释和测量模型定义。表\ref{tab:rules}给出八项决策，每项由已观察到的歧义出发，增加针对该歧义的测量，并说明不同结果支持的结论。下一实验由式\ref{eq:factor}中首个未解决的环节决定。感知尚未校准时，额外运动探针无法将效应定位到更新；测试情境改变时，单独比较训练无法分离获得；力学发生变化时，终点匹配仍留下产力过程歧义。

力场研究有两项影响尤其直接的对照。稳定与不稳定动力学能够调用不同组合的补偿指令和共激活，因此需要独立阻抗探针。名义无误差通道试次中的视觉反馈可以加速去学习，测量序列因此需要进入学习模型。视觉反馈增益还依赖训练中的感觉可用性。这些观察为力学、探针顺序及增益校准规则提供直接依据。\cite{franklin2003,unlearning2016,franklin2023}

针对来源依赖耦合这一核心问题，分阶段设计更有效。首先建立两个独立变化的误差方向，并加入反符号与零误差对照。在分开随机化的读出试次中配对预期通道力与标准反馈探针，避免一个探针改变下一次学习。随后交叉训练来源线索与测试线索，匹配视觉信息、运动速度和背景肌电。独立的主动/被动定位、增益校准及延迟探针用于估计相关干扰因子。留出单位采用完整的线索乘输入乘输出组合。

停止规则对应科学判断：若校准后的候选模型在预先指定容差内预测相同留出观测，就报告兼容机制集合，并找出下一项预测分歧最大的干预。模型恢复检验失败时，设计应转向可辨识的对比。等价界值应来自测量重测精度及足以改变模型留出预测的最小变化。样本量由该对比在多种效应和校准误差下的模拟功效决定，其中包括近等价条件。
''')
s(('Simulation calibration defines the reach of the rules','模拟校准界定规则的适用范围'),r'''
We use an existing computational archive to illustrate the distinction between estimating an effective coupling and identifying a model family. Its five calibrated families vary scalar versus patterned source modulation and rank-one versus fuller error-to-output maps, with a separable-gain alternative. The noise model resamples processed residual blocks from a public 24-participant dataset; this is an assumed transport of block-level noise to the proposed paired measurements. The simulations use specified effect distributions and calibration precision, documented in the accompanying snapshot.

In the calibrated five-family comparison, recovery was 22.1\% at four repetitions and 33.1\% at sixteen repetitions; the near-equivalent condition yielded 19.4\%, against a balanced-label chance reference of 20\%. Recovery therefore supports reporting effective response contrasts and compatible families in these regimes. Increasing optimization starts from eight to twenty-four in a 25-fit audit improved the objective by at most $5.15\times10^{-8}$, while noiseless recovery errors were below $2.6\times10^{-11}$. These checks make simple optimizer undertraining an unlikely explanation for the audited ambiguity; they leave the broader overlap of model predictions as the relevant design issue.

An input-mixing stress test shows why independent sensory calibration matters. At a simulated group size of 48 and sixteen repetitions, input mixing alone produced positive routing decisions on 18.7--20.2\% of resampled groups. Correcting the effective input using independent calibration reduced the positive rate to 2.2--2.5\% across calibration-error settings. A stronger simulated routing effect retained a 99.5--99.8\% detection rate under those settings. These are conditional simulation results with an assumed calibration model. They motivate a perceptual calibration experiment and a calibration-transport check in the target context.

For a two-input, two-output map measured in two source conditions, a useful diagnostic is
\begin{equation}\begin{split}Q={}&B_{1,11}B_{1,22}B_{0,12}B_{0,21}\\&-B_{1,12}B_{1,21}B_{0,11}B_{0,22}.\end{split}\end{equation}
Separable row and column gains preserve $Q=0$. A reliable nonzero value rejects that restricted gain account after error-input calibration. General input mixing can itself change $Q$, and some genuine mapping changes also preserve zero. Thus $Q$ serves as a targeted contrast with explicit alternatives. Its sensitivity depends on the effect size, number of repetitions and calibration uncertainty. The archive's low family recovery and its successful input-mixing control answer different experimental questions; both belong in the design assessment.
''',r'''
本文使用既有计算档案，说明估计有效耦合与辨识模型家族所需证据的差别。档案中的五个校准家族分别改变标量或结构化来源调节、秩一或更完整误差—输出映射，并包含可分增益竞争解释。噪声模型重采样公开24人数据集的已处理残差块，将块级噪声迁移至拟议配对测量；这是设计假设。模拟采用的效应分布与校准精度详见随附快照。

在校准后的五家族比较中，四次重复的恢复率为22.1\%，十六次重复为33.1\%；近等价条件为19.4\%，平衡标签的机会参照为20\%。这些条件适合报告有效响应对比与兼容家族。在25次拟合审计中，将优化初值由8个增加到24个，目标函数最多改善$5.15\times10^{-8}$；无噪声恢复误差低于$2.6\times10^{-11}$。这些检查使简单的优化训练不足难以解释已审计的歧义，并将设计重点引向模型预测本身的重叠。

输入混合压力测试说明独立感觉校准的必要性。在模拟组大小48人、十六次重复时，输入混合本身使18.7--20.2\%的重采样组被判为路由阳性。使用独立校准修正有效输入后，不同校准误差设定下的阳性率降至2.2--2.5\%。较强的模拟路由效应在这些条件下保留99.5--99.8\%检出率。这些是依赖假设校准模型的条件性模拟结果，直接支持增加感觉校准实验，并检验校准向目标情境的迁移。

对于两个来源条件下的两输入、两输出映射，可使用以下诊断量：
\begin{equation}\begin{split}Q={}&B_{1,11}B_{1,22}B_{0,12}B_{0,21}\\&-B_{1,12}B_{1,21}B_{0,11}B_{0,22}.\end{split}\end{equation}
可分的行、列增益保留$Q=0$。在校准误差输入后，可靠的非零值排除这一受限增益解释。一般输入混合也能改变$Q$，而部分真实映射变化仍可保持零值。因此，$Q$用于检验具有明确竞争解释的针对性对比，其灵敏度依赖效应大小、重复次数与校准不确定性。档案中的低家族恢复率与成功的输入混合控制分别回答不同实验问题，两者都应进入设计评估。
''')
s(('What would move the explanation forward','哪些结果能够推进解释'),r'''
Three predictions organize the next experiments. First, \emph{conditional transfer}: if source evidence changes effective learning allocation, a calibrated source-by-error-channel interaction should remain in the transfer matrix under a common test context. If the difference follows only the test cue, the result favours context-dependent expression. If independently validated report loadings explain the effect through input change, that account predicts the joint held-out responses. Second, \emph{temporal selectivity}: copying and integrated-teacher accounts should diverge on withheld error-onset and sign-reversal trials. Third, \emph{orthogonal sharing}: distinct sensory learning dynamics can coexist with transfer to both planned and corrective outputs; observing that combination supports a structured multi-input architecture.

These predictions build on established contributions. Source inference already explains generalization; contextual inference already separates updating and expression; feedback-to-learning comparisons already test a teaching signal; and modality-specific learning already challenges scalar error accounts. Our contribution is their joint evidence-to-experiment mapping, with explicit conditions under which an additional measurement changes the inferential conclusion. The most informative outcome is a reproducible pattern that survives the controls appropriate to its mechanism, even when several neural implementations remain compatible. \cite{berniker2008,coin2021,albert2016,hayashi2020}

Robotic manipulation offers an intervention testbed for this logic. In a proposed microassembly experiment, one can change camera calibration, contact mechanics or controller memory separately, train controllers to matched placement accuracy, and test whether the paired probes correctly recover the manipulated component. Contact-force and release measurements would accompany vision-based placement; a held-out part or surface would test transfer. This is a proposed validation of the measurement procedure. Biological transfer requires human data with corresponding sensory and control measurements. The common value is experimental access to otherwise confounded factors.

The emerging picture is a learning system whose useful knowledge is distributed across sensory representations, adaptive states and context-sensitive outputs. Transfer and dissociation identify how these components interact. Measuring their joint consequences turns that picture into a sequence of discriminating experiments.
''',r'''
三个预测组织下一步实验。第一，\emph{条件性迁移}：若来源证据改变有效学习分配，那么在共同测试情境中，校准后的迁移矩阵应保留来源乘误差通道交互。若差异只随测试线索变化，结果支持情境依赖表达；若独立验证的报告载荷通过输入变化解释效应，该解释应预测联合留出响应。第二，\emph{时间选择性}：复制解释与整合教学解释应在留出的误差起始时点和符号反转试次上产生分歧。第三，\emph{正交维度上的共享}：不同感觉学习动态可以与向预先准备及纠错两个输出的迁移并存；观察到这一组合将支持结构化的多输入架构。

这些预测建立在已有贡献上。来源推断已用于解释泛化，情境推断已区分更新与表达，反馈—学习比较已检验教学信号，感觉特异学习已挑战标量误差解释。本文的贡献是将它们连接成统一的证据—实验映射，明确何种追加测量会改变推断结论。最有信息量的结果，是在相应机制所需对照下保持稳定、可重复的模式，同时保留与该模式兼容的神经实现。\cite{berniker2008,coin2021,albert2016,hayashi2020}

机器人操作为这一逻辑提供干预测试平台。在拟议微装配实验中，可以分别改变相机校准、接触力学或控制器记忆，将控制器训练至匹配的放置精度，再检验配对探针能否正确识别被操纵的成分。基于视觉的放置测量应配以接触力和释放测量，留出零件或表面用于测试迁移。这是一项拟议测量程序验证；生物学迁移需要具有对应感觉与控制测量的人体数据。共同价值在于可以直接干预原本混杂的因素。

由此形成的图景是：有用知识分布于感觉表征、适应状态与情境敏感输出之间。迁移和分离揭示这些成分如何相互作用，而对联合后果的测量将这一图景转化为逐步推进的判别实验。
''')

from acceptance_content import ABSTRACT, update
SECTIONS=update(SECTIONS)
from revision_content import ABSTRACT, revise
SECTIONS=revise(SECTIONS)
