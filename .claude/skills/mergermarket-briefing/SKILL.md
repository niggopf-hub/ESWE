---
name: mergermarket-briefing
description: Erstellt das wöchentliche Mergermarket-Briefing (M&A-Wochenrückblick DACH) aus Mergermarket-Rohartikeln. Nutzen, wenn aus Mergermarket-Meldungen eine Briefing-Liste für den Montagsversand gebaut, ein bestehender Entwurf geprüft oder ein Grenzfall (rein/raus) entschieden werden soll.
---

# Mergermarket Briefing

Wöchentlicher M&A-Rückblick über den DACH-Raum, montags per Outlook. Eingang sind
Mergermarket-Rohartikel der Vorwoche, Ausgang eine einfügefertige Liste
einzeiliger Einträge.

Typischer Umfang: 13–18 Einträge pro Woche.

Drei Schritte: **filtern** (1), **formulieren** (2), **Textnormen anwenden** (3).
Abschnitt 4 beschreibt das Ausgabeformat.

---

## 1. Filter: Was kommt rein?

Jeden Artikel stur durch diese Reihenfolge schicken. Das erste zutreffende
Ausschlusskriterium beendet die Prüfung.

1. **Dublette?** Vorgang schon in dieser Liste → raus. Bei zwei Artikeln zum
   selben Vorgang die belastbarere Meldung nehmen (offizielle Mitteilung vor
   Gerücht).
2. **Insolvenz, Self-Administration, Schutzschirmverfahren?** → **raus.**
   Härtestes Kriterium, über 70 dokumentierte Fälle, keine Ausnahme. Gilt auch,
   wenn ein Investorenprozess läuft oder ein Käufer feststeht.
3. **Reines Debt-/Refinanzierungsthema?** → raus. Auch Debt-for-Equity-Swaps mit
   Kontrollwechsel und Kartellanmeldung.
4. **Startup-Finanzierungsrunde** (Seed, Series A/B/C)? → raus.
5. **M&A-Substanz?** Verkauf, Übernahme, Bolt-on, Beteiligung, Carve-out,
   Spin-off mit Listing/Verkaufsoption, IPO → weiter. Reine Aktien-Distribution
   an Altaktionäre ohne Eigentümerwechsel → raus.
6. **Abgeschlossen/vollzogen?** → raus. **Ausnahmen, die drinbleiben:**
   - Rückzug, Abbruch, Verschiebung eines Deals (das Gegenteil eines Abschlusses)
   - „steht vor Übernahme" / „set to acquire" — Signing steht noch aus
   - laufende Annahmefrist eines formellen Übernahmeangebots
