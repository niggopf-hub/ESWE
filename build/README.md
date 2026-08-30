# ESWE-Deck — Aufbau und Nachbau der evm-Struktur

Erzeugt `20260828_Metzler_ESWE Versorgungs AG_vF.pptx` — dieselbe Storyline und
dasselbe Layout wie `20260813_Metzler_evm AG_vF.pdf`, nur mit den ESWE-Inhalten
aus `ESWE_Slide_Drehbuch.md`.

## Bauen

```bash
pip install python-pptx pymupdf pillow numpy
python3 build/build_deck.py            # schreibt das PPTX ins Repo-Root
DECK_QA=1 python3 build/build_deck.py  # Vorschau-Variante (■ statt Wingdings-Bullet)
```

## Dateien

| Datei | Inhalt |
|---|---|
| `deck.py` | Grundgerüst: Seitenmaß A4 quer (842 × 595,32 pt), Farben, Schriften, Textmaß und Umbruch, Kacheln, Donut-Segmente, Schatten, geklebte Verbindungslinien (`connect`) und Textfelder mit echten Aufzählungszeichen (`bullet_box`) |
| `replay.py` | Generischer Nachbau unveränderter evm-Seiten aus `evm_layout.json` |
| `front.py` | Titelseite, Agenda, Kapiteltrenner |
| `s12.py` … `s20.py` | Die neu befüllten Inhaltsfolien |
| `s14.py` | Beteiligungsstruktur im Format der Duisburg-Unterlage (Organigramm mit Ergebnisbeiträgen) |
| `evm_layout.json` | Aus dem evm-PDF extrahierte Geometrie (Textzeilen, Vektoren, Bilder) |
| `assets/` | Freigestellte Icons, ESWE-Logo, Metzler-Logo, Titelbild |
| `make_assets.py` | Erzeugt die Icons/Logos neu aus den Quell-PDFs |

## Folienzuordnung

| Folie | Herkunft |
|---|---|
| 1, 2, 3, 11, 18 | Nachgebaut, Text auf ESWE angepasst (Ort/Datum, Agendapunkt 2, Kapiteltrenner 2) |
| 4, 5, 6, 21, 22 | Metzler-Standardseiten, 1:1 nachgebaut (Text bleibt editierbar) |
| 7, 8, 9, 10 | Metzler-Standardseiten als Bild übernommen (transparente Überlagerungen der Vorlage) |
| 12, 13, 15–17, 19, 20 | Neu gebaut nach Drehbuch, Layout 1:1 aus dem evm-Deck |
| 14 | Beteiligungsstruktur nach `20240305_Stadtwerke Duisburg_v4`, Folie 11 — Konzernbaum mit Quoten an den Verbindungslinien und je Gesellschaft Tätigkeit, Kapital-/Umsatzgröße und Ergebnisbeitrag (grün = Zufluss, rot = Verlust) |

## Folie 14 — Verbindungslinien und Logos

Alle Äste sind **Konnektoren, die an den Verbindungspunkten der Kacheln kleben**
(`connect(...)` in `deck.py`, Punkt 0 = oben, 1 = links, 2 = unten, 3 = rechts).
Verschiebt man eine Kachel in PowerPoint, läuft die Linie mit. Die Knicke einer
Reihe liegen über eine gemeinsame Adjustierung (`ADJ1`, `ADJ2` in `s14.py`) exakt
auf einer Höhe, sodass eine durchgehende Verteilerlinie entsteht. Der Abgang zur
zweiten Reihe fällt genau in die Gasse zwischen Spalte 3 und 4.

Jeder Infokasten ist **genau ein Textfeld** mit echten Aufzählungszeichen
(`bullet_box`, Wingdings-Quadrat als `buChar`) — kein separates Feld je Bullet.

**Logos:** Liegt in `assets/` eine Datei mit dem passenden Namen, setzt der Build
sie automatisch statt des Firmennamens in die Kachel:

`logo_wvv.png` · `logo_thuega.png` · `logo_swnetz.png` · `logo_witcom.png` ·
`logo_bioenergie.png` · `logo_kmw.png` · `logo_mhkw.png` · `logo_wrt.png` ·
`logo_taunuswind.png` · `logo_eswewindpark.png` · `logo_uettingen.png` ·
`logo_kahlenberg.png` · `logo_badcamberg.png` · `logo_thee.png`

Am besten als PNG mit transparentem Hintergrund; die Höhe wird auf die Kachel
skaliert.

## Schriften

Das Deck referenziert die Originalschriften des Metzler-Templates
(`Univers for Metzler`, `Univers for Metzler Light`, `Univers for Metzler 2`,
Bullets in `Wingdings`). Auf Rechnern ohne diese Schriften ersetzt PowerPoint
sie; die Zeilenumbrüche sind fest gesetzt und mit Arial-/Liberation-Metrik
(etwas breiter als Univers) gerechnet, laufen also nicht über.

## Noch zu prüfen (aus dem Drehbuch übernommene offene Punkte)

- „Ø ~22 → bis zu 80 Mio. EUR p. a." (zfk-Interview Ex-CEO Schodlok) datieren
- Strom-/Gasnetzlänge (~2.820 km / ~823 km) mit Jahresstand belegen
- Zieljahr klimaneutrales Fernwärmenetz (2035 vs. 2045)
- Net-Debt-Reihe 2021–2025 aus den HRB-Jahresabschlüssen (dann Folie 15/16 auf
  die evm-Optik Verschuldung/Net Debt umstellen)
- Wind-/PV-Bestand ~42 MW anteilig
- Folie 14: Die Duisburg-Vorlage nutzt in den Kacheln Firmenlogos; hier stehen die
  Firmierungen als Text, da keine Logos der Beteiligungen vorliegen
