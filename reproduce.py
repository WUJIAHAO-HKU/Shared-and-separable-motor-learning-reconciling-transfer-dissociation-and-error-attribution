"""Portable entry points for the deposited manuscript and analysis release."""
from pathlib import Path
import argparse,subprocess,sys,json,hashlib,zipfile
import numpy as np
import pandas as pd
R=Path(__file__).resolve().parent
def run(script):subprocess.run([sys.executable,str(R/script)],cwd=R,check=True)
def verify():
 sys.path.insert(0,str(R/'analysis'))
 from validate import load,pred
 arrays,fields=load();fits=json.loads((R/'analysis/crossstudy_fits.json').read_text());scores=pd.read_csv(R/'analysis/crossstudy_scores.csv')
 assert len(fits)==32
 max_prediction_error=0.;max_score_error=0.
 with np.load(R/'analysis/crossstudy_predictions.npz') as saved:
  for record in fits:
   source,target,w=record['source'],record['target'],record['window'];fit=record['fit'];pr=pred(fit,fields)
   key=f"{source}_{w}_{fit['model']}_{record['variant']}"
   max_prediction_error=max(max_prediction_error,float(np.max(abs(pr-saved[key]))))
   yy,base=arrays[target,w];_,sourcebase=arrays[source,w];scale=np.array(record['scale'])
   mse=np.nanmean((pr[None,:,10:]-yy[:,:,10:])**2,axis=(1,2))
   strict=pr[None]+sourcebase.mean(axis=0)[None,:,None]-base[:,:,None]
   smse=np.nanmean((strict[:,:,10:]-yy[:,:,10:])**2,axis=(1,2))
   sub=scores[(scores.source==source)&(scores.window==w)&(scores.model==fit['model'])&(scores.variant==record['variant'])].sort_values('participant')
   actual=np.column_stack([mse[:,0],mse[:,1],np.mean(mse/scale**2,axis=1),np.mean(smse/scale**2,axis=1)])
   recorded=sub[['compensation_mse','feedback_mse','joint_standardized_mse','strict_joint_standardized_mse']].to_numpy()
   np.testing.assert_allclose(actual,recorded,rtol=1e-10,atol=1e-10)
   max_score_error=max(max_score_error,float(np.max(abs(actual-recorded))))
 assert max_prediction_error<1e-10
 recovery=json.loads((R/'analysis/recovery.json').read_text());models=recovery['models']
 confusion=[[sum(x['truth']==a and x['winner']==b for x in recovery['records']) for b in models] for a in models]
 assert confusion==recovery['confusion'] and len(recovery['records'])==80
 c=json.loads((R/'analysis/counterexamples.json').read_text());H,U,poles=map(np.array,[c['H'],c['U'],c['poles']])
 B=np.array([H@np.diag(poles**k)@U for k in c['delay']]);np.testing.assert_allclose(B,c['B'],rtol=1e-12,atol=1e-12)
 with zipfile.ZipFile(R/'editable_figures/concept_figures_bilingual.pptx') as z:
  slides=[n for n in z.namelist() if n.startswith('ppt/slides/slide') and n.endswith('.xml')]
  assert len(slides)==4
  assert not any(n.startswith('ppt/media/') for n in z.namelist()),'Raster or other embedded media in concept deck'
  assert all(b'<p:pic>' not in z.read(n) for n in slides)
 expected=json.loads((R/'analysis/provenance.json').read_text())['data_sha256']
 assert hashlib.sha256((R/'public_data/block_observations.csv').read_bytes()).hexdigest()==expected
 manifest=R/'release_manifest.json';hashes_checked=0
 if manifest.exists():
  for name,digest in json.loads(manifest.read_text()).items():
   assert hashlib.sha256((R/name).read_bytes()).hexdigest()==digest,'Changed release file: '+name
   hashes_checked+=1
 run('analysis/check_numerics.py')
 report=dict(fitted_models_checked=len(fits),heldout_prediction_max_error=max_prediction_error,participant_score_max_error=max_score_error,recovery_instances=len(recovery['records']),recovery_confusion_verified=True,concept_slides=4,concept_embedded_media=0,data_sha256=expected,release_hashes_checked=hashes_checked)
 print(json.dumps(report,indent=2));return report
def figures():
 run('public_data/fetch_localization.py')
 sys.path.insert(0,str(R/'analysis'))
 from validate import counterexamples
 counterexamples();run('analysis/calibration_stress.py');run('analysis/localization.py');run('analysis/plots.py')
def manuscripts():run('build.py');run('compile.py')
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--mode',choices=['verify','figures','manuscripts','full'],default='verify');args=parser.parse_args()
 if args.mode=='verify':verify()
 elif args.mode=='figures':figures()
 elif args.mode=='manuscripts':manuscripts()
 else:
  for script in ['analysis/validate.py','analysis/recovery.py','analysis/optimization_audit.py','analysis/check_numerics.py']:run(script)
  figures();manuscripts()
