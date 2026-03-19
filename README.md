# ila

Softwareentwicklungsprojekt im Kontext individueller und sonderpädagogischer Förderung.

Stand: 2026-03-18

## Kontext
- Komplexes fachliches und organisatorisches Umfeld
- SCRUM ist formal vorhanden
- keine stringentes Zusammenarbeitsmodell vorhanden
- größter Zeitfresser: Abstimmung zwischen Fachlichkeit und Design

## Arbeitsziel (Sarah)
Prüfen, ob und wie KI den Entwicklungsprozess beschleunigen und verbessern kann, in diesem Pilotprojekt primär Fokus auf Übersetzung fachliche Anforderungen in Flows und Screens:
**Zielbild:** UI/UX-Design durch Agenten unterstützen  
→ Input: Anforderungen + bestehende Designlogik  
→ Output: neue Figma-Screens (konsistent, barrierearm, fachlich korrekt)

## Team (Pilot)
- **Sarah:** Projektsteuerung, ILA-Hauptagent  
- **Sebastian:** Fachlichkeit (ARIS-Modelle, Word-Dokumente, Anforderungen)  
- **Yves:** Design/Figma (Design-System, Screen-Erstellung)

Jedes Teammitglied erhält einen eigenen Agenten. Alle Agenten kommunizieren über Signal.  
**Gemeinsame Signal-Gruppe:** Menschen + Agenten zusammen.

## Agenten-Architektur (geplant)
1. **ILA-Hauptagent (Sarah) Claude:** Koordination, Entscheidungen, Qualitäts-Gates, finale Freigabe  
2. **Fachlichkeits-Agent - Perplexity (Sebastian):** Lieferung und QS Anforderungen, fachliche Regeln  
3. **Design-Agent - Claude (Yves):** Bereitstellung und Anpassung Design-System, QS und Weiterentwicklung Screen-Entwürfe

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

### 1) Design-System explizit machen
- Komponenten (Buttons, Tabellen, Formulare)
- Regeln (Abstände, Farben, Zustände)
- Muster je Seitentyp
- Do und Don't

### 2) Goldstandard-Daten bauen
- 80 bis 100 gute bestehende Screens
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
- Fachlicher Check
- UX-Check
- UI-Check
- Accessibility-Check
- Konsistenz mit Bestand

### 6) Pilot mit engem Scope
- 2 - 3 Seitentypen (Fokus: BSLRR)
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


## Zielgruppe im Projekt
- Auftraggeber
- ila Team


## Nächster Schritt
1. ILA-Hauptagent auf Claude Sonnet 4-5 aufsetzen  (OpenRouter Sarah)
2. Signal-Setup für 3 Bots (Token + Konfiguration)
3. Handlungsanweisung - erste Schritte für Kollgen schreiben
4. Steuerungs- und Freigabe-Matrix erstellen  
5. Figma-Zugriff und Design-System-Schnittstelle definieren
6. Zugriffe der Kollegen auf Repository klären und sichern 


## Offene Fragen
Ob und wann beim Auftraggeber echtes Interesse an KI-Einsatz entsteht.
Wenn Pilot erfolgreich - nächste Schritte


