---
name: mergermarket-briefing
description: Erstellt das wöchentliche Mergermarket-DACH-Deal-Briefing aus Mergermarket-Rohartikeln. Nutzen, wenn Artikel oder ein Mergermarket-Export zu Briefing-Einträgen verarbeitet, ein Entwurf geprüft oder ein Grenzfall (rein/raus) entschieden werden soll. Gibt die aufgenommenen Einträge einfügefertig zurück plus eine Liste der ausgeschlossenen Artikel mit Begründung.
---

# Mergermarket DACH Deal-Briefing

Wöchentlicher M&A-Rückblick über den DACH-Raum, montags per Outlook.

**Arbeitsweise:** Der Nutzer fügt Rohartikel ein. Zurück kommen zwei Blöcke:
1. die aufgenommenen Einträge im Zielformat, einfügefertig
2. darunter die ausgeschlossenen Artikel, je mit einem Satz Begründung

Nie stillschweigend aussortieren — jeder verworfene Artikel wird genannt.

**Drei Abgrenzungen, die den Arbeitsumfang bestimmen:**

- **Keine Beschaffung.** Die Artikel kommen vom Nutzer. Nicht selbst nach
  Mergermarket-Meldungen suchen, keine Quellen vorschlagen, nicht ungefragt
  tätig werden — ausschließlich auf Anfrage arbeiten.
- **Keine Recherche.** Financials, Branchen und Eigentümer stammen
  **ausschließlich aus der eingefügten Meldung**. Nie extern nachschlagen, nie
  aus Vorwissen ergänzen, nie schätzen. Nennt die Meldung keine Zahl, bleibt der
  Eintrag ohne Zahl. Der Bullet gibt wieder, was in der Meldung steht — nicht,
  was über die Firma bekannt ist.
- **Keine Zeitraumabgrenzung.** Nicht prüfen, ob ein Artikel in „die letzte
  Woche" fällt. Was eingefügt wird, wird verarbeitet. Das Datum kommt aus dem
  Artikel-Timestamp, dient aber nur der Sortierung, nie als Filter.

**Freistehende Links im Batch:** Einzeln gepastete Mergermarket-Links gehören zu
Artikeln, die als Datei angehängt wurden, weil sie zu lang sind. **Nie
ignorieren und nie als „Link ohne Artikel" abtun.** Lässt sich ein Link keinem
Artikeltext zuordnen, trotzdem einen Eintrag anlegen und als
`Quelle: unzugeordnet` markieren.

---

## 1. Aufnehmen

