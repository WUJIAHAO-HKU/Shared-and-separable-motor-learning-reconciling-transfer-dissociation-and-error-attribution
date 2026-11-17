[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)][string]$Layout,
    [Parameter(Mandatory=$true)][string]$OutputBase,
    [string]$Python = 'python',
    [switch]$ExportPdf,
    [switch]$Overwrite,
    [switch]$CloseWhenDone
)
$ErrorActionPreference = 'Stop'
$layoutPath = (Resolve-Path -LiteralPath $Layout).Path
& $Python (Join-Path $PSScriptRoot 'diagram_audit.py') validate $layoutPath
if ($LASTEXITCODE -ne 0) { throw 'Layout validation failed before opening PowerPoint.' }
$doc = Get-Content -LiteralPath $layoutPath -Raw -Encoding UTF8 | ConvertFrom-Json
$base = [IO.Path]::GetFullPath($OutputBase)
$suffixes = @('.pptx','.png','.com-audit.json')
if ($ExportPdf) { $suffixes += '.pdf' }
foreach ($ext in $suffixes) {
    if ((Test-Path -LiteralPath ($base+$ext)) -and !$Overwrite) {
        throw "Output exists: $base$ext. Use a new path or explicitly supply -Overwrite."
    }
}
[IO.Directory]::CreateDirectory([IO.Path]::GetDirectoryName($base)) | Out-Null
function Value($obj,[string]$key,$fallback) {
    if ($null -ne $obj.$key) { return $obj.$key }
    return $fallback
}
function RGB([string]$hex) {
    $hex=$hex.TrimStart('#')
    return [Convert]::ToInt32($hex.Substring(0,2),16)+256*[Convert]::ToInt32($hex.Substring(2,2),16)+65536*[Convert]::ToInt32($hex.Substring(4,2),16)
}
$scale=[double](Value $doc 'scale' .6)
function Paint($shape,$item) {
    if ($item.fill) {
        $shape.Fill.Visible=-1; $shape.Fill.Solid(); $shape.Fill.ForeColor.RGB=RGB $item.fill; $shape.Fill.Transparency=0
    } else { $shape.Fill.Visible=0 }
    if ($item.line) {
        $shape.Line.Visible=-1; $shape.Line.ForeColor.RGB=RGB $item.line
        $shape.Line.Weight=[single]((Value $item 'lineWidth' 1)*$scale)
    } else { $shape.Line.Visible=0 }
}
$audit=[Collections.Generic.List[object]]::new()
$warnings=[Collections.Generic.List[string]]::new()
function Record($shape,[string]$sourceName) {
    $shape.AlternativeText=$sourceName
    $audit.Add([pscustomobject]@{source=$sourceName; name=$shape.Name; type=[int]$shape.Type;
        x_pt=[double]$shape.Left; y_pt=[double]$shape.Top; w_pt=[double]$shape.Width; h_pt=[double]$shape.Height})
}
$app=New-Object -ComObject PowerPoint.Application
$app.Visible=-1
for ($i=1;$i -le $app.Presentations.Count;$i++) {
    if ($app.Presentations.Item($i).FullName -eq ($base+'.pptx')) {
        throw 'Output deck is already open. Choose a new output path; the open deck was not changed.'
    }
}
$deck=$app.Presentations.Add(-1)
try {
    $deck.PageSetup.SlideWidth=[single]($doc.width*$scale)
    $deck.PageSetup.SlideHeight=[single]($doc.height*$scale)
    $slide=$deck.Slides.Add(1,12)
    $slide.FollowMasterBackground=0
    $slide.Background.Fill.Solid()
    $slide.Background.Fill.ForeColor.RGB=RGB (Value $doc 'background' '#FFFFFF')
    foreach ($item in $doc.items) {
        $shape=$null
        if ($item.kind -in @('box','ellipse','text','picture')) {
            $x=[single]($item.x*$scale); $y=[single]($item.y*$scale)
            $w=[single]($item.w*$scale); $h=[single]($item.h*$scale)
        }
        switch ($item.kind) {
            'box' {
                $type=1; if ($item.rounded) { $type=5 }
                $shape=$slide.Shapes.AddShape($type,$x,$y,$w,$h)
                Paint $shape $item
                if ($item.rounded) { $shape.Adjustments.Item(1)=.12 }
            }
            'ellipse' { $shape=$slide.Shapes.AddShape(9,$x,$y,$w,$h); Paint $shape $item }
            'polygon' {
                $pts=$item.points
                $builder=$slide.Shapes.BuildFreeform(1,[single]($pts[0][0]*$scale),[single]($pts[0][1]*$scale))
                for ($j=1;$j -lt $pts.Count;$j++) { $builder.AddNodes(0,1,[single]($pts[$j][0]*$scale),[single]($pts[$j][1]*$scale)) }
                $builder.AddNodes(0,1,[single]($pts[0][0]*$scale),[single]($pts[0][1]*$scale))
                $shape=$builder.ConvertToShape(); Paint $shape $item
            }
            'wire' {
                $pts=$item.points
                for ($j=1;$j -lt $pts.Count;$j++) {
                    $segment=$slide.Shapes.AddLine([single]($pts[$j-1][0]*$scale),[single]($pts[$j-1][1]*$scale),[single]($pts[$j][0]*$scale),[single]($pts[$j][1]*$scale))
                    $segment.Name=$item.name+' / segment '+$j
                    $segment.Line.ForeColor.RGB=RGB (Value $item 'color' '#353458')
                    $segment.Line.Weight=[single]((Value $item 'lineWidth' 1.5)*$scale)
                    if ($item.dash) { $segment.Line.DashStyle=4 }
                    if ($item.arrow -and $j -eq ($pts.Count-1)) {
                        $segment.Line.EndArrowheadStyle=2
                        $segment.Line.EndArrowheadLength=2; $segment.Line.EndArrowheadWidth=2
                    }
                    Record $segment $item.name
                }
            }
            'text' {
                $shape=$slide.Shapes.AddTextbox(1,$x,$y,$w,$h)
                $shape.Fill.Visible=0; $shape.Line.Visible=0
                $tf=$shape.TextFrame2
                $tf.MarginLeft=0; $tf.MarginRight=0; $tf.MarginTop=0; $tf.MarginBottom=0
                $tf.AutoSize=0
                $tf.WordWrap=0; if ($item.wrap) { $tf.WordWrap=-1 }
                $tf.VerticalAnchor=@{top=1;middle=3;bottom=4}[(Value $item 'valign' 'top')]
                $tr=$tf.TextRange
                $tr.Text=$item.text.Replace("`r`n","`n").Replace("`n","`r")
                $tr.Font.Name=Value $item 'font' (Value $doc 'font' 'Arial')
                $tr.Font.Size=[single]((Value $item 'size' 18)*$scale)
                $tr.Font.Bold=0; if ($item.bold) { $tr.Font.Bold=-1 }
                $tr.Font.Italic=0; if ($item.italic) { $tr.Font.Italic=-1 }
                $tr.Font.Fill.Solid(); $tr.Font.Fill.ForeColor.RGB=RGB (Value $item 'color' '#353458')
                $tr.ParagraphFormat.Alignment=@{left=1;center=2;right=3}[(Value $item 'align' 'left')]
                $tr.ParagraphFormat.SpaceBefore=0; $tr.ParagraphFormat.SpaceAfter=0
                # PowerPoint can apply a legacy textbox autofit when text is assigned.
                # Disable both interfaces after formatting, then restore measured bounds.
                $shape.TextFrame.AutoSize=0; $tf.AutoSize=0
                $shape.Left=$x; $shape.Top=$y; $shape.Width=$w; $shape.Height=$h
                if ($tr.BoundWidth -gt ($w+1) -or $tr.BoundHeight -gt ($h+1)) {
                    $warnings.Add(('Text bounds exceed box: {0} ({1:N2}x{2:N2} vs {3:N2}x{4:N2} pt)' -f $item.name,$tr.BoundWidth,$tr.BoundHeight,$w,$h))
                }
            }
            'picture' {
                $src=$item.source
                if (![IO.Path]::IsPathRooted($src)) { $src=Join-Path (Split-Path $layoutPath -Parent) $src }
                $src=(Resolve-Path -LiteralPath $src).Path
                Add-Type -AssemblyName System.Drawing
                $img=[Drawing.Image]::FromFile($src)
                try { $iw=[double]$img.Width; $ih=[double]$img.Height } finally { $img.Dispose() }
                $fit=Value $item 'fit' 'contain'
                $ratio=[Math]::Min($w/$iw,$h/$ih)
                if ($fit -eq 'cover') { $ratio=[Math]::Max($w/$iw,$h/$ih) }
                $pw=[single]($iw*$ratio); $ph=[single]($ih*$ratio)
                $shape=$slide.Shapes.AddPicture($src,0,-1,[single]($x+($w-$pw)/2),[single]($y+($h-$ph)/2),$pw,$ph)
                if ($fit -eq 'cover') {
                    $shape.LockAspectRatio=0
                    $crop=$shape.PictureFormat.Crop
                    $crop.ShapeWidth=$w; $crop.ShapeHeight=$h
                    $crop.PictureWidth=$pw; $crop.PictureHeight=$ph
                    $crop.ShapeLeft=$x; $crop.ShapeTop=$y
                    $crop.PictureOffsetX=0; $crop.PictureOffsetY=0
                }
                $shape.Line.Visible=0
            }
        }
        if ($null -ne $shape) { $shape.Name=$item.name; Record $shape $item.name }
    }
    $deck.SaveAs(($base+'.pptx'),24)
    $exportW=[int](Value $doc 'exportWidth' ([Math]::Round($doc.width)))
    $exportH=[int][Math]::Round($exportW*$doc.height/$doc.width)
    $slide.Export(($base+'.png'),'PNG',$exportW,$exportH)
    if ($ExportPdf) { $deck.SaveAs(($base+'.pdf'),32) }
    [pscustomobject]@{scale=$scale; shapes=$audit.ToArray(); warnings=$warnings.ToArray()} |
        ConvertTo-Json -Depth 8 | Set-Content -LiteralPath ($base+'.com-audit.json') -Encoding UTF8
    foreach ($warning in $warnings) { Write-Warning $warning }
    Write-Output ('Created: '+$base+'.pptx')
    Write-Output ('Native shapes: '+$slide.Shapes.Count+'; text warnings: '+$warnings.Count)
    if ($CloseWhenDone) { $deck.Close() }
} catch {
    Write-Warning 'Build/export failed. The new deck remains open for inspection; unrelated presentations were not closed.'
    throw
}
