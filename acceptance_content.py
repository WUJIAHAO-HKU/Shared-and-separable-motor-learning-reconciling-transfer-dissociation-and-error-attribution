"""Bilingual additions linked to explicit evidence and actual ablation results."""
ABSTRACT=(
'Motor learning transfers between planned actions and rapid corrections, yet these outputs can also adapt independently. We integrate 27 experimental, modelling and conceptual contributions to explain how transfer, dissociation, error attribution and sensory-specific learning constrain the organization of adaptation. An adversarial evidence audit separates supported conclusions from stronger claims challenged by direct comparisons or boundary conditions. A worked two-input, two-output account reconciles sensory-specific memories with cross-output transfer and derives a delay-dependent prediction that distinguishes fixed readout from changing coupling. A second comparison shows why externally attributed display distortion and externally imposed movement perturbation can produce different learning consequences. The synthesis yields eight experiment-selection rules, each specifying competing predictions, controls and the ambiguity restored by removing a measurement. New local-model simulations test crossed training/test contexts and independent perceptual calibration: the complete design separates input, update and expression changes, whereas removing either measurement creates exact aliases. Smaller effects reduce practical recovery despite full structural rank. Together, these results define a measurable target for motor-learning experiments: the condition-dependent mapping from calibrated errors to multiple control outputs.',
'运动学习能够在预先准备的动作与快速纠错之间迁移，这些输出也能够独立适应。本文整合27项实验、建模与概念研究，解释迁移、分离、误差归因及感觉特异学习如何约束适应的组织方式。反证导向的证据审计区分已获支持的结论，以及受到直接比较或边界条件挑战的更强主张。一个完整的双输入双输出案例将感觉特异记忆与跨输出迁移纳入同一架构，并导出随延迟变化的预测，以区分固定读出和变化的耦合。第二组比较说明，归因为外部显示失真与外加运动扰动可以产生不同学习后果。综合结果形成八项实验选择规则，逐项给出竞争预测、对照及删除测量后恢复的歧义。新增局部模型模拟检验训练/测试情境交叉和独立感觉校准：完整设计区分输入、更新与表达变化，删除任一测量均产生精确混淆；效应减小时，即使结构满秩，实际恢复率仍下降。由此，运动学习实验获得明确的测量目标：校准误差到多个控制输出的条件依赖映射。')

