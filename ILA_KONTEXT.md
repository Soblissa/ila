# ILA_KONTEXT.md — Checos ILA-Briefing
*Pflichtlektüre bei jedem ILA-Thema. Immer zuerst lesen.*
*Letzte Aktualisierung: 2026-04-22 (ergänzt um Chat-Verlauf 22.03.–31.03.2026)*

---

## 1. Was ist ILA / diSAF?

- **ILA = diSAF** — ein und dasselbe Produkt. Nie verwechseln.
- Digitales System zur Abbildung von **individueller und sonderpädagogischer Förderung** an hessischen Schulen
- Zielgruppe: Lehrkräfte, Schulleitung, Schulverwaltung
- Auftraggeber: Dirk Lenz (Telegram-ID: 8233442182) — Sarah berichtet an ihn
- System-Kontext: HMKB (Hessisches Ministerium für Kultus und Bildung)

---

## 2. Aktueller Projektstand (Stand: 2026-04-22)

### Was abgeschlossen ist
- ✅ Pilotauswertung AS1 (30.01.–31.03.2026) — Gesamtbericht fertig
- ✅ FigJam-Flows: Individuelle Förderung (v12_referenz) + BSLRR (v9)
- ✅ Figma Screens: Startseite, Förderakte, Förderziel, BSLRR-Flow, Nutzerfeedback u.a.
- ✅ OnePager Pilotauswertung (Word + MD)
- ✅ Anforderungsbeschreibung Kalender/Erinnerung/Aufgaben

### Was gerade läuft
- 🔄 Neuer Flow "VM SöPädFö" (Vorbeugende Maßnahme) — flow_ab_vm_v2.json fertig, v3 in Vorbereitung
- 🔄 Neues Konzept: **Förderakte als Hub** — alle Prozesse starten von dort, kein separater Anlass-Einstieg mehr
- 🔄 Neue FigJam-Datei: `ila_Flow_ab_VM` (noch anzulegen)

### Offene TODOs
- [ ] flow_ab_vm_v3 bauen (neue Struktur: Förderakte als Hub)
- [ ] FigJam-Seite anlegen für neuen Flow
- [ ] BSLRR + IFö in neuen Ansatz überführen
- [ ] Handlungsanweisung für Sebastian und Yves schreiben
- [ ] Steuerungs- und Freigabe-Matrix erstellen

---

## 3. Entstehungsgeschichte (wichtig für Kontext)

- **22.03.2026:** Erste Session. Name zunächst "Chefkoch" (Sarahs Spitzname), dann zu **Cheko** umbenannt — Kollegen fanden "ILA-Imperator" zu provokant
- **23.03.2026:** SOUL.md bearbeitet — Humor (trocken/warm), Fachbegriffe erklären, Vorschläge zurückhalten
- **23.03.2026:** Figma-Anbindung: eigenes Plugin bauen (kein MCP als Primärweg), Figma Professional (16 USD/Monat) beschlossen
- **24.03.2026:** Anthropic API Tier 1 → Tier 2 Upgrade + Credits aufgeladen
- **25.03.2026:** Figma Professional-Account (s.bonhoff@kuubera.de) gekauft, Design Specs von HMKB-Account exportiert
- **31.03.2026:** Figma API Token eingerichtet (`/etc/openclaw/users/user1.env`), Design Specs analysiert (155 Komponenten, 24 Seiten), Plugin-Anforderungen dokumentiert
- **31.03.2026:** Agentencharta von Turiya gelesen (`ila/agent-ila/agentencharta-turyia-chefkoch.md`)
- **31.03.2026:** BOOTSTRAP.md gelöscht
- Turiya läuft inzwischen auf einem **anderen Server** (wurde neu aufgesetzt, nicht mehr auf demselben Server wie Cheko)
- Direktverbindung Turiya ↔ Cheko: noch offen — SSH-Zugang zu Turiyas Server war geplant
- Figma-Seiten im HMKB-Account: ~15 Dateien (BSLRR, Kalender, Neue Förderung, Förderziel, Förderakte, Design Specs AS 1.0+2.0, Discovery, Vision, Szenarien, Förderplan)
- **06.04.2026:** Neuer Figma-Token erstellt (alle Berechtigungen gesetzt) — Token liegt in `/etc/openclaw/users/user1.env` als `FIGMA_TOKEN`
- **06.04.2026:** `ILA Agent Workspace` Datei angelegt (Key: `sMBmRwfjOE9EMWKnTTqNOl`)
- **06.04.2026:** Frank-Agent eingerichtet: Bot `@Franks_Klaus_bot`, Läuft auf `user2`, Repo: `github.com/Soblissa/Franks_Klaus`, Anthropic API-Key separat, Brave API eingerichtet
- **06.04.2026:** Brave Search API Key eingetragen — läuft für alle Agenten (Key in `user1.env`)
- **06.04.2026:** SOUL.md ergänzt: "Denkt out of the box, reflektiert, bereit sich weiterzuentwickeln"
- **07.04.2026:** Figma Plugin v4 gebaut — 155 Komponenten aus L-Screens, kein `loadAllPagesAsync` mehr, Komponenten-Index direkt eingebettet
- **07.04.2026:** Sebastians Bot `@FelgesBot` (Bernd) gestartet, Sebastian gepairt
- Semantische Suche: noch nicht eingerichtet — Torsten muss das machen ("genauso wie Turiya")
- Figma-Plugin: Navigation Bar funktioniert mit Node-ID `58:24478`, alle L-Screen-Komponenten in `component-library-full.json`

