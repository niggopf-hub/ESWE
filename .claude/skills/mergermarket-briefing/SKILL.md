---
name: mergermarket-briefing
description: Erstellt das wöchentliche Mergermarket-Briefing (M&A-Wochenrückblick DACH) aus Mergermarket-Rohartikeln. Nutzen, wenn aus Mergermarket-Meldungen eine Briefing-Liste für den Montagsversand gebaut, ein bestehender Entwurf geprüft oder ein Grenzfall (rein/raus) entschieden werden soll.
---

# Mergermarket Briefing

Wöchentlicher M&A-Rückblick über den DACH-Raum, montags per Outlook. Eingang sind
Mergermarket-Rohartikel der Vorwoche, Ausgang eine Liste einzeiliger Einträge.

Typischer Umfang: 13–18 Einträge pro Woche (kumulierte Listen über mehrere Wochen
können 100+ erreichen).

Die Arbeit hat zwei Schritte: **filtern** (Abschnitt 1) und **formulieren**
(Abschnitt 2). Abschnitt 3 enthält die Präferenzen des konkreten Empfängers —
den Block bei einem Empfängerwechsel austauschen, der Rest bleibt gültig.

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
8. **DACH-Bezug?** Eines davon genügt:
   - Akteur sitzt in DE/AT/CH
   - Zielobjekt sitzt in DACH
   - Nicht-DACH-Akteur mit erklärtem DACH-Fokus oder großer DACH-Präsenz
   
   **Raus**, wenn DACH nur einer von vielen Zielmärkten ohne eigenen Prozess ist,
   oder wenn ein DACH-Akteur außerhalb DACH kauft **ohne jede DACH-Dimension**.
9. **Financials** aus der Meldung ziehen, soweit vorhanden (siehe 2.3).
10. **Datum** = Artikel-Timestamp.

**Bei Grenzfällen:** `research/01_aufnahme_ausschlusskriterien.md` enthält eine
27-Fall-Tabelle mit echten Firmenentscheidungen. Vergleiche mit dem ähnlichsten
dokumentierten Fall, statt neu zu entscheiden.

**Follow-ups** zu bereits früher gemeldeten Deals laufen als ganz normale neue
Einträge — ohne Hinweis, dass der Vorgang schon einmal in einer Liste stand.

---

## 2. Format

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

Reihenfolge in der Klammer: `(Länderkürzel, Branche, Financials…, Eigentümer)`

**Branche:** kurzer, gängiger Fachbegriff statt beschreibender Umschreibung.
Keine Geografie in der Branche, wenn das Länderkürzel sie schon trägt.

### 2.3 Zahlen

- Deutsches Format: `1,53 Mrd. EUR`, `239,9 Mio. EUR`
- Originalwährung, **nie umrechnen** (EUR, CHF, USD, BRL)
- `~` für Näherung, nicht „ca."; `<` / `>` statt „bis" / „über"
- Geldbeträge und Bereiche in Ziffern: `13-14 Mio. EUR`, `20-40 Mio. EUR`
- Zahlwörter unter zehn ausschreiben (`ein bis zwei`, `drei bis fünf`),
  ab etwa zehn Ziffern (`12-15`, `40 bis 100 Mitarbeitern`)
- Labels: `Umsatz:`, `EBITDA:`, `EBITDA-Marge:`, `EBIT:`, `Marktkapitalisierung:`,
  `Bewertung:`, `Portfoliowert:`, `Mitarbeiter:`

### 2.4 Sprache

- **Aktiv statt Passiv:** „prüft einen Verkauf", nicht „wird zum Verkauf geprüft"
- **Objekt direkt ans Verb, Nebensatz ans Ende:**
  `erwägt Zukäufe laut Franz von Metzler` — nicht `erwägt laut CEO … Zukäufe`
- **Timing als Präpositionalphrase in den Hauptsatz**, nicht kommagetrennt
  angehängt: „bereitet Verkaufsprozess **für 2027** vor"
- **`über`**, nicht „via"
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
der 112er-Stichprobe in keinem Fall gestrichen.

---

## 3. Empfänger-Präferenzen — bei Empfängerwechsel austauschen

Aktueller Empfänger: **Robert** (Vorgesetzter). Er redigiert die Zulieferung und
leitet sie an einen größeren Verteiler weiter.

### Mailrahmen

Zulieferung an Robert:
```
Guten Morgen Robert,

anbei das Mergermarket Briefing der letzten Woche.

<Einträge>

Viele Grüße
Nico
```

Roberts Weiterleitung (zur Orientierung, nicht selbst schreiben):
```
Liebe Kollegen,

nachfolgend schicke ich euch die Zusammenfassung der Mergermarket Intelligence der letzten Woche.
```

