# Arbeitsanleitung (Originalfassung des Absenders, 17.09.26)

Vom Absender aus einem parallelen Draft-Chat übergeben. **Diese Fassung ist die
maßgebliche Quelle für `SKILL.md`.** Sie ist präziser als die aus dem
Hauptchat rekonstruierten Regeln und hat bei Konflikten Vorrang.

Verbatim übernommen, nur Formatierung vereinheitlicht.

---

## (i) Aufnahme- und Ausschlusskriterien

### Aufnehmen
- Laufende Verkaufsprozesse in jeder Phase: Vorbereitung ("bereitet Verkauf vor"), Start ("startet Verkaufsprozess", "IMs verteilt"), Bieterrunden, finale Gebote, Frontrunner-Meldungen, "steht vor Übernahme".
- Zukaufsabsichten, auch ohne konkretes Ziel: "prüft Zukäufe", "erwägt Zukäufe", "zeigt sich offen für Zukäufe", "plant Zukäufe". Vage CEO-Aussagen zählen – das ist bewusst eine niedrige Schwelle.
- IPOs: Vorbereitung, Bankenmandate, Bewertungsindikationen, Verschiebungen, Wiederbelebungen.
- Carve-outs, Spin-offs, Abspaltungen, Sparten- und Teilverkäufe, Minderheitsbeteiligungen.
- Negativ-Ereignisse in laufenden Prozessen: Rückzug eines Bieters, gescheiterter Prozess, verschobener Exit. Das ist das Gegenteil eines Abschlusses und bleibt drin.
- Strategische Optionsprüfungen mit externen Beratern, Kartellanmeldungen, Fusionsgespräche.

### Ausschließen
- Insolvenz in jeder Form – vorläufige Insolvenzverwaltung, Eigenverwaltung, Schutzschirmverfahren, Nachlassstundung. Auch dann, wenn ein Investorenprozess läuft. Das ist der häufigste Ausschlussgrund, oft die Hälfte eines Batches.
- Finanzierungen: Startup-Runden (Pre-Seed bis Series D), PE-Fondsfundraising, Refinanzierungen, Debt-Pakete, Buyout-Finanzierungen für bereits verkündete Deals, syndizierte Kredite, TLB-Syndizierungen, Kreditfazilitäten.
- Abgeschlossene Deals.
- Interne Restrukturierungen ohne M&A-Bezug (Kostenprogramme, Outsourcing-Prüfungen).
- Marktkommentare, Podcasts, Personalstrategien von Banken, Fondsstrategie-Interviews ohne konkretes Ziel.

### DACH-Bezug – die schwierigste Abgrenzung
Aufnehmen, wenn Akteur oder Zielobjekt in DE/AT/CH sitzt. Nicht-DACH-Akteure kommen rein, wenn sie signifikante DACH-Präsenz oder einen expliziten DACH-Zielmarkt haben. Beispiele, die drin waren: AMiT (CZ, Zielmarkt Deutschland), Scandinavian Print Group (DK, sucht in DE), Blejkan (PL, sucht in DE), Elevion (NL, Gespräche in DE), Nortal (EE, Fokus DE), Equity House (CH, Fokus CH/DE/LU).

Draußen bleiben Fälle, in denen DACH nur eine Nennung unter vielen ist: Prosolia (Deutschland einer von fünf Solarmärkten), Invelon ("Deutschland könnte sich als Zielmarkt herausbilden"), CropX (DE einer von vier Shortlist-Ländern), Photocure und Swedencare (Skandinavier mit Europa-Fokus).

Draußen bleibt auch, wenn Akteur und Ziel beide außerhalb liegen – auch wenn ein deutscher Bieter im Rennen ist (Acea/Indaqua, Italgas/Floene, Fintyre, ARLANXEO).

### Vagheits-Schwelle
Drin: "prüft", "erwägt", "plant", "sucht", "offen für".
Draußen: explizit ablehnende Aussagen ("nicht aktiv im Verkaufsprozess", "Unabhängigkeit ist uns wichtiger"), rein hypothetische Überlegungen ohne Zeithorizont oder Budget, Absichten mit Horizont zwei Jahre plus ohne Substanz.

### Doppelmeldungen
Wenn ein Deal Wochen später mit neuem Stand wieder auftaucht: neuer eigenständiger Eintrag, ohne Verweis auf die frühere Zeile. Die Empfänger kennen den Verlauf nicht.

---

## (ii) Aufbau und Schreibweise

### Grundformat
```
TT.MM.JJ: **Akteur** (Land, Branche, Financials) Kerninhalt, Sell-side Berater: X [Quelle](URL)
```
Aufzählungszeichen: `•`. Sortierung strikt chronologisch absteigend. Das Datum stammt immer aus dem Artikel-Timestamp, nie aus dem Kontext umliegender Artikel – das war die häufigste Fehlerquelle.

