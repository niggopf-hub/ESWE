# -*- coding: utf-8 -*-
"""Icons und Logos aus den Quell-PDFs freistellen."""
import pymupdf, os
import numpy as np
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(BASE, 'assets')
EVM = pymupdf.open(os.path.join(BASE, '..', '20260813_Metzler_evm AG_vF.pdf'))
GB = pymupdf.open(os.path.join(BASE, '..', 'Geschaeftsbericht-25.pdf'))


def clip(doc, pno, r, dpi=600):
    pix = doc[pno - 1].get_pixmap(clip=pymupdf.Rect(*r), dpi=dpi)
    return Image.frombytes('RGB', (pix.width, pix.height), pix.samples)


def cut_out(im, dark_on_light=True, trim=True):
    """Flaechigen Hintergrund (Eckfarbe) freistellen."""
    a = np.asarray(im).astype(float)
    bg = a[0, 0].copy()
    d = (bg - a) if dark_on_light else (a - bg)
    d = np.clip(d, 0, None).max(axis=2)
    D = max(d.max(), 1.0)
    alpha = np.clip(d / D, 0, 1)
    alpha[alpha < 0.03] = 0
    safe = np.where(alpha > 0, alpha, 1)[..., None]
    col = bg - (bg - a) / safe if dark_on_light else bg + (a - bg) / safe
    col = np.clip(col, 0, 255)
    out = np.dstack([col, alpha * 255]).astype(np.uint8)
    img = Image.fromarray(out, 'RGBA')
    if trim:
        ys, xs = np.nonzero(alpha > 0.06)
        if len(ys):
            img = img.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))
    return img


def save(img, name):
    img.save(os.path.join(A, name))
    return name


# --- 6 Geschaeftsfeld-Icons (von der Icon-Leiste S. 13) -------------------
GF_X = [95.25, 225.4, 355.85, 486.2, 616.45, 747.0]
for i, cx in enumerate(GF_X, 1):
    save(cut_out(clip(EVM, 13, (cx - 26, 456, cx + 26, 504))), 'gf%d.png' % i)

# --- 6 Ziel-Icons (S. 19) -------------------------------------------------
ZIEL = [(52, 162, 101, 209), (752, 161, 793, 210), (51, 308, 102, 346),
        (757, 307, 789, 347), (55, 449, 98, 491), (744, 447, 789, 492)]
for i, r in enumerate(ZIEL, 1):
    save(cut_out(clip(EVM, 19, r)), 'ziel%d.png' % i)

# --- Dokument-Icon der Ausgangslage-Kachel (weiss auf dunkelblau) ---------
save(cut_out(clip(EVM, 12, (52, 294, 105, 359)), dark_on_light=False), 'doc_icon.png')

# --- ESWE-Logo aus dem Geschaeftsbericht 2025 -----------------------------
save(cut_out(clip(GB, 1, (36, 66, 162, 132), dpi=900)), 'eswe_logo.png')

print('assets erzeugt')
