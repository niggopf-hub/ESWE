# Antwortstruktur des Assistenten bei Rohartikel-Batches

Quelle: `briefing_utf8.txt` (8086 Zeilen). Alle Zeilennummern beziehen sich auf diese Datei.
Ausgewertet: 36 vollständige Sichtungsrunden (Z. 253 bis Z. 7963) plus alle Korrektur-/Nachfassrunden.

**Vorbemerkung zur Quelle:** Der Export ist reiner Text, Markdown-Auszeichnung wurde beim Export
gestrippt. `grep -c '\*\*'` = **0**, `grep -c '```'` = **0**. Das heißt: Fettung und Link-Syntax sind
im Transkript nicht direkt sichtbar, ihre Existenz ist aber über die Gesprächsebene belegt
(Z. 3117–3126, siehe Abschnitt 6). Umgekehrt ist damit **sicher belegt, dass NIE ein Codeblock
verwendet wurde** — Codeblock-Marker würden im Export überleben, sie kommen kein einziges Mal vor.

---

## 1. GESAMTANATOMIE DER ANTWORT

### Die stabile Blockreihenfolge (ab ca. Z. 845 unverändert bis zum Ende)

```
[1] Einleitungszeile  ("Sichtung:")
[2] Überschrift       "Ausgeschlossen:"           (ggf. mit Grund-Suffix und/oder Anzahl)
[3] Ausschlussliste   (eine Zeile je Fall, Fließtext-Bulletform ohne Zeichen)
[4] Überschrift       "Aufnahmefähig (N), chronologisch sortiert:"
[5] Eintragsliste     (N Einträge, leerzeilengetrennt, absteigend chronologisch)
[6] Nachlauf          (optional: "Kurze Anmerkung zu X:" / "Kurzer Hinweis zu X:" / Rückfrage)
```

Keine Überschrift ist je mit `#` oder `##` gesetzt. Es sind **fettgesetzte Absatzlabels mit
Doppelpunkt**, gefolgt von einer Leerzeile und dann den Zeilen. Kein Codeblock, keine Tabelle.

### Reihenfolge ist invariant: Ausschluss VOR Aufnahme

In **allen 34 Runden mit beiden Blöcken** steht "Ausgeschlossen" vor "Aufnahmefähig". Kein
einziger Gegenbeleg. Belege (Zeilenpaare Ausgeschlossen → Aufnahmefähig):
255→263, 487→494, 846→854, 1214→1237, 1316→1321, 1656→1662, 1841→1849, 2073→2085,
2391→2397, 2676→2683, 2992→3005, 3440→3446, 3629→3634, 3864→3874, 4125→4131, 4419→4427,
4531→4534, 4937→4941, 5071→5075, 5247→5251, 5346→5349, 5491→5495, 5643→5646, 5759→5764,
5914→5918, 6323→6328, 6406→6412, 6521→6526, 6696→6701, 6852→6860, 7190→7199, 7328→7331,
7505→7512, 7958→7963.

### [1] Der Einleitungssatz — wörtlich, mit Entwicklung

Frühe Runden, ausführlich:
- Z. 253: `Hier die Sichtung der neuen Artikel nach deinen Kriterien:`
- Z. 844: `Hier die Sichtung der neuen Artikel, sortiert nach deinen Kriterien:`
- Z. 485, 1654, 1839, 2071, 2389, 2674, 2990, 3438, 3627: `Sichtung der neuen Artikel:`
- Z. 1212: `Sichtung der großen Artikel-Batch – aufgeteilt nach Kategorie:`
- Z. 3862: `Sichtung der neuen Artikel – großer Batch, hier die Aufteilung:`
- Z. 4123: `Sichtung des neuen Batches:`
- Z. 4417: `Sichtung des großen Batches:`

Späte Runden, minimal — **ab Z. 4529 dominiert das blanke Einwortlabel**:
- Z. 1314, 4529, 4935, 5069, 5245, 5344, 5489, 5757, 5912, 6321, 6404, 6519, 6694, 6850,
  7326, 7503, 7956: `Sichtung:`
- Nur zwei späte Ausreißer mit Zusatz: Z. 5641 `Sichtung – guter Batch, viel Relevantes dabei:`
  und Z. 7188 `Sichtung – großer Batch:`

