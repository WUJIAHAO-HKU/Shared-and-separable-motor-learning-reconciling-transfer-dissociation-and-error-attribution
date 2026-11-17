from pathlib import Path
import numpy as np,pandas as pd,json
R=Path(__file__).resolve().parent.parent;D=R/'public_data/localization';rng=np.random.default_rng(771170)
rows=[];summary=[]
for group in ['30implicit','30explicit','cursorjump','handview']:
 d=pd.read_csv(D/(group+'_loc_p3_AOV.csv'));d=d.groupby(['participant','rotated_b','passive_b']).bias_deg.mean().unstack(['rotated_b','passive_b'])
 # Authors' circle-corrected, spatially interpolated participant estimates; average 3 directions.
 active=d[(1,0)]-d[(0,0)];passive=d[(1,1)]-d[(0,1)];diff=active-passive
 for sub in d.index:rows.append(dict(group=group,participant=sub,active=float(active[sub]),passive=float(passive[sub]),active_minus_passive=float(diff[sub])))
 vals=np.column_stack([active,passive,diff]);boot=vals[rng.integers(0,len(vals),(20000,len(vals)))].mean(1)
 summary.append(dict(group=group,n=len(vals),means=vals.mean(0).tolist(),ci95=np.quantile(boot,[.025,.975],axis=0).T.tolist()))
dd=pd.DataFrame(rows);a=dd[dd.group=='30implicit'].active_minus_passive.to_numpy();b=dd[dd.group=='handview'].active_minus_passive.to_numpy();boot=b[rng.integers(len(b),size=(20000,len(b)))].mean(1)-a[rng.integers(len(a),size=(20000,len(a)))].mean(1)
(R/'analysis/localization_summary.json').write_text(json.dumps(dict(summary=summary,contrast_handview_minus_control=dict(mean=float(b.mean()-a.mean()),ci95=np.quantile(boot,[.025,.975]).tolist()),estimator='participant mean across three author-interpolated directions; rotated minus aligned; percentile participant bootstrap; signs retained as deposited',inference='active/passive reports can differ; their difference is a report-level contrast, not an identified neural update or teaching error'),indent=2))
dd.to_csv(R/'analysis/localization_participants.csv',index=False);print(json.dumps(summary,indent=2));print('between',np.quantile(boot,[.025,.975]))
