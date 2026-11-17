from pathlib import Path
import argparse
import numpy as np,pandas as pd,json,hashlib
from scipy.io import loadmat
R=Path(__file__).resolve().parent.parent
parser=argparse.ArgumentParser(description='Re-extract processed block observations from the authors MATLAB archives.')
parser.add_argument('--raw-dir',type=Path,default=R/'public_data/raw',help='Contains visual_errors/*.mat and visual_clamp/*.mat; see public_data/README.md')
SRC=parser.parse_args().raw_dir.resolve()
rows=[];manifest=[]
for cohort,path,vpat,cpat in [('visual_errors',SRC/'visual_errors','visRJ_{}_2018.mat','RJforcecomp_{}_2018.mat'),('visual_clamp',SRC/'visual_clamp' if (SRC/'visual_clamp').exists() else SRC,'visRJ2_{}.mat','RJ2forcecomp_{}.mat')]:
 for day,code in enumerate(['A','B']):
  vp=path/vpat.format(code);cp=path/cpat.format(day+1)
  F=loadmat(vp,squeeze_me=True,struct_as_record=False)['F'];C=loadmat(cp,squeeze_me=True)['ForcePredValues']
  for sub in range(12):
   participant=sub if day==0 else (sub+6)%12
   for phase,n in [(1,10),(2,30),(3,20),(4,10)]:
    a,b=F[sub,phase].prt[1:3]
    for block in range(n):
     if a.T[block]!=1 or b.T[block]!=1:continue
     wave=b.FX[block]-a.FX[block]
     for lo,hi in [(180,230),(230,300)]:rows.append(dict(cohort=cohort,participant=participant,schedule=day,phase=phase,block=block,window=f'{lo}_{hi}',force_comp=float(C[phase,sub,block]),feedback=float(np.mean(wave[lo+49:hi+50]))))
  for p in [vp,cp]:manifest.append(dict(file=p.relative_to(SRC).as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size))
  print(cohort,code,flush=True)
a=pd.DataFrame(rows);b=pd.read_csv(R/'public_data/block_observations.csv');pd.testing.assert_frame_equal(a,b)
(R/'analysis/extraction_check.json').write_text(json.dumps(dict(rows=len(a),equal=True,raw_files=manifest,provenance='Author-processed MATLAB waveforms; perturbation indexes 1/2; waveform sample indexing follows archived authors analysis; day-B participant rotation +6 per protocol'),indent=2))
print('verified',len(a))