- **Laufende Verkaufsprozesse in jeder Phase:** Vorbereitung („bereitet Verkauf
  vor"), Start („startet Verkaufsprozess", „IMs verteilt"), Bieterrunden, finale
  Gebote, Frontrunner-Meldungen, „steht vor Übernahme".
- **Zukaufsabsichten, auch ohne konkretes Ziel:** „prüft Zukäufe", „erwägt
  Zukäufe", „zeigt sich offen für Zukäufe", „plant Zukäufe". Vage CEO-Aussagen
  zählen — die Schwelle ist bewusst niedrig.
- **IPOs:** Vorbereitung, Bankenmandate, Bewertungsindikationen, Verschiebungen,
  Wiederbelebungen.
- **Carve-outs, Spin-offs, Abspaltungen, Sparten- und Teilverkäufe,
  Minderheitsbeteiligungen.**
- **Negativ-Ereignisse in laufenden Prozessen:** Rückzug eines Bieters,
  gescheiterter Prozess, verschobener Exit. Das ist das Gegenteil eines
  Abschlusses und bleibt drin.
- **Strategische Optionsprüfungen mit externen Beratern, Kartellanmeldungen,
  Fusionsgespräche.**

Es gibt **keine Untergrenze für die Dealgröße**. Kleine Werte sind kein
Ausschlussgrund.

## 2. Ausschließen

- **Insolvenz in jeder Form** — vorläufige Insolvenzverwaltung, Eigenverwaltung,
  Schutzschirmverfahren, Nachlassstundung. Auch dann, wenn ein Investorenprozess
  läuft oder ein Käufer feststeht. Häufigster Ausschlussgrund, oft die Hälfte
  eines Batches.
- **Finanzierungen:** Startup-Runden (Pre-Seed bis Series D),
  PE-Fondsfundraising, Refinanzierungen, Debt-Pakete, Buyout-Finanzierungen für
  bereits verkündete Deals, syndizierte Kredite, TLB-Syndizierungen,
  Kreditfazilitäten. Auch Debt-for-Equity-Swaps mit Kontrollwechsel.
- **Abgeschlossene Deals.**
- **Interne Restrukturierungen ohne M&A-Bezug** (Kostenprogramme,
  Outsourcing-Prüfungen).
- **Marktkommentare, Podcasts, Personalstrategien von Banken,
  Fondsstrategie-Interviews** ohne konkretes Ziel.
- **Reine Aktien-Distribution an Altaktionäre** ohne Eigentümerwechsel.
- **Dementis und Klarstellungen** zu einem bereits gemeldeten Vorgang. Kein
  neuer Sachverhalt — auch nicht als Update.
- **Reine Berater-/Mandatsmeldungen ohne Prozessfortschritt.** Ein Bieter
  mandatiert eine Bank, aber am Prozess ändert sich nichts: keine neue Runde,
  keine neuen Zahlen → raus.
- **Nachfolgende Vorstandsempfehlungen** zu einem schon gelisteten Angebot.

**Umgekehrt:** Ein ausgeschlossener Artikel kann eine **Nebenerwähnung**
enthalten, die eigenständig aufnahmefähig ist — etwa ein separater
DACH-Verkaufsprozess, der nur beiläufig genannt wird. Solche Fälle mitnehmen und
im Nachlauf benennen.

## 3. DACH-Bezug — die schwierigste Abgrenzung

**Rein**, wenn Akteur **oder** Zielobjekt in DE/AT/CH sitzt.

**Rein** auch bei Nicht-DACH-Akteuren mit signifikanter DACH-Präsenz oder
explizitem DACH-Zielmarkt. Belegte Fälle: AMiT (CZ, Zielmarkt DE), Scandinavian
Print Group (DK, sucht in DE), Blejkan (PL, sucht in DE), Elevion (NL, Gespräche
in DE), Nortal (EE, Fokus DE), Equity House (CH, Fokus CH/DE/LU).

**Rein**, wenn die deutsche/österreichische/schweizer **Sparte einer
ausländischen Mutter** betroffen ist — das ist Aktivität im DACH-Raum,
unabhängig vom Sitz der Mutter (CSN/Stahlwerk Thüringen, Matthews/Olbrich).

**Raus**, wenn DACH nur eine Nennung unter vielen ist: Prosolia (DE einer von
fünf Solarmärkten), Invelon („Deutschland könnte sich als Zielmarkt
herausbilden"), CropX (DE einer von vier Shortlist-Ländern), Photocure und
Swedencare (Skandinavier mit Europa-Fokus).

**Raus**, wenn Akteur und Ziel beide außerhalb liegen — auch wenn ein deutscher
Bieter im Rennen ist (Acea/Indaqua, Italgas/Floene, Fintyre, ARLANXEO).

**Raus**, wenn ein DACH-Akteur **außerhalb Europas** kauft und die Meldung keine
DACH-Dimension hat (Sonova/Brasilien, Nestlé/Neuseeland). Innerhalb Europas
bleibt er drin (Kuehne+Nagel/Italien, MET Group/Spanien).

## 4. Vagheits-Schwelle

**Drin:** „prüft", „erwägt", „plant", „sucht", „offen für".

**Draußen:** explizit ablehnende Aussagen („nicht aktiv im Verkaufsprozess",
„Unabhängigkeit ist uns wichtiger"), rein hypothetische Überlegungen ohne
Zeithorizont oder Budget, Absichten mit Horizont zwei Jahre plus ohne Substanz.

## 5. Doppelmeldungen

Taucht ein Deal Wochen später mit neuem Stand wieder auf: **neuer eigenständiger
Eintrag, ohne Verweis auf die frühere Zeile.** Die Empfänger kennen den Verlauf
nicht.

Zwei Artikel zum selben Vorgang in derselben Liste: nur einmal, die belastbarere
Meldung (offizielle Mitteilung vor Gerücht).

---

## 6. Grundformat

```
TT.MM.JJ: **Akteur** (Land, Branche, Financials) Kerninhalt, Sell-side Berater: X [Quelle](URL)
```

- **Kein Aufzählungszeichen in der Antwort** — die Zeile beginnt mit der Ziffer
  des Tages. Das `•` der Arbeitsanleitung beschreibt das fertige
  Outlook-Dokument, wo der Nutzer die Aufzählung selbst setzt.
- Sortierung strikt **chronologisch absteigend**
- Kein Satzpunkt am Ende
- **Das Datum stammt immer aus dem Artikel-Timestamp**, nie aus dem Kontext
  umliegender Artikel — das ist die häufigste Fehlerquelle.
- **Quelle ist immer der Mergermarket-Link**, nie die im Artikel verlinkte
  Originalquelle (FAZ, Handelsblatt, Pressemitteilung). Muster:
  `[Quelle](https://mergermarket.ionanalytics.com/content/<ID>?)` — mit
  angehängtem `?`.

### 6.1 Wer bekommt die Klammer

Die Klammer mit Land, Branche und Financials gehört dem **grammatischen Subjekt
des Satzes**, nicht automatisch dem Zielunternehmen.

- **Investor treibt den Prozess** → er wird Subjekt und bekommt **keine**
  Klammer, das Ziel die volle:
  `**Orlando Capital** startet Verkauf von **Ludwig Pfeiffer** (DE, Infrastruktur-/Tiefbau, …)`
- **Unternehmen ist selbst Akteur** → Eigentümer steht als **letzter** Eintrag in
  der Klammer:
  `**KoRo Handels** (DE, Lebensmittel-Direktvertrieb, Umsatz: 252 Mio. EUR, **Kharis Capital**)`
- **Akteur kauft** → er bekommt die Klammer, das Ziel nur (Land, Branche):
  `**Viessmann Generations Group** steht vor Erwerb einer 5%-Beteiligung an **FC Bayern München AG** (DE, Fußballclub)`
- `via Plattform X` **nur bei Zukäufen**, nie bei Verkäufen:
  `**Bregal** erwägt via Plattform **MDT Technologies** …`
- **Akteur und verkaufte Sparte bekommen je eine eigene Klammer:**
  `**Webasto** (DE, Automobilzulieferer, Umsatz: 4 Mrd. EUR) treibt Verkauf seiner verteidigungsnahen HVAC-Sparte in Polen voran (Umsatz: 16,7 Mio. EUR, EBITDA-Marge: 40%)`
- **Mehrere Verkäufer oder Akteure** stehen als gemeinsames Satzsubjekt:
  `**CDPQ** und **Columna Capital** beleben Exit-Pläne für **Datamars** (…) wieder`
- **Staatliche und kommunale Akteure** (Bundesländer, Stadtwerke, kommunale
  Klinikträger) sind normale Akteure — sie werden fett gesetzt wie jede Firma.

### 6.2 Klammer-Inhalte

**Land:** Kürzel (DE, AT, CH, FR, IT, NL, PL, CZ, EE, DK, UK, US, BR, CN, HR,
LU). Bei Doppelsitz `DE/AT` oder `LU/DE`.

**Branche:** großgeschrieben, auch bei adjektivischen Bezeichnungen
(`Grabenlose Rohrsanierung`, `Ästhetische Medizin`). Knapp halten —
`Asset Manager` statt `Vermögensverwaltung/Konsolidierungsplattform`. Keine
Geografie, wenn das Länderkürzel sie schon trägt.

**Financials:** `Umsatz:`, `EBITDA:`, `Adj. EBITDA:`, `EBITDA-Marge:`, `EBIT:`,
`Gewinn:`, `Marktkapitalisierung:`, `Mitarbeiter:`, `Portfoliowert:`,
`Eigenkapitalwert:`, `EV-Erwartung:`, `Feuerkraft:`, `Volumen:`.
**Ohne Jahresangabe** — kein `2026e`, kein `FY25`.

`ARR:` gehört **nicht** in die Klammer, sondern in den Satz („Zielgröße bis
5-7 Mio. EUR ARR"). Ebenso `Bewertung:` und `Deal-Value:` — die stehen im Satz,
nicht in der Klammer.

**Nur aus der Meldung.** Keine externe Recherche, keine Ergänzung aus
Vorwissen, keine Schätzung. Fehlt eine Zahl in der Meldung, fehlt sie im
Eintrag — das ist kein Mangel und wird auch nicht angemerkt.

**Nur Zahlen des Klammer-Trägers.** Die häufigste inhaltliche Fehlerquelle:
Konzernzahlen suggerieren eine falsche Größenordnung für das Zielobjekt. Nennt
die Meldung nur Zahlen der Mutter, der Gruppe oder des kombinierten
Unternehmens, bleibt die Klammer des Zielobjekts schlank. Beziehen sich die
Zahlen auf die verkauften Assets, gehören sie zu den Assets — nicht zur Gruppe.

**Fallback-Hierarchie:** Umsatz/EBITDA → sonst Marktkapitalisierung → sonst
`Mitarbeiter:` als Anker. Prognose- und Run-Rate-Zahlen gelten nicht als
belastbar.

**Unbelastbare Zahlen weglassen:**
- Vom Eigentümer bestrittene Zahlen („inaccurate") → weg
- Veraltete Website-Zahlen → weg
- Unspezifisches Label → neutral übernehmen (`Gewinn:` statt EBITDA zu
  unterstellen)
- Unpräzise Angaben sinngemäß übernehmen statt eine Zahl zu erfinden
  (`Umsatz: mittlerer zweistelliger Mio.-EUR-Bereich`)
- Die Zielgröße eines Suchprofils ist **nicht** der eigene Umsatz des Akteurs

**Währung:** Originalwährung der Meldung, keine Umrechnung (CHF bleibt CHF, USD
bleibt USD).

**Zahlen:** Finanzbeträge als Ziffern mit Bindestrich (`13-15 Mio. CHF`,
`600-700 Mio. CHF`). Kleine Stückzahlen ausgeschrieben (`zehn bis zwölf
Hersteller`, `40 bis 100 Mitarbeitern`, `sechs bis zwölf Monaten`). `~` für
circa, `>` und `<` für Schwellen. Deutsches Dezimalkomma (`1,53 Mrd. EUR`).

### 6.2a Prozent- und Beteiligungsangaben

Feste Muster:
- `steht vor Erwerb einer 5%-Beteiligung an **FC Bayern München AG** (…) für 250 Mio. EUR, Bewertung: 5 Mrd. EUR`
- `meldet Erwerb von 65% an **Quabus** (…) zur Kartellprüfung an`
- `startet Verkauf seiner 50,05%-Beteiligung an **Klinikum Idar-Oberstein** (…)`
- `erwägt Rückkauf der knapp 24%-Minderheitsbeteiligung von **Sparkassen** und **Landesbanken** an der **NordLB** (…)`

Bestehende Beteiligungsquoten können in der Klammer stehen (`…, **Burda** hält
~88%`) oder im Satz (`hält nach Spin-off 51%`).

### 6.3 Berater

Am Satzende, mit Label:
- `Sell-side Berater:` bei Verkäufen
- `Buy-side Berater:` wenn die Bank einen Bieter berät
- `Global Coordinators:` bei IPOs, `Sole Global Coordinator:` im Einzelfall
- `Global-Coordinator-Kandidaten:` wenn Banken genannt, aber noch nicht
  mandatiert sind

**Nur nennen, wenn der Artikel einen nennt — nie ergänzen.** Nebenberater
weglassen. Berater werden **nie fett**.

**Gegenfall:** Sagt der Artikel ausdrücklich, dass kein Berater mandatiert ist,
kommt das in den Eintrag: `… prüft Verkauf ab Juli, ohne externen Berater`.

**Beratername:** die operative Advisory-Einheit, nie die Dachgesellschaft —
`Macquarie Capital`, nicht `Macquarie Group`; `Goldman Sachs`, nicht
`Goldman Sachs Group`. Zur Kurzform siehe Abschnitt 7.

### 6.4 Fettschrift

**Fett:** alle Unternehmens- und Akteursnamen — Käufer, Zielunternehmen,
Eigentümer, Sponsoren, Bieter, Konsortialpartner.

**Nicht fett:** Berater, Branchenbezeichnungen, Financials, Ländercodes,
Fließtext.

**Konsortien:** Partner mit Schrägstrich plus `-Konsortium`, komplett fett —
`**Astatine/USS-Konsortium**`.

**Exakter Akteursname:** Bei Holdings mit ähnlichem Markennamen wie eine
bekannte Tochter den genauen Bidder-Namen aus der
Mergermarket-Relationship-Angabe übernehmen, nicht den naheliegenderen
Markennamen — `Viessmann Generations Group`, nicht `Viessmann`.

```
08.09.26: **AUCTUS Capital Partners** treibt Verkauf von **Robert Bürkle** (DE, Oberflächenbeschichtungsmaschinen, Umsatz: 112,5 Mio. EUR) voran, Sell-side Berater: IMAP
```

### 6.5 Bieterlisten

Gebräuchlich, je nach Prozessphase — als Anhaltspunkt, nicht als Vorschrift:

- Bieterrunde erreicht → `erreicht zweite Bieterrunde mit u.a. X und Y`
- laufender Prozess → `treibt Verkauf … voran, Interessenten u.a. X`
- Gebote werden eingesammelt → `sammelt finale Gebote …, im Rennen u.a. X und Y`
- vor der Gebotsphase → `erhält Bieterinteresse vor unverbindlichen Geboten, u.a. X`

Steht das Wort „Bieter" schon im Satz, nicht wiederholen.

**Nicht stapeln:** Wenn Bieternamen genannt sind, fallen Deal-Value und
Prozessstadium („vor bindenden Geboten") weg.

- **Kein Komma vor `mit u.a.`** — `erreicht zweite Bieterrunde mit u.a. X`
- **Kein `von`** in der Bieterliste — `u.a. Chequers Capital`, nicht
  `u.a. von Chequers Capital`
- Steht ein Bieter als Satzsubjekt, braucht der Satz trotzdem ein Verb mit
  eigener Handlung. `X und Y zählen zu den Bietern für Z` weicht vom sonstigen
  Satzbau ab und wurde als Ausreißer beanstandet.

### 6.5a Verben und Wendungen

Gebräuchlich: `treibt … voran`, `prüft`, `erwägt`, `bereitet … vor`, `startet`,
`sucht Zukäufe`, `plant`, `zeigt sich offen für`, `erreicht zweite Bieterrunde`,
`steht vor`, `führt Gespräche`, `sammelt Gebote`, `mandatiert`,
`meldet … zur Kartellprüfung an`.

**Das ist ein Inventar, kein Korsett.** Die wiederkehrenden Wendungen sorgen
dafür, dass die Liste wie aus einer Feder wirkt — aber jeder Satz wird für die
jeweilige Meldung gedraftet, nicht aus Bausteinen zusammengesetzt. Passt keine
Floskel, formuliere frei.

**Verbindlich sind** die Klammerlogik (6.1), die Financials-Regeln (6.2), die
Fettung (6.4), das Kürzungsprinzip (6.6) und die Textnormen (7).
**Nicht verbindlich** ist der exakte Wortlaut des Satzes.

### 6.6 Kürzungsprinzip

Nur **wer / was / wieviel / wer berät**. Konsequent gestrichen werden:

- Motivations- und Warum-Kontext
- historischer Hintergrund („ursprünglich im Juni 2025 angekündigt", „nach
  abgesagtem Börsengang")
- Zwischentermine und Timing-Nachsätze („erste Gebote Mitte September erwartet",
  „Prozessstart im September")
- Börsensegment- und Exchange-Details
- Finanzierungsmechanik
- redundante Statuswörter („laufenden" vor „Verkaufsprozess", „im Bereich" vor
  einer Zahlenspanne)
- Stake-Prozente als eigener Nachsatz, außer die Zahl ist der zentrale
  Bewertungsfakt
- Attributionen („laut CEO", „laut Eigentümern"), **außer die Aussage der
  genannten Person ist selbst die Nachricht**
- **Keine Parenthese in der Parenthese** — `(Mitarbeiter Zielobjekt: 550+)`
  innerhalb einer Klammer fliegt raus

---

## 7. Textnormen

| Nicht so | Sondern so |
|---|---|
| `Börsengang` | `IPO` |
| `Deutschland` im Fließtext | `DE` |
| `bereinigtes EBITDA` | `Adj. EBITDA` |
| `Lincoln International` | `Lincoln` |
| `über` bei Beteiligungsketten | `via` (siehe 7.1) |
| `in Höhe von` | `i.H.v.` |
| Passiv („wird zum Verkauf geprüft") | Aktiv („prüft Verkauf") |
| `Güntner GmbH` | `Güntner` (Rechtsform weg, außer sie unterscheidet) |
| `bis 20 Mio.` | `<20 Mio.` |
| Timing als Komma-Nachsatz | Timing als Präpositionalphrase im Hauptsatz |
| beschreibende Branchenumschreibung | knapper Fachbegriff, großgeschrieben |
| `avisierte Bewertung` | `Bewertung` |
| `zwischen zehn bis fünfzig` | `zwischen zehn und fünfzig` **oder** `zehn bis fünfzig` — nie mischen |

### 7.1 `via` nur instrumental

`via` ersetzt `über` nur, wo `über` ein Mittel oder einen Weg bezeichnet
(„mittels", „durch") — und laut 6.1 nur bei Zukäufen, nie bei Verkäufen.

**Nicht ersetzen**, wenn `über` „bezüglich" oder „in Höhe von" heißt:
- `steht vor Entscheidung über Verkauf …` (bezüglich)
- `führt Gespräche über Erwerb einer Mehrheitsbeteiligung` (bezüglich)
- `Transaktionen über rund 5 Mrd. EUR` (in Höhe von)

**Test:** Lässt sich `über` durch „mittels" ersetzen, ohne dass der Satz kippt?
Dann `via`. Sonst bleibt `über`.

### 7.2 Grundhaltung

Robert kürzt in der Freigabe systematisch härter als der Entwurf. **Im Zweifel
streichen, nicht behalten.** Details, die korrekt und interessant sind, aber
nicht zum Kern gehören, fliegen raus.

Beleg: In einer 112-Einträge-Stichprobe ging keine seiner 14 Korrekturen in
Richtung „mehr Text" — ausschließlich Streichungen, Kürzungen, Umstellungen.

---

## 8. Ausgabeformat — verbindlicher Antwortvertrag

Rekonstruiert aus 36 ausgewerteten Sichtungsrunden. Details und Belege:
`research/06_antwortstruktur.md`.

Keine Begrüßung, keine Vorrede, kein Schlusssatz außerhalb der Blöcke.

### 8.0 Mailrahmen (nur beim Zusammenstellen der fertigen Mail)

Gilt **nicht** für die Sichtungsantwort — die hat keinen Vorspann. Wird die
fertige Mail gebaut, lautet der Rahmen:

```
Guten Morgen Robert,

anbei das Mergermarket Briefing der letzten Woche.

<Liste>

Viele Grüße
Nico
```

Roberts Weiterleitung an den Verteiler beginnt mit `Liebe Kollegen,` —
daran sind die beiden Fassungen auseinanderzuhalten.

### Block 1 — Einleitung

Genau eine Zeile:

```
Sichtung:
```

Nur bei auffällig großem Batch: `Sichtung – großer Batch:`

### Block 2 — Ausschlussliste (steht VOR der Aufnahmeliste)

```
**Ausgeschlossen:**

<Name> – <Begründung> → raus
<Name A>, <Name B>, <Name C> – <gemeinsame Begründung> → raus
<Name> – <Begründung> → Grenzfall, sag Bescheid
```

- **Kein Aufzählungszeichen.** Halbgeviertstrich `–` vor der Begründung, `→`
  vor dem Urteil.
- **Jeder ausgeschlossene Artikel wird namentlich genannt.** Nie „12
  Insolvenzfälle". Gleichartige Fälle in **einer** Zeile bündeln, Begründung
  einmal.
- Reihenfolge: Insolvenz/Eigenverwaltung → Refinanzierung/Debt/Fundraising →
  kein DACH-Bezug → zu vage → Grenzfälle zuletzt.
- Begründungslänge: Standardfälle **2–5 Wörter**. Mehrere Sätze nur, wenn der
  Fall an einer Regelgrenze liegt, einem Präzedenzfall widerspricht oder
  aufnahmefähig aussieht.
- Grenzfälle stehen **hier**, Default ist „draußen", markiert mit
  `→ Grenzfall, sag Bescheid`. **Ausnahme:** Sparten-, Teil- und
  Standortverkäufe kommen nach Abschnitt 1 regulär in die Aufnahmeliste und
  werden nur im Nachlauf erwähnt.
- Ist nichts auszuschließen, entfällt der Block ersatzlos.

### Block 3 — Aufnahmeliste

```
**Aufnahmefähig (N), chronologisch sortiert:**

TT.MM.JJ: <Eintrag> [Quelle](<url>)

TT.MM.JJ: <Eintrag> [Quelle](<url>)
```

- `N` ist **immer** gesetzt. Bei `N = 1`: `**Aufnahmefähig (1):**` ohne
  Sortierzusatz.
- **Kein Aufzählungszeichen vor dem Datum.** Kein `-`, kein `•`, kein `*` — die
  Zeile beginnt mit der Ziffer des Tages. Ausdrücklich so verlangt. Das `•` aus
  der Arbeitsanleitung beschreibt das fertige Outlook-Dokument, nicht die
  Antwort hier.
- **Genau eine Leerzeile** zwischen zwei Einträgen.
- Absteigend chronologisch, neuestes Datum oben.
- Alle Akteursnamen fett, Berater nie.
- **Kein Codeblock.** Die Liste steht als normaler Text, direkt kopierbar.

### Block 4 — Nachlauf (nur bei Bedarf)

Ein Fließtextabsatz, keine Überschrift. Einleitung z.B. `Kurze Anmerkung zu X:`,
`Zwei Anmerkungen:`.

**Nur diese vier Auslöser:**
1. Financials weggelassen oder unscharf übernommen → sagen *was* und *warum*,
   und anbieten, es anders zu machen. Nie stillschweigend weglassen.
2. Länderkürzel oder Branchenbezeichnung unsicher → Entscheidung offenlegen,
   Alternative anbieten.
3. Grenzfall, der eine Nutzerentscheidung braucht (sofern nicht schon in Block 2).
4. Links ohne zugeordneten Artikeltext.

**Verboten:**
- Hinweise, dass ein Deal schon früher gelistet war („Update statt Neueintrag").
  Neue Meldung = neuer eigenständiger Eintrag, ohne Verweis.
- Ausschlussquoten, Statistikblöcke, Meta-Kommentare zur eigenen Arbeitsweise.
- Ein zusammenfassender Schlusssatz.

Die Ausschlussliste und der Nachlauf sind **gewollt** — sie wurden nie als zu
lang kritisiert und dienen dem Nutzer zum Entscheiden von Grenzfällen.

### Zweiter Vertrag — Prüfmodus

Auslöser: „schau nochmal drüber", „alles richtig?"

```
Durchgesehen – <Anzahl> Punkte:

1. <Kategorie>:
<Fall> – <was ist falsch> → <Korrektur>

2. <Kategorie>:
…

<Abschlussabsatz: was geprüft und in Ordnung ist>
```

Kategorien z.B. `Tippfehler:`, `Konsistenz:`, `Berater-Label inkonsistent:`,
`Fehlende Fettung:`, `Chronologie`. Bestätigte Punkte mit `✓`.
Abschlussformel: `Ansonsten: bereit zum Verschicken.`

### Dritter Vertrag — Batch enthält nur schon Gesichtetes

```
Alles schon gesichtet – keine Änderung an der Liste:

Drin (N): <Namen> – alle mit TT.MM.JJ in der Liste

Ausgeschlossen: <Name> (<Kurzgrund>), <Name> (<Kurzgrund>)
```

### Vierter Vertrag — „sind alle Artikel abgedeckt?"

Eine Zählaussage, danach die offenen Grenzfälle einzeln:

```
Ja, alle Artikel aus diesem Briefing-Zeitraum sind abgedeckt. Die Liste umfasst
N Einträge vom TT.MM. bis TT.MM., und alles aus den Batches, die du geschickt
hast, ist entweder drin oder mit Begründung ausgeschlossen.
```

### Batchgröße

Median 5 Aufnahmen pro Runde, Maximum 11. **Nie Teilantworten, nie
Zwischenstände** — jede Runde ist in sich vollständig. Vollständigkeitssignal
ist die Pflichtzahl `N` in der Aufnahmeüberschrift.

---

## 9. Prüfliste

1. Datum aus dem **Artikel-Timestamp**, nicht aus dem Kontext?
2. Kein Insolvenz-, Finanzierungs- oder Fundraising-Fall drin?
3. Kein abgeschlossener Deal (außer Rückzug / „steht vor")?
4. DACH-Regel geprüft — auch „nur eine Nennung unter vielen" ausgeschlossen?
5. Klammer beim **grammatischen Subjekt**, nicht automatisch beim Ziel?
6. Investor als Subjekt ohne eigene Klammer, Eigentümer als letzter Klammereintrag?
7. **Gehören die Financials dem Klammer-Träger** — keine Konzern-, Gruppen- oder
   Kombinationszahlen für ein Zielobjekt?
8. Financials nur aus der Meldung, Originalwährung, deutsches Dezimalkomma,
   kein Jahres- oder Prognoselabel?
9. Unbelastbare Zahlen weggelassen (bestritten, veraltet, Zielgröße statt
   eigenem Umsatz)?
10. Textnormen aus Abschnitt 7 durchgängig?
11. `via` nur instrumental und nur bei Zukäufen?
12. Berater nur genannt, wenn im Artikel — mit korrektem Label, nicht fett?
13. **Alle** Unternehmens- und Akteursnamen fett, sonst nichts?
14. Bieterliste im richtigen Muster, nicht mit Deal-Value gestapelt?
15. Motivation, Historie, Zwischentermine, Börsensegmente, Statuswörter gestrichen?
16. Chronologisch absteigend, kein Aufzählungszeichen, eine Leerzeile je Eintrag?
17. Ausschlussliste vollständig, **vor** der Aufnahmeliste, jeder verworfene
    Artikel namentlich und begründet?
18. Pflichtzahl `N` in der Aufnahmeüberschrift gesetzt?
19. Jeder freistehende Link verarbeitet — nie als „Link ohne Artikel" abgetan?
20. Quelle ist der Mergermarket-Link mit `?`, nicht die Originalquelle?

---

## 10. Bekannte Spannungen zur Praxis

Drei Stellen, an denen die freigegebenen Zeilen von dieser Anleitung abweichen.
Zwei sind aufgelöst, die dritte ist eine bewusste Setzung. Dokumentiert, damit
niemand die Abweichungen für Regeln hält:

| Regel hier | In den freigegebenen Zeilen |
|---|---|
| Attributionen streichen | `laut Franz von Metzler` und `laut CEO Orlopp` blieben stehen — **Auflösung:** eine Attribution mit Personennamen darf bleiben, wenn sie die Aussage trägt; ein blankes „laut CEO" fliegt raus |
| Financials ohne Jahresangabe | `Umsatz H1: 176,1 Mio. CHF` (CPH Group) blieb stehen — **Auflösung:** das Verbot zielt auf Jahres- und Prognoselabels (`FY25`, `2026e`); nennt die Meldung nur eine Halbjahres- oder Quartalszahl, darf das Label mit |
| Textnormen durchgängig | 7× `Börsengang`, 4× `bereinigtes EBITDA`, 3× `Lincoln International` blieben stehen |

Die Textnormen gelten trotzdem durchgängig: Jede Korrektur des Empfängers ging in
diese Richtung, keine einzige zurück. Nur die Durchsetzung war lückenhaft.

---

## Referenzdateien

| Datei | Inhalt |
|---|---|
| `examples/musterzeilen_final.md` | 112 freigegebene Musterzeilen |
| `examples/vergleich_draft_vor_korrektur.txt` | dieselben Einträge vor der Korrektur |
| `examples/diff_tool.py` | Wort-Diff zweier Fassungen, gepaart über Content-ID |
| `research/01_aufnahme_ausschlusskriterien.md` | 27-Fall-Grenzfalltabelle, ~75 echte Rein/Raus-Beispiele |
| `research/02_format_schreibweise.md` | 58 FALSCH→RICHTIG-Paare |
| `research/03_empfaenger_praeferenzen.md` | Empfängerprofil, markiert nach Belegstärke |
| `research/04_versionsdiff_112.md` | maschineller Diff über 112 Einträge |
| `research/05_arbeitsanleitung_original.md` | Arbeitsanleitung des Absenders, verbatim — maßgebliche Quelle |
| `research/06_antwortstruktur.md` | Antwortvertrag aus 36 ausgewerteten Sichtungsrunden |
| `research/07_luecken_und_widersprueche.md` | Lückenaudit des Skills gegen das Quellmaterial |

**Wöchentliche Selbstkontrolle:** Nach dem Versand die herausgegangene Fassung
gegen den eigenen Entwurf diffen (`examples/diff_tool.py`). Jede Korrektur, die
mehrfach in dieselbe Richtung geht, gehört als neue Norm in Abschnitt 7.
