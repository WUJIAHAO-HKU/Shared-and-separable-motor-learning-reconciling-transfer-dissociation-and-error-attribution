"""Retrieve only the four source CSVs needed by localization.py; verify frozen digests."""
from pathlib import Path
import urllib.request,json,hashlib,os
R=Path(__file__).resolve().parent/'localization';R.mkdir(exist_ok=True)
manifest=json.loads((R/'download_manifest.json').read_text(encoding='utf8'))
needed={g+'_loc_p3_AOV.csv' for g in ['30implicit','30explicit','cursorjump','handview']}
entries=[x for x in manifest if x['file'] in needed]
assert {x['file'] for x in entries}==needed
for x in entries:
 p=R/x['file']
 if p.exists() and hashlib.sha256(p.read_bytes()).hexdigest()==x['sha256']:
  print('Verified cached',p.name);continue
 req=urllib.request.Request(x['url'],headers={'User-Agent':'SharedLearning-Reproducibility/1.0'})
 with urllib.request.urlopen(req,timeout=90) as response:payload=response.read()
 assert hashlib.sha256(payload).hexdigest()==x['sha256'], 'Source content changed: '+p.name
 tmp=p.with_suffix('.csv.tmp');tmp.write_bytes(payload);os.replace(tmp,p)
 print('Downloaded and verified',p.name)
