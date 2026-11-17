"""Frozen cross-study temporal-kernel prediction; run from any directory.
This estimates effective block responses, not neural storage or trial retention.
All tuning uses source participants. Target post-exposure data are scoring only.
"""
from pathlib import Path
import numpy as np, pandas as pd, json, hashlib, time
from scipy.optimize import least_squares
from scipy.signal import lfilter
R=Path(__file__).resolve().parent.parent; O=R/'analysis'; O.mkdir(exist_ok=True)
MODELS=['shared_one','separate_one','shared_two_mixed','separate_two']
SPECS={'shared_one':(1,False),'separate_one':(1,True),'shared_two_mixed':(2,False),'separate_two':(2,True)}
def basis(p,field):
    # Unit DC gain; amplitudes then have a comparable ridge scale across poles.
    p=np.sort(p)
    z=np.array([lfilter([1-q],[1,-q],field) for q in p]).T
    g=(z+np.vstack([np.zeros((1,len(p))),z[:-1]]))/2
    if len(p)==2:
        gap=p[1]-p[0]
        if gap>1e-4:g[:,1]=(g[:,1]-g[:,0])/gap
        else:
            q=np.mean(p);der=lfilter([-1,1],[1,-2*q,q*q],field)
            g[:,1]=(der+np.r_[0,der[:-1]])/2
    return g
def prediction(p,coef,fields,model):
    m,sep=SPECS[model];out=np.zeros((len(fields),len(fields[0]),2))
    for s,field in enumerate(fields):
        for j in range(2):out[s,:,j]=basis(np.array(p[j*m:(j+1)*m] if sep else p),field)@coef[j]
    return out
def fit(y,fields,scale,model,lam=0.,starts=12,seed=71):
    m,sep=SPECS[model];n=m*(2 if sep else 1);rg=np.random.default_rng(seed)
    def project(p,ret=False):
        co=[];res=[]
        for j in range(2):
            x=np.concatenate([basis(p[j*m:(j+1)*m] if sep else p,f) for f in fields])/scale[j]
            yy=y[:,:,j].ravel()/scale[j];ok=np.isfinite(yy);xx=x[ok];yy=yy[ok]
            # Mean data loss plus lambda * squared amplitude in source SD units.
            penalty=np.sqrt(lam*len(yy))/scale[j]
            c=np.linalg.lstsq(np.vstack([xx,penalty*np.eye(m)]),np.r_[yy,np.zeros(m)],rcond=None)[0]
            co.append(c);res.extend((xx@c-yy).tolist());res.extend((penalty*c).tolist())
        return (np.array(co),np.array(res)) if ret else np.array(res)
    history=[]
    for i in range(starts):
        init=rg.uniform(.02,.98,n)
        if i==0:init=np.tile(np.linspace(.35,.95,m),2 if sep else 1)
        z=least_squares(project,init,bounds=(np.zeros(n),np.ones(n)*.9995),max_nfev=600,ftol=2e-9,xtol=2e-9,gtol=2e-8)
        history.append(dict(p=z.x.tolist(),loss=float(np.mean(z.fun**2)),success=bool(z.success),nfev=int(z.nfev),optimality=float(z.optimality)))
    b=min(history,key=lambda x:x['loss']);co,res=project(np.array(b['p']),True)
    return dict(model=model,p=b['p'],coef=co.tolist(),lambda_=lam,loss=b['loss'],starts=history)
def pred(f,fields):return prediction(f['p'],np.array(f['coef']),fields,f['model'])
def load():
    df=pd.read_csv(R/'public_data/block_observations.csv');df['t']=df.phase.map({1:0,2:10,3:40,4:60})+df.block
    fields=np.zeros((2,70));fields[0,10:60]=1;fields[1,10:40]=(np.arange(30)*12+6.5)/361;fields[1,40:60]=1
    arrays={}
    for cohort in ['visual_errors','visual_clamp']:
        for w in ['180_230','230_300']:
            y=np.full((12,2,70,2),np.nan)
            for _,r in df[(df.cohort==cohort)&(df.window==w)].iterrows():y[int(r.participant),int(r.schedule),int(r.t)]=[r.force_comp,r.feedback]
            base=np.nanmean(y[:,:,:10],2);arrays[cohort,w]=(y-base[:,:,None,:],base)
    return arrays,fields
