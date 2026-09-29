# ILA_KONTEXT.md — Checos ILA-Briefing
*Pflichtlektüre bei jedem ILA-Thema. Immer zuerst lesen.*
*Letzte Aktualisierung: 2026-09-28*

---

## 0. Architektur (wichtig!)

- **LUSD** = Lehrer- und Schülerdatenbank Hessen — über 20 Jahre gewachsene Kernanwendung, Monolith + mehrere eigene Microservices
- **ila** = Teilanwendung der LUSD, besteht aus **2 Microservices** (Backend + Frontend), bezieht Schülerstammdaten aus der LUSD
- **Umgebung:** Azure DevOps, AWAs (Anwendungsanforderungen) als Grundlage für Entwickler
- **Verfahrensdoku:** Aktuell händisch erstellt, als PDF gespeichert, von Menschen gepflegt
- **Testfälle:** Händisch pro AWA erstellt, sehr fehleranfällig
- **C-LLM-Ziele für LUSD:** AWA-Assistent, Testfall-Generator, Verfahrensdoku-Generator, Anwenderhilfen-Generator, LUSD-Wissensassistent, Change-Impact-Analyse

## 1. Was ist ILA / diSAF?

- **ILA = diSAF** — ein und dasselbe Produkt. Nie verwechseln.
- Digitales System zur Abbildung von **individueller und sonderpädagogischer Förderung** an hessischen Schulen
- Zielgruppe: Lehrkräfte, Schulleitung, Schulverwaltung
- Auftraggeber: Dirk Lenz (Telegram-ID: 8233442182) — Sarah berichtet an ihn
- System-Kontext: HMKB (Hessisches Ministerium für Kultus und Bildung)

---

## 2. Aktueller Projektstand (Stand: 2026-09-11, Repo-Stand 30.07.2026)

### Was abgeschlossen ist
- ✅ Pilotauswertung AS1 (30.01.–31.03.2026) — Gesamtbericht fertig
- ✅ FigJam-Flows: Individuelle Förderung (v12_referenz) + BSLRR (v9)
- ✅ Figma Screens: Startseite, Förderakte, Förderziel, BSLRR-Flow, Nutzerfeedback u.a.
- ✅ OnePager Pilotauswertung (Word + MD)
- ✅ Anforderungsbeschreibung Kalender/Erinnerung/Aufgaben
- ✅ **Auswertung Förderakte** (18.05.2026) — Fragen + Ergebnistabelle in `Förderakte/`
- ✅ **Hessische Anforderungen Barrierefreiheit** (29.05.2026) — zusammengetragen in `Barrierefreiheit/`
- ✅ **Corporate LLM / ADO als Single Source of Truth** — Arbeitsentwurf vom 25.05.2026, in vier Teile strukturiert (MD + Word)
- ✅ **Lachnit-Screens SöPädFö** (13.07.2026) — 9 PNGs in `Downloads_Sarah/Lachnit_Screens_SOPAeDFO/`: Anlegen, Beratungsanlass, Zustimmung, Beauftragung, Durchführung, Maßnahmen (auch Sicht Auftragnehmende Schule), Abschließen
- ✅ **Einführungskonzept ila Grundschulen Hessen** (21.–25.07.2026) — 11 Abschnitte, MD + Word, in `docs/rollout-konzept/`
- ✅ **LUSD-Testautomatisierung** (30.07.2026) — Machbarkeitsstudie (Autor: Tobias Gudd, HZD Hessen), Konzept mit Corporate LLM, Management Briefing (MD + Word) in `LUSD/Testautomatisierung/`
- ✅ **LUSD-Dokumentation** — Release-Änderungen 11 bis 41 plus Anleitungen im Ordner `LUSD/`
- ✅ **EIM-Anforderungssteckbrief HZD v2.3** (03.07.2026) — von Sarah am 11.09.2026 übermittelt, als Markdown abgelegt in `EIM/`. Absichtserklärung (LoI) für die Anbindung eines Fachverfahrens an die zentrale Identitätsplattform der HZD (SSO, MFA, IGA, OIDC/SAML, SCIM). Noch nicht für diSAF ausgefüllt
- ✅ **Präsentation Corporate LLM HMKB („Keller-KI“)** — 11 Folien, neu gebaut am 11.09.2026, in `Anforderungen an eine Corporate LLM/Corporate_LLM_HMKB_Praesentation.pptx`. Reproduzierbar über `scripts/build_corporate_llm_praesentation.py`
- ✅ **Nextcloud ChekoWorkspace als primärer bearbeitbarer Ausgabekanal** (15.09.2026) — kontrollierte Struktur für Eingang, aktive Themen, Entscheidungen, Freigaben, Referenzen und Archiv eingerichtet. Erste Collabora-Dokumente zu diSAF, VM SöPädFö, EIM, Corporate LLM und LUSD-Testautomatisierung aus den bereitgestellten OTT-Vorlagen erzeugt
- ✅ **Produktbeschreibung ila sprachlich korrigiert** (28.09.2026) — Rechtschreibung, Grammatik und Lesefluss überarbeitet; Fachbegriffe und Kernaussagen beibehalten
- ✅ **UI-Textaudit der Figma Design Specs** (29.09.2026) — alle 34 Seiten eingelesen, 1.243 unterschiedliche Texte auf 16 funktionalen Seiten geprüft und Konsistenzvorschläge dokumentiert in `fachlichkeit/ui-textaudit-figma-2026-09-29.md`. Keine direkte Du-Ansprache gefunden; Schwerpunkte sind der Wechsel zwischen Sie-/Ich-/Wir-Perspektive, 25 unterschiedliche Platzhaltertexte, Rechtschreibung sowie uneinheitliche Leitbegriffe