7. **Konkret genug?** Die Latte liegt bewusst **niedrig**: „prüft Zukäufe",
   „erwägt", „zeigt sich offen für" reicht — ohne Zielobjekt, ohne Berater, ohne
   Zahl. **Raus** nur bei rein ablehnendem Grundton ohne Zukaufsdimension
   („aktuell keine Akquisitionen geplant").
8. **DACH-Bezug?** → siehe 1.1.
9. **Financials** aus der Meldung ziehen, soweit vorhanden (siehe 2.3).
10. **Datum** = Artikel-Timestamp.

**Es gibt keine Untergrenze für die Dealgröße.** Kleine Werte sind kein
Ausschlussgrund — Hohster Energy (12 Mio. EUR Umsatz) und KRUU (4 Mio. EUR
EBITDA) sind regulär gelaufen.

### 1.1 DACH-Bezug

**Rein**, wenn eines davon zutrifft:

- Akteur sitzt in DE, AT oder CH
- Zielobjekt sitzt in DACH
- **Deutsche/österreichische/schweizer Sparte einer ausländischen Mutter** ist
  betroffen — das ist Aktivität im DACH-Raum, unabhängig vom Sitz der Mutter
  (Matthews/Olbrich, CSN/Stahlwerk Thüringen: beide rein)
- **DACH ist Teilmarkt** einer breiteren Zukaufsstrategie — auch wenn daneben
  andere Länder genannt werden (Nortal, Isto Biologics, Access Hospitality)

**Raus**, wenn ein DACH-Akteur **außerhalb Europas** kauft und die Meldung keine
DACH-Dimension hat (Sonova/Brasilien, Nestlé/Neuseeland).

**Merksatz: Europa ja, außereuropäisch nein.** Ein DACH-Akteur, der innerhalb
Europas zukauft, bleibt drin (Kuehne+Nagel/Italien, MET Group/Spanien) — auch
ohne DACH-Zielobjekt.

### 1.2 Teil- und Spartenverkäufe

**Tendenziell immer erst aufnehmen**, nicht vorab aussortieren: Spartenverkäufe,
Carve-outs, Standortverkäufe, Portfolio-Teilverkäufe, Minderheitsbeteiligungen.

Den Eintrag anschließend **unter der Liste flaggen** (siehe 4.2), damit die
Entscheidung beim Absender liegt statt beim Skill.

### 1.3 Follow-ups

Follow-ups zu bereits früher gemeldeten Deals laufen als ganz normale neue
Einträge — ohne Hinweis, dass der Vorgang schon einmal in einer Liste stand.

**Bei Grenzfällen:** `research/01_aufnahme_ausschlusskriterien.md` enthält eine
27-Fall-Tabelle mit echten Firmenentscheidungen. Mit dem ähnlichsten
dokumentierten Fall vergleichen, statt neu zu entscheiden.

---

## 2. Aufbau des Eintrags

### 2.1 Template

```
* TT.MM.JJ: <Akteur> (<LK>, <Branche>[, <Financials>][, <Eigentümer>]) <Verb> <Objekt>[ (<LK>, <Branche>)][, <Zusatz>][, Sell-side Berater: <X>] [Quelle](<URL>)
```

- Kein Satzpunkt am Ende.
- Sortierung: **chronologisch absteigend**, neuester Tag oben. Innerhalb eines
  Tages keine feste Konvention.
- Keine Überschriften, keine Gruppierung, keine Einleitung, kein Wochenfazit.
- Keine Fettung im Text — Akteursnamen werden manuell in Outlook fett gesetzt,
  Berater **nie**.

### 2.2 Die Klammer — wichtigste Regel

**Die Klammer gehört dem Satzsubjekt, nicht automatisch dem Zielobjekt.**

- Handelt eine operative Firma selbst → sie bekommt die volle Klammer.
- Treibt ein Finanzinvestor den Prozess → **er wird Satzsubjekt und bekommt
  keine Klammer**; die Klammer hängt am Portfoliounternehmen.
  → `IK Partners treibt Verkauf von Ondal Medical Systems (DE, Medizintechnik, …) voran`
- Operativer Käufer **und** operatives Ziel → zwei Klammern. Der Akteur bekommt
  die Financials, das Ziel nur (Land, Branche) — außer das Ziel trägt die
  relevante Zahl.
- Eigentümer/Sponsor steht **zuletzt** in der Klammer, wenn er nur Kontext ist:
  `(DE, RegTech-Software, Umsatz: 50 Mio. EUR, Levine Leichtman Capital Partners)`
- Konkrete Stake-Zahlen gehören trotzdem in den Satz.

Reihenfolge: `(Länderkürzel, Branche, Financials…, Eigentümer)`

**Branche:** kurzer, gängiger Fachbegriff statt beschreibender Umschreibung.
Keine Geografie in der Branche, wenn das Länderkürzel sie schon trägt.
→ `Vermögensverwaltung/Konsolidierungsplattform` wird `Asset Manager`
→ `Wohnimmobilien Deutschland` wird `Wohnimmobilien`

### 2.3 Zahlen

- Deutsches Format: `1,53 Mrd. EUR`, `239,9 Mio. EUR`
- Originalwährung, **nie umrechnen** (EUR, CHF, USD, BRL)
- `~` für Näherung, nicht „ca."; `<` / `>` statt „bis" / „über"
- Geldbeträge und Bereiche in Ziffern: `13-14 Mio. EUR`, `20-40 Mio. EUR`
- Zahlwörter unter zehn ausschreiben (`ein bis zwei`, `drei bis fünf`),
  ab zehn Ziffern (`12-15`, `40 bis 100 Mitarbeitern`)
- Labels: `Umsatz:`, `Adj. EBITDA:`, `EBITDA-Marge:`, `EBIT:`,
  `Marktkapitalisierung:`, `Bewertung:`, `Portfoliowert:`, `Mitarbeiter:`

### 2.4 Satzbau

- **Aktiv statt Passiv:** „prüft einen Verkauf", nicht „wird zum Verkauf geprüft"
- **Objekt direkt ans Verb, Nebensatz ans Ende:**
  `erwägt Zukäufe laut Franz von Metzler` — nicht `erwägt laut CEO … Zukäufe`
- **Timing als Präpositionalphrase in den Hauptsatz**, nicht kommagetrennt
  angehängt: „bereitet Verkaufsprozess **für 2027** vor"
- Gängige Verben: `treibt … voran`, `prüft`, `erwägt`, `bereitet … vor`,
  `startet`, `sucht Zukäufe`, `plant`, `zeigt sich offen für`,
  `erreicht zweite Bieterrunde`, `steht vor`

### 2.5 Berater

Immer am Satzende mit Label:
`Sell-side Berater:` · `Buy-side Berater:` · `Global Coordinators:` ·
`Sole Global Coordinator:` (letztere bei IPOs)

Mehrere: Komma, letztes Paar mit „und". Nebenberater weglassen — nur den
führenden Berater nennen. Nennt die Meldung keinen Berater, entfällt das Feld.

### 2.6 Kürzen — was grundsätzlich rausfliegt

- Motivation und Zusatzkontext („organisches Wachstum bleibt Priorität")
- Historische Hintergrundinfo („ursprünglich im Juni 2025 angekündigt")
- Zwischen-Deadlines („bis 15. Juli")
- Börsensegment-Details („am Frankfurter Scale-Segment")
- Detaillierte Finanzierungsmechanik, wenn nicht zentral
- Füllwörter („für das September/Oktober-**Fenster**")

**Faustregel:** Alles, was *wie* oder *warum* im Detail beschreibt statt
*wer / was / wie viel*, kommt raus.

**Attributionen bleiben.** „laut CEO Orlopp", „laut Franz von Metzler" wurden in
der 112er-Stichprobe in keinem Fall gestrichen — nur umgestellt (Objekt ans Verb).

---

## 3. Textnormen — verbindlich

So soll der Text aussehen. Diese Normen gelten durchgängig, auch rückwirkend bei
der Überarbeitung älterer Zeilen.

| Norm | Nicht so | Sondern so |
|---|---|---|
| Anglizismus beim Listing | `Börsengang`, `Börsengangspläne` | `IPO` |
| EBITDA-Label | `bereinigtes EBITDA` | `Adj. EBITDA` |
| Beraternamen kurz | `Lincoln International`, `Macquarie Capital`, `Bregal Unternehmerkapital` | `Lincoln`, `Macquarie`, `Bregal` |
| Beteiligungsketten (nur instrumental, siehe 3.1) | `über Plattform X` | `via Plattform X` |
| Länderangabe im Fließtext | `Betriebe in Deutschland` | `Betriebe in DE` |
| Branche, erstes Wort | `grabenlose Rohrsanierung` | `Grabenlose Rohrsanierung` |
| Branche knapp | beschreibende Umschreibung | gängiger Fachbegriff |
| Füllwörter | `für das Q3-Fenster` | `für Q3` |

**Herkunft und Geltung:** Diese Normen stammen aus den Korrekturen des
Empfängers. Er selbst wendet sie punktuell an — im 112er-Vergleich stehen z.B.
noch 7× `Börsengang` und 4× `bereinigtes EBITDA` unkorrigiert. Entscheidend ist:
**jede seiner Korrekturen ging in diese Richtung, keine einzige zurück.** Die
Normen sind deshalb hier bewusst durchgängig gesetzt, auch wo er selbst
inkonsistent war. Die Liste wird dadurch einheitlicher als seine eigene Fassung
— das ist gewollt.

### 3.1 `via` nur instrumental — wichtige Einschränkung

`via` ersetzt `über` **nur dort, wo `über` ein Mittel oder einen Weg bezeichnet**
(im Sinne von „mittels", „durch"):

- `baut über neue Plattform TerraBrix …` → `baut via neue Plattform TerraBrix …`
- `plant Aufbau einer Kette über Zukäufe` → `… via Zukäufe`

**Nicht ersetzen**, wenn `über` „bezüglich" oder „in Höhe von" heißt. Dort ergibt
`via` keinen sinnvollen Satz:

- `steht vor Entscheidung über Verkauf …` (bezüglich)
- `führt Gespräche über Erwerb einer Mehrheitsbeteiligung` (bezüglich)
- `Transaktionen über rund 5 Mrd. EUR` (in Höhe von)

**Test:** Lässt sich `über` durch „mittels" ersetzen, ohne dass der Satz kippt?
Dann `via`. Sonst bleibt `über` stehen. In der 112er-Stichprobe trifft das auf
2 von 8 Vorkommen zu.

**Nicht übernehmen:** `Essenslieferplattform` → `Essenlieferplattform` ist ein
Tippfehler des Empfängers (Fugen-s), kein Hausstil. `Fokus:` mit Doppelpunkt kam
einmal in zehn Fällen vor und bleibt ohne Doppelpunkt.

---

## 4. Ausgabeformat

### 4.1 Die Liste

Reiner Text, direkt in Outlook einfügbar. Exakt im Format der
`examples/musterzeilen_final.md` — ein Eintrag pro Zeile, keine Leerzeile
dazwischen, keine Markdown-Fettung, `[Quelle](URL)` als letztes Element.

Kein Vorspann, keine Erklärungen, keine Zwischenüberschriften innerhalb der
Liste. Was oberhalb oder unterhalb steht, darf nicht versehentlich mitkopiert
werden — deshalb klar abgesetzt.

Mailrahmen für die Zulieferung:
```
Guten Morgen Robert,

anbei das Mergermarket Briefing der letzten Woche.

<Liste>

Viele Grüße
Nico
```

### 4.2 Flag-Block unter der Liste

Nach der Liste, deutlich abgesetzt, kurz auflisten:

- **Teil-/Spartenverkäufe**, die nach 1.2 aufgenommen wurden — einzeilig mit
  Begründung, damit vor dem Absenden entschieden werden kann
- **Grenzfälle beim DACH-Bezug**, wenn die Zuordnung nicht eindeutig war
- **Fehlende Financials**, wenn die Meldung keine Zahlen hergab
- **Artikel, die ausgeschlossen wurden**, falls die Entscheidung knapp war —
  mit dem Kriterium, an dem sie gescheitert sind

Format:
```
--- nicht mitkopieren ---

Zum Prüfen:
- Webasto (19.08.): Verkauf einer einzelnen Sparte in Polen — nach 1.2 aufgenommen
- Sonova (18.09.): DACH-Akteur, Ziel Brasilien — nach 1.1 ausgeschlossen
```

---

## 5. Prüfliste vor dem Absenden

1. Jeder Eintrag durch den Filter in Abschnitt 1 gelaufen?
2. Kein Insolvenz-, Debt- oder Fundraising-Fall drin?
3. Kein abgeschlossener Deal drin (außer Rückzug / „steht vor")?
4. DACH-Regel angewandt — Europa ja, außereuropäisch nein?
5. Klammer jeweils beim **Satzsubjekt**, nicht automatisch beim Ziel?
6. Finanzinvestor als Subjekt ohne eigene Klammer?
7. Financials im deutschen Zahlenformat, Originalwährung?
8. Textnormen aus Abschnitt 3 durchgängig? (`IPO`, `Adj. EBITDA`,
   Beraternamen kurz, Branche groß)
9. `via` nur gesetzt, wo „mittels" passt — nicht bei `über` im Sinne von
   „bezüglich" oder „in Höhe von"?
10. Aktiv statt Passiv, Objekt direkt am Verb, Timing im Hauptsatz?
11. Berater mit korrektem Label am Satzende, Nebenberater weg?
12. Motivation, Historie, Zwischen-Deadlines, Börsensegmente gestrichen?
13. Chronologisch absteigend sortiert?
14. Kein Satzpunkt, `[Quelle](URL)` als letztes Element?
15. Dubletten zum selben Vorgang zusammengeführt?
16. Flag-Block unter der Liste gesetzt und klar abgesetzt?
17. In Outlook: Akteursnamen fett, Berater nicht?

---

## 6. Offen — beim Onboarding klären

Nicht raten, nachfragen: **Betreffzeile** der Mail, **Uhrzeit/Deadline** am
Montag, **Verteilerkreis** der Weiterleitung. Steht nirgends im Material.

---

## Referenzdateien

| Datei | Inhalt |
|---|---|
| `examples/musterzeilen_final.md` | 112 freigegebene Musterzeilen — maßgeblich für Ton und Aufbau |
| `examples/vergleich_draft_vor_korrektur.txt` | Dieselben Einträge vor der Korrektur |
| `examples/diff_tool.py` | Wort-Diff zweier Fassungen, gepaart über Content-ID |
| `research/01_aufnahme_ausschlusskriterien.md` | 11 Aufnahme-, 12 Ausschlusskriterien, 27-Fall-Grenzfalltabelle, ~75 echte Rein/Raus-Beispiele |
| `research/02_format_schreibweise.md` | 100+ Formatregeln, 58 FALSCH→RICHTIG-Paare |
| `research/03_empfaenger_praeferenzen.md` | Empfängerprofil aus 6 Versionsvergleichen, markiert nach Belegstärke |
| `research/04_versionsdiff_112.md` | Maschineller Diff über 112 Einträge |

Alle Regeln in den Referenzdateien tragen Zeilenbelege aus dem Quellchat.

**Wöchentliche Selbstkontrolle:** Nach dem Versand die herausgegangene Fassung
gegen den eigenen Entwurf diffen (`examples/diff_tool.py`). Jede Korrektur, die
mehrfach in dieselbe Richtung geht, gehört als neue Norm in Abschnitt 3.
