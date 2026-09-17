# Mergermarket Briefing — Regelwerk SCHREIBWEISE / FORMAT / ANORDNUNG / SPRACHE

Quelle: `briefing_utf8.txt` (8086 Zeilen). Alle Zeilennummern beziehen sich auf diese Datei.
Rollen im Chat: **Nico** = Nutzer/Praktikant (schreibt das Briefing), **Robert** = Chef (korrigiert und verschickt es an die Kollegen).
Zwei Korrekturebenen: Nicos Entwurf → Roberts Endfassung. Roberts Endfassung ist immer maßgeblich.

> **Grundprinzip (Z.1384):** „Dein Chef kürzt in der finalen Freigabe grundsätzlich noch eine Stufe härter als meine erste Fassung … Faustregel: Wenn ich unsicher bin, ob ein Detail rein muss, eher raus damit – die finale Linie ist ‚so knapp wie möglich, auch auf Kosten von Kontext-Nuancen'."

---

## A) GRUNDFORMAT DES EINTRAGS

**A1.** Grundmuster (erstmals fixiert Z.55): „Format bleibt: • TT.MM.JJ: Unternehmen (Land, Branche, Financials) Kerninhalt, Sell-side Berater/Global Coordinator: X Quelle"

**A2.** Datumsformat ist **TT.MM.JJ** mit Punkten, zweistelliges Jahr — z.B. `09.07.26:`. Nie ausgeschrieben, nie ISO. Beleg: sämtliche Einträge, z.B. Z.1465.

