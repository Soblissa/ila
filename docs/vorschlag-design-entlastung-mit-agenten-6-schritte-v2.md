# Design-Entlastung durch Agenten – 6-Schritte-Vorgehen (V2)

Stand: 2026-03-11
Ziel: Entscheidungsreife Vorlage für den Freitagstermin

## Leitidee
Nicht "Design ersetzen", sondern Designkapazität von Routinearbeit entlasten.
Der Agent liefert konsistente Erstentwürfe, der Mensch steuert Qualität und Freigabe.

---

## Schritt 1 – Designstandard verbindlich machen
**Ziel:** Aus implizitem Designwissen ein verbindliches Regelwerk machen.

**Ergebnisse:**
- Komponentenliste mit Varianten (z. B. Formular, Tabelle, Status, Hinweise)
- Layout- und Abstandsregeln
- Zustandslogik (leer, validiert, Fehler, gesperrt)
- Do/Don't-Beispiele

**Abnahmekriterium:**
Mindestens 80 Prozent der Standardentscheidungen sind als Regel dokumentiert.

---

## Schritt 2 – Referenzset aufbauen
**Ziel:** Ein belastbares Trainings- und Prüfset aus bestehenden Screens.

**Ergebnisse:**
- 30 bis 80 repräsentative Screens
- Metadaten je Screen: Zweck, Rolle, Pflichtinformation, Fachlogik
- Kennzeichnung "guter Standard"

**Abnahmekriterium:**
Alle Pilotscreens können einem Referenzmuster zugeordnet werden.

---

## Schritt 3 – Agentenauftrag standardisieren
**Ziel:** Keine freien Einzelprompts, sondern ein einheitliches Auftragsformat.

**Template-Inhalte:**
- fachlicher Kontext
- Seitentyp
- Pflichtinhalte
- Design- und Barrierefreiheitsregeln
- erwarteter Output

**Abnahmekriterium:**
Derselbe Input erzeugt konsistente Erstentwürfe mit geringer Streuung.

---

## Schritt 4 – Pilotworkflow umsetzen
**Ziel:** End-to-End-Prozess für 1 bis 2 Seitentypen produktiv testen.

**Workflow:**
1. Fachanforderung aufnehmen
2. Agent erstellt Wireframe
3. Agent erstellt UI-Erstentwurf in Figma
4. Review durch Fachseite und Design
5. Korrektur oder Freigabe

**Abnahmekriterium:**
Durchlaufzeit und Übergaben sind klar dokumentiert und reproduzierbar.

---

## Schritt 5 – Qualitätsgates verpflichtend machen
**Ziel:** Verlässliche Qualität vor Freigabe sichern.

**Pflichtchecks pro Screen:**
- Fachlichkeit korrekt
- UX stimmig
- UI regelkonform
- Barrierefreiheit erfüllt
- Konsistenz mit Referenzset

**Abnahmekriterium:**
Kein Screen ohne vollständige Checkliste in die nächste Stufe.

---

## Schritt 6 – Nach 4 Wochen datenbasiert entscheiden
**Ziel:** Go/No-Go nicht nach Gefühl, sondern nach Kennzahlen.

**Messgrößen:**
- Durchlaufzeit pro Screen
- Anzahl Korrekturschleifen
- Konsistenz-Score
- Akzeptanz von Fachseite und Design

**Entscheidungsoptionen:**
- **Go:** Agent als Standard-Erstentwurf für definierte Seitentypen
- **Teil-Go:** Agent nur für Varianten und Vorarbeit
- **No-Go:** Pilot beenden, Gründe dokumentieren, Alternativen ableiten

---

## Klarer Scope für Freitag
- Pilotdauer: 4 Wochen
- Pilotumfang: 1 bis 2 Seitentypen mit hoher Wiederholbarkeit
- Rollen: Fachseite, Design, Technik, Projektleitung verbindlich benannt
- Entscheidungstermin: bereits im Kickoff fixieren
