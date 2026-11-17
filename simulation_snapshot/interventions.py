"""Prospective transfer-kernel design study. All new outcomes are synthetic.
No privileged neural intervention is assumed. Flexible rivals retain the shared subset.
"""
from pathlib import Path
import numpy as np,json,argparse,time
from scipy.optimize import least_squares
R=Path(__file__).parent
MODELS=['scalar_rank1','scalar_full','routed_rank1','routed_full','separable_gain']
LIB=np.load(R/'noise_library.npz')['residuals']
UNITS=np.array([.24,.72])

def unpack(p,m):
    if m=='scalar_rank1':
        b=np.array([[p[0],p[1]],[p[2]*p[0],p[2]*p[1]]]); mats=np.array([b,p[3]*b]);n=4
    elif m=='scalar_full':
        b=np.array(p[:4]).reshape(2,2);mats=np.array([b,p[4]*b]);n=5
    elif m=='routed_rank1':
        mats=np.array([[[p[j],p[j+1]],[p[j+2]*p[j],p[j+2]*p[j+1]]] for j in [0,3]]);n=6
    elif m=='routed_full':mats=np.array(p[:8]).reshape(2,2,2);n=8
    else:
        b=np.array(p[:4]).reshape(2,2);mats=np.array([b,np.array(p[4:6])[:,None]*b*np.array([1,p[6]])]);n=7
    return mats,np.array(p[n:n+2]),np.array(p[n+2:n+4])

def bounds(m):
    if m=='scalar_rank1':lo=[-2,-2,-2,.1];hi=[2,2,2,2]
    elif m=='scalar_full':lo=[-2]*4+[.1];hi=[2]*4+[2]
    elif m=='routed_rank1':lo=[-2]*6;hi=[2]*6
    elif m=='routed_full':lo=[-2]*8;hi=[2]*8
    else:lo=[-2]*4+[.1]*3;hi=[2]*4+[2]*3
    # Broad symmetric map bounds include every generating draw, including amplified cross-updates.
    lo=[-4 if v==-2 else v for v in lo];hi=[4 if v==2 and lo[i]==-4 else v for i,v in enumerate(hi)]
    return np.array(lo+[.5,.5,.3,.3]),np.array(hi+[.999,.999,2,2])

def pred(p,m,x):
    B,a,g=unpack(p,m);e=x[:,:2];q,qr,lag=x[:,2:].T
    mix=(1-q[:,None,None])*B[0]+q[:,None,None]*B[1]
    # q encodes mixture of two experimentally calibrated contexts, not a neural probability.
    return np.einsum('nij,nj->ni',mix,e)*a[None,:]**lag[:,None]*(1+qr[:,None]*(g-1))*UNITS

def auxiliary(p,m):
    _,a,g=unpack(p,m)
    # Independently learned reference memories at three delays; nonlearning gain probes.
    return np.r_[a**2,a**5,g]

