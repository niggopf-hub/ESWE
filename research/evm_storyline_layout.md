# Storyline- und Layout-Analyse: Metzler-Deck evm AG — Kapitel 2 (S. 12–17) und 3 (S. 19–21)

Ergänzung zur Text-Inventur `/home/user/ESWE/research/evm_deck_struktur.md` (dort: Volltexte, Stilregeln, Fehlerliste).
Hier: Slide-Messages, Argumentationsbogen, Layoutzonen mit Platzanteilen (gemessen via PyMuPDF `get_text("dict")`-Blockkoordinaten auf Seitenformat 842 × 595 pt = A4 quer) und Textmengen-Budgets für den 1:1-Nachbau (ESWE).

**Messbasis / gemeinsames Seitenraster (alle 9 Slides):**

| Zone | y-Bereich (% der Seitenhöhe) | Inhalt |
|---|---|---|
| Kopfzeile | 3–5 % | Kapitelnr. + Kapiteltitel, 10 pt grau, linksbündig ab x=4 % |
| Headline | 7–14 % | 20 pt fett, 1–2 Zeilen, Breite bis 89–97 %; darunter dünne Linie bei ~y=24 % Seitenhöhe (Seite 13ff bei y≈14 %) |
| Content-Bühne | ~20–88 % | slide-spezifisch (s. u.); nutzbare Fläche ca. 95 % Breite × 68 % Höhe |
| Fußnotenzeile | 90–93 % | 8 pt, 1–2 Zeilen, semikolongetrennt |
| Fußzeile | 95–96 % | links Seitenzahl + „Quellen: …" (8 pt), rechts Metzler-Logo (x=83–96 %, y=91–96 %) |

Headline-Budget über alle Slides: **68–138 Zeichen (Median ~111), 7–17 Wörter, max. 2 Zeilen à 20 pt.** Einzeilige Headline nur auf S. 19.

---

## KAPITEL 2 — „evm AG – Übersicht und Herausforderungen" (S. 12–17)

### Slide 12 — Ausgangslage („Unser Verständnis der Ausgangslage")

**1. Message (So-what):** „Die evm ist stark und profitabel — aber das Investitionsprogramm von fast 600 Mio. EUR bei gleichzeitiger Wahrung finanzieller und strategischer Flexibilität ist IHRE zentrale Herausforderung."
**Rolle im Bogen:** Eröffnungsslide des Kundenkapitels direkt nach dem Kapiteltrenner; definiert das Problem, das alle Folgeslides beweisen und Kapitel 3 löst. Zeigt zugleich „wir haben eure Lage verstanden" (Beratersignal via Zwischenüberschrift „Unser Verständnis der Ausgangslage").

**2. Layout-Zonen:**
- Zwischenüberschrift (14 pt, grau): y=17–19 %, linksbündig.
- **Links, schmale Vertikal-Kachel dunkelblau** (x=3–16 % ≈ 13 % Breite, y=21–81 % ≈ 60 % Höhe ⇒ ~8 % der Slidefläche): mittig weißes Label „Ausgangslage" (10,6 pt, um 90°-los, horizontal) + weißes Dokument-Icon darunter.
- **Rechts, hellblauer Bullet-Kasten** (x=16–97 % ≈ 81 % Breite, y=21–81 % ⇒ ~49 % der Fläche): 7 ◼-Bullets, Textspalte x=18–95 %.
- **Takeaway-Banner** (x=3–97 %, y=83–91 % ≈ 8 % Höhe): weißer Kasten mit dunkelblauem Rahmen, links dunkelblaues Chevron/Pfeilspitze (~3 % Breite), Text fett dunkelblau, 2 Zeilen.

**3. Textmengen-Budget:**
- Headline: 134 Zeichen / 16 Wörter / 2 Zeilen.
- 7 Bullets à 10,6 pt; Zeilen pro Bullet: 4 / 3 / 3 / 2 / 2 / 2 / 2 (insgesamt 18 Textzeilen); Wörter pro Bullet ca. 15–35 (längster Bullet 1 mit ~26 Wörtern über 3–4 Zeilen, kürzester ~14). Zeilenbreite ~630 pt ⇒ ~100–110 Zeichen/Zeile. Zwischen den Bullets großzügiger Weißraum (~15–18 pt).
- Takeaway: ~170 Zeichen / 24 Wörter / genau 2 Zeilen (10,6 pt fett).

**4. Grafik-Slots:** 1 Label-Kachel mit 1 Icon; 7 Bullet-Slots; 1 Banner-Slot. Keine Zahlengrafik.