WORKED=(('A resolved contradiction and its new prediction','一组矛盾的完整解释及新增预测'),(r'''
Sensory-specific memories and shared access across control outputs appear contradictory when both are described as claims about a single ``shared internal model''. Their experimental axes differ. Hayashi et al. varied the sensory input and measured modality-dependent learning dynamics (E17); Wagner and Smith and Maeda et al. tested transfer between control outputs (E01--E03). A concrete joint architecture assigns one adaptive state to each sensory channel and lets both outputs access both states. With independently calibrated input and fixed readout, its local transfer matrix is
\begin{equation}
B(k)=\begin{pmatrix}1&0.4\\0.6&1\end{pmatrix}
\begin{pmatrix}a_v^k&0\\0&a_p^k\end{pmatrix}
\begin{pmatrix}b_v&0\\0&b_p\end{pmatrix}.
\label{eq:worked}
\end{equation}
The numerical readout weights illustrate a constructive account; they are not fitted human estimates. Different $a_v,a_p$ permit modality-specific retention, while the nonzero off-diagonal readout weights produce cross-output consequences of either sensory state. Thus two separate sensory memories can support both anticipatory compensation and feedback correction. The apparent contradiction is resolved by specifying the input axis and the output axis. \cite{hayashi2020,wagner2008,maeda2018,maeda2020}

This joint account adds an experimentally testable constraint that a paper-by-paper discussion leaves implicit. For either sensory input $j$, the ratio $B_{1j}(k)/B_{2j}(k)$ stays constant across delay, even when the two columns decay at different rates. In the illustrative matrix the ratios are $1/0.6$ for the visual column and $0.4/1$ for the proprioceptive column. Measure both columns and both outputs at two delays using independent first probes. Different column decay with stable within-column output ratios supports sensory-specific retention with fixed shared access. A changing ratio requires an additional output-specific retention or expression process. This test compares joint patterns; every fitted decay rate must predict both outputs. Probe-induced updating, nonlinear saturation and changing readout gains are assessed using sensory-matched retention controls, small signed perturbations and baseline probe calibration. \cite{unlearning2016}

Force-field dissociation narrows the account further. Yousif and Diedrichsen found feedback structural learning after temporally inconsistent exposure while feedforward structural learning was absent (E04). The result challenges a fixed, obligatory coupling of structural changes across outputs. It remains compatible with an acquired representation whose expression depends on temporal predictability, or with selectively updated control processes. Crossing training history with a common test context distinguishes their immediate predictions: a training-history difference surviving the common first probe supports an acquired or retained difference; a reversible test-cue effect before new error establishes an expression contribution. Independent input calibration is then needed to locate the surviving training effect. This is the inferential gain from the synthesis: transfer establishes access, dissociation specifies when that access changes, and the crossed experiment assigns the change to a measurable stage. \cite{yousif2012,coin2021}
''',r'''
若把感觉特异记忆与跨控制输出的共享利用都称为对“单一共享内部模型”的判断，两者就显得矛盾。它们的实验轴不同：Hayashi等改变感觉输入，测量模态相关学习动态（E17）；Wagner和Smith以及Maeda等检验控制输出间迁移（E01--E03）。一个具体的联合架构为每个感觉通道配置一个适应状态，并允许两个输出均利用这两个状态。独立校准输入且固定读出时，局部迁移矩阵可写为
\begin{equation}
B(k)=\begin{pmatrix}1&0.4\\0.6&1\end{pmatrix}
\begin{pmatrix}a_v^k&0\\0&a_p^k\end{pmatrix}
\begin{pmatrix}b_v&0\\0&b_p\end{pmatrix}.
\label{eq:worked}
\end{equation}
这些读出权重用于给出构造性解释，数值未经人体数据拟合。不同的$a_v,a_p$允许模态特异保持；非零的交叉读出权重使任一感觉状态均影响两个控制输出。因此，两个分别的感觉记忆可以共同支持预期补偿及反馈纠错。明确输入轴与输出轴后，表面矛盾获得解决。\cite{hayashi2020,wagner2008,maeda2018,maeda2020}

这一联合解释进一步给出逐篇讨论容易遗漏的实验约束。对任一感觉输入$j$，即使两列以不同速度衰减，比例$B_{1j}(k)/B_{2j}(k)$仍随延迟保持不变。示例中，视觉列比例为$1/0.6$，本体感觉列为$0.4/1$。使用独立首次探针，在两个延迟测量两列及两个输出：列间衰减不同而列内输出比例稳定，支持感觉特异保持与固定共享利用；比例变化要求引入输出特异保持或表达过程。该检验比较联合模式，每项拟合衰减率须预测两个输出。感觉匹配保持对照、小幅正负扰动及基线探针校准，分别检验探针诱发更新、非线性饱和和读出增益变化。\cite{unlearning2016}

力场分离结果进一步约束这一解释。Yousif和Diedrichsen发现，时间不一致的暴露能够产生反馈结构学习，同时缺少前馈结构学习（E04）。该结果挑战结构变化在两个输出之间固定且必然耦合的解释。它与两种机制兼容：获得的表征随时间可预测性选择性表达，或不同控制过程被选择性更新。将训练历史与共同测试情境交叉，可区分它们的即时预测：训练历史差异在共同首次探针中保留，支持获得或保持差异；新误差出现前可逆的测试线索效应，确立表达贡献。随后还需独立输入校准，定位所保留的训练效应。综合增加的推断是：迁移确立利用关系，分离限定这种关系何时改变，交叉实验将变化归入可测环节。\cite{yousif2012,coin2021}
'''))

