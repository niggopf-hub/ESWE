# Recherche und Quellen

Alles in dieser Unterlage stammt aus öffentlich zugänglichen Quellen. Das ist die
Geschäftsgrundlage: Der Adressat hat keinen Auftrag erteilt und keine Daten geliefert.
Genau deshalb ist die Unterlage zulässig, und genau deshalb muss jede Zahl belegbar sein.

Eingabe des Skills sind die Jahresabschlüsse. Der Rest wird recherchiert.

## Inhalt

1. Quellenhierarchie in sechs Stufen
2. Jede Datei bekommt eine Rolle
3. Was aus dem Jahresabschluss zu holen ist
4. Was jede Folie braucht und wo es steht
5. Widersprüche zwischen Quellen
6. Zitierkonvention: Folie kurz, Report lang
7. Das Research-Dossier
8. Grenzen

---

## 1. Quellenhierarchie in sechs Stufen

In dieser Reihenfolge, Abbruch, sobald ein Beleg sitzt. Eine Zahl aus Stufe 5 wird nicht
gesucht, wenn Stufe 1 sie liefert.

| Stufe | Quelle | Liefert |
|---|---|---|
| 1 | Jahresabschluss und Lagebericht aus dem Unternehmensregister, bei Versorgern „Jahres- und Tätigkeitsabschlüsse nach EnWG" | Bilanz, GuV, Kapitalflussrechnung, Anteilsbesitz, Verbindlichkeitenspiegel, Investitionen nach Bereichen, Absatz, Prognose- und Risikobericht, Steuerungskennzahlen |
| 2 | Geschäftsbericht und Pressemitteilungen auf der Unternehmenswebsite | jüngstes Jahr (oft mit vollständigem Abschluss), Strategie, Projekte, Personalien, Kundenzahlen, O-Töne |
| 3 | Beteiligungsbericht der Stadt und Ratsinformationssystem | Wirtschaftsplan, Investitionsplanung, Kapitalmaßnahmen, Wärmeplanungsbeschluss, Konzernstruktur, Ausschüttungserwartung. Hier stehen oft die Summen, die im Abschluss fehlen |
| 4 | Netzstrukturdaten und Veröffentlichungen der Netztochter | Netz-km, Zählpunkte, Netzgebiet, jährliche Pflichtveröffentlichung nach StromNEV und GasNEV |
| 5 | Handelsregister | Gesellschafter, Grundkapital, Organe, Historie |
| 6 | Fach- und Regionalpresse (ZfK, energate, Lokalzeitung) | Personalien, Projekte, Politik, Förderbescheide |

Presse ist die einzige zeitnahe Quelle, aber sie steht nicht in der Quellenzeile der Folie.
Die vf-Fassungen nennen dort nur Geschäftsberichte, Abschlüsse und
„Unternehmensinformationen". Presse belegt im Report, nicht auf der Folie.

**Den Zeitraum erst festlegen, wenn Stufe 1 und 2 gesichtet sind.** Der Geschäftsbericht
enthält oft den vollständigen Abschluss des jüngsten Jahres (ESWE GB 2025: Bilanz S. 73,
GuV S. 74, Kapitalflussrechnung S. 18, Verbindlichkeitenspiegel S. 82). Dann reicht die
Reihe ein Jahr weiter als die Registerauszüge.

**Dem Dateinamen nicht trauen.** Registerportale benennen Auszüge nach Registernummer und
Abrufdatum (`Wiesbaden_HRB_2105_27.08.2026 (2).pdf`). Der Inhalt ist der Abschluss eines
Geschäftsjahres. Jede Datei öffnen, „Tag der Erstellung" und Geschäftsjahr lesen, nach
Geschäftsjahr benennen, bevor etwas übernommen wird.

**Bild-PDFs.** Konzern-Registerauszüge sind oft ZIP-Container mit Seitenbildern und
OCR-Textlayer (DVV). Geschäftsberichte betten Tabellen als Bild ein. Wo die Textextraktion
nichts liefert, die Seite rendern und lesen, statt die Quelle als unbrauchbar abzuhaken.

---

## 2. Jede Datei bekommt eine Rolle

Im Projektordner liegen Dateien sehr unterschiedlicher Verlässlichkeit nebeneinander, und
der Dateiname sagt darüber nichts:

| Rolle | Was daraus übernommen werden darf |
|---|---|
| **Primärquelle**: Abschluss, Geschäftsbericht, Registerauszug, Programmbuch, Ratsvorlage | Zahlen und Aussagen, mit Fundstelle |
| **Bestätigtes Modell**: geprüfte Mappe mit laufenden Kontrollen | Zahlen für die Folien |
| **Layoutvorlage**: die grüne DVV-vf | Struktur, Formatierung, Bauteile, Kapitel 1, keine Zahlen |
| **Sprachvorlage**: DVV-vf und ESWE-vf | Formulierungsmuster, Titel, Kommentarstruktur |
| **Historische Unterlage**: ein früher ausgeliefertes Deck desselben Mandanten | Storyline-Historie, Zahlen nur mit Datum und nur als Historie |
| **Arbeitsnotiz**: README, Briefing, Handoff | Hinweise und offene Punkte, keine belastbaren Zahlen |
| **Ungeprüfter Entwurf**: v1, v2 | nichts, bis geklärt ist, was darin geprüft wurde |

