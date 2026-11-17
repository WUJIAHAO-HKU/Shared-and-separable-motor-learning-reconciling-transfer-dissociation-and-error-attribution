"""Gain-invariant source-by-input-by-output contrast; disjoint cell noise blocks."""
import numpy as np,json
from scipy.stats import t
from interventions import R,LIB,UNITS,noise,unpack,generating,MODELS

def Q(B):
    return B[1,0,0]*B[1,1,1]*B[0,0,1]*B[0,1,0]-B[1,0,1]*B[1,1,0]*B[0,0,0]*B[0,1,1]

def run():
 rng=np.random.default_rng(9661117);out=[];records=[]
 for truth in MODELS:
  for near in [False,True]:
   for reps in [8,16,32,64]:
    vals=[];targets=[]
    for j in range(768):
     p=generating(truth,rng,near);B,_,_=unpack(p,truth);est=np.zeros((2,2,2));d=j%24
     for q in range(2):
      for e in range(2):
       yy=[]
       for sign in [-1,1]:
        z=noise(d,reps,rng,np.sqrt(2));yy.append(B[q,:,e]+sign*z.mean(0)/UNITS)
       est[q,:,e]=np.mean(yy,0)
     vals.append(Q(est));targets.append(Q(B))
    vals=np.array(vals);targets=np.array(targets)
    # Explicit Monte Carlo population centering, not adjustment of empirical observations.
    center=float(np.mean(vals-targets));raw=vals.copy();vals-=center;powers={};rawpowers={}
    for N in [12,24,48,96,144,240]:
     ix=rng.integers(768,size=(5000,N));a=vals[ix];st=a.mean(1)/(a.std(1,ddof=1)/np.sqrt(N));powers[str(N)]=float(np.mean(st>t.ppf(.975,N-1)));ar=raw[ix];sr=ar.mean(1)/(ar.std(1,ddof=1)/np.sqrt(N));rawpowers[str(N)]=float(np.mean(sr>t.ppf(.975,N-1)))
    row=dict(truth=truth,near=near,reps=reps,paired_readouts=8*reps,expected_Q=float(targets.mean()),power=powers,raw_finite_pool_power=rawpowers,monte_carlo_centering=center);out.append(row);records.append(vals)
    print(truth,near,reps,round(targets.mean(),3),round(powers['48'],3),flush=True)
 (R/'invariant_results.json').write_text(json.dumps(out,indent=2));np.savez_compressed(R/'invariant_records.npz',values=records)
if __name__=='__main__':run()
