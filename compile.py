from pathlib import Path
import subprocess,concurrent.futures,json,shutil,os,sys
R=Path(__file__).parent
B=Path(os.environ.get('LOCALAPPDATA',''))/'Programs/MiKTeX/miktex/bin/x64'
def executable(name):
 found=shutil.which(name)
 if found:return found
 candidate=B/(name+'.exe')
 if candidate.exists():return str(candidate)
 raise FileNotFoundError('Install XeLaTeX/BibTeX and add them to PATH: '+name)
def run(name):
 for exe,args in [('xelatex',['-interaction=nonstopmode','-halt-on-error',name+'.tex']),('bibtex',[name]),('xelatex',['-interaction=nonstopmode','-halt-on-error',name+'.tex']),('xelatex',['-interaction=nonstopmode','-halt-on-error',name+'.tex'])]:
  p=subprocess.run([executable(exe)]+args,cwd=R,capture_output=True)
  if p.returncode:return {'file':name,'error':p.stdout.decode('utf8',errors='replace')[-4000:]}
 return {'file':name,'bytes':(R/(name+'.pdf')).stat().st_size}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 results=list(pool.map(run,['perspective_en','perspective_zh','evidence_atlas_en','evidence_atlas_zh']))
print(json.dumps(results,ensure_ascii=False,indent=2))
if any('error' in x for x in results):sys.exit(1)
