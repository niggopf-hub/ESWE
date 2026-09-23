# Handoff: Skill „Stadtwerke-M&A-Unterlage"

Stand 23.09.2026 · Repo `niggopf-hub/eswe`, Branch `claude/stadtwerke-ma-skill-s4g43t` · kein PR

## Die Idee

Ein Claude-Skill, der Metzler-Corporate-Finance-Unterlagen für kommunale Versorger baut:
rund 20 Folien, Bogen „Kapitalflexibilisierung durch Einbindung privater Investoren" —
*wer spricht → was wir am Unternehmen sehen → worüber man reden sollte*.

Heute entsteht jede Unterlage aus der vorherigen, und Reste wandern mit: In der evm-vF steht
noch „Stadtwerke Krefeld", in der DVV-v1 stand fast überall noch evm. Der Skill soll Storyline,
Quellen, Excel-Modell und PowerPoint-Mechanik so festhalten, dass der nächste Fall sauber
aus Gerüst und neuen Belegen entsteht.

## Was ich will

- **Storyline steht fest.** Der evm-Bogen ist die Referenz. Übertragbares Gerüst und
  deal-spezifische Belege sind getrennt; Belege sind immer als variabel markiert.
- **Erster Schritt immer:** Storyline für den Fall ableiten, prüfen ob sie trägt, von mir
  bestätigen lassen. Danach kapitelweise mit Zwischenstopps, kein Durchlauf.
- **Mechanik selbstständig, Urteil mit mir.** Gliederung, Tabellen, Standardtexte und
  Vollständigkeit macht der Skill allein. Strategische Begründung und Bewertungsnarrativ:
  gezielte Rückfragen und „darf nicht fehlen"-Checklisten statt vorformuliertem Text.
- **Kennt die Quellen:** Jahresabschlüsse (Unternehmensregister), Geschäftsbericht,
  Register, Presse, Programmbücher — und weiß, was bei der Recherche zählt.
- **PowerPoint:** in die vorhandenen Boxen schreiben, nie neue Boxen einfügen.
- **Drei Vorlagen mit getrennten Rollen:** evm = Storyline · DVV-vf = Design · ESWE = Gliederung.
- **Gliederung nach ESWE:** Kapitel 2 (i)–(vi) Ausgangslage, One Pager, Beteiligungsstruktur,
  Investitionshorizont, Financials, Summary · Kapitel 3 (i) Ziele, (ii) Ansatzpunkte.
- **Financials:** drei Blöcke, erster mit Umsatz *und* Rohertrag; Zeilenlogik HGB wie im
  ESWE-Modell, nicht EBITDA-/EBIT-/EAT-Margen.
- **Grünes Haus-Design** (seit 09/2026) als Standard.
- Keine echten Mandantendaten im Skill-Paket; Ergebnis als `.skill`-Datei.

## Bestand: Unterlagen mit Storyline

**Zwei finale Versionen** (evm, DVV), eine ältere Unterlage mit demselben Bogen
(Duisburg 2024), ESWE in Arbeit ohne Deck.

| Fall | Datei | Stand | Design | Storyline | Rolle |
|---|---|---|---|---|---|
| **evm AG** | `20260813_Metzler_evm AG_vF.pdf` (ESWE-Repo) | vF · 13.08.2026 · 22 S. | blau | Standardbogen, 3 Kapitel — vollständig analysiert | **Storyline-Referenz** · nur als PDF |
| **DVV** | `20260907_Metzler DVV_vf.pptx` (DVV-Repo) | vf · 09/2026 · 19 F. | **grün** | abgewandelt: 2 Kapitel, Kap. 3 → eine Diskussionsfolie | **Design-/Template-Referenz** |
| DVV | `20260824_Metzler_DVV_v1.pptx` (DVV-Repo) | v1 · 24.08.2026 · 22 F. | blau | größtenteils noch evm-Text | Arbeitsstand, keine Zahlenquelle |
| Stadtwerke Duisburg | `20240305_Stadtwerke Duisburg_v4 1 (1).pptx` (ESWE-Repo) | v4 · 05.03.2024 · 21 F. | blau | gleicher Bogen, Zahlen 2022 | historisch · WIP-Notiz und Quell-URL drin |
| **ESWE** | kein Deck · `Briefing_ESWE_Versorgungs_AG.md` | Briefing 27.08.2026 | — | im Testlauf abgeleitet, **nicht bestätigt** | **Gliederungs-Referenz** |