Der gefährlichste Fall: ein Arbeitsdeck, das aus einer Vorlage entstanden ist und noch
Zahlen des Vorgängerfalls trägt. Die DVV-v1 war die evm-Unterlage mit DVV-Kolumnen. Vor
der Übernahme einer Zahl aus einem Deck die Frage stellen, ob sie dort belegt oder geerbt
ist. Bei einer Layoutvorlage lautet die Antwort: geerbt.

Arbeitsnotizen veralten. Ein Briefing, das eine fehlende Datei anmahnt, die inzwischen im
Projekt liegt, ist überholt. Vor der Übernahme eines offenen Punkts prüfen, ob er noch
offen ist.

---

## 3. Was aus dem Jahresabschluss zu holen ist

| Fundstelle | Wofür |
|---|---|
| Bilanz | Vermögens- und Kapitalstruktur, EK-Quote, Bankverbindlichkeiten, Kasse |
| GuV | Umsatz, Material, Betriebsergebnis, Beteiligungsergebnis, Zinsergebnis, EBT, Ergebnisverwendung |
| Kapitalflussrechnung (oft nur die drei Salden im Lagebericht) | Cashflows, Fonds |
| Anhang: Anteilsbesitz nach § 285 Nr. 11 HGB | Beteiligungen mit Quote, Eigenkapital, Jahresergebnis, Stichtag |
| Anhang: Verbindlichkeitenspiegel | Bankverbindlichkeiten, Restlaufzeiten, verbürgte Tranchen |
| Anhang: Haftungsverhältnisse, sonstige finanzielle Verpflichtungen | Bürgschaften, Bestellobligo, Investitionsverpflichtungen (DVV: 184,9 Mio. EUR) |
| Lagebericht: Grundlagen | Geschäftsmodell, Gesellschafter, Steuerungskennzahlen |
| Lagebericht: Wirtschaftsbericht | Ergebnisentwicklung, Sondereffekte, Plan-Ist, Investitionen nach Bereichen, Absatz |
| Lagebericht: Prognosebericht | Investitionsplanung, Mittelfristplanung, EK-Ziele, Finanzierungsbedarf |
| Lagebericht: Risikobericht | Regulierung, Marktpreis, Ausfall, Cyber |
| Nachtragsbericht | neu gegründete Gesellschaften, Kapitalmaßnahmen |

Der Prognosebericht ist die wichtigste Fundstelle für die Storyline: Dort steht, ob das
Unternehmen selbst von Finanzierungsbedarf oder Eigenkapitalstärkung spricht. Wo ein solcher
Satz existiert, gehört er in den Report mit Seite, und auf die Folie in eigenen Worten.

---

## 4. Was jede Folie braucht und wo es steht

| Folie | Aus dem Abschluss | Von außen (Stufe) |
|---|---|---|
| Ausgangslage | Lagebericht: Strategie, Prognose, Klimaziel, Investitionsprogramm, Planvergleich, EAV | Website, GB (2); Ratsbeschluss Wärmeplanung, Programmbuch, Wirtschaftsplan (3); Presse (6) |
| Beteiligungsstruktur | Anhang: Anteilsbesitz mit EK und Ergebnis | Beteiligungsschema Website (2), Beteiligungsbericht (3), Handelsregister (5) |
| Kunden und Netz | Umsatz, EBITDA, EBIT, EAT, CapEx, Mitarbeiter, Umsatzaufteilung | Kundenzahlen, Absatz, Netz-km: Lagebericht oder GB (2), Netzstrukturdaten (4) |
| Financials | alles | O-Töne zu Sondereffekten aus dem GB (2) |
| Verschuldung und Invest | Net-Debt-Bausteine, Investitionen nach Bereichen, Prognosebericht, Investitionsverpflichtungen | Programmbuch, Wirtschaftsplan, Ratsvorlagen (3), Pressemitteilungen zu Projekten, Förderbescheide (2, 6) |
| Kapitel 3 Ziele | Prognose- und Risikobericht | Strategiepapiere, Vorstandsaussagen (2, 6) |

---

## 5. Widersprüche zwischen Quellen

Sie sind der Normalfall. Vier Typen:

- **Vorjahreswerte weichen ab.** Cashflow 2022 im JA 2022 anders als im JA 2023, Summe
  gleich. Der jüngere Abschluss gilt, Abweichung dokumentiert.