### Was gerade läuft
- 🔄 **Wording-Überarbeitung der Figma Design Specs** (29.09.2026) — aktueller Stand der offiziellen Figma-Instanz wurde als lokale `.fig`-Datei exportiert und in Sarahs Instanz importiert. Neue Arbeitskopie: `ila _ Design Specs`, Datei-Key `mGVoWdSLQzFABJlEzOQPRn`. Neuer `FIGMA_TOKEN` liegt im geschützten OpenClaw-Schlüsselspeicher und ist auf `api.figma.com` beschränkt; die unverschlüsselte Übergabedatei wurde sicher gelöscht. Der API-Lesezugriff wurde am 29.09.2026 erfolgreich mit HTTP 200 verifiziert; alle 34 Seiten der Arbeitskopie sind erreichbar. **Plugin-Prüfung 29.09.2026:** Manifest und JavaScript sind syntaktisch gültig, aber der eingebettete Komponenten-Index ist nach dem Dateiimport teilweise veraltet: Von 155 hinterlegten Node-IDs sind nur 53 in der Arbeitskopie vorhanden, 102 fehlen. Der bisherige Drei-Komponenten-Test würde nur Navigation Bar Main und Navigation Bar Content finden; Page Heading Plan fehlt. Das Plugin ist daher derzeit nur teilweise funktionsfähig und benötigt einen neu erzeugten Komponenten-Index sowie die geplante Wording-Erweiterung
- 🔄 Neuer Flow "VM SöPädFö" (Vorbeugende Maßnahme) — flow_ab_vm_v2.json fertig, v3 in Vorbereitung
- 🔄 Neues Konzept: **Förderakte als Hub** — alle Prozesse starten von dort, kein separater Anlass-Einstieg mehr
- 🔄 Neue FigJam-Datei: `ila_Flow_ab_VM` (noch anzulegen)
- 🔄 **Corporate LLM für HMKB** — Angebot in Vorbereitung, Budget max. 100.000 € über 2 Jahre. Zweiphasenmodell: **Phase 1** (KI-Server außerhalb des Hessennetzes, manueller Dokumentenexport, ohne HZD lieferbar, ca. 80 % des Nutzens) und **Phase 2** (Server im Hessennetz, Live-Anbindung ADO + SharePoint, braucht eigenen HMKB-Serverraum oder HZD-Kooperation). Kosten 2 Jahre: 53.000–87.000 €. Hardware: NVIDIA RTX A6000 Ada 48 GB. Modelle: Mistral Small 3.2 24B (1. Wahl, EU), Qwen 2.5 32B, Llama 4 Scout. Präsentation liegt vor, Angebot noch offen

### Offene TODOs
- [ ] Figma-Plugin für die Wording-Überarbeitung erweitern: Textfelder ausgewählter Frames exportieren, Korrekturen anhand stabiler Node-IDs einlesen und nach Freigabe in der Arbeitskopie anwenden
- [ ] Komponenten-Index des Figma-Plugins aus der neuen Design-Specs-Arbeitskopie neu erzeugen (102 von 155 bisherigen Node-IDs fehlen)
- [ ] flow_ab_vm_v3 bauen (neue Struktur: Förderakte als Hub)
- [ ] FigJam-Seite anlegen für neuen Flow
- [ ] BSLRR + IFö in neuen Ansatz überführen
- [ ] Handlungsanweisung für Sebastian schreiben (Yves ist raus)
- [ ] Steuerungs- und Freigabe-Matrix erstellen
- [ ] Barrierefreiheits-Checkliste für ila aus hessischen Anforderungen ableiten
- [ ] Corporate-LLM-Angebot HMKB finalisieren — 22 Fragen an Dirk Lenz offen (u. a. eigener Serverraum? Wer verwaltet die Microsoft-Tenants? Ausschreibungspflicht? KI-Nutzungsrichtlinie? Datenschutzbeauftragter eingebunden?)
- [ ] Prüfen, ob der EIM-Steckbrief für diSAF ausgefüllt werden soll (Entscheidungspunkte: Hosting-Kategorie, Nutzergruppen, Vertrauensstufe Bronze/Silber/Gold, PPID oder Klardaten, Rollenmodell, Provisionierung)
- [ ] Einführungskonzept: Abschnitt 11 „Offene Punkte und nächste Schritte" abarbeiten

