# -*- coding: utf-8 -*-
"""Generischer Replay der evm-Seiten: Vektoren, Bilder und Text 1:1 als PPTX-Formen."""
import json, os
from deck import (Pt, rgb, rect, hline, vline, picture, line_text, FONTMAP,
                  BLACK, WHITE, DARK, GREY, MSO_SHAPE, PP_ALIGN, Run, textbox, ASSETS, QA)


def fix_glyphs(text, fontname):
    """Wingdings-Bullets auf das Zeichen der Metzler-Vorlage abbilden."""
    if fontname.startswith('Wingdings'):
        if QA:
            return text.replace('\u25fc', '\u25a0').replace('\u25a0', '\u25a0')
        return text.replace('\u25fc', 'n').replace('\u25a0', 'n')
    return text

BASE = os.path.dirname(os.path.abspath(__file__))
LAYOUT = json.load(open(os.path.join(BASE, 'evm_layout.json')))


_PAGEPIX = {}


def _page_pix(pageno, dpi=150):
    if pageno not in _PAGEPIX:
        import pymupdf
        from PIL import Image
        d = pymupdf.open(os.path.join(BASE, '..', '20260813_Metzler_evm AG_vF.pdf'))
        px = d[pageno - 1].get_pixmap(dpi=dpi)
        _PAGEPIX[pageno] = (Image.frombytes('RGB', (px.width, px.height), px.samples),
                            px.width / 842.04)
    return _PAGEPIX[pageno]


def sampled_fill(pageno, r, fallback):
    """Tatsaechlich gerenderte Flaechenfarbe abgreifen – die Vorlage arbeitet
    mit teiltransparenten Fuellungen, die im PDF-Objekt nicht sichtbar sind."""
    try:
        im, sc = _page_pix(pageno)
        pts = [(r[0] + 3, r[1] + 3), (r[2] - 3, r[1] + 3),
               (r[0] + 3, r[3] - 3), (r[2] - 3, r[3] - 3),
               (r[0] + 3, (r[1] + r[3]) / 2.0)]
        vals = []
        for x, y in pts:
            px = int(x * sc), int(y * sc)
            if 0 <= px[0] < im.width and 0 <= px[1] < im.height:
                vals.append(im.getpixel(px))
        if not vals:
            return fallback
        best = max(set(vals), key=vals.count)
        return rgb((best[0] << 16) | (best[1] << 8) | best[2])
    except Exception:
        return fallback


def col(t):
    if t is None:
        return None
    return rgb((int(round(t[0] * 255)) << 16) | (int(round(t[1] * 255)) << 8) | int(round(t[2] * 255)))


def draw_vectors(slide, page, skip=(), only_rects=False):
    for i, g in enumerate(page['drawings']):
        if i in skip:
            continue
        r = g['rect']
        w, h = r[2] - r[0], r[3] - r[1]
        fill = col(g.get('fill'))
        stroke = col(g.get('color'))
        lw = g.get('width') or 0.75
        # ganzseitiger weißer Hintergrund wird nicht repliziert
        if fill == WHITE and w > 800 and h > 550:
            continue
        if g['type'] in ('f', 'fs') and w > 0.6 and h > 0.6:
            if fill is not None and w > 20 and h > 12:
                fill = sampled_fill(page['page'], r, fill)
            rect(slide, r[0], r[1], w, h, fill=fill,
                 linecolor=stroke if g['type'] == 'fs' else None, linew=lw)
            continue
        for it in g['items']:
            if it[0] == 'l':
                (x0, y0), (x1, y1) = it[1], it[2]
                if abs(y1 - y0) < 0.4:
                    hline(slide, x0, x1, (y0 + y1) / 2.0, stroke or BLACK, max(lw, 0.5))
                elif abs(x1 - x0) < 0.4:
                    vline(slide, (x0 + x1) / 2.0, y0, y1, stroke or BLACK, max(lw, 0.5))
                else:
                    c = slide.shapes.add_connector(1, Pt(x0), Pt(y0), Pt(x1), Pt(y1))
                    c.line.color.rgb = stroke or BLACK
                    c.line.width = Pt(max(lw, 0.5))
            elif it[0] == 're':
                x0, y0, x1, y1 = it[1]
                if fill is not None and (x1 - x0) > 0.6 and (y1 - y0) > 0.6:
                    rect(slide, x0, y0, x1 - x0, y1 - y0, fill=fill)


