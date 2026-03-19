# ila

Softwareentwicklungsprojekt im Kontext individueller und sonderpädagogischer Förderung.

Stand: 2026-03-18

## Kontext
- Komplexes fachliches und organisatorisches Umfeld
- SCRUM ist formal vorhanden
- In der Praxis Spannungen zwischen Fachlichkeit und Design

## Arbeitsziel (Sarah)
Prüfen, ob und wie KI den Entwicklungsprozess beschleunigen und verbessern kann.  
**Zielbild:** UI/UX-Design durch Agenten unterstützen/ersetzen  
→ Input: Anforderungen + bestehende Designlogik  
→ Output: neue Figma-Screens (konsistent, barrierearm, fachlich korrekt)

## Team (Pilot)
- **Sarah:** Projektsteuerung, ILA-Hauptagent  
- **Sebastian:** Fachlichkeit (ARIS-Modelle, Word-Dokumente, Anforderungen)  
- **Yves:** Design/Figma (Design-System, Screen-Erstellung)

Jedes Teammitglied erhält einen eigenen Agenten. Alle Agenten kommunizieren über Signal.  
**Gemeinsame Signal-Gruppe:** Menschen + Agenten zusammen.

## Agenten-Architektur (geplant)
1. **ILA-Hauptagent (Sarah):** Koordination, Entscheidungen, Qualitäts-Gates, finale Freigabe  
2. **Fachlichkeits-Agent (Sebastian):** Anforderungen, ARIS-Modelle, fachliche Regeln  
3. **Design-Agent (Yves):** Figma-Zugriff, Design-System, Screen-Entwürfe

**Wichtig:** Alle Agenten haben Figma-Zugriff, aber oberste Steuerungsebene bleibt beim ILA-Hauptagenten.

## Technische Rahmenbedingungen
- Agenten-Steuerung: **Signal**  
- Dokumentation: **GitHub**  
- Design-Plattform: **Figma (lokales Setup / Sandbox)**  
  - Eigener Figma-Account (Sarah)  
  - Kopie der Produktiv-Figma-Instanz als Sandbox  
  - Agent arbeitet dort (kein Risiko für Live-System)  
- Fachlicher Kontext: **ARIS-Modelle + Word + Prompts**

## Vorgehen (7-Schritte-Modell, validiert)

### Stufenplan
**Agent als Junior → Co-Designer → Teilübernahme** (nicht Big Bang)

### 1) Design-System explizit machen
- Komponenten (Buttons, Tabellen, Formulare)
- Regeln (Abstände, Farben, Zustände)
- Muster je Seitentyp
- Do und Don't

### 2) Goldstandard-Daten bauen
- 30–80 gute bestehende Screens
- Je Screen: Metadaten (Zweck, Nutzerrolle, Pflichtinfos, fachliche Regeln)
- Markieren, was als „gut" gilt

### 3) Prompt-Blueprint definieren
Template mit immer gleicher Struktur:
- Kontext, Seitentyp, Pflichtinhalte, Designregeln, Accessibility, Outputformat

### 4) Agent-Workflow bauen
1. Anforderungen rein  
2. Agent macht Wireframe  
3. Agent macht High Fidelity  
4. Export nach Figma  
5. Review gegen Checkliste

### 5) Qualitäts-Gates einziehen
Kein Screen geht ungeprüft live:
- Fachlicher Check
- UX-Check
- UI-Check
- Accessibility-Check
- Konsistenz mit Bestand

### 6) Pilot mit engem Scope
- 1–2 Seitentypen (Fokus: BSLRR)
- 4 Wochen
- Messen: Time-to-First-Draft, End-to-End-Zeit, Rework-Aufwand

### 7) Entscheidungslogik
- Wenn Qualität stabil → Agent übernimmt Erstentwurf standardmäßig
- Wenn nicht → Agent nur für Varianten und Vorarbeit

## Wichtig: Spannungen strukturiert klären
Bei ila gibt es Spannungen zwischen Fachlichkeit und Design.  
**Vor Agenteneinsatz:** Gemeinsame Definition von „gut genug" erarbeiten.  
Sonst reproduziert der Agent nur den Konflikt in schneller.

## Realistische Erwartung
- **Kurzfristig:** 30–50% schneller bei Standard-Screens
- **Mittelfristig:** Starke Entlastung bei Routine und Varianten
- **Vollständiger Ersatz:** Nur bei eng standardisierten Oberflächen realistisch

## Zielgruppe im Projekt
- Auftraggeber
- Referatsleitung
- internes Pendant

## Nächster Schritt
1. Präsentation auswerten (`docs/praesentationen/ila_Agenten_Pilot_Design-Entlastung.pptx`)  
2. ILA-Hauptagent auf Claude Sonnet 4-5 aufsetzen  
3. Signal-Setup für 3 Bots (Token + Konfiguration)  
4. Steuerungs- und Freigabe-Matrix erstellen  
5. Figma-Zugriff und Design-System-Schnittstelle definieren

## Offene Frage
Ob und wann beim Auftraggeber echtes Interesse an KI-Einsatz entsteht.

## Aktueller Entscheidungsunterstützer
- `docs/vorschlag-design-entlastung-mit-agenten-2026-03-13.md`
- `docs/management-onepager-design-entlastung-2026-03-13.md`
- `docs/praesentation-ila-design-entlastung-7folien-2026-03-12.md`
- `docs/vorschlag-design-entlastung-mit-agenten-6-schritte-v2.md`
- `docs/praesentationen/ila_Agenten_Pilot_Design-Entlastung.pptx` (neueste, 2026-03-18)
