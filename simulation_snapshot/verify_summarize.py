from interventions import *
from invariant import Q
import hashlib
summ=[]
for f in sorted((R/'results').glob('*.json')):
 rows=json.loads(f.read_text());models=[g['model'] for g in rows[0]['fits']];mat=np.zeros((len(models),len(models)),int)
 for row in rows:mat[models.index(row['truth']),np.argmin([g['test_loss'] for g in row['fits']])]+=1
 hits=0;nf=0
 for row in rows:
  for ff in row['fits']:
   lo,hi=bounds(ff['model']);pp=np.array(ff['params']);hits+=int(np.any((pp-lo<1e-5)|(hi-pp<1e-5)));nf+=1
 summ.append(dict(run=f.stem,datasets=len(rows),models=models,recovery=float(np.trace(mat)/mat.sum()),confusion=mat.tolist(),train=rows[0]['train_events'],test=rows[0]['test_events'],max_gradient=max(g['optimality'] for row in rows for g in row['fits']),fits_at_bound=hits,fit_count=nf))
(R/'summary.json').write_text(json.dumps(summ,indent=2));print(summ,flush=True)
rng=np.random.default_rng(9761117);inv=[];emb=[];fullmix=[];nofits=[]
for _ in range(100):
 p=generating('separable_gain',rng);B,_,_=unpack(p,'separable_gain');inv.append(abs(Q(B)))
 p=generating('routed_rank1',rng);B,a,g=unpack(p,'routed_rank1');pf=np.r_[B.ravel(),a,g];x=design('calibrated',1,rng,True);emb.append(np.max(abs(pred(p,'routed_rank1',x)-pred(pf,'routed_full',x))))
 p=generating('routed_full',rng);B,_,_=unpack(p,'routed_full');T=np.linalg.solve(B[0],B[1]);fullmix.append(np.max(abs(B[0]@T-B[1])))
for i,m in enumerate(MODELS):
 p=generating(m,rng);x=design('calibrated',1,rng);y=pred(p,m,x);best,_=fit(m,x,y,np.array([.2,1]),auxiliary(p,m),np.array([.035]*4+[.07]*2),i,starts=12);nofits.append(dict(model=m,max_prediction_error=float(np.max(abs(pred(best[1],m,x)-y)))))
# Reconstruct 25 confirmation fits, increase budget to 24 starts including original optimum.
rows=json.loads((R/'results/calibrated_r16_near0_bias0.json').read_text());budget=[]
for row in rows[::96]:
 rng=np.random.default_rng(row['seed']);p=generating(row['truth'],rng);x=design('calibrated',16,rng);xt=design('calibrated',16,rng,True);d=row['donor'];scale=np.maximum(LIB[d].std(0)*np.sqrt(2),[.03,.2]);y=pred(p,row['truth'],x)+noise(d,len(x),rng,np.sqrt(2));_=noise(d,len(xt),rng,np.sqrt(2));auxsd=np.array([.035]*4+[.07]*2);aux=auxiliary(p,row['truth'])+rng.normal(0,auxsd)
 for f in row['fits']:
  best,h=fit(f['model'],x,y,scale,aux,auxsd,9861117,24,np.array(f['params']));budget.append(dict(truth=row['truth'],rival=f['model'],old=f['objective'],new=best[0],improvement=f['objective']-best[0]))
rng=np.random.default_rng(123);outside=0
for m in MODELS:
 for _ in range(10000):
  p=generating(m,rng);lo,hi=bounds(m);outside+=int(np.any((p<lo)|(p>hi)))
assert outside==0
assert max(inv)<1e-10 and max(emb)<1e-10 and max(fullmix)<1e-10
assert max(r['max_prediction_error'] for r in nofits)<1e-6
out=dict(generating_support_draws=50000,outside_bounds=outside,separable_gain_Q_max=max(inv),rank1_full_embedding_max=float(max(emb)),unrestricted_input_mixing_equivalence_max=float(max(fullmix)),noiseless=nofits,budget_audit=budget,noise_sha256=hashlib.sha256((R/'noise_library.npz').read_bytes()).hexdigest())
(R/'verification.json').write_text(json.dumps(out,indent=2));print(out,flush=True)