**Entwicklung:** Der Einleitungssatz schrumpft von einem vollständigen Satz ("Hier die Sichtung
der neuen Artikel nach deinen Kriterien:") über "Sichtung der neuen Artikel:" auf das nackte
"Sichtung:". Ab Z. 4529 ist "Sichtung:" die klare Norm (17 von 19 späten Runden).
Es gibt **keinen Begrüßungssatz, kein "Gerne", kein "Ich habe mir die Artikel angesehen"**.

### [4] Die Aufnahme-Überschrift — wörtlich

Das Standardlabel ist ab Z. 1237 durchgehend:
```
Aufnahmefähig (N), chronologisch sortiert:
```
Belegt in 26 Runden (Z. 1662, 1849, 2085, 2397, 2683, 3005, 3446, 3634, 3874, 4131, 4427,
4534, 4941, 5075, 5251, 5495, 5646, 5764, 5918, 6328, 6412, 6526, 6701, 6860, 7199, 7331,
7512, 7963).

Frühere/abweichende Varianten:
- Z. 263: `Aufnahmefähig (2):`  (ohne Sortierzusatz)
- Z. 494: `Aufnahmefähig (1):`
- Z. 854: `Aufnahmefähig (7), einfügefertig, chronologisch sortiert:`  (mit "einfügefertig")
- Z. 1237: `Aufnahmefähig (7 neue Einträge), chronologisch sortiert:`
- Z. 1321, 5349: `Aufnahmefähig (1):`  (bei Einzeltreffer wird der Sortierzusatz weggelassen)

**Merke:** Die Klammerzahl ist **immer** gesetzt — in allen 34 Fällen. Der Zusatz
", chronologisch sortiert" entfällt nur, wenn N = 1 (Z. 494, 1321, 5349).

Sonderüberschriften für Einzeleinträge (wenn nur ein Artikel kam, kein Batch):
- Z. 5: `Neuer Eintrag (einfügefertig)`
- Z. 498, 1325: `Neuer Eintrag (einfügefertig):`
- Z. 269: `Neue Einträge (einfügefertig, oben in die Liste vor 09.07.26):`
- Z. 660: `Neue Einträge (einfügefertig, oben in die Liste vor 10.07.26):`
- Z. 311: `Finale Liste (chronologisch absteigend, einfügefertig):`
- Z. 3158 (Nachtrag nach Korrektur): `Nachträglicher Eintrag:`

### Zusatzblöcke, die fallweise zwischen [3] und [4] auftreten

- Z. 1231: `Grenzfall, nicht automatisch aufgenommen:`
- Z. 3001: `Grenzfälle, nicht aufgenommen:`
- Z. 852: `Sonderfall – nicht als eigener Eintrag, sondern Hinweis:`
- Z. 1234: `Update statt Neueintrag:`
- Z. 6185: `Bereits im versendeten Briefing:` (bei Wiederholungs-Batches)
- Z. 7680: `Drin:` (Kurzform desselben, bei reinen Dubletten-Batches)

### Ausgabeform

**Fließtext/Markdown, nie Codeblock.** Belegt durch `grep -c '```'` = 0 über die gesamte Datei.
Der Nutzer kopiert die Einträge direkt aus dem Fließtext heraus in sein Dokument — das belegen
die Stellen, wo er die Liste mit seinen eigenen Aufzählungszeichen (`•` + Tab) zurückpastet,
z. B. Z. 5352–5368. Das Wort "einfügefertig" (Z. 5, 269, 277, 311, 498, 854, 1325) ist der
Vertrag: Der Text muss **so** kopierbar sein, ohne Nachbearbeitung.

---

## 2. DIE EINTRAGSLISTE SELBST

### Aufzählungszeichen: KEINES — und das ist eine explizite Nutzerentscheidung

Messung über die ganze Datei:
- Einträge mit Bindestrich-Präfix (`- TT.MM.JJ:`): **18 Stück**, ausschließlich in
  Z. 271, 272, 279, 280, 281, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325.
- Einträge ohne Präfix (`TT.MM.JJ:` am Zeilenanfang): **491 Stück**.

Der Umschlagpunkt ist exakt die Nutzeranweisung in **Z. 328**:
> `bitte schick nochmal so gut geordnet aber ohne den bindestrich am anfang`

**Danach kommt kein einziger Bindestrich-Eintrag mehr vor.** Die letzten Dash-Einträge stehen in
Z. 325, die Anweisung in Z. 328 — ab Z. 330 bis Z. 8086 durchgehend präfixlos. Das ist der
härteste und am klarsten belegte Formatbefund des ganzen Dokuments.

Die `•`-Zeichen im Dokument (48 Treffer) stammen **nicht vom Assistenten**, sondern aus den
Passagen, in denen der **Nutzer seine eigene Dokumentversion zurückpastet** (z. B. Z. 5352–5368,
Z. 231–245). Dort steht `•` + Tabulator — das ist die Formatierung seines Zieldokuments, nicht
die des Chat-Outputs. Der Assistent liefert roh, der Nutzer bebullet't beim Einfügen.

### Fettung

Im Export nicht sichtbar (0× `**`), aber über die Gesprächsebene eindeutig belegt.
Z. 3117 (Nutzer):
> `sind jetzt auch alle namen fett das muss immer sein, außer den sell side oder gloinbal corrdiantor`

Z. 3119–3121 (Assistent):
> `Ja, guter Fang – das ist konsistent: In dieser Version sind alle Firmennamen/Akteure fett
> (Bregal Unternehmerkapital, MDT Technologies, Güntner, PMB Capital, Orlando Capital, ...) –
> nur die Berater (Alantra, Houlihan Lokey, BofA, Deutsche Bank, Goldman Sachs, Societe Generale,
> Belgravia, Pava Partners, Morgan Stanley) bleiben unformatiert.`
> `Ich speichere das als festes Formatierungsmerkmal.`

Z. 3126:
> `Gespeichert. Ab jetzt formatiere ich alle Akteursnamen (Käufer, Ziel, Eigentümer/Sponsor)
> automatisch fett, während Berater unformatiert bleiben.`

Bestätigung im späteren Selbstcheck, Z. 5399–5401:
> `Ja, vom Format her passt alles – ich hab jede Zeile gegen die Regel geprüft (alle Akteursnamen
> fett: Käufer, Ziel, Eigentümer/Sponsor; Berater nie fett):`
> `CLSA, JPMorgan/Morgan Stanley, Rothschild, Carlsquare, ... – korrekt unformatiert ✓`

Und Z. 5947:
> `Sonst passt alles – Fettung bei Akteuren durchgängig, Financials-Klammern korrekt zugeordnet,
> keine Ausschlussfälle drin.`

**Entwicklung:** Die Fettungsregel entsteht in Z. 3117 und gilt ab da. Vor Z. 3117 gibt es keine
Belegstelle für systematische Fettung.

### Leerzeilen zwischen Einträgen

**Ja — je eine Leerzeile.** Sichtbar in jeder Aufnahmeliste ab Z. 856. Beispiel Z. 856–870:
jeder Eintrag steht auf einer eigenen Zeile, dazwischen eine Leerzeile. Ausnahme: die
allerfrühesten Dash-Listen (Z. 271–281, Z. 313–325) sind dicht ohne Leerzeilen. Der Nutzer
verlangt in Z. 328 "so gut geordnet aber ohne den bindestrich" — ab der Antwort darauf
(Z. 330 ff.) stehen die Einträge leerzeilengetrennt.

### Quellenfeld

Jeder Eintrag endet mit dem Wort `Quelle` — als Link gesetzt. Zwei Erscheinungsformen im Export:
- `[Quelle]` (Platzhalter, wenn dem Assistenten kein Link vorlag) — z. B. Z. 856–870, Z. 3446 ff.
- `Quelle` (als echter Hyperlink gesetzt, Markup gestrippt) — ab Z. 6330 ff., nachdem der Nutzer
  begonnen hatte, Mergermarket-Links mitzuschicken.

Z. 6190 (Assistent) hält den Vertrag fest:
> `Das Link-Format funktioniert so, wie du es brauchst. Schick beim nächsten Batch einfach Artikel
> plus Link, dann baue ich die Einträge direkt fertig verlinkt.`

Sonderfall bei nicht zuordenbarem Link, Z. 7236 (Assistent, nach Nutzerkorrektur):
> `Künftig: Wenn ich einen Link nicht eindeutig zuordnen kann, hänge ich ihn trotzdem an den
> Eintrag und markiere ihn als "Quelle: unzugeordnet", statt ihn wegzulassen.`

---

## 3. DIE AUSSCHLUSSLISTE

### Format

**Bulletliste ohne Aufzählungszeichen** — jede Zeile eine Zeile, kein `-`, kein `•`, keine Tabelle,
kein Fließtext-Absatz. Struktur jeder Zeile:

```
<Firmenname(n)> – <Begründung> → raus
```

Der Gedankenstrich ist ein Halbgeviertstrich `–` (U+2013), der Pfeil ist `→` (U+2192). Beide
Zeichen sind über alle 47 Ausschlussblöcke konstant.

### Gruppierung nach Grund — frühe vs. späte Runden

**Frühe Runden (Z. 1214–3001): nach Grund gruppiert, mit eigener Überschrift je Grund.**
Z. 1214–1230 ist das Extrembeispiel mit vier Untergruppen:
```
Ausgeschlossen (Startup-Finanzierung):
Ausgeschlossen (Refinanzierung/Debt):
Ausgeschlossen (Insolvenz/Administration):
Ausgeschlossen (kein DACH-Bezug):
```
Weitere Belege: Z. 1841/1846, Z. 2073/2076/2082, Z. 2992/2995/2998, Z. 3864/3867/3871.
Teilweise mit Anzahl je Gruppe: `Ausgeschlossen (Insolvenz/Administration, 4):` (Z. 2073),
`Ausgeschlossen (Refinanzierung/Debt/Fundraising, 4):` (Z. 2076),
`Ausgeschlossen (Insolvenz/Administration, 7):` (Z. 2992),
`Ausgeschlossen (kein DACH-Bezug, 3):` (Z. 2998),
`Ausgeschlossen (Insolvenz/Administration, 6):` (Z. 3864).

**Späte Runden (ab Z. 4125): eine einzige flache Liste unter `Ausgeschlossen:`.**
Belegt in Z. 4125, 4419, 4531, 4937, 5071, 5247, 5346, 5491, 5643, 5759, 5914, 6323, 6406,
6521, 6696, 6852, 7190, 7328, 7505, 7958 — 20 Runden in Folge ohne Untergruppierung. Die
Gruppierung wandert stattdessen **in die Zeile**: gleichartige Fälle werden in einer Zeile
zusammengefasst (siehe unten).

**Entwicklung:** Von "nach Grund gruppierte Unterüberschriften mit Zählung" (früh) zu
"eine flache Liste, Gleichartiges in einer Zeile zusammengezogen" (spät). Die Zählangabe in
der Ausschlussüberschrift verschwindet komplett ab Z. 4125 — nur `Ausgeschlossen:` bleibt.

### Wird jeder Artikel genannt?

**Ja, jeder wird namentlich genannt — aber gleichartige Fälle werden in einer Zeile gebündelt.**
Nie eine anonyme Sammelangabe wie "12 Insolvenzfälle". Das Bündelmuster:
- Z. 5249: `Vivanco, Arcos, aalcon, Kurt Hoffmann, Elkas – alle in Insolvenzverfahren/Eigenverwaltung → raus`
- Z. 3866: `Härterei Kirchhoff, Holzkunst Gahlenz, Büromöbel Sofort-Markt Müller, DOMO Collection, Alstakom, VIOLAS → alle raus`
- Z. 5916: `Centrum Development, Lindenfarb Textilveredlung, SpieKo Flaschenverschlüsse, Heck+Becker – alle in Insolvenz/provisorischer Verwaltung → raus`

Also: **Name immer, Begründung einmal pro Gruppe.**

### Reihenfolge innerhalb der Ausschlussliste

Nicht chronologisch, sondern **nach Ausschlussgrund sortiert, Massenfälle zuerst**. Faktisch immer:
1. Insolvenz/Eigenverwaltung (der mit Abstand häufigste Grund, meist als gebündelte Sammelzeile)
2. Refinanzierung/Debt/Fundraising
3. kein DACH-Bezug
4. zu vage / kein M&A-Charakter
5. Grenzfälle (zuletzt, weil sie eine Nutzerentscheidung anstoßen)

Belege für diese Abfolge: Z. 7190–7198, Z. 7505–7511, Z. 6852–6858, Z. 2992–3003.

### Ausführlichkeit der Begründung: 10 wörtliche Beispiele

Die Begründung ist **ein knapper Halbsatz, keine Satzkette** — außer wenn ein Präzedenzfall
zitiert oder eine Abgrenzung nötig ist. Bandbreite von 2 Wörtern bis 3 Sätzen:

1. Z. 257: `Schwedenhaus Automobile – provisorische Insolvenzverwaltung → raus`
2. Z. 260: `ZEGO Textile – Insolvenzantrag → raus`
3. Z. 849: `JPMorgan-Podcast – Marktkommentar, kein konkreter Deal → raus`
4. Z. 262: `MAX Power Mining – kein DACH-Bezug (Saskatchewan/Kanada, nur Zweitlisting an der Frankfurter Börse zählt nicht als Sitz/Fokus) → raus`
5. Z. 489: `Kalle/Hayfin – Debt-for-Equity-Swap ist ein Refinanzierungs-/Debt-Thema → raus, trotz Cartel-Filing`
6. Z. 1221: `Dalian Wanda/Infront – Darlehensrefinanzierung, zudem kein DACH-Akteur (chinesischer Konzern) → raus`
7. Z. 1844: `Newsadoo (AT) – zwar DACH, aber CEO sagt explizit "not actively pursuing a sale", Unabhängigkeit sei aktuell wichtiger. Schwächer als der Squid-Präzedenzfall (dort aktives Interesse an weiteren Gesprächen) → raus`
8. Z. 2079: `Cembra – Privatplatzierung von Aktien zur Akquisitionsfinanzierung, kein eigenständiger M&A-Prozess (die zugrunde liegende Santander-Übernahme ist bereits verkündet, das hier ist nur die Finanzierung) → raus`
9. Z. 1320: `Badischer Winzerkeller – das ist kein M&A-Thema, sondern eine interne Restrukturierung (Kostenreduktion, Outsourcing-Prüfung), keine Insolvenz, aber auch kein Verkaufs-/Zukaufs-/IPO-Prozess. Es gibt keinen Käufer, Verkäufer oder Berater – nur ein internes Sanierungsprogramm. Passt nicht in dein Format → raus.`
10. Z. 3869: `Matthews International/Olbrich – US-Mutterkonzern prüft Optionen für Olbrich-Sparte; da der handelnde Akteur (Matthews) nicht DACH ist, anders als z. B. bei EFB-Elektronik, wo trotz niederländischer Mutter (TKH) das DACH-Target selbst der Klammer-Akteur war → raus`

Weitere charakteristische Kurzformen:
- Z. 6523: `Eku Energy – Expansion über eigene Projektentwicklung (BESS-Projekte), kein M&A-Prozess → raus`
- Z. 7195: `Prosolia Energy – spanischer Akteur, Deutschland nur einer von mehreren Solarmärkten, kein Prozess → raus`
- Z. 4128: `Kammerer Medical Group – Unternehmen hat nach Veröffentlichung explizit dementiert, dass ein Verkaufsprozess läuft → raus`
- Z. 6858: `Nexopart (im SME-Digest) – DE, aber „könnte in zwei bis drei Jahren" → zu vage, raus`

**Muster:** Standardfälle (Insolvenz, Refi, Fundraising) bekommen 2–5 Wörter. Ein Fall bekommt
genau dann mehrere Sätze, wenn er (a) an einer Regelgrenze liegt, (b) einen Präzedenzfall
widerspricht oder bestätigt, oder (c) auf den ersten Blick aufnahmefähig aussieht.

---

## 4. ANMERKUNGEN / RÜCKFRAGEN

### Die Nachlaufzeile — feste Einleitungsformeln

Nach der Eintragsliste folgt fallweise genau ein Absatz. Wörtliche Einleitungen:
- `Kurze Anmerkung zu <X>:` — Z. 1329, 1861, 2093
- `Kurzer Hinweis zu <X>:` — Z. 3648, 3888 (dort `Hinweis zu <X>:`)
- `Kurzer Hinweis:` — Z. 3017
- `Zwei Anmerkungen:` — Z. 4953
- `Anmerkung zu <X>:` — Z. 5265
- `Zwei Hinweise:` — Z. 6332
- `Eine Anmerkung zu <X>:` — Z. 668
- `Zur <X>-Zeile kurz zur Einordnung:` — Z. 872

Es gibt **keine Überschrift "Anmerkungen:"** in den Batch-Runden. Der einzige Beleg für ein
eigenes Label `Anmerkungen:` ist Z. 9 — die allererste Einzelartikel-Antwort ganz zu Beginn,
bevor sich das Format eingeschwungen hat. Ab Z. 253 immer Fließtextabsatz.

### Wann wird eine Rückfrage gestellt?

Der Assistent fragt genau in vier Situationen. `sag Bescheid` / `Grenzfall` / `deine Entscheidung`
kommen zusammen 49-mal vor.

**(a) Grenzfall an der Aufnahmegrenze** — markiert mit `→ Grenzfall, sag Bescheid`:
- Z. 5074: `Nestlé/Better Health Company – Ziel ist neuseeländisch, kein DACH-Bezug außer dem Schweizer Konzernsitz; anders als beim Vitamin-Marken-Verkauf hat das hier keinerlei DACH-Dimension → Grenzfall, sag Bescheid, falls du's trotzdem drin haben willst`
- Z. 5917: `Arrow Global – UK-Akteur, MGA-Suche europaweit; DACH wird nicht als Zielmarkt genannt (...) → Grenzfall, sag Bescheid falls du's willst`
- Z. 6411: `Delivery Hero – Vorstandsempfehlung zum bereits gelisteten Uber-Angebot; kein neuer Sachverhalt, nur Zustimmung → Grenzfall, sag Bescheid falls du's willst`
- Z. 6854: `Milton Capital/Apostrophy – UK-Cash-Shell mit Schweizer Ziel, aber reine Reverse-Merger-/Listing-Konstruktion, noch nicht bindend → Grenzfall, sag Bescheid falls gewünscht`
- Z. 7197: `Hollanddak – niederländisches Unternehmen, Deutschland als Zielmarkt genannt; Deal (Borromin-MBO) bereits abgeschlossen → Grenzfall, sag Bescheid`
- Z. 7509: `ARLANXEO/Saudi Aramco – niederländisches Zielunternehmen, saudischer Verkäufer; DACH-Bezug nur über mögliche deutsche Käufer (AEQUITA, Aurelius) → Grenzfall, sag Bescheid`
- Z. 7511 / 7962: `Quarkwerk – Umsatz gut 2 Mio. EUR, sucht Molkerei als Partner; sehr klein, aber formal ein Teilexit-Prozess → Grenzfall, sag Bescheid`

**Entscheidend:** Der Grenzfall steht **in der Ausschlussliste**, nicht in der Aufnahmeliste.
Default ist "nicht aufgenommen", der Nutzer kann ihn hereinholen. Belegt durch Z. 1231
(`Grenzfall, nicht automatisch aufgenommen:`) und Z. 3001 (`Grenzfälle, nicht aufgenommen:`).

**(b) Unsicherheit bei Financials** — immer explizit gekennzeichnet:
- Z. 1329: `Kurze Anmerkung zu den Financials: Ich hab hier bewusst Mitarbeiterzahlen statt Umsatz verwendet, da für SRK selbst keine Finanzkennzahlen offengelegt wurden – die genannten 2,5 Mrd. EUR Umsatz beziehen sich auf den gesamten Alexianer-Konzern, nicht auf das Zielobjekt SRK, daher hab ich die nicht mit reingenommen, um keine falsche Größenordnung für das eigentliche Target zu suggerieren.`
- Z. 2093: `Kurze Anmerkung zu Drooms: Die "mid-double-digit million-euro"-Umsatzangabe ist unpräzise aus der Quelle – ich hab sie sinngemäß übernommen statt eine Zahl zu erfinden, passt zu unserer Regel "keine Erfindung von Fakten".`
- Z. 4953: `Zwei Anmerkungen: Bei RTS Wind habe ich bewusst keine Financials gesetzt – die im Artikel genannten ~200 Mio. EUR Umsatz / ~15 Mio. EUR EBITDA stammen von Quellen, denen der Eigentümer explizit widerspricht ("inaccurate"), und die 50 Mio. EUR von der Website sind von 2023. Bei Secop bezieht sich das EBITDA von >40 Mio. EUR auf die zum Verkauf stehenden Assets (Fokus Chinageschäft), nicht auf die Gruppe – deren bereinigtes EBITDA lag 2025 bei 24,4 Mio. EUR.`
- Z. 5265: `Anmerkung zu Swissbit: Die 250 Mio. USD sind laut Artikel "annual earnings" ohne nähere Spezifikation – ich habe das neutral als "Gewinn" übernommen statt EBITDA zu unterstellen. Sag Bescheid, falls du es anders labeln willst.`
- Z. 1861: `Kurze Anmerkung zu Webasto: Financials-Klammer bleibt hier bewusst schlank (nur DE, Automobilzulieferer), da die genannten Finanzkennzahlen (Nettogewinn/Umsatz) sich auf die indische Einheit beziehen, nicht auf Webasto selbst`
- Z. 5779: `Bei Uber/Delivery Hero habe ich bewusst keine Financials in die Klammer gesetzt – der Artikel nennt nur Bookings-Zahlen des kombinierten Unternehmens, keine Delivery-Hero-Einzelzahlen. Sag Bescheid, falls du stattdessen die Prämie (108% auf den unbeeinflussten Kurs) drin haben willst.`

**Muster bei Financials:** Nie stillschweigend weglassen. Immer: *was* weggelassen wurde,
*warum*, und das Angebot, es anders zu machen.

**(c) Unsicherheit bei Länderkürzel/Branche:**
- Z. 6706: `Bei Armacell habe ich LU/DE gesetzt, da der Konzernsitz Luxemburg ist, der europäische Hauptsitz aber in Münster liegt – sag Bescheid, falls du lieber nur LU willst.`

**(d) Dublette/Fortschreibung eines schon gelisteten Deals** — bis Z. 3890, danach abgeschafft:
- Z. 3017: `Kurzer Hinweis: Der BASF-Eintrag ist eine Fortschreibung deines bestehenden 13.07./17.07.-Eintrags (jetzt: konkrete Bank-Vorauswahl statt nur Pitch-Einladung). (...) Sag Bescheid, ob du diese als Update der bestehenden Zeilen oder als neue Einträge handhaben willst.`
- Z. 3888: `Hinweis zu Marx Krontal Partner: Das ist eine Fortschreibung deines bereits gelisteten 08.07.-Eintrags (jetzt: zweite Bieterrunde mit konkreten Namen). Sag Bescheid, ob als Update oder neuer Eintrag gewünscht.`

Der Nutzer beendet das in **Z. 3890**:
> `ne einfach neuereimtrag füge das hinzu keiner weiß dass die schon mal dirn waren`

Antwort Z. 3892:
> `Verstanden, mach ich ab jetzt so – einfach als neuer Eintrag ohne Update-Hinweis, da dein
> Chef/die Leser den Verlauf ohnehin nicht kennen. Halte ich für künftige Fälle fest.`

**Ab Z. 3892 entfällt der Update-Hinweis als Rückfrage.** Danach nur noch als knappe
Feststellung, z. B. Z. 4540:
> `Autmatec und Babtec hattest du ja schon früher als laufende Bieterprozesse gelistet – jetzt
> einfach als neue, eigenständige Einträge mit dem aktuellen Stand (Käufer feststeht), ohne
> Verweis auf die alten Zeilen, wie besprochen.`

### Offene Links / fehlende Artikeltexte

Eigener Nachlaufsatz am Ende, wenn Links ohne Text kamen:
- Z. 6418: `Drei Links ohne zugehörigen Artikeltext sind noch offen: 1004535113, 1004535300, 1004535329 – schick die Texte nach, falls dort was Relevantes dabei ist.`
- Z. 6532: `Ein Link ohne zugehörigen Artikeltext ist noch offen: 1004535482 – schick den Text nach, falls dort etwas Relevantes dabei ist.`
- Z. 6868: `Drei Links ohne Artikeltext sind noch offen: 1004536069, 1004536103, 1004536142 – schick die Texte nach, falls dort noch was Relevantes dabei ist.`
- Z. 6334: `Zwei Hinweise: Die beiden Links ohne direkt anhängenden Artikeltext habe ich nach Reihenfolge und Zeitstempel Peach Property (11:53) und Elevion (15:36) zugeordnet – kurz gegenprüfen, falls möglich.`

Der Nutzer korrigiert das in **Z. 7223**:
> `ich habe die wie vorher auch in den langen artikeln dirnnen gehabt wenn freie links dann siend
> das die angehangenen dokumente - die dann nicht ignorieren sondern dann ohne quelle markiert
> anzeigen wenn du die da noch nciht zuiordnne kannst`

---

## 5. UMGANG MIT GROSSEN BATCHES

### Typische Batchgröße

Aus den Aufnahmezahlen (`Aufnahmefähig (N)`) plus Ausschlusszeilen lässt sich die Batchgröße
rekonstruieren. Aufnahmen pro Runde über alle 34 Runden:
2, 1, 7, 7, 1, 5, 5, 3, 3, 7, 6, 6, 6, 6, 8, 6, 4, 5, 5, 6, 1, 3, 7, 6, 6, 4, 3, 5, 4, 5, 11, 2, 4, 4.

Median 5, Modus 6, Maximum 11 (Z. 7199). Dazu kommen typisch 3–8 Ausschlüsse pro Runde.
**Ein typischer Batch umfasst also rund 8–18 Rohartikel, aus denen 4–6 Einträge werden.**
Der Assistent beziffert das Verhältnis selbst, Z. 1678–1682:
> `Ja, stimmt – diese Runde hatte einen ungewöhnlich hohen Ausschussanteil: von 9 Artikeln sind
> nur 5 durchgekommen.`
> `Das ist eher zufällig so verteilt – in den Wochen davor lag die Ausschlussquote meist niedriger
> (z.B. bei der 13.-17.07-Runde waren es nur 2 von ca. 10).`

### Wird in Teilen geantwortet?

**Nein.** Es gibt keinen einzigen Beleg für eine Teilantwort, ein "Teil 1 von 2", ein
"Fortsetzung folgt" oder ein Nachreichen. Jede Runde ist in sich vollständig: eine Antwort,
ein Ausschlussblock, ein Aufnahmeblock. Bei sehr großen Batches wird lediglich der
Einleitungssatz angepasst (Z. 1212 `Sichtung der großen Artikel-Batch – aufgeteilt nach
Kategorie:`, Z. 3862 `großer Batch, hier die Aufteilung:`, Z. 7188 `Sichtung – großer Batch:`)
und in den frühen Runden die Ausschlussliste nach Grund untergliedert.

### Vollständigkeitssignal

Die Zählangabe in `Aufnahmefähig (N)` ist das Vollständigkeitssignal pro Runde.
Auf Nachfrage bestätigt der Assistent kumulativ über mehrere Runden hinweg. Wörtliche Beispiele:

- Z. 8030 (die vom Nutzer gesuchte Zählformel):
  > `Ja, alle Artikel aus diesem Briefing-Zeitraum sind abgedeckt. Die Liste umfasst 38 Einträge
  > vom 01.09. bis 14.09., und alles aus den Batches, die du geschickt hast, ist entweder drin
  > oder mit Begründung ausgeschlossen (Insolvenz, Refinanzierung, kein DACH-Bezug, zu vage).`
- Z. 3114:
  > `Ja, alle relevanten Deals aus den drei Durchgängen (03.08. bis 27.07.) sind enthalten – die
  > 13 Einträge decken alles ab, was nach deinen Kriterien reingehört. Alles andere aus den
  > durchgesehenen Artikeln fiel unter Ausschlusskategorien (Insolvenz, Refinanzierung/Debt-
  > Finanzierung, kein DACH-Bezug oder zu vage) und wurde entsprechend aussortiert. Liste ist
  > vollständig und einsatzbereit.`
- Z. 8026:
  > `Ansonsten alles korrekt: Chronologie stimmt (alle 38 Daten geprüft), Berater-Labels
  > durchgängig, Zahlenformat regelkonform, Investor-als-Subjekt überall richtig gesetzt, keine
  > Ausschlussfälle drin.`
- Z. 5383 (Abschlussformel des Selbstchecks):
  > `Keine Ausschlussfälle durchgerutscht, keine Tippfehler mehr.`
- Z. 5385: `Ansonsten: fertig zum Verschicken.`
- Z. 4696 (dieselbe Formel): `Ansonsten: bereit zum Verschicken.`

### Statistik-Block?

**Es gibt keinen festen Statistik-Block.** Der Assistent bietet ihn einmal an, Z. 1684:
> `Willst du, dass ich zukünftig kurz die Ausschlussquote mit angebe, damit du auf einen Blick
> siehst, wie viel aussortiert wurde?`

Der Nutzer geht darauf **nicht ein**; in keiner Folgerunde erscheint eine Quotenangabe.
Die Zahl in `Aufnahmefähig (N)` bleibt die einzige Statistik.

### Wiederholte/überlappende Batches

Wenn ein Batch schon Gesichtetes enthält, antwortet der Assistent mit einem Kurzformat statt
einer vollen Sichtung:
- Z. 6183–6189:
  > `Diese sind alle schon abgedeckt – die Artikel stammen aus dem Batch, den du letzte Woche
  > rausgeschickt hast:`
  > `Bereits im versendeten Briefing:`
  > `Scandinavian Print Group → Quelle` / `GBS-TEMPEST → Quelle`
  > `Ausgeschlossen (unverändert):`
- Z. 7678–7686:
  > `Drin:` / `Volkswagen/Gotion → 10.09.26, bereits in der Liste` / ...
  > `Ausgeschlossen (Insolvenz/Eigenverwaltung):` / ...
  > `Also keine Änderung an der Liste.`
- Z. 7826–7832:
  > `Alles schon gesichtet – keine Änderung an der Liste:`
  > `Drin (4): cleversoft, Aesthetify, Leaders of AI, Semdor Pharma Group – alle mit 10.09.26 in der Liste`
  > `Ausgeschlossen: Photocure (NO), Swedencare (SE), Globetrotter (Verkauf explizit ausgeschlossen), ARLANXEO (NL-Ziel, saudischer Verkäufer)`

Hier — und nur hier — wird die Ausschlussliste zu **einer einzigen Fließtextzeile** (Z. 7830)
mit Kurzbegründung in Klammern.

### Der Prüf-/Korrekturmodus (zweiter Antworttyp)

Wenn der Nutzer die fertige Liste zurückpastet (`schau noch mal final drüber`, Z. 5370;
`check ob so alles richtig ist jetzt`, Z. 5931; `so alles richtig?`, Z. 3112), antwortet der
Assistent in einem **anderen, nummerierten Format**:
- Z. 5933: `Durchgesehen – vier Punkte:` gefolgt von `1. Berater-Label inkonsistent (zwei Fälle):`,
  `2. Fehlende Fettung:`, `3. Chronologie stimmt, ...`, `4. Ein Kandidat nach Roberts Kürzungslinie:`
- Z. 4721: `Finaler Durchgang – fünf Kleinigkeiten:` mit Untergruppen `Tippfehler:`,
  `Konsistenz:`, `Nach Chef-Kürzungslinie (Timing-Nachsätze):`
- Z. 5372: `Finaler Check – alles sitzt:` mit Prüfpunkten je Kategorie und `✓`-Haken
- Z. 8020: `Fast – die vier Punkte von vorhin sind noch nicht eingearbeitet:` mit
  `1. ... 2. ... 3. ... 4. ...`
- Z. 305: `Hab alles durchgesehen – drei kleine Fixes nötig, plus Sortierung nach Datum` mit
  Überschrift `Fixes:` und anschließend `Finale Liste (chronologisch absteigend, einfügefertig):`

Charakteristisch: durchnummerierte Punkte, `✓` als Bestätigungshaken, und **ein
Abschlussabsatz, der explizit sagt, was in Ordnung ist** (Z. 4694, 5383, 5947, 8026).

---

## 6. WAS DER NUTZER AN DER ANTWORTSTRUKTUR KRITISIERT ODER GELOBT HAT

Der Nutzer greift die Darstellungsform genau viermal direkt an. Alle vier Eingriffe sind
dauerhaft wirksam.

**(1) Z. 328 — Aufzählungszeichen raus. Der härteste Formatbefund.**
> `bitte schick nochmal so gut geordnet aber ohne den bindestrich am anfang`

Wirkung: messbar. Vor Z. 328 achtzehn Dash-Einträge, danach null. Er verlangt zugleich
"so gut geordnet" — also: Ordnung ja, Bullet nein.

**(2) Z. 3117 — Fettung als Pflicht.**
> `sind jetzt auch alle namen fett das muss immer sein, außer den sell side oder gloinbal corrdiantor`

Wirkung: ab Z. 3126 festes Formatierungsmerkmal, in Z. 5399 und Z. 5947 nachgeprüft.

**(3) Z. 3890 — keine Update-Hinweise mehr, keine Rückfrage bei Fortschreibungen.**
> `ne einfach neuereimtrag füge das hinzu keiner weiß dass die schon mal dirn waren`

Das ist die einzige Stelle, an der der Nutzer eine ganze **Rückfragekategorie streicht**.
Begründung des Assistenten in Z. 3892: die Leser kennen den Verlauf nicht.

**(4) Z. 3019 — Label- und Financials-Vereinheitlichung, Ausgabe der Gesamtliste.**
> `dann lsite jetzt alle aus den 3 durchgängen auf die relevant sind und überarbeite nochmal dass
> du immer sell siode berate als berater schreibst und bei den financials das jahr weglassen nur
> umsatz: oder ebitda:`

**(5) Z. 7223 — nicht zuordenbare Links nicht verschweigen, sondern markiert ausgeben.**
> `ich habe die wie vorher auch in den langen artikeln dirnnen gehabt wenn freie links dann siend
> das die angehangenen dokumente - die dann nicht ignorieren sondern dann ohne quelle markiert
> anzeigen wenn du die da noch nciht zuiordnne kannst`

**(6) Z. 8070 — Terminologie, plus der Skill-Auftrag.**
> `okay sag ab jetzt bei lincoln immer lincoln, und immer adj. ebtida anstellebreinigtes, das von
> metzler regel kannst du weglassen. du hast hier extrem hohes wissen ahst du eine datei wo alle
> regeln und ablauf etc gespeichert ist? ich will einen skill erstellen der importierbar ist für
> meine kollegen lass usn erst durchdenken bevor wir was machen`

### Was er NICHT kritisiert hat — ebenso aussagekräftig

Über 36 Runden gibt es **kein einziges** "mach es kürzer", "nur die Liste", "keine Erklärungen",
"gib mir das als Block", "zu lang". Gezielte Suche nach allen diesen Formulierungen
(`nur die liste`, `ohne erklär`, `keine erklär`, `kurz halten`, `als block`, `codeblock`,
`zum kopieren`, `ohne kommentar`, `ohne anmerkung`, `spar dir`, `zu lang`, `weniger text`)
liefert **genau einen Treffer**, und der stammt vom Assistenten, nicht vom Nutzer (Z. 5999:
`Falls dir das zu lang wird, kannst du auch beide behalten`).

**Schlussfolgerung für den Skill:** Die Ausschlussliste und die Anmerkungen sind **gewollt**.
Der Nutzer hat sie nie gekürzt haben wollen — er nutzt sie aktiv, um Grenzfälle zu entscheiden
(Z. 4546 `mach isto biologics rein. Wella AG ist doch deutsches unternhmen oder?`) und um
Konsistenz zu prüfen (Z. 3152 `warum hast du den rausgelkassen sonst haben wir doch auch erwaägt
zukäufe oder`). Was er gekürzt hat, war ausschließlich das Aufzählungszeichen und die
Update-Rückfrage.

### Lob

- Z. 330 (implizit, durch Weiterverwendung ohne Änderung)
- Z. 518 (Nutzer hatte die Liste zurückgeschickt, Assistent bestätigt): `Sehr gut, sieht sauber aus. Kurzer Korrekturdurchgang:`
- Z. 3152 f. — der Nutzer fängt einen Regelverstoß des Assistenten selbst, dieser räumt ein
  (Z. 3154): `Guter Punkt – das ist tatsächlich inkonsistent. (...) Mein Ausschluss war ein
  Fehler – nach unserer eigenen Linie gehört das rein.`

---

## 7. IDEALE MUSTERANTWORT

Rekonstruiert aus der spätesten vom Nutzer akzeptierten Vollrunde — Z. 7956–7975 (Batch vom
14.09.26, vom Nutzer in Z. 8030 als vollständig abgenommen), ergänzt um die Grenzfallzeile aus
derselben Runde (Z. 7962) und die Anmerkungsform aus Z. 6706. Auf 4 Einträge gekürzt,
strukturell vollständig. Fettung hier mit `**` explizit gemacht.

```markdown
Sichtung:

**Ausgeschlossen:**

The Dude Food Company, Prinz-Mayweg – Insolvenz/provisorische Verwaltung → raus
Invelon – spanischer Akteur, Deutschland nur vage als mögliches künftiges Zielland genannt
("könnte sich als Zielmarkt herausbilden") → zu schwach, raus
Quarkwerk – Umsatz gut 2 Mio. EUR, deutlich unter der Größenordnung der übrigen Einträge
→ Grenzfall, sag Bescheid

**Aufnahmefähig (4), chronologisch sortiert:**

14.09.26: **Equity House** (CH, Asset Manager, **Pollen Street Capital**) plant erste Zukäufe
unabhängiger Vermögens- und Asset-Manager im vierten Quartal, Fokus Schweiz, Deutschland und
Luxemburg [Quelle](…)

14.09.26: **Aareal Bank** (DE, Immobilienfinanzierung, **Advent**/**Centerbridge Partners**)
prüft Übernahme der **Hamburg Commercial Bank** (DE, Geschäftsbank, Eigenkapitalwert:
3,3 Mrd. EUR, **Cerberus Capital Management**) [Quelle](…)

11.09.26: **STOCKMEIER Group** (DE, Chemie) prüft Verkauf seiner Chemiedistributionssparte
(Adj. EBITDA: 115 Mio. EUR), Sell-side Berater: Goldman Sachs [Quelle](…)

11.09.26: **Blejkan** (PL, Grabenlose Rohrsanierung, Umsatz: 37 Mio. EUR, EBITDA-Marge: ~15%)
prüft mehrere Zukäufe in DE, Fokus kleinere profitable Kanalsanierungsbetriebe [Quelle](…)

Bei **Armacell** habe ich LU/DE gesetzt, da der Konzernsitz Luxemburg ist, der europäische
Hauptsitz aber in Münster liegt – sag Bescheid, falls du lieber nur LU willst.
```

Anmerkung zur Rekonstruktion: `Adj. EBITDA` statt `bereinigtes EBITDA`, `DE` statt
`Deutschland`, `Asset Manager` statt `Vermögensverwaltung/Konsolidierungsplattform` und die
Großschreibung `Grabenlose Rohrsanierung` sind die in Z. 8041–8066 und Z. 8070 festgehaltenen
letzten Nutzerpräferenzen — sie gelten ab der nächsten Runde und sind hier eingearbeitet.

---

## OUTPUT-VERTRAG (kopierfertige Vorlage für den Skill)

> Wenn der Nutzer einen Batch Mergermarket-Rohartikel einfügt, antworte **immer** in genau
> dieser Form. Keine Begrüßung, keine Vorrede, kein Schlusssatz außerhalb der definierten Blöcke.

**Block 1 — Einleitung.** Genau eine Zeile:
```
Sichtung:
```
Nur bei auffällig großem Batch: `Sichtung – großer Batch:`. Sonst nichts anderes.

**Block 2 — Ausschlussliste.** Überschrift fett, dann Leerzeile, dann eine Zeile je Fall:
```
**Ausgeschlossen:**

<Name> – <Begründung> → raus
<Name A>, <Name B>, <Name C> – <gemeinsame Begründung> → raus
<Name> – <Begründung> → Grenzfall, sag Bescheid
```
Regeln:
- Kein Aufzählungszeichen. Halbgeviertstrich `–` vor der Begründung, `→` vor dem Urteil.
- Jeder ausgeschlossene Artikel wird **namentlich** genannt. Nie "12 Insolvenzfälle".
  Gleichartige Fälle in **einer** Zeile bündeln, Begründung einmal.
- Reihenfolge: Insolvenz/Eigenverwaltung → Refinanzierung/Debt/Fundraising → kein DACH-Bezug
  → zu vage → Grenzfälle zuletzt.
- Begründungslänge: Standardfälle 2–5 Wörter. Mehrere Sätze nur, wenn der Fall an einer
  Regelgrenze liegt, einem Präzedenzfall widerspricht oder aufnahmefähig aussieht.
- Grenzfälle stehen **hier**, nicht in der Aufnahmeliste. Default ist "draußen".
- Keine Untergruppierung nach Grund mehr (das war das frühe Format; ab Mitte des Verlaufs
  ersetzt durch die flache Liste mit gebündelten Zeilen).
- Wenn nichts auszuschließen ist, entfällt der Block ersatzlos.

**Block 3 — Aufnahmeliste.** Überschrift fett mit Pflicht-Zählung, dann Leerzeile:
```
**Aufnahmefähig (N), chronologisch sortiert:**

TT.MM.JJ: <Eintrag> [Quelle](<url>)

TT.MM.JJ: <Eintrag> [Quelle](<url>)
```
Regeln:
- `N` ist **immer** gesetzt. Bei `N = 1` lautet die Überschrift `**Aufnahmefähig (1):**`
  (ohne Sortierzusatz).
- **Kein Aufzählungszeichen vor dem Datum.** Kein `-`, kein `•`, kein `*`. Explizit vom
  Nutzer verlangt. Die Zeile beginnt mit der Ziffer des Tages.
- Genau eine Leerzeile zwischen zwei Einträgen.
- Absteigend chronologisch (neuestes Datum oben).
- Alle Akteursnamen fett: Käufer, Zielunternehmen, Eigentümer/Sponsor/Bieter.
  Berater **nie** fett — weder nach "Sell-side Berater:" noch nach "Global Coordinators:".
- Jeder Eintrag endet mit `Quelle` als Link. Liegt kein Link vor: `[Quelle]`. Lässt sich ein
  mitgeschickter Link nicht zuordnen: trotzdem anhängen und als `Quelle: unzugeordnet` markieren.
- **Kein Codeblock.** Die Liste steht als normaler Fließtext, damit sie direkt kopierbar ist.

**Block 4 — Nachlauf (nur bei Bedarf).** Ein Fließtextabsatz, keine Überschrift.
Einleitungsformel eine von: `Kurze Anmerkung zu <X>:` / `Kurzer Hinweis zu <X>:` /
`Anmerkung zu <X>:` / `Zwei Anmerkungen:` / `Zwei Hinweise:`.
Auslöser — und nur diese:
1. Financials weggelassen, geschätzt oder unscharf übernommen → sagen *was*, *warum*, und
   anbieten, es anders zu machen. Nie stillschweigend weglassen.
2. Länderkürzel oder Branchenbezeichnung unsicher → Entscheidung offenlegen, Alternative anbieten.
3. Grenzfall, der eine Nutzerentscheidung braucht (falls nicht schon in Block 2 abgehandelt).
4. Links ohne zugeordneten Artikeltext.

**Verboten im Nachlauf:**
- Hinweise, dass ein Deal bereits früher gelistet war ("Fortschreibung", "Update statt
  Neueintrag"). Der Nutzer hat das gestrichen: neue Meldung = neuer eigenständiger Eintrag,
  ohne Verweis auf alte Zeilen.
- Ausschlussquoten, Statistikblöcke, Meta-Kommentare zur eigenen Arbeitsweise.
- Ein zusammenfassender Schlusssatz.

**Antwort auf "schau nochmal drüber" / "alles richtig?" (Prüfmodus, anderer Vertrag).**
Kein Sichtungsformat, sondern:
```
Durchgesehen – <Anzahl> Punkte:

1. <Kategorie>:
<Fall> – <was ist falsch> → <Korrektur>

2. <Kategorie>:
...

<Abschlussabsatz: was geprüft und in Ordnung ist>
```
Kategorien wie `Tippfehler:`, `Konsistenz:`, `Berater-Label inkonsistent:`, `Fehlende Fettung:`,
`Chronologie`. Bestätigte Punkte mit `✓`. Abschlussformeln: `Keine Ausschlussfälle
durchgerutscht, keine Tippfehler mehr.` / `Ansonsten: fertig zum Verschicken.` /
`Ansonsten: bereit zum Verschicken.`

**Antwort auf einen Batch, der nur schon Gesichtetes enthält.** Kurzformat:
```
Alles schon gesichtet – keine Änderung an der Liste:

Drin (N): <Namen> – alle mit TT.MM.JJ in der Liste

Ausgeschlossen: <Name> (<Kurzgrund>), <Name> (<Kurzgrund>)
```

**Antwort auf "sind alle Artikel abgedeckt?".** Eine Zählaussage nach diesem Muster:
```
Ja, alle Artikel aus diesem Briefing-Zeitraum sind abgedeckt. Die Liste umfasst N Einträge
vom TT.MM. bis TT.MM., und alles aus den Batches, die du geschickt hast, ist entweder drin
oder mit Begründung ausgeschlossen (Insolvenz, Refinanzierung, kein DACH-Bezug, zu vage).
```
Danach, falls zutreffend, die offenen Grenzfälle einzeln auflisten.

---

## OFFENE PUNKTE

1. **Fettung im Ausschlussblock ungeklärt.** Die Regel aus Z. 3117 spricht nur von der
   Eintragsliste. Ob Firmennamen in der Ausschlussliste ebenfalls fett sind, ist aus dem
   gestrippten Export nicht rekonstruierbar. Die Musterantwort in Abschnitt 7 setzt sie
   **nicht** fett — das ist eine Annahme, keine Belegstelle.

2. **Fettung der Überschriften nicht belegbar.** Dass `Ausgeschlossen:` und
   `Aufnahmefähig (N), chronologisch sortiert:` fett gesetzt waren, ist plausibel (sie stehen
   als eigene Absätze mit Doppelpunkt), aber durch den Markup-Verlust nicht beweisbar.

3. **Link-Syntax im Zieldokument.** Der Export zeigt teils `[Quelle]`, teils `Quelle`. Ob der
   Nutzer den Link als Markdown-Link oder als Rich-Text-Hyperlink im Zieldokument braucht, ist
   nicht explizit geklärt. Z. 6190 sagt nur "fertig verlinkt".

4. **Die `Quelle: unzugeordnet`-Regel (Z. 7236) wurde nie angewandt.** Sie ist eine Zusage des
   Assistenten für künftige Fälle; im Transkript folgt danach kein Batch mit unzuordenbaren Links.
   Ihre tatsächliche Darstellungsform ist unbekannt.

5. **Ausschlussquote als Option offen.** Das Angebot in Z. 1684 wurde vom Nutzer nie beantwortet.
   Der Skill sollte sie standardmäßig weglassen — aber es ist ein offener Wunsch, kein Nein.

6. **Sekundärsortierung innerhalb eines Tages undefiniert.** Z. 16 und Z. 520 halten fest, dass
   der Nutzer dafür keine Konvention definiert hat ("Reihenfolge innerhalb des Tages ist dir
   überlassen" / "da hast du keine feste Sekundärsortierung definiert"). Bleibt offen.

7. **"Robert"/"dein Chef" als dritte Instanz.** Ab Z. 4721 referenziert der Assistent eine
   "Chef-Kürzungslinie" und "Roberts Linie" — Präferenzen des Empfängers, die über die des
   Nutzers hinausgehen (Timing-Nachsätze streichen, Attributionen streichen). Für einen
   importierbaren Kollegen-Skill ist unklar, ob diese Ebene mitgeliefert oder als
   konfigurierbar markiert werden soll. Der Assistent selbst problematisiert das in Z. 8085.
