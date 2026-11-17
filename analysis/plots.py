from pathlib import Path
import json,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parent.parent;D=R/'analysis';plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,'axes.spines.top':False,'axes.spines.right':False,'axes.labelcolor':'#193447','text.color':'#193447','axes.titleweight':'bold'})
colors=['#176e88','#d87552'];fig,ax=plt.subplots(2,2,figsize=(10,7.4),layout='constrained');p=np.load(D/'crossstudy_predictions.npz')
for j in range(2):
 a=ax[0,j];truth=p['visual_errors_180_230_shared_two_mixed_source_cv_ridge_target'][:,0,:,j];t=np.arange(70);m=np.nanmean(truth,0);se=np.nanstd(truth,0,ddof=1)/np.sqrt(12)
 a.errorbar(t,m,yerr=se,fmt='.',ms=3,elinewidth=.45,color='#778792',alpha=.75,label='Target human mean ± SEM')
 for model,c,lab in zip(['shared_two_mixed','separate_two'],colors,['Common two modes','Separate two modes']):a.plot(t,p['visual_errors_180_230_'+model+'_source_cv_ridge'][0,:,j],c=c,lw=1.8,label=lab)
 a.axvline(10,color='#b9c2c7',ls=':',lw=1);a.axvline(60,color='#b9c2c7',ls=':',lw=1);a.set(xlabel='Block (12 trials)',ylabel=['Compensation change','Feedback-force change (N)'][j],title=['a  Compensation: source E → target C','b  Feedback: source E → target C'][j]);a.legend(fontsize=7,frameon=False)
d=json.loads((D/'crossstudy_summary.json').read_text());a=ax[1,0];rows=[r for r in d['contrasts'] if r['window']=='180_230' and r['a']=='shared_two_mixed'];labels=[]
for i,r in enumerate(rows):
 m=r['delta_b_minus_a'];lo,hi=r['ci95'];a.errorbar(m,i,xerr=[[m-lo],[hi-m]],fmt='o',color=colors[i%2],capsize=3);labels.append(('C → E' if r['source']=='visual_clamp' else 'E → C')+' / '+('CV ridge' if r['variant']=='source_cv_ridge' else 'No penalty'))
a.axvline(0,color='#93a3ae',ls='--',lw=1);a.set(yticks=range(4),yticklabels=labels,xlabel='MSE: separate two − common two\nNegative favours separate',title='c  Architecture contrast depends on penalty')
a=ax[1,1];loc=json.loads((D/'localization_summary.json').read_text())['summary']
for i,r in enumerate(loc):
 m=r['means'][2];lo,hi=r['ci95'][2];a.errorbar(i,m,yerr=[[m-lo],[hi-m]],fmt='o',color='#176e88',capsize=4,ms=6)
a.axhline(0,c='#93a3ae',ls='--',lw=1);a.set(xticks=range(4),xticklabels=['Control\nn=20','Instructed\nn=21','Cursor jump\nn=20','Hand view\nn=29'],ylabel='Active − passive shift (degrees)',title='d  Reports have different learning sensitivity')
fig.savefig(R/'figures/empirical_validation.png',dpi=300);fig.savefig(R/'figures/empirical_validation.pdf');plt.close(fig)
# Exact analytic counterexample, always labelled as constructed rather than human.
d=json.loads((D/'counterexamples.json').read_text());fig,axs=plt.subplots(1,2,figsize=(9,3.3),layout='constrained');k=d['delay'];rat=np.array(d['ratios'])
for j in range(2):axs[0].plot(k,rat[:,j],c=colors[j],lw=2,label=f'Input {j+1}')
axs[0].set(xlabel='Error-free retention steps',ylabel='Output 1 / output 2',title='Fixed readout, mixed temporal states');axs[0].legend(frameon=False)
cal=json.loads((D/'calibration_stress.json').read_text())['results'];rs=[r for r in cal if r['truth']=='mixture']
for key,c,lab in [('wrong_zero_loading_parameter_mse',colors[1],'Assume selective report'),('known_loading_parameter_mse',colors[0],'Known cross-loading')]:axs[1].plot([r['loading'] for r in rs],[r[key] for r in rs],'-o',c=c,label=lab)
axs[1].set(xlabel='Update loading in report',ylabel='Summed parameter squared error',title='Mixed input and update contrasts');axs[1].legend(frameon=False,fontsize=8)
fig.savefig(R/'figures/counterexamples.png',dpi=300);plt.close(fig)
print('Figures saved')
