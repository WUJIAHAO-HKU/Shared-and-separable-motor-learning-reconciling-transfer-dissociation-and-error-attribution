"""Validate a native diagram layout or inventory PPTX objects; standard library only."""
import argparse
import json
import math
import re
import sys
import zipfile
from collections import Counter
from pathlib import Path
import xml.etree.ElementTree as ET

NS = {'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
      'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}


def validate(path):
    doc = json.loads(path.read_text(encoding='utf-8-sig'))
    def number(v, label, positive=False):
        if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v):
            raise ValueError(f'{label}: expected finite number')
        if positive and v <= 0:
            raise ValueError(f'{label}: must be positive')
        return v
    w = number(doc.get('width'), 'width', True)
    h = number(doc.get('height'), 'height', True)
    scale = number(doc.get('scale', .6), 'scale', True)
    if not (72 <= w * scale <= 4032 and 72 <= h * scale <= 4032):
        raise ValueError('Slide dimensions must each be 72..4032 points')
    ew = number(doc.get('exportWidth', round(w)), 'exportWidth', True)
    if int(ew) != ew or ew > 16000:
        raise ValueError('exportWidth must be an integer <= 16000')
    def color(v, label):
        if v is not None and not re.fullmatch(r'#[0-9a-fA-F]{6}', str(v)):
            raise ValueError(f'{label}: expected #RRGGBB')
    color(doc.get('background'), 'background')
    items = doc.get('items')
    if not isinstance(items, list) or not items:
        raise ValueError('items must be a nonempty list')
    names = set()
    actual_names = set()
    for item in items:
        name = item.get('name')
        if not isinstance(name, str) or not name.strip() or name in names:
            raise ValueError(f'Invalid or duplicate name: {name!r}')
        names.add(name)
        k = item.get('kind')
        if k not in ('box', 'ellipse', 'polygon', 'wire', 'text', 'picture'):
            raise ValueError(f'{name}: unsupported kind {k!r}')
        if 'gradient' in item:
            raise ValueError(f'{name}: gradients are not supported')
        for key in ('fill', 'line', 'color'):
            color(item.get(key), f'{name}.{key}')
        if 'lineWidth' in item:
            number(item['lineWidth'], name + '.lineWidth', True)
        for key in ('rounded', 'dash', 'arrow', 'bold', 'italic', 'wrap'):
            if key in item and not isinstance(item[key], bool):
                raise ValueError(f'{name}.{key}: expected boolean')
        if k in ('wire', 'polygon'):
            points = item.get('points')
            if not isinstance(points, list) or len(points) < (2 if k == 'wire' else 3):
                raise ValueError(f'{name}: insufficient points')
            for pt in points:
                if not isinstance(pt, list) or len(pt) != 2:
                    raise ValueError(f'{name}: expected [x,y]')
                x, y = number(pt[0], name), number(pt[1], name)
                if not (0 <= x <= w and 0 <= y <= h):
                    raise ValueError(f'{name}: point outside canvas')
            if any(a == b for a, b in zip(points, points[1:])):
                raise ValueError(f'{name}: consecutive identical points')
            generated = [f'{name} / segment {i}' for i in range(1, len(points))] if k == 'wire' else [name]
        else:
            x, y = number(item.get('x'), name+'.x'), number(item.get('y'), name+'.y')
            iw, ih = number(item.get('w'), name+'.w', True), number(item.get('h'), name+'.h', True)
            if x < 0 or y < 0 or x+iw > w+.00001 or y+ih > h+.00001:
                raise ValueError(f'{name}: bounds outside canvas')
            generated = [name]
        for native_name in generated:
            if native_name in actual_names:
                raise ValueError(f'Generated name collision: {native_name}')
            actual_names.add(native_name)
        if k == 'text':
            if not isinstance(item.get('text'), str):
                raise ValueError(f'{name}: text must be a string')
            number(item.get('size', 18), name+'.size', True)
            if item.get('align', 'left') not in ('left', 'center', 'right') or item.get('valign', 'top') not in ('top', 'middle', 'bottom'):
                raise ValueError(f'{name}: invalid text alignment')
        if k == 'picture':
            if not isinstance(item.get('source'), str) or not item['source']:
                raise ValueError(f'{name}: picture source required')
            src = Path(item['source'])
            if not src.is_absolute():
                src = path.parent / src
            if not src.is_file():
                raise ValueError(f'{name}: picture does not exist: {src}')
            if item.get('fit', 'contain') not in ('contain', 'cover'):
                raise ValueError(f'{name}: fit must be contain or cover')
    return {'valid': True, 'items': len(items), 'expected_native_objects': len(actual_names),
            'slide_points': [w*scale, h*scale]}


