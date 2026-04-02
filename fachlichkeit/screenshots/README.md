# Screenshots Testumgebung ILA

**Datum:** 2026-04-02  
**Testumgebung:** ilamrfrontendtest-devkultuscloudhessen.msappproxy.net/ila-app/  
**Testnutzer:** ila.test01@preschule.hessen.de (Willi Walter)  
**Dokumentiert von:** Cheko (ILA-Hauptagent)

---

## Workflow-Dokumentation

| Datei | Screen | Beschreibung |
|---|---|---|
| 01_startseite.jpg | Startseite | Dashboard mit Schülerübersicht, Donut-Diagramm (12% mit Förderung), "Neue Förderung anlegen" |
| 02_schuelersuche.jpg | Neue Förderung — Schülersuche | Modal, 57 Schüler, alphabetisch, Badge mit Anzahl Förderungen |
| 03_anlass_auswaehlen.jpg | Neue Förderung — Anlass | 2 sichtbare Optionen (Teilnahme an besonderer Fördermaßnahme, Drohendes Leistungsversagen) |
| 04_bestaetigung.jpg | Neue Förderung — Bestätigung | Zusammenfassung vor dem Speichern |
| 05_foerderakte_leer.jpg | Förderakte (leer) | Kanban-Board leer, Button "Förderplan erstellen" und "Förderziele hinzufügen" |
| 06_foerderbereich_auswaehlen.jpg | Förderziele — Schritt 1 | 3 Förderbereiche: Lesen, Rechtschreiben, Rechnen + Toggle Vorklasse |
| 07_lernausgangslage.jpg | Förderziele — Schritt 2 | Kompetenzkarten mit Toggle, Klassen-Dropdown, 0 Förderziele identifiziert |
| 08_foerderziele_zusammenfassung.jpg | Förderziele — Schritt 3 | 2 ausgewählte Förderziele zur Bestätigung |
| 09_foerderakte_mit_zielen.jpg | Förderakte mit Zielen | 2 Förderziele in "In Planung", Hinweis zu Maßnahmen |
| 10_foerderziel_detail.jpg | Förderziel-Detailseite | 3 Maßnahmenvorschläge, Button "Starten" |
| 11_massnahmen_unterstuetzer.jpg | Maßnahmen + Unterstützer | 2 Maßnahmen aktiviert, Unterstützer = Lehrkräfte (nicht nur Eltern) |
| 12_foerderziel_in_durchfuehrung.jpg | Förderziel aktiv | Status "In Durchführung", 2 Maßnahmen, Button "Notizen" und "Evaluieren" |
| 13_notizen_modal.jpg | Notizen-Modal | 3 Notizen, Kontext-Box mit Maßnahme, Bearbeiten/Löschen möglich |
| 14_evaluation_optionen.jpg | Evaluation — Optionen | 4 Optionen: Erreicht, Teilweise, Nicht erreicht, Passt nicht zur Lernausgangslage |
| 15_evaluation_begruendung.jpg | Evaluation — Begründung | Freitextfeld optional, Hinweis "wird im Förderplan angezeigt" |
| 16_evaluation_bestaetigung.jpg | Evaluation — Bestätigung | Zusammenfassung vor Speichern |
| 17_foerderziel_nach_evaluation.jpg | Förderziel nach Evaluation | Status bleibt "In Durchführung", Badge "Teilweise erreicht", Buttons "Bearbeiten" und "Abschließen" |
| 18_foerderakte_gesamt.jpg | Förderakte Gesamtübersicht | Ein Ziel in Planung, eines In Durchführung mit Evaluation |
| 19_foerderplan_erstellen.jpg | Förderplan erstellen | Stärken-Freitext, beide Förderziele mit Details, Buttons: Abbrechen, PDF, Speichern |

---

## Beobachtungen (Cheko, 2026-04-02)

### Was gut funktioniert
- Workflow klar und logisch — 3-Schritte-Wizard intuitiv
- Stabilität — keine Fehler im Durchlauf
- Schülersuche schnell mit Badge-Info
- 4 Evaluations-Optionen sinnvoll
- PDF-Export vorhanden
- Notiz-Funktion mit Kontext-Box

### Wording-Probleme
- Button "Förderplan erstellen" auf Förderakte → sollte "Förderung" heißen (laut ARIS-Modell)
- Hinweistext bei Begründung: "wird im Förderplan angezeigt" → gleiche Problem
- "Notizen" → sollte "Verlauf" oder ähnlich heißen

### Fehlende Inhalte (aus Feedback bestätigt)
- Nur 3 Förderbereiche: Lesen, Rechtschreiben, Rechnen — Lernverhalten, Sozialverhalten, Sprache fehlen
- Kompetenzen teilweise zu anspruchsvoll für die angezeigte Klassenstufe

### Offene Frage
- Unterstützer-Feld zeigt Lehrkräfte — widerspricht Pilot-Feedback ("nur Eltern wählbar"). Zwischenzeitlich geändert?

### UX-Beobachtung
- PDF-Button im Förderplan-Screen nicht prominent genug — daher im Pilot von Lehrkräften nicht gefunden
