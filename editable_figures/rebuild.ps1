$ErrorActionPreference='Stop'
$folder=$PSScriptRoot
python (Join-Path $folder 'make_layouts.py')
if($LASTEXITCODE -ne 0){throw 'Layout creation failed'}
foreach($name in @('figure1_en','figure2_en','figure1_zh','figure2_zh')) {
 & (Join-Path $folder 'tools/build_diagram.ps1') -Layout (Join-Path $folder ($name+'.json')) -OutputBase (Join-Path $folder $name) -ExportPdf -Overwrite -CloseWhenDone
 if($LASTEXITCODE -ne 0){throw ('Figure build failed: '+$name)}
 Copy-Item -LiteralPath (Join-Path $folder ($name+'.pdf')) -Destination (Join-Path (Split-Path $folder -Parent) ('figures/'+$name+'.pdf')) -Force
}
& (Join-Path $folder 'assemble.ps1') -Folder $folder
python (Join-Path $folder 'tools/diagram_audit.py') audit (Join-Path $folder 'concept_figures_bilingual.pptx') --output (Join-Path $folder 'native_audit.json')