def crossstudy():
    arrays,fields=load();results=[];scores=[];allpred={};rg=np.random.default_rng(118331);start=time.time()
    # Specs fixed in code before any target scoring; two time windows both reported.
    for source,target in [('visual_errors','visual_clamp'),('visual_clamp','visual_errors')]:
      for window in ['180_230','230_300']:
        yy,bb=arrays[source,window];target_y,target_b=arrays[target,window]
        scale=np.nanstd(yy[:,:,:10],axis=(0,1,2),ddof=1);mean=np.nanmean(yy,0)
        for mi,model in enumerate(MODELS):
            cv=[]
            for lam in [0.,.001,.01,.1,1.]:
                losses=[]
                for fold in range(6):
                    ix=np.arange(12);valid=ix[2*fold:2*fold+2];train=np.setdiff1d(ix,valid)
                    f=fit(np.nanmean(yy[train],0),fields,scale,model,lam,starts=6,seed=122+fold)
                    losses.append(float(np.nanmean(((pred(f,fields)[None,:,10:]-yy[valid,:,10:])/scale)**2)))
                cv.append(dict(lambda_=lam,loss=float(np.mean(losses)),fold_losses=losses))
            lam=min(cv,key=lambda x:x['loss'])['lambda_'];f=fit(mean,fields,scale,model,lam,starts=64,seed=99117)
            # Unpenalized refit reported too, regardless of target performance.
            fu=fit(mean,fields,scale,model,0.,starts=64,seed=99117)
            for variant,ff in [('source_cv_ridge',f),('unpenalized',fu)]:
                pr=pred(ff,fields);mse=np.nanmean((pr[None,:,10:]-target_y[:,:,10:])**2,axis=(1,2));norm=mse/scale**2
                # Strict source-baseline transport is a second, reported endpoint.
                strict=pr[None]+np.mean(bb,axis=0)[None,:,None]-target_b[:,:,None]
                smse=np.nanmean((strict[:,:,10:]-target_y[:,:,10:])**2,axis=(1,2))
                key=f'{source}_{window}_{model}_{variant}';allpred[key]=pr;allpred[key+'_target']=target_y
                results.append(dict(source=source,target=target,window=window,variant=variant,fit=ff,cv=cv if variant=='source_cv_ridge' else [],scale=scale.tolist(),participant_mse=mse.tolist(),participant_standardized_mse=norm.tolist(),strict_source_baseline_mse=smse.tolist()))
                for sub in range(12):scores.append(dict(source=source,target=target,window=window,model=model,variant=variant,participant=sub,compensation_mse=mse[sub,0],feedback_mse=mse[sub,1],joint_standardized_mse=np.mean(norm[sub]),strict_joint_standardized_mse=np.mean(smse[sub]/scale**2)))
            print(source,window,model,'seconds',round(time.time()-start),flush=True)
        for model,pr in [('baseline',np.zeros_like(mean)),('source_phase_template',np.concatenate([np.tile(np.nanmean(mean[:,a:b],axis=1)[:,None],(1,b-a,1)) for a,b in [(0,10),(10,40),(40,60),(60,70)]],axis=1))]:
            mse=np.nanmean((pr[None,:,10:]-target_y[:,:,10:])**2,axis=(1,2));allpred[f'{source}_{window}_{model}']=pr
            for sub in range(12):scores.append(dict(source=source,target=target,window=window,model=model,variant='benchmark',participant=sub,compensation_mse=mse[sub,0],feedback_mse=mse[sub,1],joint_standardized_mse=np.mean(mse[sub]/scale**2),strict_joint_standardized_mse=np.nan))
        (O/'crossstudy_fits.json').write_text(json.dumps(results,indent=2));pd.DataFrame(scores).to_csv(O/'crossstudy_scores.csv',index=False);np.savez_compressed(O/'crossstudy_predictions.npz',**allpred)
    d=pd.DataFrame(scores);summary=[];contrasts=[]
    for (s,w,v,m),g in d.groupby(['source','window','variant','model']):
        vals=g.joint_standardized_mse.to_numpy();boot=vals[rg.integers(0,12,(10000,12))].mean(1)
        summary.append(dict(source=s,window=w,variant=v,model=m,joint_mse=float(vals.mean()),ci95=np.quantile(boot,[.025,.975]).tolist(),rmse_compensation=float(np.sqrt(g.compensation_mse.mean())),rmse_feedback=float(np.sqrt(g.feedback_mse.mean()))))
    for (s,w,v),g in d[d.variant!='benchmark'].groupby(['source','window','variant']):
      for a,b in [('shared_one','separate_one'),('shared_two_mixed','separate_two'),('shared_one','shared_two_mixed')]:
        aa=g[g.model==a].sort_values('participant').joint_standardized_mse.to_numpy();bb=g[g.model==b].sort_values('participant').joint_standardized_mse.to_numpy();delta=bb-aa
        boot=delta[rg.integers(0,12,(10000,12))].mean(1)
        contrasts.append(dict(source=s,window=w,variant=v,a=a,b=b,delta_b_minus_a=float(delta.mean()),ci95=np.quantile(boot,[.025,.975]).tolist()))
    (O/'crossstudy_summary.json').write_text(json.dumps(dict(summary=summary,contrasts=contrasts),indent=2))
    (O/'provenance.json').write_text(json.dumps(dict(data_sha256=hashlib.sha256((R/'public_data/block_observations.csv').read_bytes()).hexdigest(),n_people=24,studies=['10.51628/001c.22336','10.51628/001c.91252'],unit='processed 12-trial blocks; mean field in block; half-block state observation',primary_window='180_230',secondary_window='230_300',calibration='target pre-exposure mean only; source-baseline-only sensitivity included',uncertainty='target-participant cluster bootstrap, conditional on trained source; no source uncertainty CI',source_cv='six fixed participant folds, all target post-exposure values excluded',mechanistic_scope='effective stable linear temporal kernels; poles are closed-loop block persistence, not neural retention'),indent=2))
    print('CROSS STUDY DONE',flush=True)