def noise(donor,n,rng,mult):
    pool=LIB[donor];idx=np.concatenate([(rng.integers(len(pool))+np.arange(5))%len(pool) for _ in range((n+4)//5)])[:n]
    return pool[idx]*mult

def design(name,reps,rng,test=False):
    if test:
        base=[[e1,e2,q,qr,lag] for e1,e2 in [(1,.35),(.45,-.8)] for q in [.25,.75] for qr in [0,1] for lag in [1,4]]
    else:
        es=[(1,1),(-1,-1)] if name=='coupled' else [(1,0),(-1,0),(0,1),(0,-1)]
        rs=[0,1] if name in ['crossed','calibrated'] else [0]
        ls=[0,3] if name in ['crossed','calibrated'] else [0]
        base=[[e1,e2,q,qr,lag] for e1,e2 in es for q in [0,1] for qr in rs for lag in ls]
    x=np.tile(base,(reps,1));return x[rng.permutation(len(x))]

def generating(truth,rng,near=False):
    # Deliberately equal average row strength; alternatives differ in transfer, not overall gain.
    b1,b2=rng.uniform(.65,1.15,2);k=rng.uniform(.7,1.2);s=rng.uniform(.55,.85)
    d=.15 if near else .65
    B0=np.array([[b1,b2],[k*b1,k*b2]])
    if truth=='scalar_rank1':p=[b1,b2,k,s]
    elif truth=='scalar_full':
        B0[1]*=[1+d,1-d];p=[*B0.ravel(),s]
    elif truth=='routed_rank1':p=[b1,b2,k,s*b1,s*b2,k*(1+d)]
    elif truth=='routed_full':
        B0[1]*=[1+d,1-d];B1=s*B0.copy();B1[1]=s*np.array([k*b1*(1-d),k*b2*(1+d)]);p=[*B0.ravel(),*B1.ravel()]
    else:
        B0[1]*=[1+d,1-d];p=[*B0.ravel(),s,s*(1+d),.7]
    a=rng.uniform(.8,.95,2);g=rng.uniform(.65,1.35,2)
    return np.r_[p,a,g]

def fit(m,x,y,scale,aux,auxsd,seed,starts=5,init=None):
    lo,hi=bounds(m);rng=np.random.default_rng(seed);best=None;history=[]
    def fun(p):
        v=((pred(p,m,x)-y)/scale).ravel()
        return np.r_[v,(auxiliary(p,m)-aux)/auxsd] if aux is not None else v
    for i in range(starts):
        p=np.clip(rng.uniform(lo*.1,hi*.5),lo+1e-5,hi-1e-5);p[-4:-2]=.88;p[-2:]=1
        if init is not None and i==0:p=init
        opt=least_squares(fun,p,bounds=(lo,hi),max_nfev=350,ftol=1e-9,xtol=1e-9,gtol=1e-8)
        loss=float(opt.fun@opt.fun);history.append(loss)
        if best is None or loss<best[0]:best=(loss,opt.x,opt.optimality,opt.nfev)
    return best,history

def run(name,n,reps,seed,near=False,miscal=0.,starts=5,legacy=False):
    rows=[];t=time.time()
    candidates=MODELS[:4] if legacy else MODELS
    for ti,truth in enumerate(candidates):
        for j in range(n):
            rng=np.random.default_rng(seed+ti*10000+j);p=generating(truth,rng,near);d=j%24
            x=design(name,reps,rng);xt=design(name,reps,rng,True)
            scale=np.maximum(LIB[d].std(0)*np.sqrt(2),[.03,.2])
            y=pred(p,truth,x)+noise(d,len(x),rng,np.sqrt(2));yt=pred(p,truth,xt)+noise(d,len(xt),rng,np.sqrt(2))
            auxsd=np.array([.035]*4+[.07]*2)
            aux=auxiliary(p,truth)+rng.normal(0,auxsd) if name=='calibrated' else None
            if aux is not None:aux[-2:]+=miscal*np.array([1,-1])
            fits=[]
            for mi,m in enumerate(candidates):
                best,h=fit(m,x,y,scale,aux,auxsd,seed+j+mi*19,starts)
                loss,pp,grad,neval=best
                fits.append(dict(model=m,params=pp.tolist(),objective=loss,start_losses=h,optimality=float(grad),nfev=int(neval),test_loss=float(np.mean(((pred(pp,m,xt)-yt)/scale)**2)),oracle_loss=float(np.mean(((pred(pp,m,xt)-pred(p,truth,xt))/scale)**2))))
            rows.append(dict(truth=truth,person=j,donor=d,parameters=p.tolist(),fits=fits,train_events=len(x),test_events=len(xt),auxiliary=None if aux is None else aux.tolist(),seed=seed+ti*10000+j))
        print(name,reps,near,miscal,truth,round(time.time()-t),flush=True)
    tag=f'{name}_r{reps}_near{int(near)}_bias{miscal:g}'
    (R/'results').mkdir(exist_ok=True);(R/'results'/f'{tag}.json').write_text(json.dumps(rows));print('DONE',tag,flush=True)

def audit():
    rng=np.random.default_rng(65712);worst=0.;rank=[]
    for _ in range(100):
        p=generating('scalar_rank1',rng);B,a,g=unpack(p,'scalar_rank1');x=design('calibrated',1,rng,True)
        # Actual duplicate-state recurrence: two stores receive identical driving updates;
        # output-specific independent reference kernels act only at readout.
        y=[]
        for e1,e2,q,qr,lag in x:
            drive=((1-q)*B[0,0]+q*B[1,0])@np.array([e1,e2]);s1=drive;s2=drive
            k=B[0,1,0]/B[0,0,0]
            y.append(np.array([s1,k*s2])*a**lag*(1+qr*(g-1))*UNITS)
        worst=max(worst,float(np.max(np.abs(np.array(y)-pred(p,'scalar_rank1',x)))))
    for name in ['coupled','orthogonal','crossed','calibrated']:
        p=generating('routed_full',rng);x=design(name,1,rng)
        def vec(p):return np.r_[pred(p,'routed_full',x).ravel(),auxiliary(p,'routed_full') if name=='calibrated' else []]
        J=np.column_stack([(vec(p+np.eye(len(p))[i]*1e-6)-vec(p-np.eye(len(p))[i]*1e-6))/2e-6 for i in range(len(p))]);sv=np.linalg.svd(J,compute_uv=False)
        rank.append(dict(design=name,rank=int(np.sum(sv>1e-7)),parameters=len(p),singular_values=sv.tolist()))
    out=dict(duplicate_state_max_discrepancy=worst,jacobian=rank)
    (R/'structural_audit.json').write_text(json.dumps(out,indent=2));print(out)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--design',default='calibrated');ap.add_argument('--people',type=int,default=48);ap.add_argument('--reps',type=int,default=4);ap.add_argument('--seed',type=int,default=9261117);ap.add_argument('--near',action='store_true');ap.add_argument('--miscal',type=float,default=0);ap.add_argument('--starts',type=int,default=5);ap.add_argument('--audit',action='store_true');ap.add_argument('--legacy-four',action='store_true');a=ap.parse_args()
    if a.audit:audit()
    else:run(a.design,a.people,a.reps,a.seed,a.near,a.miscal,a.starts,a.legacy_four)
