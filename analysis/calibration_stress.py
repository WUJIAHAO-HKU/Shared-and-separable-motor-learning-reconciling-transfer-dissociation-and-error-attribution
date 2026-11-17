"""Pure and mixed loci under cross-loaded sensory reports; equal LS budget."""
from pathlib import Path
import numpy as np,json
R=Path(__file__).resolve().parent.parent;rng=np.random.default_rng(1300117)
rows=[]
for loading in [0.,.25,.5,.75,1.]:
 for truth in ['input','update','mixture']:
  out=[]
  for rep in range(500):
   I=rng.normal(size=4);U=rng.normal(size=4)
   I*=.8/np.linalg.norm(I);U*=.8/np.linalg.norm(U)
   if truth=='input':U*=0
   if truth=='update':I*=0
   y=I+U+rng.normal(0,.05,4);ell=I+loading*U+rng.normal(0,.05,4)
   # Wrong zero-loading model: [y,l]=[I+U,I]. All 8 mixed coefficients fit exactly.
   wrongI=ell;wrongU=y-ell
   wrong=float(np.sum((wrongI-I)**2+(wrongU-U)**2))
   x=np.array([[1,1],[1,loading]])
   est=np.linalg.lstsq(x,np.array([y,ell]),rcond=None)[0]
   correct=float(np.sum((est[0]-I)**2+(est[1]-U)**2))
   # Full mixed model permits every decomposition if report loading unknown.
   losses=[float(np.sum((y-ell)**2)/2),float(np.sum(ell**2))]
   out.append((wrong,correct,int(losses[0]<losses[1])))
  a=np.array(out);rows.append(dict(loading=loading,truth=truth,n=500,wrong_zero_loading_parameter_mse=float(a[:,0].mean()),known_loading_parameter_mse=float(a[:,1].mean()),forced_pure_input_selection=float(a[:,2].mean()),known_loading_rank=int(np.linalg.matrix_rank(x))))
(R/'analysis/calibration_stress.json').write_text(json.dumps(dict(results=rows,noise_sd=.05,contrast_norm=.8,noise_status='assumed normalized report noise, not empirical human trial noise',unknown_loading='For any invertible input contrast I_star, choose U_star=y-I_star and a free report loading to reproduce ell; motor and report data alone leave a continuum. Rank deficiency at L=1 persists even with known loading.'),indent=2))
print('calibration stress done')
