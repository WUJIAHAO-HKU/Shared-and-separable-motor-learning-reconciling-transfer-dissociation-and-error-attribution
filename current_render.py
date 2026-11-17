from pathlib import Path
import json
import pandas as pd
from acceptance import CLAIMS,REMOVALS
import formatting as f
R=Path(__file__).parent
def h(x):return '\\section{'+x+'}\n'
def field(a,b):return '\\textbf{'+a+'} '+f.esc(b)+'\\par\n'
def render(z):
 s='\\clearpage'+h(('Claim-level evidence and counterexamples','逐结论证据及反例')[z])
 for i,row in enumerate(CLAIMS):
  s+=('\\clearpage' if i and i%2==0 else '\\medskip')+h(row[0]+' | '+row[1][z])
  for j,lab in enumerate([('Support','支持'),('Counterevidence','反证'),('Scope','范围'),('Retained claim and test','保留主张及检验')]):s+=field(lab[z],row[j+2][z])
 s+='\\clearpage'+h(('Measurement-removal logic','测量删除的判别后果')[z])
 for r in REMOVALS:s+='\\subsection*{'+r[z]+'}\n'+f.esc(r[z+2])+'\n\n'
 s+='\\clearpage'+h(('Cross-study prediction: complete endpoint scores','跨研究预测：完整分输出评分')[z])
 s+=('E denotes training with visual errors and C denotes visual-clamp training. The target is always the other study. Scores average participant MSE before taking the RMSE. Compensation is dimensionless; feedback is in N. Each joint MSE uses the source baseline SD for each channel, then averages channels. Both windows and both fitting strategies are retained. CIs below are conditional on the fitted source; the two studies are the complete external validation set.\n' if not z else 'E表示保留视觉误差的训练研究，C表示视觉钳制研究；目标始终为另一研究。先平均参与者MSE再取RMSE。补偿无量纲，反馈单位为N。联合MSE按来源基线各通道SD标准化后平均通道。两个时间窗和两种拟合策略均保留。下文区间以已拟合来源为条件，两项研究构成完整外部验证集。\n')
 d=json.loads((R/'analysis/crossstudy_summary.json').read_text());labels={'shared_one':'C1','separate_one':'S1','shared_two_mixed':'C2','separate_two':'S2','baseline':'Base','source_phase_template':'Phase'}
 s+=r'\small\begin{longtable}{lllr rr}\toprule'+'\n'+('Source/window & Fit & Model & Joint MSE & Comp. RMSE & FB RMSE','来源/窗口 & 拟合 & 模型 & 联合MSE & 补偿RMSE & 反馈RMSE')[z]+r'\\\midrule\endhead'+'\n'
 for r in d['summary']:
  src='E' if r['source']=='visual_errors' else 'C';v={'source_cv_ridge':'CV','unpenalized':'OLS','benchmark':'Ref'}[r['variant']]
  s+=f"{src}/{r['window'].replace('_','--')} & {v} & {labels[r['model']]} & {r['joint_mse']:.3f} & {r['rmse_compensation']:.3f} & {r['rmse_feedback']:.3f}"+r'\\'+'\n'
 s+=r'\bottomrule\end{longtable}\normalsize'+'\n'
 s+=h(('Transport without target baseline calibration','不使用目标基线校准的迁移')[z])
 s+=('The following joint standardized MSE uses source pre-exposure means, with no target baseline adjustment. All target post-exposure data remain held out.\n' if not z else '以下联合标准化MSE完全使用来源暴露前均值，不使用目标基线调整；目标暴露后数据始终留出。\n')
 raw=pd.read_csv(R/'analysis/crossstudy_scores.csv');g=raw[raw.variant!='benchmark'].groupby(['source','window','variant','model']).strict_joint_standardized_mse.mean()
 s+=r'\small\begin{longtable}{lllr}\toprule Source/window & Fit & Model & Joint MSE\\\midrule\endhead'+'\n'
 for (src,w,v,m),val in g.items():s+=('E' if src=='visual_errors' else 'C')+'/'+w.replace('_','--')+' & '+('CV' if v=='source_cv_ridge' else 'OLS')+' & '+labels[m]+f' & {val:.3f}'+r'\\'+'\n'
 s+=r'\bottomrule\end{longtable}\normalsize'+'\n'
 s+=('C1/S1: one common/output-specific temporal mode. C2/S2: two common/output-specific modes. CV: source-only selected ridge; OLS: unpenalized variable projection; Ref: baseline comparator. Model coefficients and all participant scores are supplied as JSON/CSV.\n' if not z else 'C1/S1：单共同/输出特异时间模式。C2/S2：双共同/输出特异时间模式。CV：来源内选择正则；OLS：无正则变量投影；Ref：基线比较。模型系数及全部参与者评分另附JSON/CSV。\n')
 s+=h(('Paired prediction contrasts','配对预测差异')) if False else h(('Paired prediction contrasts','配对预测差异')[z])
 s+=r'\small\begin{longtable}{llllrr}\toprule'+'\n'+('Source/window & Fit & A & B & B minus A & 95\% interval','来源/窗口 & 拟合 & A & B & B减A & 95\%区间')[z]+r'\\\midrule\endhead'+'\n'
 for r in d['contrasts']:
  src='E' if r['source']=='visual_errors' else 'C';v='CV' if r['variant']=='source_cv_ridge' else 'OLS'
  s+=f"{src}/{r['window'].replace('_','--')} & {v} & {labels[r['a']]} & {labels[r['b']]} & {r['delta_b_minus_a']:.3f} & [{r['ci95'][0]:.3f}, {r['ci95'][1]:.3f}]"+r'\\'+'\n'
 s+=r'\bottomrule\end{longtable}\normalsize'+'\n'
 s+='\\clearpage'+h(('Constructed counterexamples','构造性反例')[z])
 s+=r'\begin{center}\includegraphics[width=\textwidth]{counterexamples.png}\end{center}'+'\n'
 s+=('Left: exact fixed-readout two-mode construction. Right: pure and mixed-factor simulations under known or wrongly assumed zero report cross-loading. These are constructed examples and simulated parameter errors, separate from the human measurements. The singular case at loading one has an unresolved factor decomposition.\n' if not z else '左：固定读出双模式的精确构造。右：已知或错误设为零的报告交叉载荷下，纯机制与混合因子的模拟参数误差。此处为构造反例及模拟误差，与人体测量分别报告。载荷为1的奇异情形保留因子分解歧义。\n')
 s+='\\clearpage'+h(('Noise-preserving model recovery','保留噪声结构的模型恢复')[z]);rec=json.loads((R/'analysis/recovery.json').read_text())
 s+=('Each row contains twenty fresh generating instances. Columns are forced winning labels on gradual-exposure prediction after abrupt-exposure fitting. Parameter perturbations and noise draws are new; generating families and penalty values come from the visual-error source study. The source residual library preserves paired channels and five-block segments. This is a protocol-specific diagnostic with finite Monte Carlo precision.\n' if not z else '每行包含20个新生成实例。列为拟合突然暴露后，在渐变暴露预测中强制选出的标签。参数扰动及噪声抽样为新增，生成家族及正则值来自视觉误差来源研究。来源残差保留通道配对及五块片段。该结果为特定方案诊断，具有有限蒙特卡洛精度。\n')
 s+=r'\begin{center}\begin{tabular}{lrrrr}\toprule True / selected & C1 & S1 & C2 & S2\\\midrule'+'\n'
 for model,row in zip(rec['models'],rec['confusion']):s+=labels[model]+' & '+' & '.join(map(str,row))+r'\\'+'\n'
 s+=r'\bottomrule\end{tabular}\end{center}'+'\n'
 s+=h(('Cross-loading stress: pure and mixed changes','交叉载荷压力测试：纯机制及混合变化')[z])
 cal=json.loads((R/'analysis/calibration_stress.json').read_text())
 s+=('This test uses normalized assumed report noise SD 0.05 and factor norm 0.8, with 500 instances per cell. Parameter error sums squared errors over four input and four update coefficients. Known-loading fits and erroneous zero-loading fits use exact least squares. At loading one, the known model has rank one and its minimum-norm solution is not unique mechanistic recovery.\n' if not z else '该测试使用设定的归一化报告噪声SD 0.05、因子范数0.8，每格500个实例。参数误差为四个输入及四个更新系数平方误差之和。已知载荷及错误零载荷模型均用精确最小二乘。载荷为1时已知模型的秩为1，最小范数解保留机制非唯一性。\n')
 s+=r'\small\begin{longtable}{llrrr}\toprule Loading & Truth & Wrong-model error & Known-loading error & Rank\\\midrule\endhead'+'\n'
 for r in cal['results']:s+=f"{r['loading']:.2f} & {r['truth']} & {r['wrong_zero_loading_parameter_mse']:.4f} & {r['known_loading_parameter_mse']:.4f} & {r['known_loading_rank']}"+r'\\'+'\n'
 s+=r'\bottomrule\end{longtable}\normalsize'+'\n'
 s+=h(('Independent localization check','独立定位数据检查')[z]);loc=json.loads((R/'analysis/localization_summary.json').read_text())
 for r in loc['summary']:s+=field(r['group']+f" (n={r['n']})",('Active, passive, active-minus-passive shifts: ' if not z else '主动、被动、主动减被动变化：')+', '.join(f'{m:.2f} [{ci[0]:.2f}, {ci[1]:.2f}]' for m,ci in zip(r['means'],r['ci95'])))
 s+=('Intervals use participant resampling; all three author-interpolated spatial directions are averaged. The control/instructed groups were reused from an earlier publication and are counted once here. This reanalysis tests report selectivity within a study; it is separate from the cross-study force-field prediction.\n' if not z else '区间采用参与者重采样，平均作者插值得到的三个空间方向。对照/指示组曾用于更早发表研究，此处只计数一次。该重分析检验单研究中的报告选择性，与跨研究力场预测分别报告。\n')
 s+=h(('Optimization and numerical representation','优化与数值表示')[z]);audit=json.loads((R/'analysis/optimization_audit.json').read_text())
 s+=('The 64-start source-only audit used a fresh random seed against the 64-start final fits. Maximum loss improvement: ' if not z else '64初值来源内审计用新随机种子与64初值最终拟合比较，最大损失改善为：')+f"{max(x['improvement'] for x in audit):.3g}. "+('Close-pole divided differences avoid opposite-coefficient cancellation. Baseline-only transport scores, complete optimizer records, data hashes and source extraction checks are supplied.\n' if not z else '接近极点采用差商表示，避免相反系数抵消。随附仅来源基线迁移评分、完整优化记录、数据哈希及来源提取核查。\n')
 return s
