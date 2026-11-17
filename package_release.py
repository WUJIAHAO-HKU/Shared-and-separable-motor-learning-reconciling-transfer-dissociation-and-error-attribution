"""Package the current curated tree and record content hashes (no recursive ZIPs)."""
from pathlib import Path
import hashlib,json,zipfile
R=Path(__file__).resolve().parent
def included(p):
 rel=p.relative_to(R)
 return p.is_file() and not any(x in ['.git','__pycache__','.venv','dist'] for x in rel.parts) and p.suffix not in ['.pyc','.log','.aux','.out','.bbl','.blg','.tmp'] and rel.as_posix()!='release_manifest.json' and not rel.as_posix().startswith(('public_data/raw/','qa/perspective_','qa/evidence_atlas_')) and not (rel.as_posix().startswith('public_data/localization/') and p.suffix=='.csv')
files=sorted([p for p in R.rglob('*') if included(p)])
manifest={p.relative_to(R).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
(R/'release_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
dist=R/'dist';dist.mkdir(exist_ok=True)
with zipfile.ZipFile(dist/'reproducibility_package.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in files+[R/'release_manifest.json']:z.write(p,p.relative_to(R))
with zipfile.ZipFile(dist/'reproducibility_package.zip') as z:assert z.testzip() is None
print(json.dumps(dict(files=len(files),archive_bytes=(dist/'reproducibility_package.zip').stat().st_size),indent=2))