### Lücke im Kontext
Zwischen dem letzten Repo-Commit (30.07.2026) und dem 11.09.2026 liegen rund sechs Wochen ohne Repo-Aktivität. Laut Sarah ist in dieser Zeit wenig passiert. Aus Sessions belegt ist nur die Corporate-LLM-Diskussion vom 07.09.2026 (siehe oben).

### Festgestellte Klarstellung (11.09.2026)
Der EIM-Steckbrief weist Firewall-Freischaltungen den Fachverfahrensverantwortlichen zu („rechtzeitig beim IT-Betrieb zu beantragen“). Das ist eine Zuständigkeitszuweisung, **keine Zusage auf Genehmigung**. Die zugesagten „≤ 3 Arbeitstage“ gelten nur für das EIM-Onboarding, nicht für Netzfreigaben. Beantragen heißt nicht durchsetzen — und der EIM-Fall (HZD-intern, Eigeninteresse der HZD) ist nicht vergleichbar mit unserem Fall (externer Server will ins Hessennetz).

### Wording-Entscheidung (29.09.2026)

- Direkte Ansprache konsequent mit „Sie“, „Ihr“ und „Ihre“
- Persönliche Begrüßung auf der Startseite: `Willkommen, [Nutzername]`
- Eigene Entitäten sichtbar aus der Ich-Perspektive über Besitz: „Mein Schüler“, „Meine Förderakten“
- „Ich …“ nur für ausdrückliche Erklärungen, Bestätigungen oder Einwilligungen
- Systemmeldungen neutral formulieren

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
- **13.04.2026:** Repo aufgeräumt — kein freischwebendes Dokument mehr, alles in Ordnern
- **13.04.2026:** Bernd (linux-user `sebastian`) hat Schreibzugriff auf ila-Repo, Repo geklont unter `/home/sebastian/ila/`, Git-Identity: `Bernd <bernd@ila-agent.local>`
- **13.04.2026:** LUSD-Ordner angelegt, Bernd hat 95 LUSD-Anleitungsdateien eingecheckt
- **13.04.2026:** C-LLM-Dokument ausgebaut (Abschnitte 1–6, LUSD-Anwendungsfälle, Ausgangslage HMKB)
- **13.04.2026:** Dirk Lenz freigeschaltet für `@ila_chefkoch_bot`, Anschreiben formuliert
- **14.04.2026:** Figma-Datei "ILA Agent Workspace" heißt eigentlich **"ila _ Design Specs - Agent-Entwürfe"** (Tab in der Design Specs Datei)
- **14.04.2026:** Plugin-Pfad auf Sarahs Rechner: `C:\Users\sbonh\OneDrive - Kuubera UG\Business\Automagia\ila\plugin\`
- **14.04.2026:** Yves ist raus — wir machen das zu zweit
- **15.04.2026:** Plugin-Bug gefunden: JSON-Feld `component_id` vs. `nodeId` Mismatch — gefixt, aber Fehlerausgabe noch nicht verifiziert
- **15.04.2026:** Erfolgreicher Test: Förderplan-Screen (3 Komponenten) gebaut — Navigation Bar Main, Navigation Bar Content, Page Heading Plan
- Aktuelle Node-IDs (verifiziert 15.04):
  - Navigation Bar Main: `116:80916`
  - Navigation Bar Content: `116:83187`
  - Page Heading Plan: `1:116020`
  - Förderplan Screen: `5:43555`
- Figma-Plugin: 2 verbleibende Fehler sind wahrscheinlich Warnungen ohne visuelle Auswirkung
- Semantische Suche: noch nicht eingerichtet — Torsten muss das machen ("genauso wie Turiya")
- Figma-Plugin Hot-Reload: aktiviert — `code.js` speichern → Plugin startet neu

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
- Repo lokal: `/home/cheko/.openclaw/workspace/ila`
- Remote: `git@github.com:soblissa/ila` (SSH-Schlüssel `~/.ssh/id_ed25519`, Konto Soblissa, Schreibzugriff verifiziert 11.09.2026)
- Branch: `main`
- Identity: `Cheko <cheko@ila-agent.local>` (global gesetzt 11.09.2026)
- Hinweis: `AGENTS.md` nennt fälschlich `/home/cheko/ila` — gültig ist der Pfad oben

### Nextcloud / Collabora
- WebDAV-Einbindung: `/home/cheko/.openclaw/workspace/nextcloud-shared`
- Primärer Ausgabebereich: `nextcloud-shared/ChekoWorkspace/`
- Start und Arbeitsregeln: `ChekoWorkspace/00_START/README.md`
- Unveränderte Vorlagen: `ChekoWorkspace/40_Collabora-Vorlagen/`
- Bearbeitbare Ausgaben werden als `.odt` aus der passenden `.ott`-Vorlage erzeugt
- Git bleibt die technische Quelle für versionierte Projektartefakte; Nextcloud dient gemeinsamer Sichtung, Bearbeitung und Freigabe

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
