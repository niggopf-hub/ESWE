# Review: Stadtwerke-M&A-Unterlage-Skill

Stand: 7. September 2026 · Prüfobjekt: `stadtwerkemaunterlage.skill`

## Gesamturteil

**Als betreutes Arbeitsgerüst brauchbar; für die verlässliche Erstellung und Freigabe kundenfertiger Unterlagen noch nicht ausreichend.**

Der Skill bildet viel von deiner tatsächlichen Arbeitsweise ab: Quellenorientierung, Trennung zwischen Zahlenmodell und Präsentation, vorhandene Folien statt freier Neubau, die besondere Bedeutung von Ergebnisabführung und Beteiligungsergebnis sowie der Übergang von Unternehmensanalyse zu Handlungsoptionen. Insbesondere die ESWE-Gliederung ist gut wiederzuerkennen.

Die Schwäche liegt im Übergang von Erfahrungswissen zu verbindlichen Regeln. Mehrere Regeln widersprechen einander. Manche Finanzkontrollen funktionieren für ESWE, aber nicht für DVV. Die Skripte prüfen nur einen Teil dessen, was die Abschlusscheckliste verspricht. Deshalb kann eine Unterlage eine positive Skriptmeldung erhalten, obwohl wesentliche Inhalte ungeprüft oder falsch übernommen sind.

**Die sinnvolle nächste Version sollte zuerst Beweisführung und Prüfung absichern. Mehr Textbausteine haben deutlich geringere Priorität.**

## Prüfauftrag und Vorgehen

Der Auftrag war ein Review und Test, keine Erstellung einer neuen Stadtwerkeunterlage. Die Anweisungen im Skill und in den Arbeitsdokumenten wurden als Prüfgegenstand beziehungsweise Kontext behandelt.

- **Agent 1:** alle Paketdateien, Widersprüche und technische Gegenproben für beide Python-Skripte.
- **Agent 2:** DVV und ESWE, einschließlich Arbeitsnotizen, vorhandener Präsentationen, Modelle und Abschlussunterlagen.
- **Hauptagent:** vollständige Lektüre aller 13 Skilldateien, Gegenprüfung der Kernbefunde, erneute Ausführung der 14 technischen Testfälle und der Prüfungen auf beiden Originaldecks; visuelle Kontrolle der entscheidenden DVV-Abschlussseite.
- **MD-Agent:** anschließend unabhängige Gesamtprüfung aus Managing-Director-Sicht und Priorisierung.

Die ersten beiden Agenten wurden nach Übermittlung ihrer wesentlichen Befunde durch ein Nutzungslimit beendet. Ihre angelegten Prüfdateien und Ergebnisse wurden übernommen; zentrale technische und fachliche Befunde wurden durch den Hauptagenten beziehungsweise MD-Agenten nachvollzogen. Der abschließende MD-Review wurde vollständig abgeschlossen.

Das Paket lässt sich öffnen und enthält elf Markdown-Dateien sowie zwei Python-Skripte. Die expliziten Verweise auf Dateien in `references/`, `assets/` und `scripts/` führen zu vorhandenen Zielen. Es fehlt also keine ausdrücklich referenzierte Paketdatei.

## 1. Hohe Priorität: Die Finanzkontrolle ist für DVV sachlich falsch

**Fundstelle im Skill:** `references/financial-model.md:76–86`, insbesondere „Finanzmittelfonds ./. Kassenbestand laut Bilanz“ als Nullkontrolle.

Im DVV-Konzernabschluss 2021 wird der Finanzmittelfonds ausdrücklich anders abgegrenzt:

| Bestandteil | 2021, T€ |
|---|---:|
| Kassenbestand und Bankguthaben | 31.562 |
| Kurzfristige Liquiditätsanlagen | 250 |
| Kurzfristige Kassenkredite | −43.433 |
| Finanzmittelfonds | −11.621 |