**A3.** Nach dem Datum folgt **Doppelpunkt + genau ein Leerzeichen**, dann sofort das Satzsubjekt. Beleg Z.1465: „13.07.26: Flix (DE, …"

**A4.** **Kein Bullet, kein Spiegelstrich, kein Aufzählungszeichen am Zeilenanfang.** Explizite Nutzeranweisung Z.328: „bitte schick nochmal so gut geordnet aber **ohne den bindestrich am anfang**". Frühere Versionen mit „- " bzw. „• " (Z.271, Z.286) sind überholt. In allen finalen Mails (Z.1465 ff., Z.2264 ff.) steht die nackte Datumszeile.

**A5.** Reihenfolge der Bausteine innerhalb der Zeile — verbindlich:
1. Datum + `: `
2. Satzsubjekt/Akteur (fett)
3. ggf. Klammer `(Land, Branche, Financials[, Eigentümer])` — direkt hinter dem Namen, zu dem sie gehört
4. Verb + Kerninhalt (Objekt direkt ans Verb)
5. ggf. Zusatzfakten (Bieterliste, Deal-Value/Bewertung, Zielgröße) als Komma-Anhang
6. Berater-Feld `Sell-side Berater: X` / `Global Coordinators: X`
7. `Quelle` bzw. `[Quelle](URL)` als letztes Element

**A6.** Die Zeile endet **ohne Satzpunkt**; letztes Zeichen ist die Quellenangabe. Beleg: alle Einträge, z.B. Z.1465–1480.

**A7.** Trennzeichen zwischen den Blöcken ist das **Komma**, nicht Semikolon/Gedankenstrich. Beleg Z.1477: „…erreicht zweite Bieterrunde mit u.a. Apleona und OMS Prüfservice, Sell-side Berater: Lincoln International [Quelle]"

**A8.** Die Klammer steht **direkt hinter dem Namen des Unternehmens**, nicht hinter dem Verb. Offener Monitum Z.5385: „Bei Webasto steht die Sparten-Klammer erst nach ‚voran' statt direkt hinter ‚HVAC-Sparte in Polen' – das ist die einzige Zeile, wo die Financials-Klammer nicht direkt am Objekt hängt wie sonst überall (vgl. Secop, SWARCO)."

**A9. FETTUNG (ab Z.3117 verbindlich).** Nutzeranweisung Z.3117: „sind jetzt auch alle namen fett das muss immer sein, außer den sell side oder gloinbal corrdiantor". Präzisierung Z.3126: „Ab jetzt formatiere ich **alle Akteursnamen (Käufer, Ziel, Eigentümer/Sponsor) automatisch fett, während Berater unformatiert bleiben.**"
- Fett: Käufer, Zielunternehmen, Eigentümer/Sponsor, Bieter, Konsortien, auch Gebietskörperschaften als Akteur (Z.5941: „bei Niedersachsen (31.08.) ist das Bundesland als Käufer nicht fett … sollte es konsistent auch fett sein").
- Nie fett: jede Bank/Boutique im Berater-Feld (Z.3135: „Nur Morgan Stanley (der Sell-side Berater) bleibt unformatiert"), auch Buy-side-Berater (Z.5959: „Nomura ist aktuell fett, obwohl Berater nie fett sein sollen").
- Die Fettung wird in Outlook gesetzt; im Chat-Text ist sie oft nicht sichtbar (Z.5313: „In der Textfassung ist nichts fett – falls du wie sonst vor dem Versenden in Outlook formatierst, denk an die Akteursnamen").

**A10.** Rechtsformen im Firmennamen werden weggelassen, außer sie sind Teil der offiziellen Marke/zur Unterscheidung nötig. Z.101: „‚Güntner GmbH' → ‚Güntner', außer sie ist Teil der offiziellen Bezeichnung und wichtig zur Unterscheidung (SMAG ‚AG' bleibt)". Gegenbeispiel wo sie bleibt: „FC Bayern München AG" (Z.4579).

**A11.** Exakter Firmenname aus der Quelle, auch wenn ein bekannterer Markenname naheliegt. Z.4569: „Bidder ist **Viessmann Generations Group**, die Familienholding, nicht das operative Heiztechnik-Unternehmen".

---

## B) DIE KLAMMER (Land, Branche, Financials, Eigentümer)

**B1. KERNREGEL — wer bekommt die Klammer (Z.66–70).** „Das ist die wichtigste Korrektur. **Nicht automatisch das Zielunternehmen – sondern wer der Satzsubjekt/Akteur ist.** … → Regel: Wer handelt (Käufer, verkaufender Investor), bekommt die vollständigen Financials. Das Ziel nur Land/Branche, wenn es nicht selbst Subjekt ist."
V1→V2-Beleg (Raymond/Deharde, Z.69): V1 hatte die Financials beim Target Deharde; V2 gibt dem Käufer **Raymond** die volle Klammer `(IN, Textil-/Bekleidungsindustrie & Zement, EBITDA, EV)`, **Deharde** nur `(DE, Branche)` ohne Financials.

**B2. Praktische Präzisierung.** Ist das Satzsubjekt ein reiner Finanzinvestor/Sponsor (DBAG, Permira, H.I.G., Burda, Emeram, CDPQ), bekommt **er keine Klammer** — die volle Klammer hängt am operativen Portfoliounternehmen, weil nur dort Branche/Financials existieren. Belege: Z.1473 „H.I.G. Capital treibt Verkauf von PLIXXENT (DE, Polyurethan-Systeme, Umsatz: 270 Mio. EUR, EBITDA: ~20 Mio. EUR) voran"; Z.1475 „DBAG bereitet Verkauf von Fischer TireTech (DE, Reifenmaschinenbau, EBITDA: ~25 Mio. EUR) vor".

**B3. Mehrere Klammern in einer Zeile sind erlaubt und erwünscht**, wenn beide Seiten operative Unternehmen sind: Akteur bekommt volle Financials, Ziel nur Land/Branche.
Beleg Z.7575: „Bei Webasto hast du es korrekt gemacht (**Akteur und verkaufte Sparte bekommen je eine Klammer**)."
Muster-Beleg (Z.4947): „Saubermacher Österreich (AT, Abfallwirtschaft, Umsatz: 508 Mio. EUR) meldet Erwerb von 65% an Quabus (AT, Abwasserentsorgung/Tiefbau) zur Kartellprüfung an"
Weiterer Beleg (Z.7333): „Volkswagen (DE, Automobilindustrie) treibt Teilverkauf seiner über 24%-Beteiligung an Gotion High-Tech (CN, Lithium-Ionen-Batterien) voran"

**B4. Reihenfolge innerhalb der Klammer (ausnahmslos):**
`(Länderkürzel, Branche[, Umsatz:][, EBITDA:][, weitere Financials][, Eigentümer/Sponsor])`
Der Eigentümer/Sponsor steht **immer als letztes Element**. Belege: Z.1472 „(CH, Energiekonzern, Umsatz: 28,6 Mrd. EUR)"; Z.1337 „(DE, Tech-Versicherungsmakler-Plattform, Umsatz: 339 Mio. EUR, **Warburg Pincus**)"; Z.7967 „(DE, Geschäftsbank, Eigenkapitalwert: 3,3 Mrd. EUR, **Cerberus Capital Management**)".

**B5. Eigentümer/Investor — drei Fälle (Z.76–80, revidiert Z.1374):**
- **Treibt der Eigentümer aktiv** → Eigentümer wird **Satzsubjekt**: „X treibt Verkauf von Y voran". V1→V2-Beleg Z.72: V1 „Polytech (…) Besitzer DBAG treibt … voran" → V2 „**DBAG treibt Verkauf von Polytech (…) voran**".
- **Ist die Firma selbst Akteur, Eigentümer nur Kontext** → Eigentümername **nur in die Klammer**, **kein eigener Nebensatz**. V1→V2-Beleg Z.73: V1 „im Besitz von Equistone" als Nebensatz → V2 „(CH, Filterhersteller/-vertrieb, Umsatz: …, **Equistone**)". Ebenso Z.74 (Volpi/KGS): V1 „… von GENUI" als Endphrase → V2 GENUI wandert in die Klammer.
- **Stake-Zahl:** ursprüngliche Regel (Z.80) „Gibt's eine konkrete Stake-Zahl … trotzdem als eigener Satz am Ende, PLUS Name in der Klammer" wurde **revidiert** (Z.1374): „Moin Group – In der finalen Version ist der separate Stake-Satz (‚Warburg Pincus hält indirekt 60%…') komplett raus, nur noch Name in der Klammer. … **Stake-Zahl nur behalten, wenn sie zentral für die Deal-Bewertung ist** (wie bei HolidayCheck/Burda), sonst reicht der Name in der Klammer."
  - Behalten-Beispiel (Stake ist der Kern der Nachricht): Z.1468 „(DE, …, Marktkapitalisierung: ~367 Mio. EUR, **Burda hält ~88%**)"; Z.4621 Commerzbank/UniCredit „knapp 50%" bleibt, „weil die 50% der eigentliche Kern der Nachricht sind".
  - Streichen-Beispiel: Z.4622 Thyssenkrupp „hält nach Spin-off 51%" — „Kandidat zum Streichen", weil weniger zentral als das IPO.

**B6. Wenn der Akteur Subjekt ist, wandert der Stake NICHT als eigener Satz ans Ende** (Z.326): „Bei HolidayCheck hab ich ‚Burda hält ~88%' in der Klammer gelassen statt als eigenen Schlusssatz, weil Burda hier schon selbst das Satzsubjekt ist – die Extra-Satz-Regel für Stake-Zahlen greift eigentlich nur, wenn der Eigentümer nicht schon Subjekt ist."

**B7. Länderkürzel: immer Zwei-Buchstaben-ISO-Kürzel, nie ausgeschriebene Länder.** Nutzerkorrektur Z.4581: „der a1 telekom punkt sit falsch da krotiaen in kalmmern steht **mach on kürzel**" → Z.4585: „(HR, Glasfasernetz, Umsatz: 1,9 Mio. EUR)". Bestätigung Z.4583: „konsistent mit den anderen Länderkürzeln (DE, AT, CH, FR, IN, US)".
Im Korpus belegte Kürzel: DE (346×), CH (111×), AT (35×), UK, US, NL, PL, CZ, CN, HR, DK, EE, LU, BR, SE, IN, FR.

**B8. Mehrere Länder werden mit Slash ohne Leerzeichen verbunden**, Hauptsitz zuerst: `DE/AT` (Z.1465, Best Secret), `DE/AT/CH` (Babtec), `CH/SE` (ABB), `FR/DE`, `LU/DE` (Z.6709: „Bei Armacell habe ich LU/DE gesetzt, da der Konzernsitz Luxemburg ist, der europäische Hauptsitz aber in Münster liegt").

**B9. Branchenbezeichnung — Schreibweise:**
- **Erstes Wort immer groß**, auch wenn es ein Adjektiv ist. Chef-Korrektur Z.8054/8055: „grabenlose Rohrsanierung" → „**Grabenlose** Rohrsanierung"; „ästhetische Medizin" → „**Ästhetische** Medizin". Überschrift dazu Z.8053: „Groß-/Kleinschreibung in der Branchenklammer".
- **Slash `/` ohne Leerzeichen** trennt zwei gleichrangige Tätigkeitsfelder: „Reisebuchungs-/Bewertungsplattform", „Kommunal-/Nutzfahrzeugtechnik", „SAP-/IT-Beratung", „Krypto-/Blockchain-Plattform", „Off-Price-Luxusmode/Online-Plattform", „TIC/Labor- & Prüfdienstleistungen".
- **Bindestrich mit Ergänzungsstrich** bei geteilten Komposita: „Outdoor-Bekleidung/**-**Ausrüstung", „Filterhersteller/**-**vertrieb", „KI-Modelle/**-**Software".
- **`&`** statt „und" innerhalb der Branche: „Labor- & Prüfdienstleistungen", „Infrastruktur & Tragwerksplanung", „Textil-/Bekleidungsindustrie & Zement".
- Branche **so knapp wie möglich**; Chef kürzt sie nach. Z.8050: „(CH, Vermögensverwaltung/Konsolidierungsplattform, …)" → „(CH, **Asset Manager**, …)". Z.8051: „(CH, Wohnimmobilien Deutschland, …)" → „(CH, **Wohnimmobilien**, …)". Z.1383: „Groupe Chaumont: ‚/Buy-and-Build-Plattform' aus der Klammer raus, wird implizit durch den Satz klar."
- Keine Redundanz zum Satz. Z.1378: „CTS Reisen: ‚im Bildungsreise-Segment' raus (redundant, da Branche schon in Klammer steht)".

**B10.** Steht zum Akteur nur Land + Branche zur Verfügung, ist das vollständig genug: „(DE, Agrarchemie)", „(CH, Kommunal-/Nutzfahrzeugtechnik)", „(DE, Automobilzulieferer)".

**B11.** Keine Financials in die Klammer, die sich auf eine andere Einheit beziehen als das genannte Unternehmen. Z.1329 (Klinikum Leverkusen): „die genannten 2,5 Mrd. EUR Umsatz beziehen sich auf den gesamten Alexianer-Konzern, nicht auf das Zielobjekt SRK, daher hab ich die nicht mit reingenommen, um keine falsche Größenordnung … zu suggerieren." Ebenso Z.1861 (Webasto) und Z.4953 (RTS Wind: widersprochene Zahlen → gar keine Financials).

**B12.** Verschachtelte Klammer in der Klammer ist verboten. Z.1410: „‚(Mitarbeiter Zielobjekt: 550+)' ist ein **Parenthese-in-Parenthese-Konstrukt**, das nach der härteren Linie raus sollte."

**B13. Deal-Value / Bewertung gehört NICHT in die Klammer, sondern in den Satz** nach dem Kerninhalt. Z.4666: „Die Klammer ist für Land/Branche/Financials des Unternehmens (Umsatz, EBITDA, Marktkap), **die Deal-Bewertung ist ein Transaktionsfakt und steht nach dem Kerninhalt**." Bestätigt Z.5306: „Bewertung im Satz statt Klammer (APCOA) ✓ – konsistent mit FC Bayern/SGB-SMIT". Beleg Z.2272: „…treibt Börsengang von SGB-SMIT (DE, Stromtransformatoren, EBITDA: 300 Mio. EUR) voran, **Bewertung 5-7,5 Mrd. EUR**, Global Coordinators: …". *(Altlast/Inkonsistenz: Mammut führt „Deal-Value: 600-700 Mio. CHF" noch in der Klammer, Z.4674.)*

---

## C) ZAHLEN & FINANCIALS

**C1. Deutsches Zahlenformat**: Komma als Dezimaltrenner, Punkt als Tausendertrenner. Belege: „1,53 Mrd. EUR", „239,9 Mio. EUR", „737,4 Mio. EUR", „Mitarbeiter: 2.950", „Mitarbeiter: ~6.200". Z.14: „Umsatz und bereinigtes EBITDA sind sauber aus der Meldung, **deutsches Zahlenformat**. ✓"

**C2. Einheiten immer `Mio. EUR` / `Mrd. EUR`** (mit Punkt nach Mio./Mrd., Leerzeichen, dann Währungscode). Nie „m", „bn", „Millionen", „€".

**C3. Originalwährung beibehalten, nie umrechnen.** Z.550: „Financials bleiben in der **Originalwährung der Meldung**, wenn die Quelle CHF nennt …, wird das nicht in EUR umgerechnet – genauso wenig wie bei USD-Angaben." Im Korpus: EUR, CHF, USD, BRL.

**C4. Labels mit Doppelpunkt + Leerzeichen.** Belegte Labels (Häufigkeit im Korpus):
`Umsatz:` · `EBITDA:` · `bereinigtes EBITDA:` (→ ab Z.8070 **`Adj. EBITDA:`**) · `EBITDA-Marge:` · `EBIT:` · `Marktkapitalisierung:` · `Mitarbeiter:` · `Gewinn:` · `EV:` · `EV-Erwartung:` · `Deal-Value:` · `Portfoliowert:` · `Eigenkapitalwert:` · `Volumen:` · `Bewertung:` · `Zielgröße:`

**C5. `bereinigtes EBITDA` → `Adj. EBITDA` (Endstand).** Chef-Änderung Z.8048; Nutzer macht daraus eine feste Regel Z.8070: „und **immer adj. ebtida anstellebreinigtes**". *Vorher-Stand: „bereinigtes EBITDA" (Z.1465 Best Secret, Z.6332 Toolport). Der Chef selbst war noch inkonsistent (Z.8061).*

**C6. Keine Jahres-/Perioden-Labels an den Financials (Endstand).** Nutzeranweisung Z.3019: „überarbeite nochmal … und **bei den financials das jahr weglassen nur umsatz: oder ebitda:**". Ursprung: Chef strich „EBITDA 2026e" → „EBITDA" bei Fischer TireTech (Z.1491). Gleiches gilt für Halbjahres-Labels (Z.7582: „CPH Group – ‚Umsatz H1: 176,1 Mio. CHF' … dasselbe Muster wie ‚2026e' … Entweder ‚Umsatz: 176,1 Mio. CHF' oder ganz weglassen").
*Regel-Evolution: In frühen Listen standen „Umsatz 2026e:" / „EBITDA 2026e:" (Z.1478/1479, GBC/bpc), und der Chef ließ sie dort stehen — Z.1548: „das bestätigt nochmal, dass es keine feste Regel ist, sondern situativ/inkonsistent gehandhabt wird". Ab Z.3019 gilt die Weglass-Regel.*

**C7. Näherungswerte immer mit `~` direkt vor der Zahl** (156 Belege), nie „ca.", nie „etwa"; „rund" nur in seltenen Ausnahmen. Beispiele: „EBITDA: ~96 Mio. EUR", „Marktkapitalisierung: ~367 Mio. EUR", „Mitarbeiter: ~6.200".

**C8. Ober-/Untergrenzen mit `<` bzw. `>` statt „bis"/„über".** Z.100: „Unpräzise Näherungen präzisieren: ‚EBITDA: bis 20 Mio. EUR' → ‚**EBITDA: <20 Mio. EUR**'". Belege im Korpus: „EBITDA: >15 Mio. EUR", „Umsatz: >2 Mrd. EUR", „EBITDA: >50 Mio. EUR", „Zielgröße < 15 Mio. CHF Umsatz" (Z.2266), „Zielgröße < 2 Mio. CHF EBITDA" (Z.2275). *Schreibweise schwankt zwischen `<20` (ohne Leerzeichen, in Labels) und `< 15` (mit Leerzeichen, in Zielgrößen-Angaben) — siehe offene Punkte.*

**C9. Abkürzungen bevorzugt.** Z.99: „‚mit rund 30 Mio. EUR Primärerlös' → ‚**i.H.v. 30 Mio. EUR**'". Z.107: „Abkürzungen wie ‚i.H.v.' nutzen." Weitere: `u.a.`, `ggf.`, `Adj.`, `2R` wird ausgeschrieben („zweite Bieterrunde").

**C10. Zahlenbereiche — Endstand (Z.1497/5304/5381):**
- **Finanzbeträge: Ziffern mit Bindestrich**, kein Leerzeichen: „140-150 Mio. EUR", „600-700 Mio. CHF", „20-30 Mrd. EUR", „5-7,5 Mrd. EUR", „400-500 Mio. USD", „2-2,5 Mrd. EUR", „45-46 Mio. CHF".
- **Kleine Stück-/Anzahl-Größen: ausgeschrieben** — „zehn bis zwölf Uhrenkomponenten-Herstellern", „zehn bis zwanzig Mitarbeitern", „sechs bis zwölf Monaten", „zwei bis drei Jahre", „fünf bis zehn Zukaufszielen", „drei bis vier".
*Regel-Evolution: Ursprüngliche „Regel 7" lautete generell „Zahlenbereiche ausschreiben" (Z.1495). Chef schrieb „zwischen zehn und fünfzig Mio. EUR" zu „**zwischen 10-50 Mio. EUR**" um → Regel gespalten (Z.1499: „Ziffern bei Finanzbeträgen, ausgeschrieben bei Stück-/Anzahl-Größen").*

**C11. Grammatik bei Bereichen:** entweder „zwischen X **und** Y" oder „X **bis** Y" — nie mischen. Z.1456: „‚zwischen zehn bis fünfzig' ist falsch kombiniert".

**C12. Prozent-/Stake-Angaben:** Ziffer + `%` ohne Leerzeichen. Als Attribut mit Bindestrich: „5%-Beteiligung an", „über 24%-Beteiligung", „50,05%-Beteiligung". Als Objekt: „Erwerb von 65% an Quabus", „Burda hält ~88%", „EBITDA-Marge: ~28%".

**C13. Mitarbeiterzahl ist ein vollwertiger Financials-Anker**, wenn kein Umsatz/EBITDA vorliegt (Z.265, Z.496, Z.1329): „Als Financials-Anker nutze ich Mitarbeiterzahl (25), da kein belastbarer aktueller Umsatz vorliegt".

**C14. Unpräzise Quellenangaben sinngemäß übernehmen statt Zahlen erfinden.** Z.2093: „Die ‚mid-double-digit million-euro'-Umsatzangabe ist unpräzise aus der Quelle – ich hab sie sinngemäß übernommen statt eine Zahl zu erfinden" → im Eintrag: „Umsatz: mittlerer zweistelliger Mio.-EUR-Bereich" (Z.2264). Z.5265: unspezifizierte „annual earnings" → neutral als „Gewinn" labeln, nicht als EBITDA.

---

## D) SATZBAU & WORTWAHL

**D1. Aktiv statt Passiv.** Z.97: „Passiv → Aktiv wo möglich: ‚wird … zum Verkauf geprüft' → ‚**prüft … einen Verkauf**' (Jäger Pharma)".

**D2. Timing als Präpositionalphrase in den Hauptsatz, nie als komma-angehängter Nachsatz (Z.81–85).** Drei V1→V2-Belege:
- Smartemis (Z.82): „bereitet Verkaufsprozess vor, Launch für 2027 geplant" → „bereitet Verkaufsprozess **für 2027** vor"
- Güntner (Z.83): „wird zum Verkauf vorbereitet, Prozessstart nach Sommerpause erwartet" → „wird … zum Verkauf **nach Sommerpause** vorbereitet"
- GetYourGuide (Z.84): „bereitet Börsengang vor, Notierung für Ende 2026/Anfang 2027 anvisiert" → „bereitet Börsengang **für Ende 2026/Anfang 2027** vor"
- Anwendung HelloBetter (Z.308): „prüft Verkauf **mit Start im Juli**" → „prüft Verkauf **ab Juli**"

**D3. Objekt direkt ans Verb, Nebensatz/Umstandsangabe ans Ende.** Z.98: „‚erwägt nach Aktienplatzierung … Zukäufe' → ‚**erwägt Zukäufe** nach Aktienplatzierung …'"

**D4. Kein Satz ohne finites Verb.** Z.306/307: „‚in zweiter Bieterrunde' braucht ein ‚**befindet sich**', sonst hängt der Satz in der Luft"; „‚im laufenden Verkaufsprozess' → ‚**befindet sich** im laufenden Verkaufsprozess'". Später auch Z.2229 zur autmatec-Zeile: „hier fehlt das Verb komplett … macht den Satz informationsärmer als sonst."

**D5. Attributionsphrasen streichen** („laut CEO", „laut Bericht", „laut CEO X"). Chef-Korrekturen Z.1495 (Doppstadt „laut CEO" gestrichen), Z.4616–4618:
- „laut Bericht vor Erwerb" → „**steht vor Erwerb**" (Viessmann)
- „könnte laut CEO künftigen Börsengang" → „**könnte künftigen Börsengang**" (Burgermeister)
- „nehmen laut CEO Orlopp Gespräche auf" → „**nehmen Gespräche auf**" (Commerzbank)
**Ausnahme (Z.4769):** „Wenn die Aussage einer namentlich genannten Führungsperson die eigentliche Nachricht ist (hier: Earnings-Call-Statement), bleibt die Attribution drin. Gestrichen wird sie nur, wo sie bloß Beiwerk ist (‚laut CEO erwägt X Zukäufe')." — Belegt: Commerzbank/Orlopp ließ der Chef stehen.
*Randnotiz (Z.8057): Beim Metzler-Eintrag stellte der Chef auf vollen Namen + Attribution ans Satzende um („erwägt Zukäufe laut Franz von Metzler") — der Nutzer hat diese Regel ausdrücklich verworfen (Z.8070: „das von metzler regel kannst du weglassen").*

**D6. Präposition `via`/`über` bei Beteiligungsketten.** Ursprungsregel Z.96: „‚über' → ‚**via**' bei Beteiligungsketten (Audi/Porsche-Beispiel) – Englisch auch für diese Präposition, nicht nur für Fachbegriffe."
*In den finalen Listen dominiert aber „über": „Valu Invest treibt **über** Plattform SB Holding weitere Zukäufe … voran" (Z.2275). → siehe offene Punkte.*
**Wichtige Einschränkung (Z.4646):** „Das ‚über [Plattform]'-Konstrukt gehört **nur dorthin, wo der Investor tatsächlich durch die Plattform zukauft** (Bregal/MDT, Valu Invest/SB Holding, Helveon/Bubbles Crèches, Family Trust/TerraBrix) – **nicht wenn er sie verkauft**." Verkauft der Investor, gilt „X treibt Verkauf von Y voran" (Z.4642/4644, Nord Holding/LivEye, Greenpeak/CERTANIA).

**D7. Bevorzugte Verben (Häufigkeiten im Korpus).** Sponsor/Investor als Subjekt: **treibt … voran** (77), **bereitet … vor** (38), **startet** (36), **führt** (46), **verschiebt**, **belebt … wieder**, **legt … vor**, **meldet**. Unternehmen als Subjekt: **prüft** (77), **erwägt** (41), **plant** (39), **sucht** (27), **sondiert** (9), **befindet sich in/im**, **erreicht** (zweite Bieterrunde), **sammelt** (Gebote), **erhält** (Übernahmeangebote), **zeigt sich offen für**, **verfolgt** (Bolt-on-Zukäufe), **erwartet**, **hält an … fest**, **steht vor**.
Signalwirkung des Verbs ersetzt Unsicherheits-Zusätze (Z.24): „reicht ‚treibt voran' im Verb schon als Signal – ‚Launch 2026/2027 möglich' wäre redundant."

**D8. Anglizismen/Fachbegriffe werden unübersetzt verwendet**, wo sie M&A-Standard sind: Bolt-on(s), Carve-out, Buy-and-Build, Bieterrunde/2R, Sell-side, Buy-side, Global Coordinator(s), Deal-Value, EV, Stake, Frontrunner, Exit, Spin-off, IPO, Teaser/IM, LTL-Netzwerk, TIC, DiGA, BESS, HDD.

**D9. Deutsch für Prozessbegriffe:** „Zukäufe", „Verkaufsprozess", „Bieterrunde", „Übernahmeangebot", „Bewertung", „Zielgröße", „Verkaufsgespräche", „Mehrheits-/Minderheitsbeteiligung".

**D10. `Börsengang` vs. `IPO`.** Standard im Korpus ist **Börsengang**; der Chef hat zweimal auf **IPO** umgestellt (Z.6046 KNDS: „bereitet erneuten Börsengang für das September/Oktober-Fenster vor" → „bereitet erneuten **IPO** für September/Oktober vor"; Z.8045 Autodoc: „hält an Börsengangsplänen fest" → „hält an **IPO** fest"). Endstand (Z.8068): „beim nächsten Briefing wende ich **‚IPO'** … direkt an." → **IPO ist der Endstand.**

**D11. Länderkürzel auch im Fließtext**, nicht nur in der Klammer. Chef-Korrektur Z.8046: „Blejkan – ‚Zukäufe … in Deutschland' → ‚in **DE**'".

**D12. „Fokus" wird mit `mit` angebunden, nicht per Komma.** Nutzer-Feedback Z.672: „feedback bei dem war dass ein mit vor Fokus soll" → Z.675: „…Uhrenkomponenten-Herstellern **mit Fokus Schweiz**". Begründung Z.677: „Liest sich runder, weil ‚Fokus Schweiz' so als Adjektiv-Phrase … andockt, statt als eigener, leicht abgehackter Nachsatz zu wirken." *(Ältere Zeilen führen noch „, Fokus Schweiz".)* Ebenfalls belegt: „mit Fokus auf Power-Plattformen, BESS und LNG-Assets in Europa" (Z.1472).

**D13. Bieterlisten: `Bieter u.a. X, Y, Z` — ohne „von", ohne wertende Adjektive.**
- „Finalisten" → „**Bieter**" (Chef-Entscheidung Z.1375; Claudes Vorschlag „verbliebene Bieter" wurde verworfen).
- „Interessenten u.a." → „**Bieter u.a.**" (Z.1414).
- **Wortwiederholung vermeiden:** steht „Bieterrunde" schon im Satz, entfällt „Bieter": „erreicht zweite Bieterrunde, Bieter u.a. Apleona…" → „erreicht zweite Bieterrunde **mit u.a.** Apleona…" (Z.1493/1546). Regel Z.1546: „Nur wenn das Wort ‚Bieter' noch nicht im Satz vorkam, wird ‚Bieter u.a.' verwendet – sonst reicht ‚mit u.a.'".
- **Kein Komma vor „mit u.a."** (Z.2165): „‚erreicht zweite Bieterrunde, mit u.a.' … für Konsistenz würde ich das Komma rausnehmen".
- **Kein „von" nach „u.a."** (Z.4601): „SK Pharma nutzt ‚u.a. **von** Chequers Capital…' während alle anderen Bieterlisten ohne ‚von' auskommen … Für Einheitlichkeit würde ich ‚von' streichen."
- Aufzählung: Komma zwischen allen, letztes Paar mit „und" — „Bieter u.a. Apleona **und** OMS Prüfservice"; bei langen Listen auch rein kommagetrennt: „Bieter u.a. CPE, Boyu, Hillhouse, HSG".

**D14. Redundante Füllwörter streichen.** Z.1382: „Marx Krontal: ‚laufenden' vor Verkaufsprozess raus (**redundantes Füllwort**)". Z.1420: „Doppstadt – ‚im Bereich' ist Füllwort, kann direkt raus". Z.1418: „‚mit strategischen und PE-Interessenten' raus – redundant, da ‚Bieterrunde' das schon impliziert".

**D15. Keine Erfindung von Fakten.** Z.537: „wir … nie einen Berater ergänzen, der in der Quelle nicht auftaucht." Z.658: „noch nicht fix mandatiert … daher kein ‚Global Coordinators'-Label, … um nichts zu erfinden."

---

## E) BERATER-FELD

**E1. Position: immer am Satzende, direkt vor der Quelle**, nach einem Komma. Nie mitten im Satz. Z.5955: „Aktuell steht der Name mitten im Satz ohne Label, während du sonst **Berater immer ans Ende mit Label** setzt."

**E2. Label-Wahl:**
| Fall | Label |
|---|---|
| Verkaufsprozess / Auktion / Exit | `Sell-side Berater:` |
| IPO / Börsengang, mehrere Banken | `Global Coordinators:` |
| IPO, nur eine Bank | `Sole Global Coordinator:` |
| Berater eines einzelnen Bieters | `Buy-side Berater:` |
| generisches „Berater:" | **verboten** (siehe E3) |

Belege: Z.12 „Hier bewusst ‚Global Coordinators' statt ‚Sell-side Berater', weil es ein IPO ist und die Meldung explizit die Global Coordinators nennt"; Z.20 „‚Sell-side Berater: Cantor' → ‚**Sole Global Coordinator: Cantor**' … sonst hast du zwei Label für dasselbe Konzept"; Z.5957 „**Buy-side Berater: Nomura**".

**E3. „Berater:" allein ist nicht zulässig — immer „Sell-side Berater:" bzw. „Global Coordinators:".** Nutzeranweisung Z.3019: „überarbeite nochmal dass du **immer sell siode berate als berater schreibst**". Konsistenzprüfungen, die das durchsetzen: Z.4594–4600 (EFB-Elektronik, Wella, August Hildebrandt, firstcolo, Evonik C4), Z.4686 (CVC DIF/firstcolo), Z.5937/5938 (EUTOP, Siemens Energy).
*Regel-Evolution: frühe Einträge nutzten noch „Berater: Konzept Nachfolge", „Berater: Clairfield", „Berater: Piper Sandler" (Z.1241/1245/1251) — überholt.*

**E4. Mehrere Berater:** Komma zwischen allen, **„und" vor dem letzten**. Belege: „Global Coordinators: Deutsche Bank, JPMorgan **und** Goldman Sachs" (Z.1474); „Sell-side Berater: Morgan Stanley **und** Macquarie" (Z.1469); „Sell-side Berater: Baird **und** Jefferies" (Z.4644); „Global Coordinators: Goldman Sachs, JPMorgan **und** Morgan Stanley" (Z.2272).

**E5. Nur führende Berater nennen; Nebenberater weglassen.** Z.22: „dein Format bei Sell-side-Deals … nennt meist nur den führenden Berater und nicht jeden Nebenberater. … wenn Lilja nicht der Global Coordinator ist, raus damit." Bestätigt Z.282: „Lilja & Co … ist kein Global Coordinator, sondern eine separate Beraterrolle, passt also laut deiner eigenen Kürzungsregel (nur führende Berater/Global Coordinators rein) nicht rein."

**E6. Kein Berater in der Quelle = kein Berater-Feld** — kein Platzhalter. Z.544: „**Kein Berater im Text = kein Berater im Eintrag.** … aktuell lassen wir das Feld einfach ganz weg." Betrifft typischerweise „prüft/erwägt/sucht Zukäufe"-Fälle (Z.539).

**E7. Ausnahme:** Sagt der Artikel explizit, dass **kein** Berater mandatiert ist, wird das als Textbaustein statt Berater-Feld gesetzt: „…prüft Verkauf ab Juli, **ohne externen Berater**" (Z.1480, HelloBetter).

**E8. Berater-Namen: Kurzform ohne Konzernzusatz.** Chef-Korrektur Z.8047: „Sell-side Berater: **Lincoln International**" → „**Lincoln**"; Nutzer macht daraus eine feste Regel (Z.8070): „sag ab jetzt bei lincoln immer lincoln". Prinzip auch Z.4702: „‚Macquarie Group' wäre die Dachgesellschaft und für ein Berater-Feld zu unspezifisch, ähnlich wie du ja auch nicht ‚Goldman Sachs Group' schreibst, sondern nur ‚Goldman Sachs'." Gegenbeispiel mit nötiger Präzision: **Macquarie Capital** (Advisory-Sparte) statt „Macquarie" (Z.4698–4704).

**E9. Berater-Namen nie fett** (siehe A9).

**E10. Kein Leerzeichen vor dem Doppelpunkt.** Fehlerbeleg Z.4683: „Wella – ‚Global Coordinators **:**' hat ein Leerzeichen vor dem Doppelpunkt".

---

## F) KÜRZUNGSREGELN — was grundsätzlich rausfliegt

**F0. Faustregel (Z.93):** „**Alles was *wie* oder *warum* im Detail beschreibt, statt *wer/was/wieviel*, kommt raus.**" Checkliste Z.106: „Radikal kürzen: nur wer/was/wieviel/wer berät – kein Warum, keine Exchange-Details, keine Zwischen-Deadlines." Verschärfung Z.1384: „Wenn ich unsicher bin, ob ein Detail rein muss, eher raus damit."

**F1. Zusatzkontext/Motivation** (Z.88): „‚organisches Wachstum bleibt Priorität' (Medacta), ‚sobald eigene Ziele erreicht sind' (Ascom)". Auch: „laut CEO Geißdörfer bislang ohne konkrete Zielobjekte" (EBM-Papst, Z.1377).

**F2. Historische Hintergrundinfo** (Z.89): „‚ursprünglich im Juni 2025 angekündigt' (Naxicap)". Weiterer Fall Z.5312: „Freenet – ‚nach abgesagtem Börsengang' ist historischer Hintergrundkontext"; Z.5946: Bertelsmann „7,7 Mrd. EUR des 10 Mrd. EUR schweren ‚Boost'-Programms bereits investiert" → kürzen auf „erwägt weitere Zukäufe in diesem Jahr".

**F3. Konkrete Zwischen-Deadlines und Timing-Nachsätze** (Z.90): „‚bis 15. Juli' (Jacobs Capital/Mammut)". Vom Chef gestrichene Beispiele (Z.4623): „erste Gebote Mitte September erwartet" (Güntner), „Prozessstart im September" (Ludwig Pfeiffer). Weitere Kandidaten derselben Kategorie (Z.4625–4628): „unverbindliche Gebote bis 28. August erwartet" (ib vogt), „Prozessstart Ende 2026 erwartet" (EFB-Elektronik), „Start gegen Jahresende erwartet" (LivEye), „außerordentliche Aufsichtsratssitzung Ende August erwartet" (Siemens Energy), „weitere Transaktionen in zwei bis drei Monaten möglich" (RTS Wind, Z.5311).

**F4. Börsensegment-/Exchange-Details** (Z.91): „‚am Frankfurter Scale-Segment' (SMAG), ‚am Nasdaq First North Growth Market' (Kanaan)".

**F5. Detaillierte Finanzierungsmechanik** (Z.92): Kapitalerhöhungs-Details bei Raymond/Deharde; die CHF-33m-Kreditlinie bei Groupe Chaumont (Z.267); die Term-Loan-Refinanzierung bei Frostkrone (Z.872).

**F6. Prognose-/Unsicherheits-Fluff** (Z.24): „Timing-Detail … Weglassen ist konsistent mit deinem SOP (du willst Kerninhalt, nicht Prognose-Fluff)."

**F7. Nicht doppelt absichern — eine Fakten-Ebene reicht** (Z.1489, Babtec): „‚vor bindenden Geboten, Deal-Value: ~150 Mio. EUR' komplett gestrichen. Auch Bieterprozess-Status und Deal-Value fliegen raus, wenn schon Bieter-Namen und Financials genannt sind – offenbar gilt: **nicht alles doppelt absichern, eine Zahl/Fakt-Ebene reicht**."

**F8. Länderlisten/Detailaufzählungen** (Z.1381): „ib vogt: Länderliste ‚(u.a. Philippinen, Malaysia)' raus, nur ‚Südostasien-Portfolio' bleibt."

**F9. Nicht-fixer Mandatsstatus** (Z.1380): „BASF: ‚Mandate an Deutsche Bank und Goldman Sachs noch nicht fix' raus."

**F10. Kennzahlen, die nicht der Kern sind** (Z.1379): „Raymond/Deharde: EV-Angabe (552,6 Mio. USD) raus, nur EBITDA bleibt."

**F11. Nachgeordnete Prozessdetails im Schlussteil** (Z.1486): Klinikum Leverkusen — „der komplette zweite Halbsatz (‚Verkäufer Alexianer prüft Vorschlag, Abschluss der Gespräche im Herbst erwartet') ist raus. Nur noch der nackte Kernfakt bleibt."

**F12. Keine Update-/Verweis-Hinweise auf frühere Einträge.** Nutzeranweisung Z.3890: „ne einfach neuereimtrag füge das hinzu **keiner weiß dass die schon mal dirn waren**" → Z.3892: „einfach als neuer Eintrag ohne Update-Hinweis, da dein Chef/die Leser den Verlauf ohnehin nicht kennen."

---

## G) ANORDNUNG / SORTIERUNG DER GESAMTLISTE

**G1. Sortierung: chronologisch ABSTEIGEND — neuester Tag zuerst.** Belege Z.302 („Sortierung nach Datum … ich hab wieder **absteigend chronologisch** sortiert wie in deinem Standardformat"), Z.311 („Finale Liste (chronologisch absteigend, einfügefertig)"), Z.356/360 („korrekt sortiert (10.07. → 06.07.)"), Z.2163, Z.5299, Z.5375.
Nutzer reklamiert Verstöße scharf (Z.358): „**das ist jetzt nicht mehr geordnet nach datum!!**"

**G2. Innerhalb eines Tages gibt es KEINE festgelegte Sekundärsortierung.** Z.16: „Reihenfolge innerhalb des Tages ist dir überlassen." Z.30: „chronologisch innerhalb eines Tages hat ohnehin keine feste Konvention in deinem SOP". Z.520: „innerhalb des 09.07. sind mehrere Einträge – das ist ok, da hast du keine feste Sekundärsortierung definiert." (Faktisch folgt die Reihenfolge meist absteigend dem Artikel-Timestamp.)

**G3. Keine Gruppierung, keine Zwischenüberschriften, keine Branchen-/Länder-Abschnitte.** Die Liste ist eine flache, durchgehende Folge von Datumszeilen (alle finalen Mails: Z.1465–1480, Z.2264–2276).

**G4. Keine Leerzeile zwischen den Einträgen** — die Zeilen folgen direkt aufeinander (verifiziert an Z.2264–2276).

**G5. Datum = Artikel-Timestamp des Mergermarket-Artikels, einzeln geprüft.** Wiederkehrende Fehlerquelle (Z.2095: „was hast du gemacht teilweise falsches datum???"). Z.2107: „bei drei Einträgen aus einem Batch achte ich … nochmal genauer darauf, **jedes Datum einzeln am Artikel-Timestamp zu prüfen** statt vom Dokument-Kontext zu übernehmen."

**G6. Gesamtaufbau der Mail — zwei Varianten:**

*(a) Nutzer → Chef (Nico an Robert), Belege Z.2207/2237/2260:*
```
Guten Morgen Robert,
<Leerzeile>
anbei das Mergermarket Briefing der letzten Woche.
<Leerzeile>
<Eintrag 1>
<Eintrag 2>
…
Viele Grüße
Nico
```

*(b) Chef → Kollegen (Endversion, „beginnt immer mit liebe kollegen", Z.1368), Belege Z.1346/1461:*
```
Liebe Kollegen,
<Leerzeile>
nachfolgend schicke ich euch die Zusammenfassung der Mergermarket Intelligence der letzten Woche.
<Leerzeile>
<Eintrag 1>
<Eintrag 2>
…
```

**G7.** Keine Einleitung mit Wochenfazit, keine Zusammenfassung, keine Statistik, kein Abschlusstext nach der Liste (in Variante b endet die Mail mit dem letzten Eintrag).

**G8. Turnus:** montags, Rückblick auf die Vorwoche (Z.37: „oich mache montags immer merger market briefing über die letzte woiche"). In der Praxis deckt eine Liste Mo–So bzw. den Zeitraum seit dem letzten Briefing ab (Z.8030: „Die Liste umfasst 38 Einträge vom 01.09. bis 14.09.").

---

## H) QUELLENANGABE

**H1. Jede Zeile endet mit einer Quellenangabe.** Zwei Stufen der Evolution:
- **Früh:** nur das Wort `Quelle` am Zeilenende (Z.28, Z.286 ff.), das in Outlook manuell per Strg+K verlinkt wurde.
- **Endstand:** Markdown-Link `[Quelle](URL)` (Z.504 ff., alle finalen Mails). Bewertung Z.522: „Quellen-Links sind jetzt eingebettet statt nur ‚Quelle' – guter zusätzlicher Mehrwert, kein Regelbruch."

**H2. Format exakt:** `[Quelle](https://mergermarket.ionanalytics.com/content/<ID>?)` — ein Leerzeichen vor der eckigen Klammer, kein Punkt danach. Die Mergermarket-Content-URLs tragen meist ein anhängendes `?` (Z.1465 ff.).

**H3. Der Link zeigt auf den Mergermarket-Artikel**, nicht auf die dort verlinkte Originalquelle.

**H4. Kopieren nach Outlook** (Z.6056): „Markdown wird dort nicht automatisch in einen klickbaren Link umgewandelt. Wenn du aus einem Markdown-fähigen Renderer kopierst …, kommt der Link meist als echter Hyperlink mit an. Falls nicht, müsstest du in Outlook manuell verlinken (Strg+K auf ‚Quelle')."

**H5. Nicht zuordenbarer Link** (Z.7233): „Wenn ich einen Link nicht eindeutig zuordnen kann, hänge ich ihn trotzdem an den Eintrag und **markiere ihn als ‚Quelle: unzugeordnet'**, statt ihn wegzulassen."

---

## EXAKTES TEMPLATE

```
TT.MM.JJ: **<Akteur/Satzsubjekt>** (<LK>, <Branche>[, Umsatz: <x,y> Mio. EUR][, EBITDA: <x,y> Mio. EUR][, <weitere Financials>][, <Eigentümer/Sponsor>]) <Verb> <Objekt/Kerninhalt>[ (<LK>, <Branche des Ziels>)][ <Präpositionalphrase Timing/Fokus>][, <Bewertung/Deal-Value>][, Bieter u.a. <A>, <B> und <C>][, Sell-side Berater: <X> und <Y>] [Quelle](https://mergermarket.ionanalytics.com/content/<ID>?)
```

Feldregeln in Kurzform:
```
TT.MM.JJ      Artikel-Timestamp, zweistelliges Jahr, danach ": " (ein Leerzeichen)
Zeilenanfang  kein Bullet, kein Spiegelstrich
Akteur        fett; wer handelt, steht vorne; Rechtsform i.d.R. weglassen
Klammer       (Land, Branche[, Financials][, Eigentümer]) — direkt hinter dem Namen
LK            2-Buchstaben-Kürzel; mehrere mit "/" ohne Leerzeichen (DE/AT)
Branche       erstes Wort groß; "/" für gleichrangige Felder; "&" statt "und"
Financials    Label + ": "; deutsches Zahlenformat; Mio./Mrd. + Originalwährung;
              "~" für Näherung; "<" / ">" für Grenzen; kein Jahres-/Perioden-Label
Verb          aktiv; Objekt direkt ans Verb; Timing als Präpositionalphrase
Bewertung     im Satz nach dem Kerninhalt, nicht in der Klammer
Bieterliste   "Bieter u.a. …" — bzw. "mit u.a. …", wenn "Bieterrunde" schon im Satz
Berater       immer am Ende; "Sell-side Berater:" / "Global Coordinators:" /
              "Sole Global Coordinator:" / "Buy-side Berater:"; nie fett;
              mehrere: Komma, letztes Paar mit "und"; fehlt in der Quelle → Feld weg
Quelle        [Quelle](URL) als letztes Element; kein Satzpunkt am Zeilenende
```

---

## TABELLE: FALSCH → RICHTIG

| # | FALSCH (V1 / Nicos Entwurf) | RICHTIG (V2 / Chef-Endfassung) | Regel | Zeile |
|---|---|---|---|---|
| 1 | „Polytech (…) Besitzer DBAG treibt … voran" | „**DBAG** treibt Verkauf von **Polytech** (…) **voran**" | Aktiver Eigentümer wird Satzsubjekt | 72 |
| 2 | „… (CH, Filterhersteller/-vertrieb, Umsatz: …), **im Besitz von Equistone**" | „(CH, Filterhersteller/-vertrieb, Umsatz: …, **Equistone**)" | Passiver Eigentümer in die Klammer | 73 |
| 3 | „… KGS … **von GENUI**" (Endphrase) | GENUI in die Klammer | Kein Eigentümer-Nachsatz | 74 |
| 4 | Financials-Klammer beim Target Deharde + Nebensatz zur Kapitalerhöhung | Käufer **Raymond** bekommt volle Klammer `(IN, …, EBITDA, EV)`, Deharde nur `(DE, Branche)`; Finanzierungsdetails raus | Akteur bekommt Financials | 69 |
| 5 | „bereitet Verkaufsprozess vor, **Launch für 2027 geplant**" | „bereitet Verkaufsprozess **für 2027** vor" | Timing in den Hauptsatz | 82 |
| 6 | „wird zum Verkauf vorbereitet, **Prozessstart nach Sommerpause erwartet**" | „wird … zum Verkauf **nach Sommerpause** vorbereitet" | Timing in den Hauptsatz | 83 |
| 7 | „bereitet Börsengang vor, **Notierung für Ende 2026/Anfang 2027 anvisiert**" | „bereitet Börsengang **für Ende 2026/Anfang 2027** vor" | Timing in den Hauptsatz | 84 |
| 8 | „prüft Verkauf **mit Start im Juli**" | „prüft Verkauf **ab Juli**" | Timing in den Hauptsatz | 308 |
| 9 | „wird … zum Verkauf **geprüft**" (Passiv) | „**prüft** … einen Verkauf" (Aktiv) | Aktiv statt Passiv | 97 |
| 10 | „erwägt **nach Aktienplatzierung** … Zukäufe" | „erwägt **Zukäufe** nach Aktienplatzierung …" | Objekt direkt ans Verb | 98 |
| 11 | „mit **rund 30 Mio. EUR** Primärerlös" | „**i.H.v. 30 Mio. EUR**" | Abkürzungen bevorzugt | 99 |
| 12 | „EBITDA: **bis** 20 Mio. EUR" | „EBITDA: **<20 Mio. EUR**" | Grenzen mit `<`/`>` | 100 |
| 13 | „Güntner **GmbH**" | „Güntner" | Rechtsform weglassen | 101 |
| 14 | „Schmabo (…) **in zweiter Bieterrunde**" | „Schmabo (…) **befindet sich in** zweiter Bieterrunde" | Finites Verb nötig | 306 |
| 15 | „Marx Krontal (…) **im laufenden Verkaufsprozess**" | „Marx Krontal (…) **befindet sich im Verkaufsprozess**" | Verb ergänzen + „laufenden" als Füllwort raus | 307 / 1382 |
| 16 | „…Uhrenkomponenten-Herstellern**, Fokus Schweiz**" | „…Uhrenkomponenten-Herstellern **mit Fokus Schweiz**" | „mit" vor Fokus | 672–675 |
| 17 | „**Finalisten** u.a. CPE, Boyu, Hillhouse, HSG" | „**Bieter** u.a. CPE, Boyu, Hillhouse, HSG" | Kürzeste, neutrale Variante | 1375 |
| 18 | „erreicht zweite Bieterrunde**, Bieter u.a.** Apleona…" | „erreicht zweite Bieterrunde **mit u.a.** Apleona…" | Keine Wortwiederholung, kein Komma | 1493 / 1546 / 2165 |
| 19 | „erreicht zweite Bieterrunde **mit strategischen und PE-Interessenten u.a.**" | „erreicht zweite Bieterrunde **mit u.a.**" | Redundanz zu „Bieterrunde" | 1418 |
| 20 | „u.a. **von** Chequers Capital…" | „u.a. Chequers Capital…" | Kein „von" nach „u.a." | 4601 |
| 21 | „Zukäufe **im Bereich** zehn bis fünfzig Mio. EUR Umsatz" | „Zukäufe **zwischen 10-50 Mio. EUR Umsatz**" | Füllwort raus + Ziffern bei Geldbeträgen | 1420 / 1495 |
| 22 | „zwischen zehn **bis** fünfzig" | „zwischen zehn **und** fünfzig" bzw. „10-50" | „zwischen X und Y" / „X bis Y" nie mischen | 1456 |
| 23 | „erwägt **laut CEO** Zusammenschluss…" | „erwägt Zusammenschluss…" | Attribution streichen | 1495 |
| 24 | „steht **laut Bericht** vor Erwerb" | „**steht vor Erwerb**" | Attribution streichen | 4616 |
| 25 | „könnte **laut CEO** künftigen Börsengang…" | „könnte künftigen Börsengang…" | Attribution streichen | 4617 |
| 26 | „EBITDA **2026e**: ~25 Mio. EUR" | „**EBITDA**: ~25 Mio. EUR" | Kein Jahreslabel | 1491 / 3019 |
| 27 | „Umsatz **H1**: 176,1 Mio. CHF" | „Umsatz: 176,1 Mio. CHF" (oder ganz weg) | Kein Periodenlabel | 7582 |
| 28 | „**Berater:** Commerzbank" | „**Sell-side Berater:** Commerzbank" | Label-Pflicht | 4596 |
| 29 | „**Berater:** Bank of America und Goldman Sachs" (IPO) | „**Global Coordinators:** Bank of America und Goldman Sachs" | IPO-Label | 4597 |
| 30 | „**Sell-side Berater:** Cantor" (IPO, eine Bank) | „**Sole Global Coordinator:** Cantor" | IPO-Label, Singular | 20 |
| 31 | „…, Nomura berät CIP" (Name mitten im Satz, fett) | „…, **Buy-side Berater:** Nomura" (unformatiert, am Ende) | Berater ans Ende mit Label, nie fett | 5955–5959 |
| 32 | „Global Coordinators **:** …" | „Global Coordinators: …" | Kein Leerzeichen vor Doppelpunkt | 4683 |
| 33 | „Sell-side **erater**: Carlsquare" | „Sell-side **Berater**: Carlsquare" | Tippfehler | 4684 |
| 34 | „(**Kroatien**, Glasfasernetz, …)" | „(**HR**, Glasfasernetz, …)" | Länderkürzel statt Land | 4581–4585 |
| 35 | „Zukäufe … in **Deutschland**" | „Zukäufe … in **DE**" | Kürzel auch im Fließtext | 8046 |
| 36 | „Nord Holding … **über Plattform LivEye**…" | „**Nord Holding treibt Verkauf von LivEye** (…) **voran**" | „über [Plattform]" nur beim Zukauf, nie beim Verkauf | 4636–4646 |
| 37 | „(Mitarbeiter Zielobjekt: 550+)" innerhalb der Zeile | gestrichen | Keine Parenthese in Parenthese | 1410 |
| 38 | „…vor, Verkäufer Alexianer prüft Vorschlag, Abschluss der Gespräche im Herbst erwartet" | „…**legt Übernahmeangebot für St Remigius Krankenhaus vor**" | Nur der nackte Kernfakt | 1486–1487 |
| 39 | „…**vor bindenden Geboten, Deal-Value: ~150 Mio. EUR**, Sell-side Berater: Drake Star" | „…, Sell-side Berater: Drake Star" | Nicht doppelt absichern | 1489 |
| 40 | „Südostasien-Portfolio **(u.a. Philippinen, Malaysia)**" | „Südostasien-Portfolio" | Länderliste raus | 1381 |
| 41 | „…, **Mandate an Deutsche Bank und Goldman Sachs noch nicht fix**" | gestrichen | Mandatsstatus raus | 1380 |
| 42 | „(CH, Uhrenkomponenten**/Buy-and-Build-Plattform**, …)" | „(CH, Uhrenkomponenten, …)" | Branche knapp, Redundanz raus | 1383 |
| 43 | „(CH, **Vermögensverwaltung/Konsolidierungsplattform**, …)" | „(CH, **Asset Manager**, …)" | Branche knapp | 8050 |
| 44 | „(CH, **Wohnimmobilien Deutschland**, …)" | „(CH, **Wohnimmobilien**, …)" | Branche knapp | 8051 |
| 45 | „(PL, **g**rabenlose Rohrsanierung, …)" | „(PL, **G**rabenlose Rohrsanierung, …)" | Branche: erstes Wort groß | 8054 |
| 46 | „(DE, **ä**sthetische Medizin, …)" | „(DE, **Ä**sthetische Medizin, …)" | Branche: erstes Wort groß | 8055 |
| 47 | „hält an **Börsengangsplänen** fest" | „hält an **IPO** fest" | IPO statt Börsengang | 8045 |
| 48 | „bereitet erneuten **Börsengang für das September/Oktober-Fenster** vor" | „bereitet erneuten **IPO für September/Oktober** vor" | IPO + Kürze | 6046 |
| 49 | „Sell-side Berater: **Lincoln International**" | „Sell-side Berater: **Lincoln**" | Kurzform der Beraternamen | 8047 / 8070 |
| 50 | „**bereinigtes EBITDA**: 30 Mio. EUR" | „**Adj. EBITDA**: 30 Mio. EUR" | Endstand-Label | 8048 / 8070 |
| 51 | „Warburg Pincus hält indirekt 60% …" als eigener Schlusssatz | nur „…, **Warburg Pincus**)" in der Klammer | Stake nur wenn Kern der Nachricht | 1374 |
| 52 | „CTS Reisen … **im Bildungsreise-Segment**" | gestrichen | Redundant zur Branche | 1378 |
| 53 | „EBM-Papst … **laut CEO Geißdörfer bislang ohne konkrete Zielobjekte**" | gestrichen | Zusatzkontext raus | 1377 |
| 54 | „Raymond … EBITDA …, **EV: 552,6 Mio. USD**" | nur EBITDA | Nicht-Kern-Kennzahl raus | 1379 |
| 55 | „Elevion Group … **führt Gespräche Zukaufszielen**" | „führt Gespräche **mit** fünf bis zehn Zukaufszielen" | Grammatik/fehlendes Wort | 7572 |
| 56 | „**CSN** steht vor Entscheidung…" (Akteur ohne Klammer) | „**CSN (BR, Stahlindustrie)** steht vor Entscheidung…" | Akteur braucht Klammer | 7575 |
| 57 | „- 10.07.26: Giotto.ai …" / „• 08.07.26: Agrana …" | „10.07.26: Giotto.ai …" | Kein Bullet/Spiegelstrich | 328 |
| 58 | Liste unsortiert / 09.07. vor 10.07. | absteigend 10.07. → 06.07. | Chronologie absteigend | 358–360 |

---

## 15 FINALE MUSTERZEILEN (vom Chef freigegeben/verschickt)

Alle aus den Endversionen (Z.1465–1480 und Z.2264–2276). Fettung ist im Klartext nicht darstellbar — in Outlook wären alle Akteursnamen fett, Berater nicht.

```
13.07.26: Flix (DE, Fernbus-/Bahnverkehr, EBITDA: ~300 Mio. EUR) sondiert in frühem Stadium eine Wiederbelebung des Börsengangs, ggf. bereits 2027 [Quelle](…)

13.07.26: ib vogt (DE, PV-Anlagenentwicklung, CVC DIF) führt Verkaufsgespräche für sein Südostasien-Portfolio, Interessenten u.a. Actis und Brookfield, Sell-side Berater: UBS [Quelle](…)

10.07.26: Groupe Chaumont (CH, Uhrenkomponenten, Vam Investments) plant Zukauf von zehn bis zwölf Uhrenkomponenten-Herstellern mit Fokus Schweiz [Quelle](…)

09.07.26: Burda bereitet Verkauf von HolidayCheck (DE, Reisebuchungs-/Bewertungsplattform, Gewinn: 41,4 Mio. EUR, Marktkapitalisierung: ~367 Mio. EUR, Burda hält ~88%) vor, Sell-side Berater: Raymond James [Quelle](…)

09.07.26: Permira treibt Börsengang von Best Secret (DE/AT, Off-Price-Luxusmode/Online-Plattform, Umsatz: 1,53 Mrd. EUR, bereinigtes EBITDA: 239,9 Mio. EUR) voran, Global Coordinators: Deutsche Bank, JPMorgan und Goldman Sachs [Quelle](…)

08.07.26: Agrana (AT, Lebensmittelzutaten, Marktkapitalisierung: 737,4 Mio. EUR) erwägt Zukäufe für Sparte Food & Beverage Solutions [Quelle](…)

08.07.26: Marx Krontal Partner (DE, Ingenieurberatung/Infrastruktur & Tragwerksplanung, Umsatz: 17 Mio. EUR, EBITDA: 5,3 Mio. EUR) befindet sich im Verkaufsprozess, Sell-side Berater: Translink [Quelle](…)

06.07.26: HelloBetter (DE, digitale Therapeutika/DiGA, Umsatz: ~10 Mio. EUR) prüft Verkauf ab Juli, ohne externen Berater [Quelle](…)

19.07.26: Klinikum Leverkusen (DE, Krankenhausbetreiber, Mitarbeiter: 2.950) legt Übernahmeangebot für St Remigius Krankenhaus vor [Quelle](…)

16.07.26: Carlyle sondiert Carve-out der Medtech-CMO-Sparte von Acrotec (CH, Präzisionskomponenten, EBITDA: 40-45 Mio. EUR), Berater: Piper Sandler [Quelle](…)
    ↑ Altstand: „Berater:" — nach der heutigen Regel „Sell-side Berater: Piper Sandler"

15.07.26: DPG Deutsche Elektro Prüfgesellschaft (DE, Elektroprüfdienstleistungen, EBITDA: ~10 Mio. EUR) erreicht zweite Bieterrunde mit u.a. Apleona und OMS Prüfservice, Sell-side Berater: Lincoln International [Quelle](…)

15.07.26: Emeram verschiebt Exit-Pläne für Frostkrone (DE, Tiefkühl-Fingerfood, EBITDA: ~40 Mio. EUR) nach gescheitertem Verkaufsprozess mit Baird [Quelle](…)

24.07.26: Helveon treibt mit Bubbles Crèches (CH, Kinderbetreuung) Konsolidierung des Schweizer Kinderbetreuungsmarkts voran, Zielgröße < 15 Mio. CHF Umsatz [Quelle](…)

22.07.26: One Equity Partners treibt Börsengang von SGB-SMIT (DE, Stromtransformatoren, EBITDA: 300 Mio. EUR) voran, Bewertung 5-7,5 Mrd. EUR, Global Coordinators: Goldman Sachs, JPMorgan und Morgan Stanley [Quelle](…)

22.07.26: Siemens Energy (DE, Energietechnik) prüft Verkauf der Sparte Transformation of Industry (Umsatz: 5,7 Mrd. EUR, EBIT: 646 Mio. EUR), Sell-side Berater: Goldman Sachs [Quelle](…)

20.07.26: Valu Invest treibt über Plattform SB Holding weitere Zukäufe von Schädlingsbekämpfungsunternehmen im DACH-Raum voran, Zielgröße < 2 Mio. CHF EBITDA [Quelle](…)

21.08.26: Saubermacher Österreich (AT, Abfallwirtschaft, Umsatz: 508 Mio. EUR) meldet Erwerb von 65% an Quabus (AT, Abwasserentsorgung/Tiefbau) zur Kartellprüfung an [Quelle](…)

21.08.26: Obersteirische Molkerei (AT, Molkerei, Umsatz: 160 Mio. EUR) führt vertiefte Fusionsgespräche mit Berglandmilch (AT, Molkerei, Umsatz: 1,3 Mrd. EUR) [Quelle](…)
```

---

## REGEL-EVOLUTION (Kurzchronik)

| Regel | Früher Stand | Endstand | Zeile |
|---|---|---|---|
| Zeilenanfang | „- " / „• " | nacktes Datum, kein Zeichen | 328 |
| Quelle | Wort „Quelle" | `[Quelle](URL)` | 504 / 522 |
| Berater-Label | „Berater: X" zulässig | immer „Sell-side Berater:" / „Global Coordinators:" | 3019 / 4594 |
| Stake-Zahl | eigener Satz am Ende + Name in Klammer | nur Name in Klammer, Stake nur wenn Kern der Nachricht | 80 → 1374 |
| Zahlenbereiche | generell ausschreiben („Regel 7") | Ziffern bei Geldbeträgen, ausgeschrieben bei Stückzahlen | 1495 → 1499 |
| Jahreslabel | „Umsatz 2026e:" toleriert | kein Jahres-/Periodenlabel | 1491 → 3019 |
| Bieterliste | „Finalisten u.a." / „Interessenten u.a." | „Bieter u.a." bzw. „mit u.a." | 1375 / 1414 / 1546 |
| Fettung | nicht geregelt | Akteure fett, Berater nie fett | 3117–3126 |
| „Fokus …" | „, Fokus Schweiz" | „mit Fokus Schweiz" | 672–677 |
| Bereinigtes EBITDA | „bereinigtes EBITDA" | „Adj. EBITDA" | 8048 / 8070 |
| Beratername | „Lincoln International" | „Lincoln" | 8047 / 8070 |
| Börsengang | „Börsengang" | „IPO" | 6046 / 8045 / 8068 |
| Land im Fließtext | „in Deutschland" | „in DE" | 8046 |
| Update-Einträge | Hinweis „Fortschreibung von …" | neuer eigenständiger Eintrag ohne Verweis | 3890–3892 |

---

## OFFENE / UNKLARE PUNKTE

1. **`via` vs. `über`** — Regel Z.96 fordert „via" bei Beteiligungsketten („‚über' → ‚via'"), aber sämtliche freigegebenen Endfassungen verwenden **„über"** („Valu Invest treibt **über** Plattform SB Holding … voran", Z.2275). Die „via"-Regel scheint faktisch nie angewendet worden zu sein. Klärungsbedarf.
2. **`<`-Schreibweise uneinheitlich:** in Financials-Labels ohne Leerzeichen („EBITDA: <20 Mio. EUR", „EBITDA: >15 Mio. EUR"), bei Zielgrößen mit Leerzeichen („Zielgröße < 15 Mio. CHF Umsatz", Z.2266). Keine explizite Festlegung im Chat.
3. **Sekundärsortierung innerhalb eines Tages** ist explizit nicht definiert (Z.16, Z.30, Z.520). Faktisch meist absteigender Artikel-Timestamp, aber ohne Regelstatus.
4. **Deal-Value-Position:** Regel „Bewertung im Satz" (Z.4666) steht gegen die Mammut-Altzeile „Deal-Value: 600-700 Mio. CHF" in der Klammer (Z.4674). Empfehlung im Chat: auf „im Satz" vereinheitlichen; nie beschlossen.
5. **`Adj. EBITDA` vs. `bereinigtes EBITDA`:** Nutzer hat „immer Adj. EBITDA" angeordnet (Z.8070); der Chef selbst war in derselben Mail inkonsistent (Z.8061: „‚Adj. EBITDA' nur bei Peach Property, während Ondal, Ludwig Pfeiffer, Toolport und Tricise weiterhin ‚bereinigtes EBITDA' haben").
6. **`Lincoln` vs. `Lincoln International`:** Nutzeranweisung Z.8070 gilt für Lincoln; der Chef hatte es nur an einer Stelle gekürzt (Z.8062). Ob die Kurzform generell für alle Beraternamen gilt (z.B. „Macquarie" vs. „Macquarie Capital", Z.4698–4704), ist nicht abschließend geklärt — dort wurde die *längere*, präzisere Form empfohlen.
7. **`Börsengang` → `IPO`:** Bei zwei Belegen (Z.6046, Z.8045) als Endstand übernommen (Z.8068), aber in derselben Liste stehen weiterhin „Börsengang"-Zeilen (Mahle, Wella, Gategroup, Thyssenkrupp, SGB-SMIT — Z.6048). Umstellung ist beschlossen, aber nicht rückwirkend durchgesetzt.
8. **Metzler-Attributionsmuster** („erwägt Zukäufe laut Franz von Metzler", voller Name + Attribution ans Satzende, Z.8057) wurde vom Nutzer ausdrücklich verworfen (Z.8070) — die allgemeine Attributions-Streichregel (D5) bleibt maßgeblich.
9. **Akteurs-Klammer bei Nicht-DACH-Verkäufern:** Claude forderte „CSN (BR, Stahlindustrie)"; der Chef ließ CSN ohne Klammer stehen (Z.8063: „CSN hat er ohne Akteurs-Klammer gelassen … beides Punkte, die ihn offenbar nicht gestört haben"). Damit ist die Klammer beim Akteur *erwünscht, aber nicht zwingend*.
10. **Periodenlabel „Umsatz H1":** Claude forderte Streichung; der Chef ließ es stehen (Z.8063). Widerspruch zu C6 nicht aufgelöst.
11. **Typo im Chef-Text:** „Essenslieferplattform" → „Essenlieferplattform" (Z.6044) wurde als Tippfehler des Chefs eingestuft, nicht als Regel — korrekt bleibt „Essenslieferplattform".
12. **Fettung im Klartext:** Die Fettung entsteht erst in Outlook. Ob der Skill Markdown-Fettung (`**…**`) ausgeben soll oder unformatierten Text, ist im Chat nie festgelegt worden (Z.5313 legt manuelles Formatieren in Outlook nahe).