Financial Models: evm `evm_enm_financial_model_2020_2024_v5` · DVV
`DVV_Konzern_Financials_2020-2025` (Konzern) · ESWE `ESWE_Versorgungs_AG_Jahresabschluss_2020-2024`
(Einzelabschluss; Erweiterung bis 2025 aus einem Testlauf im Workspace).

## Stand des Skills

`.claude/skills/stadtwerke-ma-unterlage/` · Paket per `package_skill` nach `dist/` (nicht im Repo)

- **SKILL.md** — Ablauf in acht Schritten mit Zwischenstopps: Analyseprofil → Material →
  Storyline-Hypothese → Modell und Finanzierungsüberleitung → Storyline bestätigen →
  Kapitel schreiben → PowerPoint → Prüfung und Fertigstatus.
- **references/** — Storyline, Recherche, Financial Model, PowerPoint, je Kapitel eine Datei.
- **assets/** — Musterdokument, Textbausteine, Tabellenlayouts (anonymisiert).
- **scripts/** — `inspect_deck.py` (Inventar, `--check`, `--vergleich`, `--fremdnamen`),
  `fill_deck.py` (schreibt nur in vorhandene Boxen und Tabellenzellen, Adressierung über
  `rolle:`), `vorlage.py` (erkennt blaues und grünes Template).
- **Getestet:** drei Testfälle mit und ohne Skill (94 % gegen 73 %, noch gegen die alte
  Gliederung), 14 Skript-Gegenproben aus dem externen Review, Prüfer auf allen drei pptx-Decks.
- **Externes Review (07.09.2026):** acht Befunde, alle behoben →
  `analysen/20260907_Stadtwerke_Skill_Review.md`.

## Offene Entscheidungen

Die DVV-vf weicht an drei Stellen vom Skill ab. Das ändert den Bogen, deshalb nicht übernommen:

1. **Kapitel 3 streichen** und durch eine Diskussionsfolie am Ende von Kapitel 2 ersetzen?
2. **Neuer Titel** „Vorstellung Metzler Corporate Finance und unser Blick auf die
   Herausforderungen der ‹X›" statt „Überlegungen zur Kapitalflexibilisierung …"?
3. **Reihenfolge Kapitel 2** wie DVV-vf (Beteiligung vor Kennzahlen, Financials vor
   Investitionshorizont) oder wie ESWE?

Einbaufertig ohne Strukturfrage: die zweite Belastung im Kernsatz (Querverbund/ÖPNV) und
„etablierte Minderheitspartner" als Argument auf der Beteiligungsfolie.

## Nächste Schritte

1. Die drei Entscheidungen treffen, Skill anpassen.
2. Testfälle gegen die aktuelle Fassung neu laufen lassen.
3. Probelauf von der Recherche bis zur abgenommenen Folie, je auf Kopien: DVV (Konzern,
   Sondererlöse, Definitionswechsel) und ESWE (Einzelgesellschaft, EAV, Beteiligungsergebnis,
   Netztochter).
4. DVV-vf korrigieren: Cashflow-Chart 2024 (Investing/Financing vertauscht), Kommentar „ab
   2023 decken die operativen Mittel die Investitionen", Quellen auf F16/F17, ungenutzter
   Eigenmittelbedarf 0,75–1,0 Mrd. aus dem Programmbuch → `analysen/20260923_DVV_v1_vs_vf.md`.
5. ESWE-Deck aus der grünen DVV-vf bauen.

## Hinweise für die nächste Session

- Das DVV-Repo (`niggopf-hub/dvv`) muss per `add_repo` neu angehängt werden; in dieser Session
  nur gelesen. Sein `README.md` ist an drei Stellen überholt (Net Debt 2024, Free Cashflow 2024,
  Herkunft der 2,5–3,5 Mrd. — steht im Programmbuch S. 29).
- Die vier `Wiesbaden_HRB_2105_*.pdf` sind Jahresabschlüsse 2021–2024, keine Registerauszüge.
- Die `.skill`-Datei wird nicht versioniert; neu erzeugen mit
  `python -m scripts.package_skill .claude/skills/stadtwerke-ma-unterlage dist` (aus dem
  skill-creator-Verzeichnis).