**5. Dramaturgie:** Führt das Leitmotiv **„fast 600 Mio. EUR"** ein (Bullet 6 + Takeaway = doppelt auf einer Seite). Bullets sind zugleich die Gliederung des Kapitels: Bullet 1–2 → S. 13 (Geschäftsmodell/KPIs), Bullet 2 (enm) + implizit → S. 14 (Struktur), Bullet 3 → S. 13/16 (Financials), Bullet 4–6 → S. 15 (Klimaziele/Investitionen), Bullet 7 (Verpflichtungen ggü. Stadt) bleibt als offener Haken für die Investorendiskussion.

---

### Slide 13 — KPI-Grid + Umsatzsplit-Donut

**1. Message:** „Solides, breit aufgestelltes Unternehmen — aber ~90 % des Umsatzes sind Commodity-Vertrieb (Strom+Gas), und es gibt substanzielle Netz-Assets."
**Rolle:** Beantwortet die nach S. 12 offene Frage „Wie groß und wie profitabel ist das Unternehmen eigentlich genau?" — Faktenfundament; zeigt implizit die Assets (Netze, Wasser), an denen später Investoren beteiligt werden könnten.

**2. Layout-Zonen:**
- **Links: KPI-Kachelgrid** (x=3–33 % ≈ 30 % Breite, y=22–75 % ⇒ ~16 % Fläche): 2 Spalten × 3 Zeilen Finanzkacheln (y=22–50 %), dann Zwischenüberschrift „Kunden und Netzinfrastruktur" (10 pt fett, y=53–55 %), dann 2×2 weitere Kacheln (y=57–75 %). Kachelgröße je ~110 × 38 pt (≈ 13 % × 6,4 % der Seite).
- **Rechts: grauer Chart-Hintergrundkasten** (x=57–?; sichtbar hellgrauer Block x≈37–97 %, y=21–75 % ⇒ ~42 % Fläche) mit **Donut** (Zentrum bei ca. x=68 %, y=33 %; Durchmesser ~20 % Seitenbreite), Zentrumstext „100 % ≙ 999 Mio. EUR" (9 pt); Segment-%-Labels 10 pt auf/neben den Segmenten.
- **5 gestrichelte Callout-Boxen** um den Donut: 2 oben links/rechts des Donuts (x=39–50 % und x=80–95 %, y=28–41 %), 3 in einer unteren Reihe (x=39–52 %, 59–75 %, 79–95 %; y=48–63 %); per dünner Linie mit Segmenten verbunden. Callout-Format: Titel fett blau (10 pt) + 1–2 ◼-Bullets (9 pt).
- **Unten: Icon-Leiste Geschäftsfelder** (hellblaues Band x=3–97 %, y=77–90 % ≈ 12 % Höhe): 6 Icons + Labels (10 pt fett blau), getrennt durch 5 vertikale gestrichelte Linien.

**3. Textmengen-Budget:**
- Headline: 109 Zeichen / 16 Wörter / 2 Zeilen.
- KPI-Kachel: Zeile 1 Label+Jahr (10 pt, ~12–15 Zeichen), Zeile 2 Wert fett (10 pt), Zeile 3 Vorjahr kursiv in Klammern (nur bei den 5 Finanzkacheln; die 5 unteren Kacheln haben 2 Zeilen).
- Callouts: Titel 8–22 Zeichen; Bullets je 3–8 Wörter, 2–4 Zeilen à ~25 Zeichen (schmale Spalte!). Größter Callout (Dienstleistungserträge): 2 Bullets, zusammen 10 Zeilen-Äquivalente.
- Icon-Leisten-Labels: 1–2 Zeilen, 12–35 Zeichen.
- Fußnoten: 3 Stück in 2 Zeilen à 8 pt.

**4. Grafik-Slots:** **10 KPI-Kacheln** (5 Finanz + 1 Mitarbeiter + 2 Kunden + 2 Netz-km); **Donut mit 5 Segmenten** (48/41/4/3/4 %) + 1 Zentrumslabel; **5 Callouts** (mit 1–2 Bullets); **6 Icons** in der Leiste. Insgesamt 22 füllbare Slots.

**5. Dramaturgie:** Die 999 Mio. EUR Umsatz aus S. 12 kehren als Donut-Zentrum und Kachel 1 wieder; die 6 Geschäftsfeld-Icons werden hier eingeführt und auf S. 14 (Kachel-Tags + Legende) und S. 17 (Strategie-Zeilen) exakt wiederverwendet — die Icon-Leiste ist das visuelle Rückgrat des Kapitels. CapEx-Kachel (43 vs. 24 Mio. EUR) sät bereits den „Investitions-Hochlauf", der auf S. 15/16 ausgebaut wird.

---

### Slide 14 — Aktionärs- und Beteiligungsstruktur (Organigramm)