DISPUTE=(('The counterevidence changes the experiment','反证如何改变实验'),(r'''
Some disagreements survive the integration and determine additional controls. Tsay et al. found that task error modulated implicit recalibration in the presence of sensory prediction error, with target flicker also attenuating learning (E22). Oza et al. attributed task-error benefits to instruction-sensitive action selection and found dissociable implicit recalibration (E23). Their contrast exposes a concrete dispute over automatic interaction, with target events, instructions and attention differing between protocols. A matched comparison must hold the cursor-error schedule fixed, cross task error with a target-flicker control, and measure aim plus the immediate instructed no-feedback aftereffect. The interaction account predicts a task-error effect in the residual implicit component; strategic addition predicts instruction-sensitive total improvement with a stable implicit component. Aim reporting is matched across groups because the report itself can change strategy. These are competing predictions for a common protocol; the existing studies establish the disagreement. \cite{tsay2022,oza2024}

Two further findings sharpen the control set. Hewitson et al. observed uncertainty-dependent movement changes insensitive to error magnitude and direction (E24). Balanced positive, negative and zero errors therefore separate an additive context-dependent shift from an error-dependent learning slope. Liddy et al. found enhanced implicit adaptation under a concurrent attention task, sustained by contingent feedback (E27). Attention controls must measure engagement and performance; a fixed suppressive ``distraction'' coefficient cannot be assumed across protocols. PReMo and perceptual prediction-error accounts also make different claims about the internal error represented by a physical displacement (E25--E26). Independent localization adds a measured constraint, and held-out learning tests whether that reported percept predicts the teaching signal in the target task. \cite{uncertain2023,attention2026,premo2022,percept2026}
''',r'''
部分分歧在整合后仍然存在，并决定需要哪些追加对照。Tsay等发现，在感觉预测误差存在时，任务误差调节隐式重校准，目标闪烁也会减弱学习（E22）；Oza等将任务误差的收益归于指示敏感的动作选择，并发现可分的隐式重校准（E23）。两项研究围绕自动交互形成具体争议，方案中的目标事件、指示和注意同时不同。共同方案应固定光标误差序列，交叉任务误差与目标闪烁对照，并测量瞄准及即时按指示无反馈后效。交互解释预测残余隐式成分中的任务误差效应；策略叠加解释预测总改善随指示变化而隐式成分稳定。由于瞄准报告本身能够改变策略，各组报告要求须一致。这些预测为共同方案提供竞争检验，现有研究确立了待检验的分歧。\cite{tsay2022,oza2024}

另外两项发现进一步明确对照。Hewitson等观察到对误差大小和方向不敏感的不确定性依赖运动变化（E24）；因此，需要平衡正误差、负误差和零误差，将加性情境变化与误差依赖学习斜率分离。Liddy等发现并行注意任务增强隐式适应，表现依赖反馈使增强持续（E27）；注意对照须记录投入及任务表现，分心系数的方向应由具体方案估计。PReMo与感知预测误差解释还对物理位移所对应的内部误差提出不同主张（E25--E26）。独立定位增加可测约束，留出学习检验所报告感知能否预测目标任务中的教学信号。\cite{uncertain2023,attention2026,premo2022,percept2026}
'''))

