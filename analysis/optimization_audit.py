from validate import *
arrays,fields=load();fits=json.loads((O/'crossstudy_fits.json').read_text());out=[]
for x in fits:
 if x['variant']!='source_cv_ridge':continue
 y,_=arrays[x['source'],x['window']];f=x['fit'];new=fit(np.nanmean(y,0),fields,np.array(x['scale']),f['model'],f['lambda_'],starts=64,seed=222919)
 pp=pred(f,fields);pn=pred(new,fields)
 out.append(dict(source=x['source'],window=x['window'],model=f['model'],original_loss=f['loss'],audit_loss=new['loss'],improvement=f['loss']-new['loss'],prediction_max_difference=float(np.max(abs(pp-pn))),all_64_success=sum(z['success'] for z in new['starts']),max_coefficient=float(np.max(abs(np.array(new['coef']))))))
 print(x['source'],x['window'],f['model'],f['loss']-new['loss'],flush=True)
(O/'optimization_audit.json').write_text(json.dumps(out,indent=2))
