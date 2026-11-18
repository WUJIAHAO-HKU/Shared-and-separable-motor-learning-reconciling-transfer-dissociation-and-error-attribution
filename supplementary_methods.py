"""Detailed derivations and numerical procedures relocated from the main text."""
from revision_content import WORKED, CALIBRATION

def render(z):
    h=lambda en,zh:'\\clearpage\\section{'+(zh if z else en)+'}\n'
    s=h('Supplementary Methods SM1 | Temporal mixtures and equivalent implementations','补充方法SM1 | 时间混合与等价实现')
    s+=WORKED[1][z]+'\n'
    s+=h('Supplementary Methods SM2 | Report loadings and factor recovery','补充方法SM2 | 报告载荷与因子恢复')
    s+=CALIBRATION[1][z]+'\n'
    s+=h('Supplementary Methods SM3 | Cross-study fitting and recovery','补充方法SM3 | 跨研究拟合与恢复')
    s+=(r'''
The force-field archives contribute twelve participants each. Block observations contain two schedules, seventy blocks per schedule and two response windows (180--230 ms and 230--300 ms). The first ten blocks define schedule- and participant-specific baseline means. The joint score divides each output's MSE by its source baseline variance and averages the two standardized scores. The target pre-exposure baseline is used for the primary change-score analysis; a second analysis transports the source baseline without target calibration. Target post-exposure observations are excluded from parameter fitting and penalty selection. The complete two-study set is the external validation set. \cite{franklin2021,franklin2023}

The four candidates have one common temporal mode (three parameters), one mode per output (four), two common modes with mixed readout (six), or two modes per output (eight). In block coordinates,
\begin{equation}z_{r,t+1}=p_rz_{r,t}+(1-p_r)f_t,\qquad y_{i,t}=\sum_r c_{ir}(z_{r,t}+z_{r,t+1})/2.\end{equation}
All candidates use the same normalized field schedule, zero initial states, observation timing and source-derived output scales. The poles describe effective closed-loop block persistence. Pole bounds are 0 to 0.9995. Close poles use a divided-difference basis, switching to its derivative limit at a gap of $10^{-4}$; coefficients refer to this implemented basis. For fixed poles, linear coefficients are solved by least squares with an optional ridge penalty. Numerical pole optimization uses variable projection, at most 600 function evaluations per start and tolerances recorded in \texttt{analysis/validate.py}.

Ridge strength is chosen from $0,0.001,0.01,0.1,1$ using six folds of source participants. Each fold holds out two of the twelve source participants and uses six starts per candidate. Final source fits use 64 starts; unpenalized fits receive the same final budget and are retained regardless of target performance. Equal penalty grids do not force equal effective complexity, so both penalty variants, both windows and both transport directions are reported. A pre-exposure baseline and a source phase-mean template serve as prediction comparators. Paired target-participant bootstrap intervals are conditional on the fitted source; they do not incorporate resampling of source studies. The deposited scores and fitted parameters provide all output-specific and joint endpoints.

Recovery uses twenty new instances per family (eighty total). Source-fit poles receive Gaussian perturbations with SD 0.03, clipped to $[0.001,0.999]$; output coefficients receive independent per-output multipliers drawn uniformly from $[0.8,1.2]$. Residuals from the visual-error source study are resampled in circular five-block segments, preserving the pairing of output channels. Each synthetic group averages twelve participant residual draws. Every candidate fits abrupt exposure with twelve starts and predicts gradual exposure using its source-selected ridge strength. A forced label is assigned by held-out standardized MSE; the complete loss vector, runner-up gap and confusion matrix are retained. The generating distributions are local perturbations of fitted families, so this exercise evaluates discrimination in the specified protocol and parameter neighbourhood.

The source-only convergence audit repeats 64 starts with a fresh seed. Its losses and the close-pole numerical check are reported below with the full endpoint tables. Saved fits, human observations, predictions and recovery draws accompany the public repository, from which all stages can be rebuilt.
''' if not z else r'''
两项力场档案各包含12名参与者。块级观测包含两种序列，每序列70个块及两个响应窗口（180--230 ms、230--300 ms）。前10块确定各参与者、各序列的基线均值。联合评分先用来源基线方差归一化各输出MSE，再平均两项标准化评分。主分析使用目标暴露前基线计算变化；另一分析完全迁移来源基线，不对目标进行校准。目标暴露后观测不参与参数拟合和惩罚项选择。两项研究构成完整的外部验证集。\cite{franklin2021,franklin2023}

四类候选模型分别具有单共同时间模式（三参数）、各输出单模式（四参数）、带混合读出的双共同模式（六参数）、各输出双模式（八参数）。块级表示为
\begin{equation}z_{r,t+1}=p_rz_{r,t}+(1-p_r)f_t,\qquad y_{i,t}=\sum_r c_{ir}(z_{r,t}+z_{r,t+1})/2.\end{equation}
全部候选使用相同归一化力场序列、零初态、测量时点及来源输出尺度。极点描述有效闭环块级持续性，取值范围为0至0.9995。接近极点采用差商基，并在间距$10^{-4}$时切换为导数极限；系数对应实际使用的基。在极点给定时，以最小二乘及可选岭惩罚求解线性系数。极点采用变量投影优化，各初值最多600次函数评价，容差记录于\texttt{analysis/validate.py}。

岭强度从$0,0.001,0.01,0.1,1$中通过来源参与者六折验证选择。每折留出12名来源参与者中的两人，各候选使用六个初值。来源最终拟合使用64初值，无正则拟合具有相同最终预算，并独立于目标表现全部保留。相同惩罚网格不保证相同有效复杂度，因此同时报告两种惩罚策略、两个窗口和两个迁移方向。暴露前基线与来源阶段均值模板作为预测比较。配对目标参与者自助法区间以已拟合来源为条件，不包含来源研究重采样。存档评分与拟合参数提供全部分输出及联合指标。

恢复对每家族抽取20个新实例，共80个。来源拟合极点加入SD为0.03的高斯扰动并截断到$[0.001,0.999]$；每个输出的系数乘以从$[0.8,1.2]$独立抽取的系数。视觉误差来源研究残差以循环五块片段重采样，保留输出通道配对。每组合成数据平均12个参与者残差抽样。各候选以12初值拟合突然暴露，并用来源选择的岭强度预测渐变暴露。以留出标准化MSE强制分配标签，保留完整损失向量、次优差值及混淆矩阵。生成分布是拟合家族的局部扰动，因此本检验评价的是指定方案与参数邻域中的判别力。

来源内收敛审计以新随机种子重复64初值，相关损失与接近极点数值检查在下文和完整评分表共同报告。拟合、人体观测、预测及恢复抽样均存档于公开仓库，各阶段可以重建。
''')
    return s