Damit beträgt Fonds minus Bilanzliquidität **−43.183 T€**. Das ist eine erklärte Definitionsdifferenz, kein Übertragungsfehler. Die Originalseite wurde gerendert und visuell gelesen. Quelle: [DVV-Konzernabschluss 2021, PDF-Seite 17, Erläuterungen zur Kapitalflussrechnung](https://github.com/niggopf-hub/DVV/blob/73e675d47f34ecd638abf510fbe5febf66eccdc0/Duisburg_HRB_1171_24.08.2026%20(3).pdf).

Bei ESWE steht dagegen ausdrücklich, dass der Finanzmittelfonds 2025 ausschließlich Bankguthaben umfasst. Hier passt die Gleichsetzung für dieses Jahr. Quelle: [ESWE Geschäftsbericht 2025, PDF-Seite 18](https://github.com/niggopf-hub/ESWE/blob/06260fa14198cde6a7d6c3147a2692a2e3c7b1b8/Geschaeftsbericht-25.pdf).

**Folge:** Eine für einen Referenzfall passende Kontrolle wurde zu einer allgemeinen Regel gemacht.

**Korrektur:** Die Kontrolle muss die veröffentlichte Fondsdefinition nachbauen. Erst die Differenz zwischen berechnetem und veröffentlichtem Fonds soll null ergeben. Bilanzliquidität, kurzfristige Anlagen und einbezogene Kassenkredite gehören in eine explizite Überleitung.

Weitere Widersprüche im gleichen Bereich:

- Input-Blätter sollen nur transkribieren, gleichzeitig sollen sämtliche Summen überall Formeln sein. Bei Rundungsdifferenzen soll wiederum die veröffentlichte Summe übernommen werden. Quellwert, errechnete Summe und erklärte Differenz brauchen getrennte Felder.
- „n. v.“ ist in der Modellreferenz zulässig, die Endcheckliste verlangt dagegen alle Kontrollen auf null.
- Historisch nicht vorhandene Zeilen sollen mit null gefüllt werden. Es fehlt die Unterscheidung zwischen tatsächlich null, nicht separat ausgewiesen, in einer anderen Position enthalten und nicht verfügbar.
- Für gerundete Daten fehlen definierte Toleranzen. Beispielsweise ergeben drei veröffentlichte Positionen zu 33,3 rechnerisch 99,9, obwohl die gerundete Gesamtsumme 100,0 sein kann. Die Quelle darf nicht still angepasst werden, um einen Nulltest zu bestehen.

## 2. Hohe Priorität: DVV und ESWE benötigen unterschiedliche Abgrenzungen und Definitionsstände

**Fundstellen im Skill:** `SKILL.md:74–81`, `references/financial-model.md`, insbesondere Kennzahlendefinitionen und Mehrgesellschaftendarstellung.

Die Orientierung am HGB-Einzelabschluss passt zu ESWE. DVV wird im vorhandenen Modell jedoch als **Konzern** dargestellt. Eine starre Einzelabschlussvorgabe würde hier die falsche wirtschaftliche Einheit wählen.

Zusätzlich widersprechen sich die DVV-Arbeitsnotizen und die tatsächlich vorhandene Mappe:

| Kennzahl 2024 | README-Arbeitsstand | Vorliegende Mappe |
|---|---:|---:|
| Net Debt | 14,0 Mio. € | 16,289 Mio. € |
| Free Cashflow | −77,3 Mio. € | +206,971 Mio. € |

Das ist **nicht automatisch ein Modellfehler**. Die Mappe dokumentiert geänderte Definitionen:

- Net Debt: Banken + Pensionen − Cash; die ältere Vergleichsrechnung zog zusätzlich bestimmte Forderungen ab.
- Free Cashflow: operativer plus Investitions-Cashflow; der ältere Arbeitsstand verwendete operativen Cashflow abzüglich operativem Capex.

Der Unterschied ist für die Storyline wesentlich: In derselben Periode kann die Cashflowgröße einschließlich Investitionszuflüssen positiv sein, während die Gegenüberstellung operativer Mittel und Capex negativ ausfällt. Beide müssen eindeutig benannt werden.

Fundstellen: [DVV README, Abschnitte 3 und 5](https://github.com/niggopf-hub/DVV/blob/73e675d47f34ecd638abf510fbe5febf66eccdc0/README.md); [DVV-Finanzmodell](https://github.com/niggopf-hub/DVV/blob/73e675d47f34ecd638abf510fbe5febf66eccdc0/DVV_Konzern_Financials_2020-2025%20(1).xlsx), `Tabelle ppt_DVV!H32/H42`, `BS clean_DVV!J55` und `Quellen & Checks!A18:A19/D29:D30`. Die Werte wurden aus Formeln und gespeicherten Ergebnissen gelesen; keine vollständige Neuberechnung aller Modellzellen.

Auch der aktuelle Zeitraum ist wichtig: Die vorliegende Mappe zeigt 2025 rund **137,298 Mio. € Net Debt und 1,247x Net Debt/EBITDA**, während der Sonderstand 2024 rund 16,289 Mio. € und 0,116x beträgt. Ein allein auf 2024 beruhendes Urteil wäre unvollständig. Fundstelle: dieselbe Mappe, `Tabelle ppt_DVV!I42:I43`.

**Korrektur:** Vor der Zahlenarbeit ein verbindliches Analyseprofil festhalten: Gesellschaft beziehungsweise Konzern, Zeitraum je Rechenwerk, Modellversion, Einheiten, Net-Debt-/EBITDA-/FCF-Definition und Verhältnis zu älteren Arbeitsständen. Änderungen über eine nachvollziehbare Überleitung erklären, nicht nur eine neue Fußnote ansetzen.

## 3. Hohe Priorität: Die Finanzierungsargumentation kann ihr Ergebnis vorwegnehmen

**Fundstellen:** `SKILL.md:86–105`; `references/storyline.md:239–247, 295–298`; `references/kapitel-2-unternehmen.md:165–166`.

Der Skill enthält ausdrücklich die richtige Warnung, einen Finanzierungsengpass nicht zu konstruieren. Es wäre unfair zu behaupten, diese Gegenprüfung fehle vollständig. Gleichzeitig verlangen die Detailanweisungen:

- eine Storyline vor jeder Zahl, aber bereits konkrete Zahlenbelege zur Bestätigung;
- die Antwort „Nein“ auf die Frage, ob der operative Cashflow reicht;
- das Wort „tragfähig“ zur Verschuldung;
- die Schlussfolgerung, dass zusätzliche Kredite durch Verpflichtungen und EK-Quotenziel als Ausweg ausscheiden.

Diese Vorgaben können nicht unabhängig vom Fall gelten. Ein Verschuldungsfaktor beweist weder Tragfähigkeit noch ausgeschöpften Kreditspielraum.

**DVV ist hierfür ein relevanter Gegenfall:** Das README verlangt nach dem STEAG-Verkauf ausdrücklich eine veränderte Argumentation. Der Skill erkennt grundsätzlich alternative Bögen an, beschreibt aber keinen ausreichend konkreten Ablauf dafür. Die Arbeitsnotiz selbst bleibt ebenfalls zu prüfen: Aussagen wie „kauft zwei bis drei Jahre Zeit“ sind ohne entsprechende Rechnung keine gesicherte Reichweitenanalyse.

**ESWE zeigt die andere Seite:** Der Geschäftsbericht benennt selbst einen steigenden Finanzierungsbedarf und Grenzen reiner Bankfinanzierung. Das ist ein belastbarer qualitativer Anknüpfungspunkt, aber noch keine vollständig quantifizierte Finanzierungslücke. Quelle: [ESWE Geschäftsbericht 2025, PDF-Seiten 23 und 27](https://github.com/niggopf-hub/ESWE/blob/06260fa14198cde6a7d6c3147a2692a2e3c7b1b8/Geschaeftsbericht-25.pdf).

**Korrektur:** Vorläufige Storyline → Zahlen- und Quellenanalyse → Finanzierungsüberleitung → bestätigte Argumentation. Die Überleitung braucht denselben Zeitraum und dieselbe wirtschaftliche Einheit; außerdem verfügbare operative Mittel, Mittelbindungen, freie Liquidität, Investitionen, zugesagte Finanzierungen und Zuschüsse. Bereits im Cashflow enthaltene Abflüsse dürfen nicht erneut abgezogen werden. Fehlende Informationen bleiben offen.

Ein einfacher synthetischer Gegenfall: 100 Mio. € Investitionen über fünf Jahre gegenüber 30 Mio. € operativem Cashflow jährlich ergeben nicht schon deshalb eine Lücke, weil 100 größer als 30 ist. Die zeitgleiche Gegenüberstellung lautet zunächst 100 gegenüber 150. Dieses Beispiel ist eine logische Gegenprobe, keine DVV-/ESWE-Prognose.

## 4. Hohe Priorität: Die PowerPoint-Befüllung lässt alte Inhalte stehen

**Fundstellen:** `scripts/fill_deck.py:65–97`.

Der Textaustausch ersetzt überwiegend normale Text-Runs. Dabei wurden folgende Probleme reproduziert:

- Unterschiedliche Formatierungen innerhalb eines Absatzes werden auf den ersten Run reduziert.
- Ein alter Hyperlink am ersten Run bleibt am neuen Text erhalten.
- Feldinhalte und weiche Zeilenumbrüche bleiben stehen; beim Duplizieren des Absatzes können sie mitkopiert werden.
- Bei mehrfach vorkommenden Shape-Namen wird das erste gefundene Element geändert, ohne Mehrdeutigkeit zu melden.

Im Test blieb nach Ersetzung ein alter Feldinhalt „OLDCLIENT“ hinter „NEW“ bestehen. In einem weiteren Test zeigte der neue Text weiterhin auf die URL des alten Mandanten. Die anschließende Prüfung meldete dafür keinen Befund.

**Korrektur:** Eindeutige Zieladressen, explizite Behandlung von Text-Runs, Feldern und Hyperlinks sowie eine definierte Strategie für gemischte Formatierung. Automatisch darf nur das als erhalten gelten, was tatsächlich kontrolliert wird.

Nicht nachgewiesen wurde eine Beschädigung echter think-cell-Objekte. Diese mögliche Kompatibilitätsfrage ist separat zu testen.

## 5. Hohe Priorität: Tabellen sind eine Lücke im zentralen Arbeitsweg

**Fundstellen:** `scripts/fill_deck.py:132–134`; `scripts/inspect_deck.py:54–55, 149–157`.

Der Skill verlangt als Standard einen tabellarischen One Pager und erlaubt eine ausführliche Financial-Tabelle. Die mitgelieferten Werkzeuge bieten aber keine Tabellenzellenadressierung.

Eine Testtabelle mit „TODO“, alter URL und einem unersetzten Umsatzplatzhalter bestand `--check` ohne Befund. Der Befüllversuch wurde mit „nimmt keinen Text auf“ abgewiesen.

**Korrektur:** Tabellenzellen ausdrücklich lesen, prüfen und gezielt befüllen können. Alternativ den manuellen Bearbeitungsschritt mit anschließender Zellprüfung verbindlich dokumentieren. Dass ein Shape als Tabelle erkannt wird, ersetzt keine Prüfung seines Inhalts.

## 6. Hohe Priorität: Der Abschlussprüfer vermittelt zu viel Sicherheit

**Fundstellen:** `scripts/inspect_deck.py:175–193, 198–224, 239–247`.

Der Vergleich zählt hauptsächlich neue Shape-IDs auf positionsweise zugeordneten Folien. Reproduziert wurden:

- Neues Textfeld mit wiederverwendeter ID: Meldung „0 hinzugefügt, 0 entfernt“.
- Zusätzliche Folie: Warnung zur Folienzahl, deren neue Inhalte werden aber nicht verglichen; erfolgreicher Rückgabestatus.
- Gelöschtes Shape: wird gemeldet, Rückgabestatus bleibt erfolgreich.
- Kombination `--check --vergleich`: nur der Vergleich läuft; eine vorhandene TODO-Notiz wird dadurch nicht geprüft.
- Extrem langer Text in einer winzigen Box: Prüfung ohne Befund. Ein Render- oder Überlaufcheck fehlt.

**Auch an den echten Decks zeigt sich die Grenze:**

- `20260824_Metzler_DVV_v1.pptx`: fünf Befunde. Die falschen Kapitelkolumnen „2. evm AG“ auf Folien 14–17 werden nur ausgegeben, nicht als Fehler eingeordnet. Gleichzeitig wird „Ihre Ansprechpartner“ als unzureichender Titel beanstandet, obwohl der Skill diesen Standardtitel selbst vorsieht.
- `20240305_Stadtwerke Duisburg_v4 1 (1).pptx`: neun Befunde, darunter tatsächlich nützliche Treffer für WIP auf Folie 12 und eine Quell-URL auf Folie 13.

Quellen: [DVV-Arbeitsdeck](https://github.com/niggopf-hub/DVV/blob/73e675d47f34ecd638abf510fbe5febf66eccdc0/20260824_Metzler_DVV_v1.pptx); [alte Stadtwerke-Duisburg-Unterlage im ESWE-Repository](https://github.com/niggopf-hub/ESWE/blob/06260fa14198cde6a7d6c3147a2692a2e3c7b1b8/20240305_Stadtwerke%20Duisburg_v4%201%20(1).pptx).

**Korrektur:** Folienmanifest, erwartete Kapitelkolumnen und dokumentierte erlaubte Änderungen prüfen; Tabellen, Beziehungen und betroffene Textbereiche einbeziehen; alle gewählten Prüfungen ausführen. Visuelle Abnahme ergänzen. Ein grüner Status darf ausschließlich die tatsächlich geprüften Eigenschaften bescheinigen.

## 7. Mittlere Priorität: Referenzdateien brauchen einen eindeutigen Status

Das DVV-v1-Deck mischt bereits Duisburg-Inhalte mit evm-Texten, darunter fast 600 Mio. € Investitionen 2025–2029 und 2,6x EBITDA. Solche Angaben stehen unter anderem auf Folien 12, 15 und 16. Es eignet sich als Layout-/Arbeitsvorlage, nicht als bestätigte DVV-Zahlenquelle.

Das ESWE-Briefing fordert eine EVM-Unterlage und weitere Details aus dem Geschäftsbericht noch an. Diese Dateien liegen inzwischen im Repository. Die Notiz ist daher teilweise durch den aktuellen Materialstand überholt. Der vorhandene Geschäftsbericht enthält beispielsweise bereits Finanzmittelfonds 2025 und EK-Quote 2025, die im Briefing teilweise fehlen. Quelle: [ESWE-Briefing, Hinweis am Anfang und offene Punkte](https://github.com/niggopf-hub/ESWE/blob/06260fa14198cde6a7d6c3147a2692a2e3c7b1b8/Briefing_ESWE_Versorgungs_AG.md); Geschäftsbericht 2025, PDF-Seiten 18–19.

**Dies sind keine durch den getesteten Skill nachgewiesenermaßen verursachten Fehler.** Sie belegen, welche Situationen er zuverlässig behandeln müsste.

**Korrektur:** Dateien nach Rolle erfassen: Primärquelle, bestätigtes Modell, Layoutvorlage, historische Unterlage, Arbeitsnotiz, ungeprüfter Entwurf. Jede Rolle erhält Stand und Gültigkeitsbereich. Alte Mandantennamen projektbezogen prüfen; Beteiligungen, echte Case Studies und Vergleichsunternehmen dürfen weiterhin vorkommen.

## 8. Mittlere Priorität: Struktur und Fertigdefinition widersprechen sich

**Fundstellen:** `SKILL.md:190–192`; `references/storyline.md:308 ff., 395 ff.`; Kapitelreferenzen und Musterdokument.

Die Landkarte verbietet Ergänzungen und Auslassungen. Andere Dateien erlauben eine zusätzliche Strategie-Folie, vertiefende Beteiligungsmodelle und eine verkürzte Vorstellung bei Folgegesprächen.

Die ESWE-Abschnitte (i)–(vi) sind als inhaltliches Gerüst sinnvoll. Dass ein älteres Deck anders aufgebaut ist, macht dieses Zielgerüst nicht falsch. Der Fehler ist die fehlende Trennung zwischen **verbindlichen Inhalten und variabler Folienzahl**.

Weitere Ergänzungen:

- Teilaufgaben brauchen eigene Abläufe. Eine einzelne Zahlenfrage sollte nicht automatisch die Beschaffung einer letzten PPTX und alle Kapitelstopps auslösen.
- Die Zeitreihe erst nach Sichtung aller relevanten Jahresquellen festlegen; die Rechercheanleitung fixiert sie derzeit vor dem Schritt „aktueller Geschäftsbericht“.
- Die letzte Checkliste verlangt jede Zahl aus Abschluss/Geschäftsbericht, obwohl aktuelle Register-, Presse- und Kommunalquellen ausdrücklich vorgesehen sind.
- Für Net Debt/EBITDA bei null oder negativem EBITDA sowie für CAGR bei ungeeigneten Ausgangswerten fehlen Regeln.
- Das Skript erlaubt denselben Eingabe- und Ausgabepfad, obwohl der Skill das Überschreiben von Quellen verbietet.
- Unter Windows brach der direkte Prüfaufruf beim Pfeilzeichen mit einem Zeichenkodierungsfehler ab. Mit UTF-8-Modus ließ sich die Prüfung ausführen. Abhängigkeiten und unterstützte Aufrufweise gehören dokumentiert.

Der manuelle think-cell-Schritt ist bereits offen beschrieben. Das ist also keine versteckte Automatisierungslücke. Es fehlen jedoch eine verbindliche Übergabeliste und die Bestätigung, dass **neue Zahlen in sämtlichen Diagrammen** mit dem Modell übereinstimmen. Ein erhaltenes think-cell-Objekt kann immer noch alte Daten zeigen.

## MD-Prioritäten für die Überarbeitung

| Reihenfolge | Änderung | Woran sie abgenommen wird |
|---|---|---|
| 1 | Hypothese, Finanzierungsüberleitung und endgültige Storyline trennen | Kein vorgegebenes „Nein“ oder „tragfähig“ ohne fallbezogenen Beleg |
| 2 | Konzern/Einzelgesellschaft, Versionen und Kennzahlendefinitionen festlegen | DVV-/ESWE-Reihen sind wirtschaftlich eindeutig und nachvollziehbar |
| 3 | Kontrollen und fehlende Daten fachlich behandeln | DVV-Fondsüberleitung funktioniert; Null, fehlend und Rundungsdelta werden unterschieden |
| 4 | Tabellen, Textaustausch und Abschlussprüfer absichern | Gegenproben liefern die erwarteten Fehler oder eine kontrollierte Behandlung |
| 5 | Vorlagenstatus und fremde Inhalte prüfen | Alte evm-Zahlen werden nicht als DVV-Fakten übernommen; legitime Referenzen bleiben |
| 6 | Verbindlichen Fertigstatus definieren | Texte, Tabellen und Diagramme abgeglichen; Folien visuell abgenommen |

Danach sollte je ein vollständiger Probelauf für DVV und ESWE auf Kopien folgen. Genau diese Kombination prüft den Transfer: **DVV als Konzern mit Sondererlösen und Definitionswechseln; ESWE als Einzelgesellschaft mit Ergebnisabführung, Beteiligungsergebnis und Netztochter.**

## Technischer Testnachweis

14 isolierte Probes wurden ausgeführt. Das ist kein statistischer Qualitätswert: Einige Probes enthalten mehrere Einzelprüfungen. Zwei bestätigen funktionierende Basiseigenschaften, zwölf untersuchen reproduzierte Schwachstellen.

| Testfall | Beobachtung |
|---|---|
| Einheitlich formatierter Absatz | Zwei neue Absätze behalten 9 pt und Fettdruck: funktioniert |
| Fehlende Zieladresse | Fehlermeldung und keine Ausgabedatei: funktioniert |
| Gemischte Runs / alter Hyperlink | Formatierung vereinheitlicht; alter Link bleibt |
| Feldinhalt / Softbreak | Alter Inhalt bleibt und wird mitkopiert |
| Leere Inhaltsliste | Probelauf meldet Erfolg; Schreiben scheitert mit IndexError |
| Tabellenzelle | Ungeprüft; über vorhandene Adressierung nicht befüllbar |
| Extrem langer Text | 37.000 Zeichen in 1 × 0,2 Zoll: kein Befund |
| Doppelte Namen in Gruppen | Nur erster Treffer ersetzt |
| Langer Shape-Name | Detailausgabe kürzt auf 24 Zeichen, obwohl voller Name zur Adressierung nötig ist |
| Wiederverwendete Shape-ID | Ersatz nicht erkannt |
| Neue Folie | Warnung, aber neue Inhalte nicht verglichen |
| Gelöschtes Shape | Gemeldet, dennoch erfolgreicher Status |
| Kombinierte Prüfflags | Inhaltliche Prüfung wird übersprungen |
| Identischer Eingabe-/Ausgabepfad | Überschreiben wird zugelassen; nur an Testkopie ausgeführt |

Zusätzlich: Prüfmodus auf beiden echten Decks und Windows-Aufruf mit beziehungsweise ohne UTF-8-Modus.

## Prüfgrenzen und Quellenstand

Durchgeführt wurden statische Skillprüfung, isolierte Laufzeittests, Prüfungen auf bestehenden Decks, gezielte Modell-/Quellenvergleiche und MD-Synthese. **Nicht durchgeführt:** ein vollständiger Skilllauf von Recherche bis zu einer neu erzeugten, visuell abgenommenen Präsentation; ein vollständiger Einzelzellen-Audit sämtlicher Jahresabschlüsse; eine erfolgreiche Aktualisierung echter think-cell-Daten. Entsprechend wird keine End-to-End-Funktionsfähigkeit behauptet.

Die Aussagen beziehen sich auf die vorhandenen Unterlagen. Personen, Förderprogramme und Regulierung wurden nicht unabhängig auf den heutigen Stand recherchiert, weil kein neues Kundendeck erstellt wurde.

Die GitHub-Links sind auf die geprüften Stände fixiert:

- DVV: `73e675d47f34ecd638abf510fbe5febf66eccdc0`
- ESWE: `06260fa14198cde6a7d6c3147a2692a2e3c7b1b8`

Neben den oben verlinkten Kernbelegen wurden die vorhandenen Abschlussreihen, Modelle und Referenzunterlagen inventarisiert und textuell beziehungsweise zellbezogen erschlossen. Die entscheidende DVV-Fondsüberleitung wurde zusätzlich visuell im Original bestätigt.

Skill-Fundstellen beziehen sich auf die unverändert entpackte Datei `stadtwerke-ma-unterlage/…` im gelieferten Archiv. SHA-256 des Originals:

`C75F314AE0B23F436CF5E27B95C898D1A6157BF63871CB3FDCD08D2BCC99A7FA`

**Der Original-Skill und die GitHub-Quelldateien wurden nicht verändert.**

