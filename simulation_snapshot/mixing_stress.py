"""Independent input-calibration stress; its transfer to learning is an assumption."""
from interventions import *
from invariant import Q
from scipy.stats import t
rng=np.random.default_rng(9961117);out=[]
for truth in ['input_mixing','routed_full']:
 for se in [0,.03,.10]:
  raw=[];corrected=[];target=[]
  for j in range(4096):
   p=generating('scalar_full' if truth=='input_mixing' else 'routed_full',rng);B,_,_=unpack(p,'scalar_full' if truth=='input_mixing' else 'routed_full')
   T=np.array([[1,.3],[-.2,1.]])
   if truth=='input_mixing':B[1]=B[0]@T
   else:T=np.eye(2)
   Tb=T+rng.normal(0,se,(2,2));est=np.zeros((2,2,2,2))
   for half in range(2):
    for q in range(2):
     for e in range(2):
      yy=[]
      for sign in [-1,1]:yy.append(B[q,:,e]+sign*noise(j%24,8,rng,np.sqrt(2)).mean(0)/UNITS)
      est[half,q,:,e]=np.mean(yy,0)
   def crossQ(E):
    return np.mean([E[i,1,0,0]*E[1-i,1,1,1]*E[h,0,0,1]*E[1-h,0,1,0]-E[i,1,0,1]*E[1-i,1,1,0]*E[h,0,0,0]*E[1-h,0,1,1] for i in [0,1] for h in [0,1]])
   raw.append(crossQ(est));est[:,1]=est[:,1]@np.linalg.inv(Tb);corrected.append(crossQ(est))
   B[1]=B[1]@np.linalg.inv(T);target.append(Q(B))
  result=dict(truth=truth,input_calibration_se=se,people_simulated=4096,reps=16,estimator='two independent halves; cross-products across halves')
  for name,values in [('raw',raw),('corrected',corrected)]:
   v=np.array(values);a=v[rng.integers(4096,size=(5000,48))];stats=a.mean(1)/(a.std(1,ddof=1)/np.sqrt(48));result[name+'_positive_rate_N48']=float(np.mean(stats>t.ppf(.975,47)));result[name+'_mean']=float(v.mean())
  result['analytic_corrected_target']=float(np.mean(target));out.append(result)
(R/'mixing_stress.json').write_text(json.dumps(out,indent=2));print(out)