**1. Message:** „Kommunal verankert (83,7 % über EKO2, dahinter SWK/thüga), mit 17 direkten Beteiligungen — es gibt konkrete gesellschaftsrechtliche Andockpunkte für Transaktionen."
**Rolle:** Beantwortet „Wem gehört das Unternehmen, und wo genau könnte man strukturell ansetzen?" — die stille Vorbereitung von S. 20 (dort werden genau diese Gesellschaften als beteiligungsfähige Assets genannt).

**2. Layout-Zonen:**
- **Aktionärsband oben** (y=20–31 % ≈ 11 % Höhe): links vertikal beschriftete blaue Label-Kachel „Aktionäre der evm AG" (x=3–9 %), daneben hellblaues Band mit **4 weißen Aktionärs-Kacheln** (Logo/Name + %-Quote; je ~14–21 % Breite), von x=13 bis ~80 %.
- **Seitenkasten rechts** „Gesellschafter der EKO2 GmbH" (grau, x=81–97 %, y=21–43 % ⇒ ~6 % Fläche): 4 Zeilen Logo + Quote, mit Pfeil/Klammer an die EKO2-Kachel angebunden.
- **Mitte:** evm-AG-Kachel mit Logo + Icon-Reihe (x≈41–55 %, y=33–42 %), Verbindungslinien nach oben/unten.
- **Beteiligungsband unten** (y=43–90 % ≈ 47 % Höhe, größte Zone ~45 % Fläche): links vertikale Label-Kachel „Beteiligungsstruktur¹⁾" (x=3–9 %), rechts **Kachelgrid 5 Spalten × 4 Reihen** (17 Kacheln belegt, Position 18–20 der letzten Reihe = Icon-Legende). Kachel ~110 × 45 pt: weiß, Logo bzw. Name (8 pt) + Quote fett (9 pt), Geschäftsfeld-Mini-Icons oben rechts.
- **Icon-Legende** in der rechten unteren Grid-Fläche (x=52–95 %, y=80–89 %): 2 Spalten × 3 Zeilen (Icon + Label 8 pt).

**3. Textmengen-Budget:**
- Headline: 115 Zeichen / 15 Wörter / 2 Zeilen.
- Kacheltexte: Firmenname 1–3 Zeilen à 8 pt (max. ~22 Zeichen/Zeile), Quote 9 pt fett. Keine Sätze auf dieser Slide — reine Namen/Quoten.
- Fußnote: 1 Stück über 2 Zeilen (~200 Zeichen).

**4. Grafik-Slots:** 4 Aktionärs-Kacheln + 4 Zeilen im EKO2-Seitenkasten + 1 Zentral-Kachel + **17 Beteiligungs-Kacheln** (sortiert absteigend nach Quote: Reihe 1 = 5×100 %, Reihe 2 = 5×50 %, Reihe 3 = 49/49/42,9/33,3/33,3 %, Reihe 4 = 25,1/31,75 %) + 6 Legenden-Icons. Bei ESWE: Grid flexibel 4–5 Spalten; Sortierlogik (Quote absteigend, Reihen ≈ Quoten-Cluster) beibehalten.

