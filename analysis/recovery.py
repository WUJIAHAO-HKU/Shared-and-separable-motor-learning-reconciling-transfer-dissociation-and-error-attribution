from validate import *
def run():
 arrays,fields=load();fits=json.loads((O/'crossstudy_fits.json').read_text());rng=np.random.default_rng(202611174);records=[]
 yy,_=arrays['visual_errors','180_230'];mean=np.nanmean(yy,0);noise=yy-mean
 scale=np.nanstd(yy[:,:,:10],axis=(0,1,2),ddof=1)
 truthfits={x['fit']['model']:x['fit'] for x in fits if x['source']=='visual_errors' and x['window']=='180_230' and x['variant']=='source_cv_ridge'}
 for truth in MODELS:
  for rep in range(20):
   tf=truthfits[truth].copy();tf['p']=np.clip(np.array(tf['p'])+rng.normal(0,.03,len(tf['p'])),.001,.999).tolist();tf['coef']=(np.array(tf['coef'])*rng.uniform(.8,1.2,(2,1))).tolist();mu=pred(tf,fields)
   nn=[]
   for sch in range(2):
    # Same row indices for both channels, moving blocks length five; n=12 group mean.
    draws=[]
    for i in range(12):
     sub=rng.integers(12);ix=np.concatenate([(rng.integers(70)+np.arange(5))%70 for _ in range(14)]);draws.append(noise[sub,sch,ix])
    nn.append(np.nanmean(draws,0))
   sy=mu+np.array(nn);loss=[];models=[]
   for cand in MODELS:
    f=fit(sy[:1],fields[:1],scale,cand,lam=truthfits[cand]['lambda_'],starts=12,seed=991+rep);pr=pred(f,fields[1:])[0]
    loss.append(float(np.nanmean(((pr[10:]-sy[1,10:])/scale)**2)));models.append(f)
   order=np.argsort(loss);records.append(dict(truth=truth,rep=rep,parameters=tf,winner=MODELS[order[0]],loss=loss,gap=float(loss[order[1]]-loss[order[0]]),fits=models))
  print('recovery',truth,flush=True)
 confusion=[[sum(r['truth']==a and r['winner']==b for r in records) for b in MODELS] for a in MODELS]
 (O/'recovery.json').write_text(json.dumps(dict(models=MODELS,n=80,reps=20,confusion=confusion,records=records,noise='source participant residuals, paired five-block bootstrap; group mean of 12; fresh instances; abrupt fit, gradual holdout',scope='effective temporal-kernel families, forced assignment; common poles can be duplicated in separate circuits'),indent=2))
 print(confusion,flush=True)
if __name__=='__main__':run()
