from validate import *
from scipy.signal import lfilter
rg=np.random.default_rng(100);field=rg.normal(size=80);errors=[]
for p in [np.array([.2,.8]),np.array([.7,.7002]),np.array([.7,.70001]),np.array([.7,.7])]:
 x=basis(p,field)
 if p[1]-p[0]>1e-4:
  z=np.array([lfilter([1-q],[1,-q],field) for q in p]).T;g=(z+np.vstack([np.zeros((1,2)),z[:-1]]))/2
  c=np.array([.4,-.2]);w=np.array([c.sum(),c[1]*(p[1]-p[0])]);errors.append(float(np.max(abs(x@w-g@c))))
 else:
  q=p.mean();ep=1e-6
  der=(basis(np.array([q+ep]),field)[:,0]-basis(np.array([q-ep]),field)[:,0])/(2*ep)
  errors.append(float(np.max(abs(x[:,1]-der))))
audit=json.loads((O/'optimization_audit.json').read_text());assert max(errors)<1e-7
assert max(x['improvement'] for x in audit)<1e-6
f=json.loads((O/'crossstudy_fits.json').read_text());assert len(f)==32
assert all(len(x['fit']['starts'])==64 for x in f)
meta=dict(basis_error_max=max(errors),source_optimization_max_improvement=max(x['improvement'] for x in audit),final_fits=32,all_final_starts_per_fit=64,heldout_model_labels=list(MODELS),note='Tests target numerical equivalence and source refit convergence; source-target separation is explicit in validate.py.')
(O/'numerical_checks.json').write_text(json.dumps(meta,indent=2));print(meta)
