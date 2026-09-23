# Brainstorm: Gemeinsamer Kern der Stadtwerke-Unterlagen und Automatisierungsplan

Stand 23.09.2026 · Grundlage: sechs Unterlagen (Duisburg 2024, Krefeld 2024, Krefeld-Update 2026,
evm vF, DVV vf, ESWE vf), drei Financial Models (evm, DVV, ESWE), Skill-Stand auf Branch
`claude/stadtwerke-ma-skill-s4g43t`, Handoff vom 23.09.2026.

Ziel dieses Papiers: den Bogen herausarbeiten, der in allen Unterlagen gleich ist, die Stellen
benennen, an denen sie voneinander abweichen, und daraus ableiten, was der Skill automatisieren
kann und was Urteil bleibt. Es ist ein Diskussionsstand, keine Skill-Fassung.

---

## 1. Bestand: Was tatsächlich vorliegt

| Fall | Datei | Datum | Design | Kapitel | Folien | Bogen |
|---|---|---|---|---|---|---|
| Stadtwerke Duisburg | `20240305_Stadtwerke Duisburg_v4 1 (1).pptx` | 05.03.2024 | blau | 3 | 21 | Engpass („Finanzierungsspielraum eng") |
| Stadtwerke Krefeld | `20240523_Krefeld_vf.pdf` (DVV-Repo) | 23.05.2024 | blau | 3 | 19 | **Stark, Wachstum** („gut aufgestellt, Net Cash") |
| Krefeld-Update | `20260722_Krefeld_Update_v3.pptx` | 22.07.2026 | blau | 3 (Kap. 1 verkürzt) | 17 | Stark, Wachstum, Fortsetzung |
| evm AG | `20260813_Metzler_evm AG_vF.pdf` | 13.08.2026 | blau | 3 | 22 | Engpass („tragfähig, aber Spielraum reduziert") |
| DVV | `20260907_Metzler DVV_vf.pptx` (DVV-Repo) | 07.09.2026 | **grün** | **2** + Diskussionsfolie | 19 | Stark, aber Programm übersteigt Spielraum |
| ESWE | `20260916_ESWE AG_vf.pdf` | 16.09.2026 | blau | 3 | 20 | Engpass („Anstieg steht bevor") |

Drei Korrekturen zum Handoff:

- **Es gibt ein fertiges ESWE-Deck.** Der Handoff kannte nur das Briefing. Die ESWE-vf vom
  16.09. ist die jüngste Unterlage und folgt in Kapitel 2 der DVV-Reihenfolge, nicht der
  Briefing-Gliederung (kein One Pager als Tabelle, keine Summary-Folie, keine sieben Ziele).
- **Die ESWE-vf ist blau und heißt „Metzler Mergers & Acquisitions"**, durchgehend: Kapiteltitel,
  Profile, Geschäftsfeld-Folie, Disclaimer. Die DVV-vf (neun Tage älter) sagt überall
  „Corporate Finance". Welche Bezeichnung ab jetzt gilt, muss festgelegt werden, weil sie auf
  sieben Folien steht.
- **Krefeld ist ein eigener Fall mit zwei Unterlagen** (2024 und Update 2026), nicht nur der
  Fremdname in der evm-Kolumne. Krefeld ist der Beleg dafür, dass der Bogen auch ohne
  Finanzierungsnot funktioniert.

Die drei Financial Models sind unterschiedlich gebaut: ESWE (Bilanz, GuV, KFR, Overview FS,
Quellen), evm (Cover, Overview, Overview FS, EVM- und ENM-Input, KPIs, Capex Revenue,
Netzinfrastruktur), DVV (Tabelle ppt, BS/PL/CF clean, Quellen & Checks). Nur die DVV-Mappe hat
ein Blatt, das genau die Folienzahlen liefert („Tabelle ppt_DVV"). Das ist das Vorbild.

---

## 2. Der gemeinsame Kern: Folie für Folie

Was in allen sechs Unterlagen steht, ist das Gerüst. Was nur in einigen steht, ist Variante
und wird als solche markiert.

### 2.1 Rahmen (in allen sechs identisch oder fast identisch)

| Baustein | Konstant | Variabel |
|---|---|---|
| Titel | „Streng vertraulich", Ort / Frankfurt, Datum | Titelformel (siehe 4.2), Adressat namentlich (Krefeld, Duisburg) |
| Agenda | drei Zeilen, Kapitel 2 heißt immer „‹X› – Übersicht und Herausforderungen" | Name Kapitel 1 und 3 |
| Kapitel 1 | Ansprechpartner (2 Profile), Haus seit 1674, vier Geschäftsfelder, Sektorfokus, Track Record, 1–2 Case Studies | Auswahl Tombstones/Case Studies; beim Update schrumpft es auf Sektorfokus + Track Record + Case Studies |
| Mehrwert Metzler | sechs Bullets, seit 2024 wortgleich | Titel („ideal positioniert…" 2024 vs. „verbindet tiefes Branchen-Know-how…" 2026) |
| Disclaimer | Standardtext | Einheitsname |

Kapitel 1 und der Mehrwert sind reine Kopie. Der Skill sollte sie als Block behandeln, der aus
der Vorlage übernommen und nur auf Aktualität geprüft wird (laufende Mandate, Titel der Personen).

### 2.2 Kapitel 2: fünf Pflichtfolien

Alle sechs Unterlagen haben dieselben fünf Inhaltsfolien. Die Reihenfolge und einzelne
Ausprägungen weichen ab.

**(a) Ausgangslage.** Kasten „Ausgangslage" mit einem Kernsatz, darunter 5–7 Bullets unter
„Unser Verständnis der Ausgangslage". Feste Bullet-Dramaturgie in allen Fassungen ab 2026:

1. Wer das Unternehmen ist (Region, Kunden, Sparten)
2. Geschäftsmodell und wo das Netz sitzt (eigene AG, Tochter, KG)
3. Ergebnisbeleg des letzten Jahres, gern mit „übertraf Plan"
4. Gesellschafter und vertragliche Bindung (EAV, Ausgleichszahlung, Querverbund)
5. Klimaziel der Kommune und Rolle in der Wärmeplanung
6. **Das bezifferte Investitionsprogramm** (600 Mio. bis 2029 / 2,5–3,5 Mrd. bis 2035 / von 22 auf 80 Mio. p. a.)
7. Die Gegenkraft: Verpflichtungen gegenüber der Stadt, ÖPNV-Fehlbetrag, Ausschüttungsbedarf

Der Kernsatz hat in allen Fällen dieselbe Form: *„Die Umsetzung/Finanzierung von ‹Programm› bei
gleichzeitig ‹Gegenkraft› ist die zentrale Herausforderung der ‹X›."* Die Gegenkraft ist der
variable Teil: „Wahrung finanzieller und strategischer Flexibilität" (evm, ESWE), „steigende
Belastung aus dem ÖPNV" (DVV), „hohe Ausschüttungen an die Stadt" (Krefeld 2024), „schwierige
makroökonomische Lage und Ausschüttungen" (Krefeld 2026).

Titelmuster seit 2026: *„Die ‹X› verbindet eine starke Versorgungs- und Infrastrukturposition mit
einem Transformationsprogramm von ‹Summe›"* (DVV, ESWE) bzw. *„Starke Markt- und Ergebnisposition
mit einem umfangreichen Investitionsprogramm…"* (evm). Immer: Stärke zuerst, Programm danach.

**(b) Beteiligungsstruktur.** Schaubild: Gesellschafter oben mit Quoten, darunter Beteiligungen
nach Geschäftsbereichen, farbcodiert. Zwei Ausprägungen: als reines Quoten-Schaubild (evm, DVV)
oder mit Kästchen je Gesellschaft (Tätigkeit, Eigenkapital, Ergebnis/Gewinnabführung: Duisburg,
Krefeld, ESWE). Fußnote immer: Stichtag der Anteilsbesitzliste, was weggelassen wurde
(Beteiligungen unter 20 %, Verwaltungsvehikel), Zuordnung der Geschäftsbereiche durch Metzler.
Titel trägt seit DVV ein Argument („mit etablierten Minderheitspartnern", „kommunal und
strategisch verankert").

**(c) Kunden und Netzinfrastruktur.** Seit 2024 stabil: zehn Kacheln mit Vorjahreswert
(Stromkunden oder -absatz, Gaskunden oder -absatz, Stromnetz km, Gasnetz km, Umsatz, EBITDA,
EBIT, EAT, CapEx, Mitarbeiter), Umsatzring mit 5–6 Erlösquellen und Erklärkästen, Legende der
sechs Geschäftsfelder (Energievertrieb & -beschaffung, Netzgeschäft, Energieerzeugung,
Energiedienstleistungen/Wärme, Telekommunikation, Wasser). Titel nennt den Anteil der
Energieverkäufe am Umsatz („~90 %", „95 %", „ca. 73 %"). Diese Folie ist vollständig mechanisch.

Zu beachten: Die Kacheln erzwingen EBITDA/EBIT/EAT auch dort, wo mit Betriebsergebnis und
Beteiligungsergebnis gesteuert wird. ESWE löst das per Fußnote („EBIT = Betriebliches Ergebnis
inklusive Beteiligungsergebnis"). Diese Definition gehört als Standard ins Modell.

**(d) Verschuldung und Investitionsbedarf.** Zwei Hälften, in allen sechs gleich gebaut:

- Tabelle „Investitionsbedarf": Zeilen Investitionsschwerpunkt / CapEx (letztes Jahr, teils
  Vorjahr in Klammern) / Geplante Projekte, 3–7 Spalten nach Segment, plus eine
  Gesamtsumme als Balken oder Kasten („Fast 600 Mio. EUR 2025–2029", „ca. 2,5–3,5 Mrd. EUR",
  „Anstieg auf bis zu 80 Mio. EUR p. a.").
- Diagramm „Entwicklung der Verschuldung": Net Debt (oder Net Cash) fünf Jahre als Säulen,
  Net Debt / EBITDA als Kreise darüber, rechts ein Kernsatz im Kasten.

Der Kernsatz-Kasten ist der Schlüsselsatz jeder Unterlage. Vier belegte Formulierungen:

| Fall | Kernsatz |
|---|---|
| evm | Die Verschuldung bleibt mit 2,6x EBITDA tragfähig, reduziert jedoch den finanziellen Spielraum für das Investitionsprogramm von fast 600 Mio. EUR |
| DVV | Mit 1,2x EBITDA ist die Verschuldung heute niedrig und bietet Spielraum, für einen Fremdmittelbedarf von 1,75–2,5 Mrd. EUR reicht dieser Spielraum jedoch nicht aus |
| ESWE | Die Nettoverschuldung ist 2025 auf das 1,7-fache des EBITDA gestiegen – moderat, doch Investitionshochlauf steht noch bevor |
| Krefeld 2026 | Trotz Abbau des Net-Cash-Puffers bleibt die Verschuldung 2025 mit 0,0x Net Debt / EBITDA sehr niedrig |

Immer derselbe Bau: *Faktor als Kompliment, dann „jedoch/doch" und der Grund, warum es trotzdem
nicht reicht.* Bei Krefeld fehlt das „jedoch", weil der Bogen dort Wachstum ist.

**Die Net-Debt-Definition driftet.** Das ist der wichtigste Befund an dieser Folie:

| Fall | Net Debt = |
|---|---|
| Duisburg 2024, evm, Krefeld | Finanzverbindlichkeiten + Pensionsrückstellungen + Verb. gg. verbundene/assoziierte − liquide Mittel − Forderungen gg. verbundene/assoziierte |
| DVV vf | Verb. gg. Kreditinstituten + Pensionsrückstellungen − liquide Mittel |
| ESWE vf | Verb. gg. Kreditinstituten − liquide Mittel |

Drei Definitionen in drei Wochen. Die Faktoren sind damit nicht vergleichbar, und ein Vorstand,
der zwei Unterlagen nebeneinanderlegt, merkt es. Der Skill braucht eine Standarddefinition mit
ausgewiesener Ausnahme (Einzelabschluss ohne Pensionen, Konzern mit Cash-Pool).

**(e) Financials.** Seit 2026 drei think-cell-Blöcke nebeneinander (GuV, Kapitalflussrechnung,
Bilanzpositionen) plus Kommentar. 2024 war es noch eine Tabelle mit EBITDA-/EBIT-/EAT-Margen.
Die drei Blöcke sind gleich, der erste Block ist es nicht:

| Fall | Block 1 | Block 2 | Block 3 |
|---|---|---|---|
| evm | Umsatz, Rohertrag, Rohertrag-Marge, CAGR | OCF/ICF/FCF, Total CF | Kassenbestand, Net Debt, EK-Quote |
| Krefeld 2026 | Umsatz, Rohertrag, Rohertrag-Marge, CAGR | dito | Kassenbestand, Net Debt/(Net Cash), EK-Quote |
| DVV | Umsatz, Rohertrag, EBITDA, Rohertrag-Marge, EBITDA-Marge | dito | Liquide Mittel, Net Debt, EK-Quote |
| ESWE | Umsatz, EBITDA, EBITDA-Marge, CAGR | dito | Liquide Mittel, Net Debt, EK-Quote |

Der Handoff hatte „Umsatz *und* Rohertrag, nicht EBITDA-Margen" festgelegt. Die fertige ESWE-vf
zeigt genau das Gegenteil. Vorschlag: DVV als Obermenge zum Standard machen (Umsatz, Rohertrag,
EBITDA, beide Margen), Rohertrag weglassen nur, wo er im Einzelabschluss nicht sauber
ableitbar ist.

Der Kommentar hat in allen drei Fällen dieselbe Rollenverteilung: Umsatz normalisiert nach
Preisspitze, Materialaufwand und Marge, Sondereffekte im Ergebnis, Cashflow-Erklärung, dann der
Schlusssatz. Der Schlusssatz wandert: bei evm steht er im Kommentar („scheint nicht aus dem
operativen Cash Flow finanzierbar"), bei ESWE in einem eigenen Kasten unter dem Kommentar
(„bereits 2025 Kapitaleinlage der Aktionäre von 10 Mio. EUR erforderlich"), bei DVV im Titel.

**Bester Beleg ist immer das Unternehmen selbst:** DVV-Lagebericht („Investitionen können bei
weitem nicht durch Abschreibungen gedeckt werden"), ESWE-Lagebericht („Stärkung der
Eigenkapitalausstattung", Kapitalerhöhung 10 Mio.), evm (Planübererfüllung). Diese Sätze gehören
gezielt gesucht und wörtlich verwendet.

### 2.3 Kapitel 2: optionale Folien

- **Strategische Stoßrichtungen** (evm, Krefeld 2026): fünf bis sechs Geschäftsfelder, je ein
  Satz in der Sprache des Lageberichts. Fehlt bei DVV und ESWE.
- **Diskussionspunkte** (nur DVV): fünf Thesen als Ersatz für Kapitel 3.

Nie gebaut, obwohl im Handoff als Pflicht geführt: **One Pager als Merkmal-Angabe-Tabelle** und
**Summary/Überleitung mit Leitfrage**. Beides stammt aus dem ESWE-Briefing und hat es in keine
Unterlage geschafft. Die Kacheln übernehmen die Steckbrief-Funktion, der Kernsatz-Kasten auf der
Verschuldungsfolie übernimmt die Überleitung.

### 2.4 Kapitel 3: drei Bausteine, davon einer Pflicht

| Baustein | Duisburg 2024 | Krefeld 2024 | Krefeld 2026 | evm | DVV | ESWE |
|---|---|---|---|---|---|---|
| Mögliche strategische Ziele (6 Kacheln) | – | ✓ „Quo vadis" | ✓ „akquisitiv werden" | ✓ | – | ✓ |
| Beteiligungsmodell / JV-Impulse (SPV-Grafik, Aspekte, Assets, Vorteile) | ✓ (3 Folien: Vorteile, Optionen, Matrix) | ✓ (Segmente) | ✓ | ✓ | – | ✓ (Beispiel sw netz) |
| Investorentypen (Strategen vs. institutionell) | ✓ | – | – | – | – | – |
| Diskussionspunkte statt Kapitel 3 | – | – | – | – | ✓ | – |
| Mehrwert Metzler | ✓ | ✓ | ✓ | ✓ | ✓ (in Kap. 2) | ✓ |

Der Kern von Kapitel 3 seit 2024 ist also: **Ziele-Kacheln → eine Strukturfolie → Mehrwert.**
Die sechs Ziele sind halb standardisiert. evm und ESWE teilen vier von sechs wortgleich
(Fremdfinanzierungsspielraum, Eigenkapitalbasis, Akquisitionen, Plattform-Erweiterung); zwei
sind fallspezifisch (evm: Risikoteilung, Kapitalfreisetzung; ESWE: kommunale Mehrheit und
Thüga-Partnerschaft erhalten, Kapital unterhalb der AG-Ebene). Die Strukturfolie zeigt bei allen
dasselbe Schema: SPV post Carve-out oder bestehende Tochter, Investor mit X %, Einbringung,
„Wesentliche Aspekte bei der Gestaltung einer Partnerschaft" (fünf Bullets, seit 2024
wortgleich), geeignete Assets, Vorteile.

Auch hier hat der Handoff etwas vorgesehen, das nie gebaut wurde: sieben nummerierte Ziele aus
dem Jahresabschluss und vier Kategorien Ansatzpunkte. Die Praxis ist knapper und visueller.

---

## 3. Die Storyline: ein Bogen, drei Tonlagen

Der Bogen ist in allen sechs derselbe: *Ihr seid stark → euer Programm ist größer als eure
Innenfinanzierung, und ein Teil des Ergebnisses ist gebunden → privates Kapital ist gestaltbar →
wir können das.* Was sich ändert, ist die Tonlage der zweiten Bewegung. Aus den Unterlagen
lassen sich drei Varianten belegen:

**A · Engpass.** Verschuldung tragfähig, Spielraum aber reduziert; Programm nicht aus dem
operativen Cashflow finanzierbar. Belege: steigendes Net Debt/EBITDA, negative Total Cashflows
bei Investitionshochlauf, Kapitalerhöhung oder EK-Ziel im Lagebericht. Fälle: evm, ESWE,
Duisburg 2024. Kernsatzform: „tragfähig, reduziert jedoch".

**B · Stark, aber.** Bilanz sehr solide (Net Cash, Sondererlös, niedrige Verschuldung), das
Programm übersteigt trotzdem den Spielraum, und eine zweite Belastung (ÖPNV, Ausschüttung)
bindet Mittel. Botschaft: *eine starke Bilanz ist der beste Zeitpunkt für einen Partner, nicht
der schlechteste.* Fall: DVV. Kernsatzform: „niedrig und bietet Spielraum, reicht jedoch nicht
für ‹Fremdmittelbedarf›".

**C · Wachstum.** Net Cash, hohe Ausschüttungen an die Stadt, keine Not. Der Bogen dreht sich:
nicht „wie finanzieren wir", sondern „wie nutzen wir die Stärke" (Akquisitionen, Plattformen,
Co-Investition). Fall: Krefeld 2024 und 2026. Kernsatzform: „sehr niedrig, Basis für
Investitionen bzw. Ausschüttungspotenzial".

Der bestehende Skill kennt die drei Befunde („Saldo negativ / nicht bestimmbar / tragfähig"),
sagt aber beim dritten nur „anderen Bogen vorschlagen". Krefeld liefert diesen Bogen fertig. Er
gehört als Variante C in den Skill, mit eigenen Ziel-Kacheln (Zukauf, Regionen, Plattformen)
statt der Finanzierungs-Kacheln.

**Was die Tonlage entscheidet, ist rechenbar:** Net Debt/EBITDA im letzten Jahr, Vorzeichen des
Total Cashflow in den letzten zwei Jahren, Verhältnis geplanter Investitionen pro Jahr zum
operativen Cashflow, und ob der Lagebericht selbst von EK-Stärkung oder Finanzierungsbedarf
spricht. Diese vier Größen kann der Skill aus Modell und Lagebericht ableiten und als
Hypothese vorlegen. Die Entscheidung bleibt beim Nutzer, aber sie ist dann eine Bestätigung,
keine Erfindung.

---

## 4. Die offenen Entscheidungen des Handoffs, mit Befund

**4.1 Kapitel 3 streichen?** Nein. Die jüngste Unterlage (ESWE, 16.09.) hat wieder ein volles
Kapitel 3. Die DVV-Diskussionsfolie ist die Kurzform für den Erstkontakt vom Typ
„Vorstellung". Vorschlag: Kapitel 3 modular mit zwei Ausbaustufen, *voll* (Ziele + Struktur +
Mehrwert) und *kurz* (Diskussionspunkte + Mehrwert). Auswahl nach Anlass.

**4.2 Titel.** Zwei Titelformeln sind belegt und beide aktuell:
- „Überlegungen zur Kapitalflexibilisierung ‹durch Einbindung privater Investoren› / ‹der X›"
  (evm, ESWE, Duisburg, Krefeld)
- „Vorstellung Metzler Corporate Finance und unser Blick auf die Herausforderungen der X" (DVV)

Die erste passt, wenn der Adressat das Thema schon kennt; die zweite beim ersten Termin. Beide
in den Skill, Auswahl nach Anlass. Dazu die Krefeld-Form „Catch-up: …" für Updates.

**4.3 Reihenfolge Kapitel 2.** DVV und ESWE stimmen überein: Ausgangslage → Beteiligungsstruktur
→ Kunden & Netz → Financials → Verschuldung & Investitionsbedarf. Das ist die neue
Regelbesetzung. Die Logik dahinter ist besser als die evm-Reihenfolge: erst die Historie
(Financials), dann der Ausblick (Investitionsbedarf), und der Kernsatz-Kasten der
Verschuldungsfolie schließt das Kapitel.

**4.4 Nicht im Handoff, aber zu entscheiden:**
- Einheitsname „Corporate Finance" oder „Mergers & Acquisitions".
- Standard-Net-Debt-Definition (Vorschlag: Krefeld/evm-Definition als Standard, weil sie den
  Cash-Pool der Konzerne abbildet; für Einzelabschlüsse ohne Konzernverrechnung reduziert sie
  sich von selbst auf Bankverbindlichkeiten plus Pensionen minus Kasse).
- Financials Block 1: DVV-Variante als Standard.
- One Pager-Tabelle, Summary-Folie, sieben Ziele, vier Ansatzpunkt-Kategorien aus dem Skill
  streichen oder als optionale Vertiefung führen.

---

## 5. Financials: aus den Jahresabschlüssen zur Folie

Der Weg ist in allen drei Modellen gleich, nur nicht gleich gebaut. Vorschlag für eine
Standard-Mappe, die jeder Fall bekommt:

**Input (ein Blatt je Rechenwerk, zeilengetreu, blau):** Bilanz, GuV, Kapitalflussrechnung,
Anlagenspiegel (Investitionen nach Segment, soweit ausgewiesen), Anteilsbesitzliste,
Absatz- und Kundenzahlen aus dem Lagebericht. Vier Abschlüsse mit Vorjahresspalte ergeben die
fünf Jahre. Ein Blatt „Vorjahresabweichungen", in dem steht, welche Fassung angesetzt wurde,
wenn der Folgeabschluss umgliedert.

**Definitionen (ein Blatt, einmal festgelegt):** Rohertrag (Umsatz + Bestandsveränderung +
aktivierte Eigenleistungen − Materialaufwand, oder nur Umsatz − Material: festlegen), EBITDA
(Betriebsergebnis + Abschreibungen, mit oder ohne Beteiligungsergebnis: festlegen), EBIT, EAT
(vor oder nach Ergebnisabführung: bei ESWE „vor Ausgleich und Abführung", das gehört als Regel
hin), CapEx (KFR-Auszahlung vs. Anlagenspiegel: DVV weicht bewusst ab), Net Debt (siehe 2.2 d),
EK-Quote (mit oder ohne Sonderposten und Minderheiten), Umsatz brutto/netto Strom- und
Gassteuer (DVV: 31 Mio. Differenz).

**Output „Tabelle ppt":** genau die Reihen, die die drei Charts, die zehn Kacheln, das
Net-Debt-Diagramm und die Investitionstabelle brauchen, in fester Zeilenordnung. Dieses Blatt
ist die Schnittstelle zur PowerPoint: think-cell wird daraus befüllt, die Kacheln per Skript.

**Checks:** Bilanzsumme, Bilanzgewinn, Cashflow-Brücke, EK-Quote gegen die im Lagebericht
genannte, Investitionssumme gegen Anlagenspiegel. Nur Übertragung prüfen, nie Definitionen
passend machen.

**Was heute noch nicht automatisiert ist und der eigentliche Engpass bleibt:** das Lesen der
Abschlüsse. Die Unternehmensregister-PDFs sind bei DVV Bild-Container mit OCR-Layer, bei ESWE
Text-PDFs. Der Skill braucht einen Extraktionsschritt, der beides kann, und danach eine
Sichtprüfung der Input-Blätter durch dich. Alles danach ist Formel.

---

## 6. Research: Jahresabschluss als Input, der Rest aus dem Netz

Was jede Folie braucht und wo es steht, aus den sechs Unterlagen rückwärts gelesen:

| Folie | Aus dem Jahresabschluss | Von außen |
|---|---|---|
| Ausgangslage | Lagebericht: Strategie, Prognose, Klimaziel, Investitionsprogramm, Planvergleich | Website, Geschäftsbericht, Ratsbeschluss Wärmeplanung, Programmbuch, Presse |
| Beteiligungsstruktur | Anhang: Anteilsbesitz nach § 285 Nr. 11 HGB mit EK und Ergebnis | Beteiligungsbericht der Stadt, Beteiligungsschema auf der Website, Handelsregister |
| Kunden & Netz | Umsatz, EBITDA, EBIT, EAT, CapEx, Mitarbeiter, Umsatzaufteilung im Anhang | Kundenzahlen, Netz-km, Absatz: Lagebericht oder Website; Netzstrukturdaten des Netzbetreibers (Pflichtveröffentlichung, jährlich) |
| Financials | alles | Nichts, außer O-Töne aus dem Geschäftsbericht |
| Verschuldung & Invest | Net Debt-Bausteine, Investitionen nach Segment, Prognosebericht | Programmbuch, Wirtschaftsplan im Ratsinformationssystem, Pressemitteilungen zu Projekten, Förderbescheide |
| Ziele Kapitel 3 | Chancen-/Risikobericht, Prognosebericht | Presse, Strategiepapiere, Aussagen des Vorstands |

Quellenhierarchie, die der Skill durchlaufen sollte, in dieser Reihenfolge und mit Abbruch,
sobald ein Beleg sitzt:

1. Jahresabschluss und Lagebericht (Unternehmensregister), Tätigkeitsabschlüsse nach EnWG
2. Geschäftsbericht und Pressemitteilungen auf der Unternehmenswebsite
3. Beteiligungsbericht der Stadt und Ratsinformationssystem (Wirtschaftsplan, Wärmeplanung,
   Kapitalmaßnahmen: hier stehen oft die Summen, die im Abschluss fehlen)
4. Netzstrukturdaten und Veröffentlichungen der Netztochter
5. Handelsregister (Organe, Kapital, Gesellschafter)
6. Fach- und Regionalpresse (ZfK, energate, Lokalzeitung) für Personalien, Projekte, Politik

Jeder Fakt bekommt Quelle und Stichtag, weil die Quellenzeile auf jeder Folie Pflicht ist.
Wo zwei Quellen abweichen (Mitarbeiterzahl im Abschluss vs. Website, evm: 500 vs. 1.000),
beide nennen und die Fußnote schreiben, wie evm es vormacht.

Was Research nicht liefert und der Skill deshalb nicht vortäuschen darf: die
Mittelfristplanung, die interne Investitionsaufteilung (evm-Fußnote: „keine öffentliche
quantitative Aufteilung verfügbar"), die politische Lage im Rat. Dafür gehören Rückfragen an
dich in den Ablauf, an den drei Stellen, die der Skill schon kennt (Tonlage, Bewertungsnarrativ,
Auswahl der Assets in Kapitel 3).

---

## 7. Automatisierungsgrad je Baustein

| Baustein | Grad | Begründung |
|---|---|---|
| Financial Model aus Abschlüssen | mechanisch, nach Sichtprüfung des Inputs | Formeln und Checks, Definitionen einmal fixiert |
| Kacheln, Umsatzring, Net-Debt-Reihe, drei Financial-Charts | mechanisch | alles aus „Tabelle ppt" |
| Beteiligungsstruktur | halb | Daten aus Anhang mechanisch, Schaubild-Layout von Hand oder aus Vorlage |
| Investitionstabelle (Projekte je Segment) | halb | Projekte per Research, Zuordnung und Auswahl Urteil |
| Ausgangslage-Bullets | halb | sieben Bullets nach festem Muster, Kernsatz nach Tonlage, Freigabe nötig |
| Kernsatz-Kästen (Verschuldung, Financials) | Vorschlag nach Tonlage, Freigabe nötig | Formeln aus 2.2 d, Zahlen aus Modell |
| Financial-Kommentar | halb | Zahlenbewegung mechanisch, Sondereffekte und Einordnung Urteil |
| Kapitel 3 Ziele | Vorschlag aus sechs Standardkacheln plus zwei fallspezifische | die zwei fallspezifischen kommen von dir |
| Kapitel 3 Strukturfolie | Vorlage, Assets und Beispielstruktur nach Rückfrage | politische Durchsetzbarkeit |
| Kapitel 1, Mehrwert, Disclaimer | Kopie mit Aktualitätsprüfung | – |
| think-cell-Diagramme | offen | programmatisch nicht befüllbar; Datenübergabe aus „Tabelle ppt" und Handarbeit, oder Template auf native Charts umstellen |

Der letzte Punkt ist die größte technische Entscheidung: Solange die Charts think-cell sind,
bleibt der Foliensatz halbautomatisch. Native PowerPoint-Charts ließen sich vollständig aus dem
Modell schreiben, sehen aber im Haus-Design anders aus, und die Vorlage müsste einmal umgebaut
werden.

---

## 8. Vorschlag für den Ablauf des Skills, neu geschnitten

1. **Eingabe:** Firmenname, Abschlüsse (4–5 Jahre), Anlass (Erstkontakt / Update), Adressat,
   Einheit (Einzel / Konzern).
2. **Modell:** Extraktion → Input-Blätter → Sichtprüfung durch dich → Output „Tabelle ppt" mit
   Checks. Zwischenstopp mit Kennzahlenübersicht.
3. **Research-Dossier:** je Folie die Belege mit Quelle, dazu eine Lückenliste (was nicht
   öffentlich ist) und eine Widerspruchsliste (zwei Quellen, eine Zahl). Zwischenstopp.
4. **Storyline-Hypothese:** Tonlage A/B/C aus den vier Kennzahlen abgeleitet, Kernsätze für
   Ausgangslage, Verschuldung und Financials als Vorschlag, Gegenhypothese dazu. **Freigabe.**
5. **Kapitel 2 füllen:** grüne Vorlage kopieren, Reihenfolge nach 4.3, in vorhandene Boxen
   schreiben, think-cell-Daten übergeben. Zwischenstopp je Folie mit Zahlenabgleich.
6. **Kapitel 3:** Ausbaustufe wählen, sechs Ziele vorschlagen, Assets für die Strukturfolie
   abfragen. Zwischenstopp.
7. **Kapitel 1 und Rahmen:** Kopie, Aktualitätsprüfung, Titel nach Anlass, Einheitsname.
8. **Prüfung:** Fremdnamen, Quellenzeilen, Fußnoten, Zahlen gegen Modell, Diagramme einzeln,
   Sichtprüfung. Übergabe mit Definitionsnotiz.

Das ist im Kern der bestehende Acht-Schritte-Ablauf; neu sind die Tonlagen-Ableitung in
Schritt 4, das Standard-Output-Blatt in Schritt 2 und das Research-Dossier als eigener
Zwischenstopp in Schritt 3.

---

## 9. Fragen an dich, bevor der Skill angepasst wird

1. Einheitsname: „Metzler Corporate Finance" (DVV) oder „Metzler Mergers & Acquisitions" (ESWE)?
2. Net Debt: eine Standarddefinition für alle Fälle, mit Fußnote bei Abweichung? Welche?
3. Financials Block 1: Umsatz + Rohertrag + EBITDA (DVV) als Standard?
4. Kapitel 3 zweistufig (voll / kurz) nach Anlass, oder immer voll?
5. One Pager-Tabelle, Summary-Folie, sieben Ziele, vier Ansatzpunkt-Kategorien: streichen?
6. think-cell behalten (halbautomatisch) oder Vorlage auf native Charts umbauen (vollautomatisch)?
7. Ist der Krefeld-Bogen (Wachstum, Variante C) ein Fall, der wiederkommt, oder ein Einzelfall?