**5. Dramaturgie:** Wiederholt die 6 Geschäftsfeld-Icons als Tagging-System (jede Beteiligung bekommt ihre Felder). Der Seitenkasten (SWK/thüga) greift Bullet 7 von S. 12 („Verpflichtungen ggü. Stadtwerke Koblenz/Stadt") auf. S. 20 nennt später zwei der hier gezeigten Gesellschaften (Energienetze Mittelrhein KG, Naturstrom Rheinland-Pfalz) namentlich als Beteiligungsobjekte — die Slide ist also der „Asset-Katalog".

---

### Slide 15 — Investitionsmatrix + Verschuldungs-Chart

**1. Message:** „Der 600-Mio.-Bedarf ist real und konkret (3 Schwerpunkte mit benannten Projekten) — und die Bilanz ist zwar tragfähig (2,6x), lässt aber wenig Spielraum."
**Rolle:** Beantwortet „Wofür genau werden die 600 Mio. gebraucht — und kann evm sich das leisten?" Erste Hälfte der Beweiskette Finanzierungslücke (Bilanzseite); S. 16 liefert die zweite Hälfte (Cashflow-Seite).

**2. Layout-Zonen (Zweiteilung ca. 2/3 oben, 1/3 unten):**
- **Oben: Matrix „Investitionsbedarf"** (x=3–97 %, y=20–66 % ⇒ ~45 % Fläche): Titelband hellblau „Investitionsbedarf" (y=20–23 %); linke Zeilen-Label-Spalte (x=3–15 %, mittelblaue Kacheln): „Investitionsschwerpunkt" / „CapEx" / „Geplante Projekte". Drei Inhaltsspalten (je ~27 % Breite, getrennt durch vertikale gestrichelte Linien): Zeile 1 (y=23–33 %) Kreis-Icon (Ø ~55 pt) + Spaltentitel fett (10 pt); Zeile 2 (y=33–39 %) **eine spaltenübergreifende Klammer** mit zentriertem „Fast 600 Mio. EUR" (10,6 pt fett) + Unterzeile „Geplante Investitionen 2025-2029¹⁾" (9 pt blau); Zeile 3 (y=39–66 %) je Spalte 3–4 ◼-Bullets (9 pt).
- **Unten: Balkendiagramm** (x=3–58 %, y=68–90 % ⇒ ~13 % Fläche): Charttitel fett blau (10 pt), Legende (2 Einträge), 5 Balken (Jahre 2021–2025) mit Wert über dem Balken (10 pt) und je 1 **ovaler Badge** (dunkelblau gefüllt, weiße Schrift „3,1x" …) darüber.
- **Rechts daneben: Pfeil-Takeaway** (x=63–95 %, y=75–83 %): dicker blauer Blockpfeil (→) + 3 Zeilen fetter blauer Text.

**3. Textmengen-Budget:**
- Headline: 102 Zeichen / 15 Wörter / 2 Zeilen.
- Projekt-Bullets: Spalte 1: 3 Bullets (4/2/4 Zeilen), Spalte 2: 4 Bullets (3/3/2/3 Zeilen), Spalte 3: 4 Bullets (2/3/2/3 Zeilen) — je Bullet 8–22 Wörter, Spaltenbreite ~200 pt ⇒ ~45–50 Zeichen/Zeile. Max. ~11 Textzeilen je Spalte.
- Pfeil-Takeaway: ~145 Zeichen / 21 Wörter / 3 Zeilen (10 pt fett).
- Fußnoten: 2 Stück in 2 Zeilen (Fußnote 2 = lange Net-Debt-Definition, ~150 Zeichen).

**4. Grafik-Slots:** 3 Kreis-Icons + 3 Spaltentitel; 1 Klammer-Summe (Betrag + Zeitraum); 11 Projekt-Bullets (3+4+4); **5 Balken + 5 Werte + 5 Multiple-Ovale + 5 Jahreslabels**; 1 Blockpfeil-Takeaway; 3 Zeilen-Label-Kacheln.

**5. Dramaturgie:** „Fast 600 Mio. EUR" erscheint hier zum 3. und 4. Mal (Klammer + Pfeiltext) — das Leitmotiv wird an die konkrete Projektliste UND an die Bilanzgrenze gekoppelt. Die drei Investitionsschwerpunkte spiegeln exakt Bullet 6 von S. 12 („Energienetze, Wind- und Solarparks sowie Wärmenetze"). Das Net-Debt-Chart (249→237, 2,6x) wird auf S. 16 im Bilanz-Panel wiederholt — bewusste Redundanz als Beweisverstärkung.

---

### Slide 16 — Financials-Tripel (GuV / Cashflow / Bilanz) + Kommentar

**1. Message:** „Ordentliche Marge, aber volatile Cashflows und steigende Nettoverschuldung — die 600 Mio. sind aus dem operativen Cashflow NICHT finanzierbar." (Schlussbullet = analytischer Kern des ganzen Kapitels.)
**Rolle:** Beantwortet „Kann evm das nicht einfach selbst verdienen?" mit einem klaren Nein — der Beweis, dass externes Kapital nötig ist. Ohne diese Slide hätte Kapitel 3 keine Existenzberechtigung.

**2. Layout-Zonen (Vierteilung: 3 Charts oben, Kommentarband unten):**
- **3 gleich breite Chart-Panels** nebeneinander (y=21–66 % ⇒ je ~13 % Fläche): Panel 1 GuV x=4–32 %, Panel 2 Cashflow x=37–63 %, Panel 3 Bilanz x=69–96 %. Jedes Panel: Charttitel fett blau (10 pt, y=22–24 %), 2-zeilige Legende (9 pt, y=25–29 %), Chartfläche y=29–65 % mit 5 Jahres-Clustern, Jahreszeile (y=64–65 %).
  - Panel 1: gepaarte Säulen (dunkel-/mittelblau) + 5 ovale Margen-Badges (schwebend über den Säulen, y=25–43 %) + orangefarbener diagonaler CAGR-Pfeil mit Oval „+4% p.a.".
  - Panel 2: gestapelte ±-Säulen um eine Nulllinie; Positivwerte in den Säulen (weiß), Negativwerte in Klammern seitlich/unterhalb (9 pt); Jahressumme fett über/unter dem Cluster.
  - Panel 3: gepaarte Säulen (Kasse/Net Debt) + 5 EK-Quoten-Ovale oben.
- **Kommentarband** (x=3–97 %, y=72–88 % ≈ 16 % Höhe, hellgrau hinterlegt): Label „Kommentar:" fett (9 pt) + 4 ◼-Bullets volle Breite.

**3. Textmengen-Budget:**
- Headline: 128 Zeichen / 14 Wörter / 2 Zeilen.
- Alle Chart-Beschriftungen 9 pt. Legenden: Panel 1 = 4 Einträge, Panel 2 = 4, Panel 3 = 3.
- Kommentar-Bullets: 3 / 22 / 45 / 21 Wörter — Bullet 1 bewusst ultrakurz („Umsatz 2025 stabil"), Bullet 3 ist der längste (2 Zeilen volle Breite ~140 Zeichen/Zeile). Insgesamt 5 Textzeilen im Kommentarband.
- Fußnote: 1 kurze (~40 Zeichen).

**4. Grafik-Slots:** Panel 1: 5×2 Säulen + 10 Wertlabels + 5 Margen-Ovale + 1 CAGR-Pfeil + 1 CAGR-Oval. Panel 2: 5 Säulen-Stacks à 3 Segmente (15 Segmente) + ~15 Wertlabels + 5 Summenlabels. Panel 3: 5×2 Säulen + 10 Wertlabels + 5 EK-Ovale. Plus 4 Kommentar-Bullets. Dichteste Slide des Decks (~85 Beschriftungselemente).

**5. Dramaturgie:** Leitmotiv-Auftritte 5 und 6: „fast 600 Mio. EUR" im Schlussbullet + Net-Debt-Reihe (237) als Wiederholung von S. 15. Der CAGR-Pfeil (orange) ist der einzige Orange-Akzent in Kapitel 2 — Orange kehrt auf S. 20 als „Investor"-Box wieder (Farbe = externes Element). Headline-Muster „These − jedoch Einschränkung" erreicht hier den dramatischen Höhepunkt des Kapitels.

---

### Slide 17 — Strategie je Geschäftsfeld (6 Icon-Zeilen)

**1. Message:** „Die Strategie steht in allen 6 Feldern — und sie ist durchweg investitionsintensiv." (Implizit: nicht die Strategie ist das Problem, sondern deren Finanzierung.)
**Rolle:** Ruhige Abschluss-/Scharnier-Slide: fasst das Unternehmen nach Geschäftsfeldern zusammen und übergibt an Kapitel 3 mit der offenen Frage „Wie wird das alles bezahlt?".

**2. Layout-Zonen:** 6 horizontale hellblaue Voll-Breiten-Balken (x=3–97 %, je ~10 % Seitenhöhe + ~2 % Zwischenraum, gestapelt y=20–88 %): links Icon-Zone (~10 % Breite, Icon dunkelblau ~40 pt), rechts Textzone ab x=15 % bis max. 96 %. Kein Takeaway, keine Fußnote — die luftigste Slide des Kapitels.

**3. Textmengen-Budget:**
- Headline: 111 Zeichen / 14 Wörter / 2 Zeilen (Dreiklang+1-Aufzählung).
- Je Balken **genau 1 Satz**, 10,6 pt dunkelblau (nicht fett), **immer 2 Zeilen**, 17–28 Wörter (~130–200 Zeichen). Nominal-/Verbalsubstantiv-Start („Stärkung…", „Bedarfsgerechter Ausbau…", „Weiterer Ausbau…", „Unterstützung…", „Ausbau…", „Langfristige Absicherung…").

**4. Grafik-Slots:** 6 Balken × (1 Icon + 1 Satz). Icon-Reihenfolge = exakt die Geschäftsfelder-Reihenfolge der Icon-Leiste S. 13.

**5. Dramaturgie:** Drittes Auftauchen der 6 Geschäftsfeld-Icons (nach S. 13 Leiste, S. 14 Tags/Legende) — schließt die visuelle Klammer des Kapitels. Inhaltlich nimmt jeder Satz Investitionsthemen von S. 15 wieder auf (Netzausbau, Wind/Solar inkl. Schneifelhöhe, Wärmeplanung). Formal identischer Zwilling von S. 21 (gleiche Balken-Anatomie) — Kapitel 2 endet, wie Kapitel 3 endet: Symmetrie Kunde ↔ Berater.

---

## KAPITEL 3 — „Diskussion möglicher Handlungsoptionen" (S. 19–21)

### Slide 19 — Mögliche strategische Ziele (Hub-and-Spoke)

**1. Message:** „Bevor über Strukturen geredet wird: Diese 6 strategischen Ziele könnte evm verfolgen — Finanzierung, Risikoteilung, Kapitalfreisetzung, Wachstum."
**Rolle:** Öffnet den Lösungsraum, ohne etwas zu verkaufen („Mögliche…", „Diskussion…"). Beantwortet die aus Kapitel 2 mitgebrachte Frage „Was können wir überhaupt tun?" auf Zielebene — die Optionsebene folgt erst auf S. 20.

**2. Layout-Zonen:**
- **Zentrum:** großer hellblauer Kreis (Mittelpunkt x≈50 %, y≈56 %; Ø ~34 % Seitenhöhe ⇒ ~9 % Fläche) mit Titel „Mögliche strategische Ziele" (14 pt fett) + evm-Logo (Bild 13 % × 8 %).
- **6 Ziel-Slots im 2×3-Raster** um den Kreis: linke Spalte Text x=14–34 % mit Icon links außen (x=9–13 %); rechte Spalte Text x=63–83 % mit Icon rechts außen (x=90–95 %) — Icons spiegeln nach außen. Reihen-y: 27–36 % / 51–60 % / 73–85 %.
- **2 horizontale gestrichelte Trennlinien** über die volle Breite (y≈41 % und y≈65 %), die die 3 Reihen trennen (laufen optisch „hinter" dem Kreis durch).
- Farbdramaturgie: Textfarbe wird von Reihe zu Reihe heller (Reihe 1 dunkelblau → Reihe 2 mittel/grau → Reihe 3 hellblau) — Lesereihenfolge/Priorität von Finanzzielen (oben) zu Wachstumszielen (unten).

**3. Textmengen-Budget:**
- Headline: 68 Zeichen / 7 Wörter / **1 Zeile** (kürzeste des Decks, Nominalstil).
- Je Ziel: 1 Nominalphrase, 12 pt fett, **3–5 Zeilen** à ~20–25 Zeichen (Spaltenbreite nur ~160 pt!), 7–11 Wörter. Kein Punkt.

**4. Grafik-Slots:** 1 Zentrumskreis (Titel + Logo) + 6 × (Icon + Nominalphrase) + 2 Trennlinien. Keine Zahlen.

**5. Dramaturgie:** Die 6 Ziele antworten paarweise auf Kapitel-2-Befunde: Ziel 1/2 (Fremd-/Eigenkapital) ← S. 15/16 Finanzierungslücke; Ziel 3 (Risikoteilung) ← S. 15 Großprojekte; Ziel 4 (Kapitalfreisetzung aus Assets) ← S. 13/14 Asset-/Beteiligungskatalog; Ziel 5/6 (Akquisitionen, Plattformen) ← S. 17 Wachstumsstrategie. Das Firmenlogo im Zentrum sagt: „Ihr steht im Mittelpunkt, nicht das Produkt."

---

### Slide 20 — Beteiligungsmodelle („ausgewählte Impulse")

**1. Message:** „So könnte es konkret aussehen: z. B. ein JV/SPV nach Carve-out mit einem Investor — oder direkte Beteiligungen an konkreten Gesellschaften; die Vorteile überwiegen, die Gestaltung bleibt in eurer Hand."
**Rolle:** Konkretisierung — beantwortet „Und wie ginge das praktisch, ohne Kontrolle zu verlieren?" Kernslide des Pitches; die Quadranten unten (Gestaltungsaspekte/Governance) entkräften präventiv den Haupteinwand kommunaler Eigentümer.

**2. Layout-Zonen (2×2-Quadranten, Spaltengrenze bei x=50 %):**
- **Oben links** (x=3–50 %, y=22–63 % ⇒ ~19 % Fläche): Kasten mit mittelblauem Titelbalken „Joint Venture Energieerzeugung/Netzbetrieb¹⁾" (weiße Schrift, zentriert, y=22–24 %), darunter hellblaue Fläche mit **Strukturdiagramm**: oben links Firmenlogo, oben rechts **orange Box „Investor"**; beide mit abgewinkelten Pfeilen und „X%"-Labels auf eine zentrale Kachel „Wärme/Netze SPV / *post Carve-Out*" (dunkelblauer Kopf + weißer Körper mit 2 Icon+Label-Zeilen „Wärmeerzeugung", „Energienetze"); Badge „Minderheit" am Investor-Pfeil; links/rechts flankierend 2 gestrichelte Kommentar-Boxen (blau kursiv „Einbringung Energienetze/EE-Erzeugung" | orange kursiv „Einbringung EK für Capex und Kaufpreis").
- **Oben rechts** (x=50–97 %, gleiche Höhe): Kasten mit Titelbalken „(private) Beteiligung an Unternehmen/Assets", hellblaue Fläche, oben links **3 ◼-Bullets** (Gesellschaftsnamen) — Rest der Fläche bewusst leer (Verhandlungsmasse!).
- **Unten links** (y=66–88 % ⇒ ~10 % Fläche): Überschrift fett blau „Wesentliche Aspekte bei der Gestaltung einer Partnerschaft" (10 pt) + weißer Kasten mit **5 ◼-Bullets**.
- **Unten rechts:** Überschrift „Vorteile für die evm AG" + weißer Kasten mit **5 ◼-Bullets**.

**3. Textmengen-Budget:**
- Headline: 138 Zeichen / 17 Wörter / 2 Zeilen (längste des Decks; Muster „Angebot − ausgewählte Impulse").
- Diagramm-Labels: 9 pt, 1–3 Wörter je Element; Kommentar-Boxen 2–3 Zeilen à ~18 Zeichen, kursiv.
- Bullets unten: 10 pt; links 5 Bullets à 3–10 Wörter (1 Bullet zweizeilig), rechts 5 Bullets à 3–6 Wörter, alle einzeilig. Asset-Liste oben rechts: 3 Bullets à 2–4 Wörter.
- Fußnote: 1 (~80 Zeichen). KEINE Quellenzeile.

**4. Grafik-Slots:** Strukturchart: 2 Gesellschafter-Slots (Logo + Investor-Box) + 2 „X%"-Anteilslabels + 1 SPV-Kachel mit 2 Asset-Icon-Zeilen + 1 „Minderheit"-Badge + 2 gestrichelte Einbringungs-Boxen. Asset-Liste: 3 Bullet-Slots (erweiterbar auf ~6). Unten: 2 × 5 Bullet-Slots + 2 Überschriften.

**5. Dramaturgie:** Orange markiert konsequent „das Externe" (Investor-Box + EK-Einbringung; vgl. oranges evm-Logo und CAGR-Pfeil). Die 3 genannten Gesellschaften sind exakt aus dem Organigramm S. 14 gegriffen (AG selbst, Netz-KG, Ökostromtochter) — S. 14 war der Katalog, S. 20 die Bestellung. „Bei Bedarf können …" + „X%" + „ausgewählte Impulse" halten alles unverbindlich: kein Verkaufsdruck, Diskussionseinladung (spiegelt den Kapiteltitel „Diskussion möglicher Handlungsoptionen"). Vorteil-Bullet 1 („Teilung von Risiken und Investitionsbedarf") schließt den Kreis zum Takeaway S. 12.

---

### Slide 21 — Why Metzler (6 Credential-Zeilen)

**1. Message:** „Für genau diesen Weg ist Metzler der richtige Begleiter: Sektor-Know-how, Investorenzugang, Erfahrung mit der öffentlichen Hand, unabhängig und ohne Interessenkonflikte."
**Rolle:** Abschluss/Call-to-Action des Pitches; beantwortet die letzte Leserfrage „Und warum mit euch?" — verweist implizit zurück auf die Referenzen aus Kapitel 1 (Kreisschluss des Decks).

**2. Layout-Zonen:** Baugleich mit S. 17: 6 horizontale Balken voller Breite (x=3–97 %), y=20–90 %, je ~10 % Höhe; hier mit sehr hellem (fast weißem) Verlaufs-Hintergrund und **gestrichelten horizontalen Trennlinien** zwischen den Balken (statt Weißraum wie S. 17). Icon links (~ x=4–8 %), Text ab x=15 %. Keine Fußnoten-/Quellenzeile.

**3. Textmengen-Budget:**
- Headline: 110 Zeichen / 9 Wörter / 2 Zeilen (Dreiklang-Muster).
- Je Balken 1 Aussage, **11 pt fett** dunkelblau (vs. S. 17: 10,6 pt nicht fett), 1–2 Zeilen, 5–18 Wörter. Zeilenlängen gestaffelt: die kürzesten Aussagen (Zeile 3 „Team", Zeile 6 „Unternehmerisches Denken") wirken als Rhythmuswechsel.
- Zeile 5 enthält das einzige Sonderzeichen-Stilmittel: „… ➔ keine Interessenkonflikte".

**4. Grafik-Slots:** 6 × (Icon + fetter Satz). Inhalt unternehmensunabhängig — für das ESWE-Deck nahezu wörtlich übernehmbar (nur „öffentliche Hand"-Bezüge prüfen).

**5. Dramaturgie:** Formale Spiegelung von S. 17 (Kundenstrategie ↔ Beraterstärken in identischer Formensprache = „wir passen zusammen"). Credential 1 und 4 (Energiesektor, öffentliche Hand) docken exakt an das Profil des Kunden an (kommunaler Versorger); Credential 5 (Unabhängigkeit) antizipiert den Einwand „Banken wollen doch nur ihre Produkte verkaufen".

---

## Roter Faden Kapitel 2 + 3 (Gesamtstoryline)

1. **S. 12** stellt die Frage „Was ist eure Lage?" und beantwortet sie selbst: starkes Unternehmen, aber ein Investitionsprogramm von fast 600 Mio. EUR, das finanzielle und strategische Flexibilität bedroht — die These des gesamten Decks steht im Takeaway-Banner der ersten Inhaltsslide.
2. **S. 13** beantwortet „Wie groß und profitabel seid ihr wirklich?" mit dem KPI/Donut-Fundament — und zeigt nebenbei die Assets (Netze, Wasser, ~90 % Commodity-Umsatz), um die es später gehen wird.
3. **S. 14** beantwortet „Wem gehört ihr und wo kann man strukturell ansetzen?" mit dem Organigramm — der stille Asset- und Andockpunkt-Katalog für Slide 20.
4. **S. 15** beantwortet „Wofür genau braucht ihr 600 Mio., und trägt das eure Bilanz?" — Projekte konkret, Verschuldung tragfähig (2,6x), aber der Spielraum schrumpft.
5. **S. 16** beantwortet die entscheidende Frage „Könnt ihr das nicht selbst verdienen?" mit Nein: volatile Cashflows, steigende Nettoverschuldung, Investitionsprogramm „scheint nicht aus dem operativen Cash Flow finanzierbar" — der analytische Wendepunkt.
6. **S. 17** beantwortet „Ist wenigstens die Strategie klar?" mit Ja — sechs investitionsintensive Stoßrichtungen, womit die offene Frage nur noch lautet: Wer bezahlt das?
7. **S. 19** öffnet darauf den Lösungsraum: „Was könnt ihr tun?" — sechs mögliche strategische Ziele um das Kundenlogo herum, bewusst als Diskussionsangebot, nicht als Empfehlung.
8. **S. 20** konkretisiert: „Wie ginge das praktisch?" — exemplarisch JV/SPV nach Carve-out plus direkte Beteiligungen an den auf S. 14 gezeigten Gesellschaften, flankiert von Governance-Beruhigung und Vorteilsliste (die den 600-Mio.-Schmerz von S. 12 direkt adressiert).
9. **S. 21** schließt mit „Warum mit Metzler?" — sechs Credentials in derselben Formensprache wie die Kundenstrategie auf S. 17.
10. Zusammengehalten wird alles durch drei Leitmotive: die Zahl **„fast 600 Mio. EUR"** (6 Auftritte: S. 12 ×2, 15 ×2, 16 ×1 sowie Headline S. 15), die **6 Geschäftsfeld-Icons** (S. 13 Leiste → S. 14 Tags/Legende → S. 17 Zeilen) und die Farbe **Orange = das Externe/Neue** (evm-Logo, CAGR-Pfeil, Investor-Box).

---

## Anhang: Wiederverwendbare Layout-Kurzformeln (für ESWE-Nachbau)

| Slide | Kurzformel |
|---|---|
| 12 | Links 13 % B vertikale Label-Kachel • rechts 81 % B hellblauer Kasten mit 7 Bullets (18 Zeilen) • unten 8 % H Chevron-Takeaway-Banner (2 Zeilen fett) |
| 13 | Links 30 % B KPI-Grid (2×3 + Zwischentitel + 2×2) • Mitte/rechts 42 % Fläche Donut (5 Segmente, Zentrumslabel) + 5 gestrichelte Callouts • unten 12 % H Icon-Band (6 Icons) |
| 14 | Oben 11 % H Aktionärsband (4 Kacheln) + Seitenkasten rechts (4 Gesellschafter) • Mitte Logo-Kachel • unten 47 % H Beteiligungsgrid 5×4 (17 Kacheln + Icon-Legende 2×3) |
| 15 | Oben ~45 % Fläche 3-Spalten-Matrix (Icons / Klammer „Fast 600 Mio. EUR" / je 3–4 Bullets) • unten links 5-Balken-Chart mit 5 Multiple-Ovalen • unten rechts Blockpfeil-Takeaway (3 Zeilen) |
| 16 | 3 gleich breite Chart-Panels (GuV-Paare+Margen-Ovale+CAGR-Pfeil / CF-Stacks±+∑ / Bilanz-Paare+EK-Ovale, je 5 Jahre) • unten 16 % H „Kommentar:"-Band mit 4 Bullets |
| 17 | 6 hellblaue Voll-Breiten-Balken à ~10 % H: Icon links + genau 1 Satz (2 Zeilen, 17–28 Wörter) |
| 19 | Zentraler Kreis (Titel + Logo) • 6 Ziel-Slots 2×3 (Icon außen + Nominalphrase 12 pt fett, 3–5 kurze Zeilen) • 2 gestrichelte Reihen-Trennlinien |
| 20 | 2×2-Quadranten: JV-Strukturchart (Logo/Investor → SPV, X %, 2 Einbringungs-Boxen) | 3-Bullet-Assetliste | 5 Bullets Gestaltungsaspekte | 5 Bullets Vorteile |
| 21 | Wie S. 17, aber Text 11 pt fett, gestrichelte Trennlinien, 1–2 Zeilen je Credential; keine Quellenzeile |