- **Lagebericht gegen Anhang.** Bankverbindlichkeiten, EBT. Der Anhang und die GuV gelten.
- **Abschluss gegen Website.** Mitarbeiter (Gesellschaft gegen Gruppe), Kunden (Zählpunkte
  gegen Verträge), Netzlängen (Trassen- gegen Leitungskilometer). Beide nennen, Fußnote
  erklärt die Bezugsgröße. Stillschweigend eine wählen ist die schlechteste Option; der
  Adressat kennt beide.
- **Ältere Unterlage gegen Modell.** Umsatz brutto gegen netto Stromsteuer (DVV 2022:
  5.509 gegen 5.478), ein um ein Jahr verschobener Faktor in einer alten Grafik. Vor der
  Wiederverwendung klären, nicht übernehmen.

Alle vier gehören ins Blatt `Quellen & Hinweise` des Modells und in den Report.

---

## 6. Zitierkonvention: Folie kurz, Report lang

**Auf der Folie** die Quellenzeile, wie die vf-Fassungen sie führen:

| Kapitel | Quellenzeile |
|---|---|
| 2 | Quellen: Geschäftsberichte ‹X›, Unternehmensinformationen |
| 2, Konzern mit Einzelbelegen | Quellen: ‹X›-Konzernabschluss 2025, Pressemitteilung ‹X›-Bilanz 2025, Unternehmensinformationen |
| 2, Beteiligungsstruktur | Quellen: ‹X›-Beteiligungsschema (Stand ‹Datum›), ‹X›-Konzernabschluss ‹Jahr› |
| 3 | Quellen: Metzler-Recherche, Jahresabschlüsse ‹X› ‹J1›–‹J5›, Unternehmenswebsite |

Keine Presse, keine URLs, kein „Metzler-Recherche" in Kapitel 2 (die ESWE-vf hat es
gestrichen), „Unternehmensinformationen" statt „Unternehmenswebsite".

**Fußnoten** in einer eigenen Zeile darüber, mit `1)`, `2)` nummeriert, durch Semikolon
getrennt (das ist die eine Stelle, an der das Semikolon bleibt, weil es die Konvention der
Vorlage ist). Sie tragen Definitionen (EBIT, EAT, Net Debt), Stichtage, Bezugsgesellschaften
(„Netzlängen der Netze Duisburg GmbH, Stand 2025"), Abweichungen zwischen Quellen, und den
Hinweis auf eigene Zuordnungen („Zuordnung der Geschäftsbereiche auf Basis der beschriebenen
Tätigkeit der jeweiligen Gesellschaft durch Metzler").

**Im Report** die Langfassung je Folie: Dokument, Jahr, Seite, bei Websites die URL und das
Abrufdatum, bei Ratsvorlagen die Vorlagennummer. Format:

> Umsatz 2025 474 Mio. EUR: Geschäftsbericht 2025, GuV, S. 74.
> Kommunale Wärmeplanung beschlossen Juni 2026: Magistratsvorlage 26/0412, Ratsinformationssystem Wiesbaden, abgerufen 24.09.2026.

Damit ist „Geschäftsberichte ESWE, Unternehmensinformationen" auf der Folie nachprüfbar,
ohne die Folie zu überladen.

---

## 7. Das Research-Dossier

Ergebnis von Schritt 3, ein Zwischenstopp vor der Storyline. Drei Teile:

1. **Belege je Folie** in der Langfassung aus Abschnitt 6, geordnet nach den fünf Folien
   von Kapitel 2 und den Zielen von Kapitel 3.
2. **Lückenliste**: was nicht öffentlich ist (Mittelfristplanung, Aufteilung der
   Investitionssumme, Kundenzahlen beim Konzern, Cashflow eines frühen Jahres). Jede Lücke
   mit dem Satz, wie die Folie damit umgeht (Fußnote, `n. v.`, qualitative Aussage).
3. **Widerspruchsliste**: zwei Quellen, eine Zahl, mit Entscheidung.

Das Dossier wird wortgleich Teil des Reports.

---

## 8. Grenzen

Was öffentlich nicht verfügbar ist und daher nicht behauptet wird:

- Die Mittelfristplanung im Detail (nur, was der Prognosebericht nennt)
- Die Aufteilung des Investitionsprogramms, wenn nur eine Gesamtsumme kommuniziert wurde;
  Fußnote „Keine öffentliche quantitative Aufteilung nach Investitionsschwerpunkten
  verfügbar"
- Interne Margen, Vertragsdetails, Beschaffungsstrategie
- Die politische Lage im Rat
- Bewertungen jeder Art

Wo eine Zahl fehlt, ist die Lücke offen zu zeigen statt geschätzt. Eine als Recherche
getarnte Schätzung ist der schnellste Weg, im Termin die Glaubwürdigkeit für alles andere
zu verlieren.
