# Schreibregeln

Abgeleitet aus dem Vergleich Vorversion gegen vf bei DVV, evm und ESWE, ergänzt um die
Vorgaben des Hauses. Jede Regel hat einen Beleg, an dem sie in einer Vorversion verletzt
und in der vf korrigiert wurde. `scripts/stil_check.py` prüft die mechanischen Regeln in
PowerPoint und Report.

## Zahlen und Einheiten

| Regel | Richtig | Falsch |
|---|---|---|
| Währung immer „Mio. EUR" und „Mrd. EUR", nie das Euro-Zeichen, auch nicht im Excel | 474 Mio. EUR | 474 Mio. €, T€, EUR 474 Mio. |
| Prozent als Zeichen mit geschütztem Leerzeichen, auch im Fließtext | 25 %, 50,62 % | 25 Prozent, 25% |
| Vielfache mit nachgestelltem x, ohne Leerzeichen | 1,7x | 1,7 x, 1,7-fach |
| Deutsche Zahlformatierung | 3.816 Mio. EUR, 13,2 % | 3,816 Mio. EUR, 13.2 % |
| Eine Nachkommastelle bei Mio.-Beträgen unter 100, keine darüber | 47,1 Mio. EUR, 217 Mio. EUR | 47,13 Mio. EUR |
| Negative Werte in Diagrammen und Tabellen in runden Klammern | (24) | -24, −24 |
| „rund" und „durchschnittlich" ausgeschrieben, „ca." nur in Kacheln | rund 22 Mio. EUR, durchschnittlich rund 57 Mio. EUR | ~22 Mio. EUR, Ø ~22 |
| Jahresangaben ohne Klammern im Bullet, in Klammern nur beim Vorjahr in Kacheln | Umsatz 2025 von 474 Mio. EUR | Umsatz (2025) |
| Absolute Beträge statt Prozentänderungen im Kommentar | auf 535 und 474 Mio. EUR normalisiert | um 11 % zurückgegangen |
| Spannen mit Bindestrich und Leerzeichen wie in der vf | 2,5 - 3,5 Mrd. EUR, 2025-2029 | 2,5–3,5 Mrd. EUR |

Belege: ESWE v2 „um 11 % zurück, während die Rohertragsmarge auf 27,9 % gestiegen ist"
wurde in der vf „auf 535 und 474 Mio. EUR normalisiert". ESWE v2 „Ø ~22 Mio. EUR p. a."
wurde „durchschnittlich rund 22 Mio. EUR". DVV v1 „~2.500 km" wurde „rund 2.500 km".

## Begriffe

| Regel | Richtig | Falsch |
|---|---|---|
| „Cashflow" im Text, Legenden bleiben wie im Template | operativer Cashflow, Total Cashflow | Cash Flow, Cash-Flow (im Text) |
| Einheitsname | Metzler Mergers & Acquisitions | Metzler Corporate Finance |
| Ergebnisgröße wie in der Kachel | Ergebnis nach Steuern | Jahresüberschuss, Rekordergebnis, EAT (im Bullet) |
| Kennzahlen mit Definition beim ersten Auftreten in Fußnote | EAT = Ergebnis nach Steuern, vor Ausgleichszahlung und Gewinnabführung | EAT ohne Fußnote |
| Quellenzeile Kapitel 2 | Quellen: Geschäftsberichte ‹X›, Unternehmensinformationen | Metzler-Recherche, Unternehmenswebsite, Pressequellen |
| Quellenzeile Kapitel 3 | Quellen: Metzler-Recherche, Jahresabschlüsse ‹X› ‹J1›–‹J5›, Unternehmenswebsite | |
| Der Name der Gesellschaft mit Artikel | Die ESWE, die DVV, die evm | ESWE ist, EVM ist |
| „Kundinnen und Kunden" im ersten Bullet | rund 200.000 Kundinnen und Kunden | 200.000 Kunden |

## Satzbau

**Nominalstil mit Partizip am Ende.** Der Kommentar und die Projektbullets sind keine
Sätze, sondern Feststellungen.

| Vorversion | vf |
|---|---|
| Der Umsatz ging 2025 preisbedingt um 11 % zurück, während die Rohertragsmarge gestiegen ist | Umsatz 2024 und 2025 nach dem energiepreis- und handelsbedingten Höchststand 2023 (634 Mio. EUR) auf 535 und 474 Mio. EUR normalisiert |
| Der operative Cashflow wird nahezu vollständig durch die Ergebnisabführung absorbiert, sodass die liquiden Mittel auf 2,5 Mio. EUR gesunken sind | Operativer Cashflow von durchschnittlich rund 57 Mio. EUR nahezu vollständig durch Ergebnisabführung und Investitionshochlauf gebunden |
| Die Rekordergebnisse der Jahre 2023 und 2024 waren sondereffektgetrieben | Ergebnis nach Steuern 2023 und 2024 sondereffektgetrieben, vor allem Rückstellungsauflösungen von 20,6 Mio. EUR im Jahr 2024, 2025 mit 49 Mio. EUR dennoch deutlich über Plan |

**Keine Kausalketten.** „während", „sodass", „denn", „obwohl", „um zu" verbinden zwei
Aussagen zu einer Argumentation, die der Leser nicht prüfen kann. Zwei Aussagen sind zwei
Bullets.