## 4. Technisches Setup

### Figma API
- **Token:** `/etc/openclaw/users/user1.env` → `FIGMA_TOKEN`
- **Getesteter Zugriff:** ✅ aktiv (s.bonhoff@kuubera.de)
- **Design Specs Datei-Key:** `yIb1pCbdjaUqpnrPf0RMF1`
- **Gesamtflow Ist-Stand:** `HdhS7kIsuv4mcHOmwmKBGp`
- **Vision und Gesamtüberblick:** `WYVQAFZjmeZcme1Hr3CEmu`

### Figma-Plugin (Screen Builder)
- Pfad: `ila/agent-ila/figma-plugin/`
- Datei: `manifest.json` + `index.js` + `ui.html`
- Für: Figma-Screens erstellen via JSON

### FigJam-Plugin (Flow Builder)
- Pfad: `ila/agent-ila/figjam-plugin/`
- Datei: `manifest.json` + `code.js` + `ui.html`
- Hot-Reload: `code.js` lokal ersetzen aus GitHub → Plugin aktualisiert sich automatisch
- Für: FigJam-Flows zeichnen via JSON

### Plugin-Befehle (JSON-Dateien)
- Pfad: `ila/agent-ila/plugin-befehle/`
- Referenz: `gesamtflow_ist_stand_v12_referenz.json`
- Aktuellster VM-Flow: `flow_ab_vm_v2.json`
- BSLRR aktuell: `bslrr_flow_v9.json`

### Git
- Repo: `/home/user1/ila` → GitHub: `github-soblissa:Soblissa/ila`
- Branch: `main`
- Identity: `Cheko <cheko@ila-agent.local>`

---

## 4. FigJam Flow-Bauregeln (IMMER einhalten)

| Element | Typ | fillColor | textColor | Position |
|---|---|---|---|---|
| Screen (Hauptseite) | SQUARE | `blue` | `white` | horizontal, y=200, x-Abstand ~550px |
| Modal / Unterschritt | SQUARE | `lightGray` | `darkBlue` | vertikal unter Screen, y-Abstand ~200px |
| Parallele Unterschritte (5.1, 5.2) | SQUARE | `lightGray` | `darkBlue` | horizontal nebeneinander, gleiche y-Höhe |

- **Kein ROUNDED_RECTANGLE** — Text wird abgeschnitten
- **Keine fixen width/height** bei SQUARE
- **Keine Connectors** (`connectors: []`) — Pfeile manuell setzen
- **Keine Legende**
- **Kein Abschluss-Shape**

---

## 5. Neues UX-Konzept (ab VM-Flow)

**Paradigmenwechsel:** Die **Förderakte ist der Hub** für jeden Schüler.

```
Startseite
  ↓ Modal: Schüler suchen
Förderakte (Schüler-Zentrale)
  ├── [Platzhalter] Individuelle Förderung
  ├── [Platzhalter] BSLRR
  └── VM SöPädFö → Modals → Förderakte (aktiv) → Förderplan
```

Kein separater Anlass-Screen mehr — Prozesse starten direkt von der Förderakte.

---

## 6. VM SöPädFö — Prozessstruktur

**Modals ab Förderakte:**
1. Förderart, Förderschwerpunkt und Zeitraum wählen
2. Beratungsanlass beschreiben
3. Bisherige Förderung zusammenfassen

**Screens (Seiten):**
- Zustimmung Eltern VM SöPädFö
- Anmeldung VM beauftragende Schule
- Prüfung der Anmeldung durch die Durchführende Schule
- Auftragnehmende Schule nimmt Anmeldung an
  - Modal: Beauftragung BFZ Lehrkraft