### Wer bekommt die Klammer
Die Klammer mit Land, Branche und Financials gehört dem grammatischen Subjekt des Satzes, nicht automatisch dem Zielunternehmen.
- Treibt ein Investor den Prozess, wird er Subjekt: "Orlando Capital startet Verkauf von Ludwig Pfeiffer (DE, Infrastruktur-/Tiefbau, …)". Der Investor selbst bekommt keine Klammer, das Ziel die volle.
- Ist das Unternehmen selbst Akteur, steht der Eigentümer als letzter Eintrag in der Klammer: "KoRo Handels (DE, Lebensmittel-Direktvertrieb, Umsatz: 252 Mio. EUR, Kharis Capital)".
- Kauft ein Akteur, bekommt er die Klammer, das Ziel nur (Land, Branche): "Viessmann Generations Group steht vor Erwerb einer 5%-Beteiligung an FC Bayern München AG (DE, Fußballclub)".
- "über Plattform X" nur bei Zukäufen ("Bregal Unternehmerkapital erwägt über Plattform MDT Technologies …"), nie bei Verkäufen.

### Klammer-Inhalte
Land: Kürzel (DE, AT, CH, FR, IT, NL, PL, CZ, EE, DK, UK, US, BR, CN, HR, LU). Bei Doppelsitz DE/AT oder LU/DE.
Branche: großgeschrieben, auch bei adjektivischen Bezeichnungen ("Grabenlose Rohrsanierung", "Ästhetische Medizin"). Knapp halten – "Asset Manager" statt "Vermögensverwaltung/Konsolidierungsplattform".
Financials: `Umsatz:`, `EBITDA:`, `Adj. EBITDA:`, `EBIT:`, `Marktkapitalisierung:`, `Mitarbeiter:`, `ARR:`, `Portfoliowert:`, `Bewertung:`, `Deal-Value:`. Ohne Jahresangabe – kein "2026e", kein "FY25".
Währung: Originalwährung der Meldung, keine Umrechnung (CHF bleibt CHF, USD bleibt USD).
Zahlen: Finanzbeträge als Ziffern mit Bindestrich ("13-15 Mio. CHF", "600-700 Mio. CHF"). Kleine Stückzahlen ausgeschrieben ("zehn bis zwölf Hersteller", "40 bis 100 Mitarbeitern", "sechs bis zwölf Monaten"). `~` für circa, `>` und `<` für Schwellen.

### Berater
Am Satzende, mit Label: `Sell-side Berater:` bei Verkäufen, `Global Coordinators:` bei IPOs. Nur nennen, wenn der Artikel einen nennt – nie ergänzen. Berater werden nie fett geschrieben.

### Fettschrift
Fett: alle Unternehmens- und Akteursnamen – Käufer, Zielunternehmen, Eigentümer, Sponsoren, Bieter, Konsortialpartner.
Nicht fett: Berater, Branchenbezeichnungen, Financials, Ländercodes, Fließtext.
Beispiel: `08.09.26: **AUCTUS Capital Partners** treibt Verkauf von **Robert Bürkle** (DE, Oberflächenbeschichtungsmaschinen, Umsatz: 112,5 Mio. EUR) voran, Sell-side Berater: IMAP`

### Kürzungsprinzip
Nur wer / was / wieviel / wer berät. Konsequent gestrichen werden:
- Motivations- und Warum-Kontext
- historischer Hintergrund ("ursprünglich im Juni 2025 angekündigt", "nach abgesagtem Börsengang")
- Zwischentermine und Timing-Nachsätze ("erste Gebote Mitte September erwartet", "Prozessstart im September")
- Börsensegment- und Exchange-Details
- Finanzierungsmechanik
- redundante Statuswörter ("laufenden" vor "Verkaufsprozess", "im Bereich" vor einer Zahlenspanne)
- Stake-Prozente als eigener Nachsatz, außer die Zahl ist der zentrale Bewertungsfakt
- Attributionen ("laut CEO", "laut Eigentümern"), außer die Aussage der genannten Person ist selbst die Nachricht

### Bieterlisten
Standard: `Bieter u.a. X, Y und Z`. Wenn das Wort "Bieter" schon im Satz steht ("erreicht zweite Bieterrunde"), nicht wiederholen – dann `mit u.a. X und Y`. Nicht "Finalisten", nicht "Interessenten".
Nicht stapeln: Wenn Bieternamen genannt sind, fallen Deal-Value und Prozessstadium ("vor bindenden Geboten") weg.

---

## (iii) Roberts Präferenzen im Einzelnen

### Wortwahl
- "IPO" statt "Börsengang"
- "DE" statt "Deutschland" im Fließtext
- "Adj. EBITDA" statt "bereinigtes EBITDA"
- "Lincoln" statt "Lincoln International"
- "via" statt "über" bei Beteiligungsketten
- "i.H.v." nutzen
- Aktiv statt Passiv ("prüft Verkauf" statt "wird zum Verkauf geprüft")

### Formulierung
- Branchenbezeichnung großgeschrieben und so knapp wie möglich
- Rechtsformen weglassen ("Güntner" statt "Güntner GmbH"), außer sie unterscheidet
- Unpräzises präzisieren ("bis 20 Mio." → "<20 Mio.")
- Timing als Präpositionalphrase in den Hauptsatz, nicht als Komma-Nachsatz

### Grundhaltung
Robert kürzt in der Freigabe systematisch härter als der Entwurf. Im Zweifel streichen, nicht behalten. Details, die korrekt und interessant sind, aber nicht zum Kern gehören, fliegen raus.