VALIDATION=(('What each measurement makes identifiable','每项测量带来哪些可辨识信息'),(r'''
We tested the two central choices---crossed training/test contexts and independent perceptual calibration---in a local experiment-design benchmark. The normalized baseline mapping is independently calibrated to the identity. Small condition contrasts satisfy
\begin{align}
\delta\mathbf y&=[q_{\rm train}(\Delta_I+\Delta_U)+q_{\rm test}\Delta_X]\mathbf e,\\
\delta\boldsymbol\ell&=\Delta_I\mathbf e .
\label{eq:ablation}
\end{align}
Here $\Delta_I$, $\Delta_U$ and $\Delta_X$ are two-by-two input, update and expression contrasts. The calibration relation is explicit: the perceptual measurement is assumed to observe the input contrast in the same local coordinates. A baseline map measured with uncertainty would require joint estimation and uncertainty propagation. Pure candidates each have four free coefficients, fitted by exact weighted least squares. The mixed model retains all twelve coefficients. Two independent signed error directions, two motor outputs and a two-by-two context crossing identify all twelve. Removing the crossed contexts makes update and expression interchangeable; removing perceptual calibration makes input and update interchangeable. Both removals reduce rank from twelve to eight. Removing one error direction reduces rank to six. Removing one motor output leaves rank eight because perceptual calibration still observes both sensory dimensions.

The accompanying executable analysis includes 7,200 newly generated noisy instances across eight conditions and 300 mixed-mechanism noiseless checks. Motor noise is resampled from archived residual blocks of 24 human participants; perceptual precision and effect amplitudes are assumed design values. At the larger specified effect (contrast norm 0.8, sixteen blocks per condition mean, perceptual standard deviation 0.1), the full design recovers the generating pure locus in 97.6\% of 900 instances. Off-axis error directions and independent noise are held out with all parameters frozen; every ablation is evaluated against the complete held-out context/output design. Exact ties are recorded as unresolved. The lower-effect and poorer-calibration conditions, full confusion matrices and prediction errors appear in the atlas. These simulations assess local factor contrasts; the archived neural-architecture competitors retain their near-equivalent shared/separate realizations.

The ablation changes the interpretation of a ``minimal'' experiment. A single motor output can still classify a pure locus in many simulated instances while leaving cross-output coupling unidentified. Likewise, a single sensory direction leaves an unobserved input column. The necessary measurements therefore follow the claim being tested: a scalar change needs fewer measurements than a statement about redistribution across sensory channels and control outputs. For the latter, retain the complete matrix, independent calibration and crossed contexts. Zero-error controls additionally test an additive policy/context shift; first-probe and delay controls test probe-induced learning and retention. The present centered benchmark implements the matrix contrasts, while E24 and E20 establish why those additional empirical controls are required. \cite{uncertain2023,unlearning2016}
''',r'''
我们在局部实验设计基准中检验两项核心选择：训练/测试情境交叉及独立感觉校准。归一化基线映射通过独立校准设为单位阵，小幅条件差异满足
\begin{align}
\delta\mathbf y&=[q_{\rm train}(\Delta_I+\Delta_U)+q_{\rm test}\Delta_X]\mathbf e,\\
\delta\boldsymbol\ell&=\Delta_I\mathbf e .
\label{eq:ablation}
\end{align}
其中$\Delta_I$、$\Delta_U$和$\Delta_X$为二乘二输入、更新及表达差异。校准关系明确假设：感觉测量在相同局部坐标下观察输入差异。若基线映射存在测量不确定性，则需要联合估计并传播该不确定性。每个纯机制候选包含四个自由系数，用精确加权最小二乘拟合；混合模型保留全部十二个系数。两个独立正负误差方向、两个运动输出及二乘二情境交叉能够辨识十二个系数。删除情境交叉后，更新与表达可互换；删除感觉校准后，输入与更新可互换；两种删除均使秩从十二降至八。删除一个误差方向使秩降至六；删除一个运动输出后，感觉校准仍观察两种感觉维度，秩为八。

随附可执行分析包含八种条件下新增的7200个含噪实例，以及300个混合机制无噪检查。运动噪声从24名人体参与者的存档残差块重采样，感觉精度与效应幅度为设定的设计值。在较大设定效应下（差异范数0.8、每条件均值含十六个块、感觉标准差0.1），完整设计在900个实例中以97.6\%恢复生成的纯机制位置。所有参数冻结后，预测留出的非轴向误差及独立噪声；每项消融均针对完整留出情境/输出设计评估。精确并列记录为未分辨。较小效应、较差校准条件、完整混淆矩阵及预测误差详见图谱。这些模拟检验局部因子差异；存档神经架构竞争者仍包含近等价的共享/分别实现。

消融结果明确了“最小”实验的含义。在许多模拟实例中，单个运动输出仍可分类纯机制位置，同时跨输出耦合无法辨识；单个感觉方向同样留下未观测输入列。因此，所需测量由主张决定：测量标量变化所需信息较少，判断跨感觉通道及控制输出的重新分配则须保留完整矩阵、独立校准和交叉情境。零误差对照进一步检验加性策略/情境变化；首次探针及延迟对照检验探针诱发学习和保持。当前中心化基准实现矩阵差异，E24与E20则确立这些额外经验对照的必要性。\cite{uncertain2023,unlearning2016}
'''))

def update(sections):
 out=[]
 for i,item in enumerate(sections):
  out.append(item)
  if i==5:out.append(WORKED)
  if i==6:out.append(DISPUTE)
  if i==8:out.append(VALIDATION)
 return out
