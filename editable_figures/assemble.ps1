param([string]$Folder=$PSScriptRoot)
$ErrorActionPreference='Stop'
$app=New-Object -ComObject PowerPoint.Application
$app.Visible=-1
$out=Join-Path $Folder 'concept_figures_bilingual.pptx'
for($i=1;$i -le $app.Presentations.Count;$i++) {if($app.Presentations.Item($i).FullName -eq $out){throw 'Combined output is open; save and close it before rebuilding.'}}
$deck=$app.Presentations.Add(-1)
$deck.PageSetup.SlideWidth=720
$deck.PageSetup.SlideHeight=468
foreach($name in @('figure1_en','figure2_en','figure1_zh','figure2_zh')) {
 $file=Join-Path $Folder ($name+'.pptx')
 $null=$deck.Slides.InsertFromFile($file,$deck.Slides.Count,1,1)
}
$deck.SaveAs($out,24)
$deck.SaveAs((Join-Path $Folder 'concept_figures_bilingual.pdf'),32)
$deck.Close()
Write-Output ('Saved four editable slides: '+$out)