def _flat_asset(pageno, im):
    """Bilder mit Transparenz werden aus der Quellseite flach gerastert –
    so bleibt die Komposition mit dem Untergrund erhalten."""
    import os
    from PIL import Image
    src = os.path.join(ASSETS, im['file'])
    try:
        if Image.open(src).mode not in ('RGBA', 'LA', 'P'):
            return im['file']
    except Exception:
        return im['file']
    b = im['bbox']
    fn = 'flat_p%02d_%d.png' % (pageno, im['xref'])
    path = os.path.join(ASSETS, fn)
    if not os.path.exists(path):
        import pymupdf
        d = pymupdf.open(os.path.join(BASE, '..', '20260813_Metzler_evm AG_vF.pdf'))
        d[pageno - 1].get_pixmap(clip=pymupdf.Rect(*b), dpi=300).save(path)
    return fn


def draw_images(slide, page, skip_files=(), only_files=None):
    for im in page['images']:
        fn = im['file']
        if not fn or fn in skip_files:
            continue
        if only_files is not None and fn not in only_files:
            continue
        b = im['bbox']
        picture(slide, _flat_asset(page['page'], im), b[0], b[1],
                b[2] - b[0], b[3] - b[1])


def draw_text(slide, page, subs=None, skip_text=(), width_pad=40):
    """Jede Zeile des Originals wird als exakt platzierte Textzeile gesetzt."""
    subs = subs or {}
    for b in page['blocks']:
        if b['kind'] != 'text':
            continue
        for l in b['lines']:
            spans = l['spans']
            txts = ''.join(s['text'] for s in spans)
            if not txts.strip():
                continue
            if txts.strip() in skip_text:
                continue
            if txts in subs:
                txts_new = subs[txts]
                if txts_new is None:
                    continue
            else:
                txts_new = None
            s0 = spans[0]
            fam, bold, ital = FONTMAP.get(s0['font'], ('Arial', False, False))
            y0, y1 = l['bbox'][1], l['bbox'][3]
            if len(spans) == 1 or txts_new is not None:
                line_text(slide, l['bbox'][0], y0, y1,
                          fix_glyphs(txts_new if txts_new is not None else txts, fam),
                          fam, s0['size'], rgb(s0['color']), bold, ital,
                          w=(l['bbox'][2] - l['bbox'][0]) + width_pad)
            else:
                runs = []
                for s in spans:
                    f, bo, it = FONTMAP.get(s['font'], ('Arial', False, False))
                    runs.append(Run(fix_glyphs(s['text'], f), f, s['size'],
                                    rgb(s['color']), bo, it))
                textbox(slide, l['bbox'][0], y0 - 3,
                        (l['bbox'][2] - l['bbox'][0]) + width_pad, (y1 - y0) + 6,
                        [runs], anchor='m', wrap=False)


def replay(slide, pageno, subs=None, skip_text=(), skip_vectors=(), skip_files=(),
           text_first=False):
    page = LAYOUT[pageno - 1]
    draw_vectors(slide, page, skip=skip_vectors)
    if text_first:
        draw_text(slide, page, subs=subs, skip_text=skip_text)
        draw_images(slide, page, skip_files=skip_files)
    else:
        draw_images(slide, page, skip_files=skip_files)
        draw_text(slide, page, subs=subs, skip_text=skip_text)
    return page


def page_image(slide, pageno, dpi=200):
    """Unveraenderte Metzler-Standardseite als vollflaechiges Bild uebernehmen."""
    import os
    fn = 'page_%02d.png' % pageno
    path = os.path.join(ASSETS, fn)
    if not os.path.exists(path):
        import pymupdf
        d = pymupdf.open(os.path.join(BASE, '..', '20260813_Metzler_evm AG_vF.pdf'))
        d[pageno - 1].get_pixmap(dpi=dpi).save(path)
    picture(slide, fn, 0, 0, 842.04, 595.32)
    return slide