### Was belegt ist

- **Er streicht nur, er ergänzt nie.** In 6 Korrekturrunden plus einer
  112-Einträge-Stichprobe kein einziger inhaltlicher Zusatz. Im Zweifel kürzer.
- **Er greift selten ein.** 98 von 112 Einträgen gingen unverändert raus.
  Wer sauber nach Abschnitt 1 und 2 arbeitet, trifft seinen Ton.

### Was ausdrücklich KEINE Regel ist

Robert poliert beim Lesen punktuell. Diese Varianten hat er jeweils einmal
geändert und mehrfach unbeanstandet stehen lassen — beide Schreibweisen sind
zulässig, keine ist ein Fehler:

| Variante A | Variante B | Robert im Final |
|---|---|---|
| `Börsengang` | `IPO` | 7× A, 3× B |
| `bereinigtes EBITDA` | `Adj. EBITDA` | 4× A, 1× B |
| `Lincoln International` | `Lincoln` | 3× A, 1× B |
| `in Deutschland` | `in DE` | 3× A, 1× B |
| `medizinische Bildgebung` | `Ästhetische Medizin` | 6× klein, 2× groß |
| `Fokus X` | `Fokus: X` | 9× ohne, 1× mit |

**Nicht auf Einheitlichkeit korrigieren.** Ein Skill, der das erzwingt, ändert
Formulierungen, die Robert selbst mehrfach durchgewinkt hat.

Detail und Belege: `research/03_empfaenger_praeferenzen.md`,
`research/04_versionsdiff_112.md`.

---

## 4. Prüfliste vor dem Absenden

1. Jeder Eintrag durch den Filter in Abschnitt 1 gelaufen?
2. Kein Insolvenz-, Debt- oder Fundraising-Fall drin?
3. Kein abgeschlossener Deal drin (außer Rückzug/„steht vor")?
4. Klammer jeweils beim **Satzsubjekt**, nicht automatisch beim Ziel?
5. Finanzinvestor als Subjekt ohne eigene Klammer?
6. Financials im deutschen Zahlenformat, Originalwährung?
7. Aktiv statt Passiv, Objekt direkt am Verb?
8. Timing im Hauptsatz statt kommagetrennt angehängt?
9. Berater mit korrektem Label am Satzende, Nebenberater weg?
10. Motivation, Historie, Zwischen-Deadlines, Börsensegmente gestrichen?
11. Chronologisch absteigend sortiert?
12. Kein Satzpunkt, `[Quelle](URL)` als letztes Element?
13. Dubletten zum selben Vorgang zusammengeführt?
14. In Outlook: Akteursnamen fett, Berater nicht?

---

## 5. Offene Punkte — beim Onboarding klären

Diese Fragen beantwortet das ausgewertete Material nicht. Nicht raten:

- **Untergrenze der Dealgröße.** Nie festgelegt. Quarkwerk (~2 Mio. EUR Umsatz)
  wurde dreimal als Grenzfall vorgelegt und nie entschieden; gleichzeitig sind
  Hohster (12 Mio. EUR) und KRUU (4 Mio. EUR EBITDA) drin.
- **DACH-Akteur kauft außerhalb DACH.** Sonova/Brasilien raus, aber
  Kuehne+Nagel/Italien und MET Group/Spanien rein. Möglicherweise
  „Europa ja, außereuropäisch nein" — nirgends ausgesprochen.
- **Asset- vs. Sparten-Verkauf.** Lenzing/Heiligenkreuz (einzelne Anlage) raus,
  Webasto-Polen und Stadtwerke Teterow (Sparten) rein. Vermutete Trennlinie:
  abgrenzbare Geschäftseinheit mit eigenem Umsatz ja, reines Werk nein.
- **Betreffzeile** der Mail, **Deadline** am Montag, **Verteilerkreis** —
  nirgends dokumentiert.

---

## Referenzdateien

| Datei | Inhalt |
|---|---|
| `research/01_aufnahme_ausschlusskriterien.md` | 11 Aufnahme-, 12 Ausschlusskriterien, 27-Fall-Grenzfalltabelle, ~75 echte Rein/Raus-Beispiele |
| `research/02_format_schreibweise.md` | 100+ Formatregeln, 58 FALSCH→RICHTIG-Paare, 18 freigegebene Musterzeilen |
| `research/03_empfaenger_praeferenzen.md` | Empfängerprofil aus 6 Versionsvergleichen, markiert nach Belegstärke |
| `research/04_versionsdiff_112.md` | Maschineller Diff Draft→Final über 112 Einträge |

Alle Regeln in den Referenzdateien tragen Zeilenbelege aus dem Quellchat.