def counterexamples():
    H=np.array([[1,.4],[.6,1]]);U=np.array([[.3,.1],[.15,.5]]);p=np.array([.9,.7]);ks=np.arange(13)
    B=np.array([H@np.diag(p**k)@U for k in ks]);ratios=B[:,0,:]/B[:,1,:]
    # Shared states copied into separate output modules are observationally equal.
    separate=np.array([np.array([[sum(H[i,l]*p[l]**k*U[l,j] for l in range(2)) for j in range(2)] for i in range(2)]) for k in ks])
    # Calibration has unknown update loading L. I+U and C*I+L*U observed.
    # Scalar factor blocks suffice: each entry of a 2x2 contrast repeats this design.
    rows=[]
    for L in [0.,.1,.25,.5,.75,1.]:
        x=np.array([[1,1],[1,L]])
        rows.append(dict(update_loading=L,smallest_singular=float(np.linalg.svd(x)[1][-1]),condition_number=float(np.linalg.cond(x)),inferred_input_when_true_update= L,inferred_update=1-L))
    D=np.array([[.4,.1],[.2,.3]])
    out=dict(H=H.tolist(),U=U.tolist(),poles=p.tolist(),delay=ks.tolist(),B=B.tolist(),ratios=ratios.tolist(),separate_clone_max_error=float(np.max(abs(B-separate))),calibration=rows,alias_true_update=D.tolist(),alias_inferred_input=D.tolist(),alias_max_residual=0.,interpretation='constant H and mixed U generate changing ratios; report cross-loading produces exact input/update alias')
    (O/'counterexamples.json').write_text(json.dumps(out,indent=2));print('COUNTEREXAMPLES DONE',flush=True)
if __name__=='__main__':
    counterexamples();crossstudy()
