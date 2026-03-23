# ILA Agent-UI-Vorgehen — Version 1

**Stand:** 2026-03-23  
**Grundlage:** Konzept von Turiya, ausgearbeitet von Cheko (ILA-Hauptagent)  
**Status:** Entwurf — zur Freigabe durch Sarah

---

## Zielbild

**Input:** Fachliche Anforderungen + bestehendes Design (Gestaltungsstand)  
**Output:** Neue Figma-Screens (Entwurfsseiten), konsistent mit dem aktuellen Stil  
**Qualität:** Konsistent, barrierearm (zugänglich für alle Nutzer), fachlich korrekt, wenig Nacharbeit

Der Agent arbeitet zuerst wie ein guter Juniordesigner.  
Dann wie ein verlässlicher Co-Designer.  
Erst dann übernimmt er größere Teile eigenständig.

---

## Rollen im Pilot

| Rolle | Mensch | Agent | Verantwortung |
|---|---|---|---|
| Projektsteuerung | Sarah | Cheko (ILA-Hauptagent) | Entscheidungen, Qualitäts-Gates, Eskalation |
| Fachlichkeit | Sebastian | Fachlichkeits-Agent | Anforderungen, fachliche Regeln, Abnahme |
| Design | Yves | Design-Agent | Design-System, Screen-Erstellung, Review |

**Grundregel:** Keine finale Entscheidung ohne Sarah. Kein Screen geht ungeprüft weiter.

---

## Vorgehen in 7 Schritten

### Schritt 1 — Design-System explizit machen
Alles sichtbar machen, was bisher im Kopf von Yves ist.

Lieferobjekte:
- Komponentenliste (Buttons, Formulare, Tabellen, Navigation)
- Layout-Regeln (Abstände, Raster, Zustände: aktiv/inaktiv/Fehler)
- Muster je Seitentyp (pro Seitentyp ein Referenzbeispiel)
- Do/Don't-Liste

**Verantwortung:** Yves (mit Design-Agent als Unterstützung)  
**Ablage:** `ila/agent-ila/01_fachlichkeit/design-system/`

---

### Schritt 2 — Goldstandard-Daten (Referenzbeispiele) aufbauen
Ein kuratiertes (sorgfältig ausgewähltes) Set guter bestehender Screens als Lern- und Prüfgrundlage.

Lieferobjekte:
- 30–80 bestehende Screens aus der aktuellen Figma-Datei
- Je Screen: Zweck, Nutzerrolle, Pflichtinformationen, fachliche Regeln
- Kennzeichnung: was gilt als „guter Standard"

**Verantwortung:** Yves + Sebastian (gemeinsam)  
**Ablage:** `ila/agent-ila/01_fachlichkeit/goldstandard/`

---

### Schritt 3 — Prompt-Vorlage (Arbeitsanweisung) definieren
Einheitliche Eingabestruktur statt freiem Prompten (freien Anweisungen).  
Jede Anforderung an den Agenten folgt demselben Aufbau:

```
Kontext:        [Fachlicher Hintergrund]
Seitentyp:      [z. B. Förderplan bearbeiten]
Pflichtinhalte: [Was muss auf dem Screen erscheinen]
Designregeln:   [Welche Komponenten, welches Layout]
Barrierefreiheit: [Besondere Anforderungen]
Ausgabeformat:  [Wireframe / High Fidelity / JSON für Plugin]
```

**Verantwortung:** Cheko (ILA-Hauptagent) erstellt Vorlage, Sarah gibt frei  
**Ablage:** `ila/agent-ila/00_inbox/prompt-vorlage.md`

---

### Schritt 4 — Agent-Workflow aufbauen
Technischer Ablauf (Kette) für jeden Screen:

1. Anforderung kommt rein (`00_inbox/`)
2. Fachlichkeits-Agent prüft Vollständigkeit, ergänzt Regeln
3. ILA-Hauptagent erstellt Wireframe (Grobstruktur) als Beschreibung
4. Design-Agent baut High Fidelity (ausgearbeiteten Screen) in Figma
5. Export nach Figma via Plugin
6. Review gegen Checkliste durch ILA-Hauptagent
7. Zur Freigabe an Sarah (`03_review/`)

**Technische Voraussetzung:** Figma-Plugin (in Entwicklung bei Torsten)

---

### Schritt 5 — Qualitäts-Gates (Prüfpunkte) festlegen
Kein Screen kommt ohne vollständige Prüfung zu Sarah.

Checkliste je Screen:

- [ ] **Fachlichkeit:** Alle Pflichtinhalte vorhanden, fachliche Regeln eingehalten
- [ ] **UX (Nutzungserlebnis):** Logischer Aufbau, klare Nutzerführung
- [ ] **UI (Oberflächengestaltung):** Komponenten korrekt, Abstände und Farben regelkonform
- [ ] **Barrierefreiheit:** Kontraste, Schriftgrößen, Tastaturbedienbarkeit beachtet
- [ ] **Konsistenz:** Passt zu bestehenden Screens im Design-System

**Verantwortung:** ILA-Hauptagent (Cheko) führt Check durch, dokumentiert Abweichungen

---

### Schritt 6 — Pilot mit engem Umfang
Nicht das gesamte Produkt auf einmal — erst ein Seitentyp.

**Pilotumfang:**
- 1–2 Seitentypen mit hoher Wiederholbarkeit (Vorschlag: Bearbeitungsansicht mit Formularlogik, z. B. BSLRR)
- Dauer: 4 Wochen
- Messen: Zeitersparnis, Anzahl Korrekturschleifen, Akzeptanz bei Fachseite und Design

**Wichtig vorab:**  
Bei ILA gibt es Spannungen zwischen Fachlichkeit und Design.  
Vor dem Agenten-Einsatz muss eine gemeinsame Definition von „gut genug" erarbeitet werden.  
Sonst reproduziert der Agent nur den Konflikt — nur schneller.

---

### Schritt 7 — Entscheidung nach Pilot

| Ergebnis | Konsequenz |
|---|---|
| Qualität stabil, Zeitersparnis messbar | Agent übernimmt Erstentwurf standardmäßig |
| Qualität schwankend | Agent nur für Varianten und Vorarbeit |
| Akzeptanz fehlt | Rollendiskussion zuerst klären, dann weiter |

---

## Erfolgskriterien (messbar)

- **Time-to-First-Draft** (Zeit bis zum ersten Entwurf): Anforderung → erster Screen-Entwurf
- **End-to-End-Zeit:** Anforderung → reviewfähiger Screen bei Sarah
- **Rework-Aufwand** (Nacharbeit): Anzahl und Dauer der Korrekturschleifen
- **Konsistenz-Score:** Anteil bestandener Qualitäts-Gate-Punkte je Screen

Dokumentation: wöchentlich in `ila/agent-ila/04_metrics/`

---

## Realistische Erwartung

- **Kurzfristig:** 30–50 % schneller bei Standard-Screens
- **Mittelfristig:** Starke Entlastung bei Routine und Varianten
- **Vollständiger Ersatz:** Nur bei eng standardisierten Oberflächen realistisch

---

## Offene Punkte vor Pilotstart

- [ ] Gemeinsame Definition „gut genug" zwischen Fachlichkeit und Design erarbeiten
- [ ] Figma Professional-Plan aktivieren
- [ ] Figma-Plugin durch Torsten entwickeln lassen
- [ ] Repo-Struktur `ila/agent-ila/` anlegen
- [ ] Signal-Setup für 3 Agenten-Tokens
- [ ] Goldstandard-Screens von Yves zusammenstellen lassen