def audit(path):
    with zipfile.ZipFile(path) as z:
        pres = ET.fromstring(z.read('ppt/presentation.xml'))
        size = pres.find('p:sldSz', NS)
        sw, sh = int(size.get('cx')), int(size.get('cy'))
        reports = []
        files = sorted((n for n in z.namelist() if re.fullmatch(r'ppt/slides/slide\d+\.xml', n)),
                       key=lambda n: int(re.search(r'(\d+)\.xml', n).group(1)))
        for filename in files:
            root = ET.fromstring(z.read(filename))
            tree = root.find('p:cSld/p:spTree', NS)
            objects = []
            warnings = []
            def visit(parent, depth=0):
                for node in parent:
                    kind = node.tag.split('}')[-1]
                    if kind not in ('sp', 'cxnSp', 'pic', 'grpSp', 'graphicFrame'):
                        continue
                    c = node.find('.//p:cNvPr', NS)
                    name = c.get('name', '') if c is not None else ''
                    tx = node.findall('p:txBody/a:p', NS)
                    text = '\n'.join(''.join(p.itertext()) for p in tx)
                    xfrm = node.find('p:spPr/a:xfrm', NS)
                    if xfrm is None:
                        xfrm = node.find('p:grpSpPr/a:xfrm', NS)
                    rect = None
                    if xfrm is not None:
                        off, ext = xfrm.find('a:off', NS), xfrm.find('a:ext', NS)
                        if off is not None and ext is not None:
                            vals = [int(off.get('x')), int(off.get('y')), int(ext.get('cx')), int(ext.get('cy'))]
                            rect = [round(v/12700, 4) for v in vals]
                            x,y,w,h = vals
                            if depth == 0 and (x < -12700 or y < -12700 or x+w > sw+12700 or y+h > sh+12700):
                                warnings.append(f'Top-level bounds outside slide: {name}')
                    objects.append({'name': name, 'kind': kind, 'depth': depth, 'text': text, 'bounds_pt': rect})
                    if kind == 'grpSp':
                        visit(node, depth+1)
            visit(tree)
            counts = dict(Counter(o['kind'] for o in objects))
            gradients = len(root.findall('.//a:gradFill', NS))
            duplicates = [n for n,c in Counter(o['name'] for o in objects).items() if c>1]
            if duplicates:
                warnings.append('Duplicate native names: ' + ', '.join(duplicates))
            if not any(o['text'] for o in objects):
                warnings.append('No native text found; verify editability')
            reports.append({'slide_xml': filename, 'counts': counts, 'direct_gradient_fills': gradients,
                            'warnings': warnings, 'objects': objects})
        return {'file': str(path.resolve()), 'slide_size_pt': [sw/12700, sh/12700],
                'note': 'Inventory, not visual verification. Group-child bounds use local coordinates; theme-inherited fills are not resolved.',
                'slides': reports}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['validate', 'audit'])
    parser.add_argument('path', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    try:
        result = validate(args.path.resolve()) if args.mode == 'validate' else audit(args.path)
        output = json.dumps(result, ensure_ascii=False, indent=2)
        if args.output:
            args.output.write_text(output, encoding='utf-8')
            print('Report written: ' + str(args.output))
        else:
            print(output)
    except (ValueError, KeyError, OSError, zipfile.BadZipFile, ET.ParseError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