---

## 7. Fachliche Begriffe (Pflicht-Wording)

| ✅ Richtig | ❌ Falsch | Hinweis |
|---|---|---|
| Förderung | Förderplan (als Prozess-Begriff) | Laut ARIS-Prozessmodell |
| diSAF | ILA (wenn technisch gemeint) | ILA = Projektname, diSAF = System |
| Förderakte | Akte | Amtlicher Begriff |
| Förderziel | Ziel | Fachbegriff beibehalten |
| Vorbeugende Maßnahme (VM) | — | Vollform beim ersten Auftreten |
| SöPädFö | SOPÄDFÖ | Korrekte Schreibweise |
| BFZ | Beratungs- und Förderzentrum | Abkürzung im Fachkontext OK |
| BSLRR | — | Besondere Schwierigkeiten Lesen/Rechtschreiben/Rechnen |

---

## 8. Team

| Person | Rolle | Kontakt |
|---|---|---|
| Sarah (Soblissa) | Projektleitung, letzte Entscheidungsinstanz | Telegram: 6171498156 |
| Dirk Lenz | Auftraggeber | Telegram: 8233442182 |
| Sebastian | Fachlichkeit (Mensch) | Sein Agent: Bernd (@FelgesBot) |
| Yves | Design (Mensch) | Kein eigener Agent |
| Torsten | Technik-Partner | Implementierung |

---

## 9. Wichtige Dateipfade

| Was | Pfad |
|---|---|
| Gesamtbericht Pilotauswertung | `ila/pilot-ergebnisse/Pilotauswertung_Gesamtbericht_20260410.md` |
| OnePager Pilotauswertung | `ila/pilot-ergebnisse/Pilotauswertung_OnePager.docx` |
| Kompetenzen & Maßnahmen | `ila/Kompetenzen und Maßnahmen/` |
| ARIS Prozessmodelle | `ila/fachlichkeit/` |
| VM-Prozess durchführen | `ila/fachlichkeit/Aufgaben im Prozess - Vorbeugende Maßnahmen BFZ durchführen.docx` |
| VM-Prozess abschließen | `ila/fachlichkeit/Aufgaben im Prozess - Vorbeugende Maßnahmen BFZ abschließen.docx` |
| SöPädFö FDS beauftragen | `ila/fachlichkeit/Aufgaben im Prozess - Entscheidungsverfahren zum Anspruch auf SOPÄDFÖ durchführen - FDS beauftragen.docx` |
| SöPädFö FDS erstellen | `ila/fachlichkeit/Aufgaben im Prozess - Entscheidungsverfahren zum Anspruch auf SOPÄDFÖ durchführen - FDS erstellen.docx` |
| SöPädFö Förderausschuss | `ila/fachlichkeit/Aufgaben im Prozess - Entscheidungsverfahren zum Anspruch auf SOPÄDFÖ durchführen - Förderausschuss durchführen.docx` |
| Kompetenzen überfachlich (Sebastians v5) | `ila/Kompetenzen und Maßnahmen/überfachliche Kompetenzen Vorklasse und Grundstufe Klassenstufe 0 bis 4 Version 5.xlsx` |
| Figma Design-Analyse | `ila/agent-ila/figma-analyse-design-specs-2026-03-31.md` |
| UI-Wording-Regeln | `ila/fachlichkeit/ui-wording-regeln-v1.md` |
| Begriffsmodell | `ila/fachlichkeit/begriffsmodell-v1.md` |
| Anforderung Kalender/Erinnerung | `ila/docs/Anforderungsbeschreibung_Kalender_Erinnerung_Aufgaben.md` |
| Plugin-Befehle (JSONs) | `ila/agent-ila/plugin-befehle/` |

---

## 10. Pilotauswertung — Kernerkenntnisse für Design

- **Workflow funktioniert:** 82% der Förderpläne direkt nach Förderungsanlage erstellt
- **Technik gut:** Stabilität Ø 3,85 — nicht anfassen
- **Fachlicher Inhalt schlecht:** Förderziele reichen aus: Ø 2,15 — schlechtester Wert
- **Top-3-Probleme:** Unterstützer-Feld (nur Vater/Mutter), Maßnahmen zu unkonkret, keine Bearbeitung nach Speichern
- **Goldschatz:** 235 eigene Maßnahmen der Lehrkräfte = Vorlage für Katalog-Erweiterung
- **Vorklasse (Jg. 0):** meiste Einträge, schlechteste Unterstützung → dringend nachbessern
