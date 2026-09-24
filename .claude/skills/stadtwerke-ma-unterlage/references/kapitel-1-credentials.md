# Kapitel 1: Vorstellung und Referenzen

Das Standardkapitel. Es wird aus der grünen Referenzunterlage übernommen, und genau deshalb
ist es die häufigste Fehlerquelle: übernommene Folien tragen den alten Fall mit sich.

Einheitsname überall: **Metzler Mergers & Acquisitions**. Er steht in der Agenda („Metzler
Mergers & Acquisitions – Vorstellung und Referenzen"), auf dem Kapiteltrenner, in jeder
Kolumne von Kapitel 1, in den Profilen („Managing Director / Co-Head Mergers &
Acquisitions"), in der Geschäftsfeld-Folie (Spalte „Mergers & Acquisitions") und im
Disclaimer. Die DVV-vf trägt noch „Corporate Finance"; beim Kopieren aus ihr ist der Name an
allen sieben Stellen zu ersetzen. `stil_check.py` meldet jedes verbliebene „Corporate
Finance".

## Umfang nach Anlass

| Anlass | Folien | Belegt |
|---|---|---|
| Erstkontakt | Ansprechpartner, Haus seit 1674, vier Geschäftsfelder, Sektorfokus, Track Record, zwei Case Studies | evm, DVV, ESWE |
| Fortsetzung oder Update | Sektorfokus, Track Record, zwei Case Studies; Kapitelname „Metzler Mergers & Acquisitions – Update seit ‹Jahr›" | Krefeld 2026 |

## Die Folien

| Folie | Inhalt | Änderungsbedarf |
|---|---|---|
| Ihre Ansprechpartner | Zwei Senior-Profile: Rolle, Erfahrungsjahre, Stationen, ausgewählte Referenzprojekte | Team des Falls; Referenzprojekte passend wählen; Titel „Mergers & Acquisitions" |
| Bankhaus Metzler seit 1674 | Familienbesitz, Netzwerk, Unabhängigkeit, Langfristigkeit, Werte | keiner |
| Vier Geschäftsfelder | Asset Management, Mergers & Acquisitions, Capital Markets, Private Banking; Standorte | Spaltenname |
| Sektorfokus | Energy & Infrastructure als einer von drei Fokussektoren, mit „Stadtwerke / EVV" | keiner |
| Track Record | Aktuelle Mandate als Tombstones, zwei Gruppen: „Erneuerbare Energien Entwickler und Asset Manager", „Stadtwerke und andere EVU" | aktualisieren; Aktualität schlägt Vollständigkeit; gelber Kasten `PRUEFEN` |
| Case Studies | Zwei Transaktionen: Transaktion, dann Rolle Metzler mit Leistungskatalog | passend zum Anlass wählen |

## Case Studies richtig wählen

Der Aufbau ist zweiteilig, beide Teile sind nötig:

- **Transaktion**: was verkauft oder erworben wurde, Größenordnung, Struktur, wie viele
  Investoren angesprochen wurden.
- **Rolle Metzler**: die Leistungen einzeln: Mitgestaltung des Carve-outs, Investment Case,
  Vermarktungsunterlagen und Finanzmodell, Entscheidungsvorlagen und
  Verhandlungsempfehlungen, Koordination des Investorenprozesses, Due Diligence,
  Verhandlungsunterstützung, kaufmännische Aspekte des Kaufvertrags.

Der zweite Teil ist der Zweck: Der Adressat soll sich vorstellen können, was das Haus in
seinem Prozess tun würde. Eine Case Study ohne Leistungskatalog ist eine Anekdote.

Auswahl nach Anlass: Wärme, dann die Wärme-Contracting-Transaktion (EWE / WCG). Netz oder
Erneuerbare, dann der Portfolio-Verkauf (WIND-projekt / Blue Elephant). Kommunaler Kontext,
dann eine Transaktion mit öffentlich-rechtlichem Hintergrund (DEW21, MVV). Seit 2026 stehen
in allen drei Unterlagen dieselben zwei; das bleibt so, bis das Haus neue liefert.

## Was der Skill hier tut

Kopieren, den Namen setzen, die Kolumnen auf den Kapitelnamen setzen, und einen gelben
Kasten `PRUEFEN` auf den Track Record legen, weil der Skill nicht wissen kann, welche
Mandate seit der Vorlage dazugekommen sind. Profile und Case Studies nicht umschreiben.

## Fallstricke

- **Der alte Fall bleibt stehen.** Kolumnen und Fußzeilen tragen den vorherigen Mandanten.
  `inspect_deck.py --fremdnamen` mit dem Namen der Vorlage laufen lassen, hier also
  „DVV,Duisburg".
- **Veraltete Tombstones.** Ein Mandat von vor vier Jahren als „laufend" zu zeigen, fällt
  auf. Lieber vier aktuelle als acht gemischte.
- **Personenbezogene Daten.** Mobilnummern gehören nur in die ausgehende Unterlage, nicht
  in Muster, Report oder Archivstände.
- **Zu langes Kapitel 1 beim Update.** Der Adressat kennt das Haus. Drei Folien und weiter.