**Kein Semikolon im Fließtext, danach kein Großbuchstabe.** Statt Semikolon ein neuer
Bullet. Auch die vf-Dateien verstoßen an drei Stellen dagegen (ESWE-vf Ausgangslage
Bullet 4, DVV-vf zwei Projektbullets); das ist keine Lizenz, sondern ein Befund.

**Keine Gedankenstriche innerhalb von Bullets.** Der Halbgeviertstrich mit Minuszeichen
(−) trennt nur im Titel Haupt- und Nebenaussage. In Bullets ein Komma oder ein neuer
Bullet.

**Keine Klammern für Nebensätze.** „Planergebnis (33 Mio. EUR)" wurde „Planergebnis von
33 Mio. EUR". Klammern nur für Vorjahreswerte in Kacheln und Bezugswerte im Kommentar
(„Höchststand 2023 (634 Mio. EUR)").

**Keine wörtlichen Zitate aus dem Lagebericht.** Das Zitat „‚in den nächsten Jahren
nochmals erheblich steigern'" flog in der ESWE-vf raus. Die Aussage wird in eigene Worte
mit Zahl übersetzt. Ein Zitat gehört in den Report, nicht auf die Folie.

## Wortwahl

**Keine wertenden Adjektive über den Adressaten.** Gestrichen wurden: kerngesund,
investitionsintensivste Phase seiner Geschichte, konsequenter Fernwärmeausbau,
wirtschaftlichkeitsgeprüft, massiv, erheblich (als Verstärker), robust, komfortabel.
Erlaubt sind Einordnungen mit Zahl: „moderat" bei 1,7x, „niedrig" bei 1,2x, „stabil" bei
Planübererfüllung.

**Keine Prognose-Sprache in Projektbullets.** „Der erwartete Hochlauf von Wärmepumpen
erfordert erhebliche Netzverstärkung" wurde „Stromnetzausbau (UW Hölderlinstraße,
Deponiestraße) liegt in der sw netz". Was auf die Folie gehört, ist das Vorhaben, nicht
seine Begründung.

**Keine Genehmigungs- oder Gerichtshistorie.** „nach positivem VGH-Entscheid" flog raus,
„10 Anlagen, ~30 MW, ~85 GWh p. a." blieb.

**Kein Hedging in der Schlussfolgerung, wenn der Beleg da ist.** ESWE v2 „scheint nicht
finanzierbar zu sein, denn bereits 2025 waren Kapitaleinlagen erforderlich" wurde in der vf
„nicht aus dem operativen Cashflow finanzierbar, bereits 2025 Kapitaleinlage der Aktionäre
von 10 Mio. EUR erforderlich". Die Kapitaleinlage ist der Beleg; mit Beleg braucht es kein
„scheint". Ohne Beleg (evm: keine Mittelfristplanung öffentlich) bleibt „scheint".

**Beratersprache ohne Inhalt** bleibt draußen: ganzheitlich, maßgeschneidert, Synergien
heben, Mehrwert schaffen.

## Titel

Der Titel ist ein Aussagesatz. Wer nur die Titel liest, kennt die Argumentation.

| Folie | Muster (Tonlage A und B) |
|---|---|
| Ausgangslage | Die ‹X› verbindet eine starke Versorgungs- und Infrastrukturposition mit einem Transformationsprogramm von ‹Summe› |
| Beteiligungsstruktur | Die ‹X› bündelt ‹Bereiche› in einer kommunalen Konzernstruktur mit etablierten Minderheitspartnern / ist kommunal und strategisch verankert und verfügt über ein breit diversifiziertes Beteiligungsportfolio |
| Kunden und Netz | Die ‹X› erwirtschaftet ‹n› % ihres Umsatzes mit ‹Sparten› und verfügt über eine umfassende Energie- und Netzinfrastruktur |
| Financials | Stabile Ertragsbasis ‹Jahr› nach den Sondereffekten der Vorjahre, jedoch übersteigt der Investitionsbedarf die operative Cash-Generierung |
| Verschuldung und Invest | Die ‹X› ist finanziell solide aufgestellt, aber Investitionsbedarf von ‹Summe› bis ‹Jahr› mit Schwerpunkten auf ‹Segmenten› / Die ‹X› investiert bislang vor allem in den Bestand − der Investitionsbedarf für die Wärmewende steht noch bevor |

Titel, die nicht tragen: „Financials", „Überblick", „Beteiligungsstruktur",
„Handlungsoptionen". Das sind Etiketten.

## Länge

- Ausgangslage: sechs bis sieben Bullets, je ein bis zwei Zeilen.
- Kommentar Financials: vier bis sechs Bullets, je eine Zeile, plus Kasten.
- Projektbullets: maximal drei je Segment, je eine Zeile, je eine Zahl.
- Kernsatz-Kasten: ein Satz, maximal zwei Zeilen.
- Ziele-Kacheln: sieben bis zwölf Wörter.

Was nicht in die Box passt, ist zu lang, nicht die Box zu klein. Die Vorlage wird nicht
angepasst.

## Was im Report anders ist

Der Report ist Prosa und darf Sätze haben. Die Regeln zu Zahlen, Einheiten, Begriffen und
Einheitsname gelten dort genauso. Zitate aus dem Lagebericht gehören in den Report, mit
Seite. Prozentänderungen sind im Report erlaubt, wenn der absolute Wert danebensteht.
