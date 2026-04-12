# Statusbericht KI-Einsatz
*Referat VI 3.1 | HMKB*
*Stand: KW 15 / 2026-04-12*

---

## 1. KI-Pilot

**Ziel:** Nachweis, dass ein KI-Agent (Cheko) Designaufgaben übernehmen kann, die zur Weiterentwicklung der ILA-Anwendung führen. Der Pilot läuft den gesamten April 2026.

### Fortschritt

- Cheko (ILA-Hauptagent) vollständig eingerichtet und betriebsbereit
- Figma Design Specs analysiert: 24 Seiten, 9 Hauptflows, 155 Komponenten erfasst
- Screenshots der aktuellen Anwendung (19 Stück) dokumentiert, vollständiger Workflow erfasst
- ARIS-Prozessmodelle gelesen und dokumentiert
- Figma-Plugin entwickelt: generiert Screens direkt in Figma auf Basis der vorhandenen Komponenten
- Erste Screen-Generierung erfolgreich (Navigation, Heading, Strukturaufbau)
- Agenten-Team aufgebaut: Sebastians Agent (Bernd) eingerichtet und betriebsbereit
- Repository-Struktur aufgebaut: `agent-ila/`, `fachlichkeit/`, `docs/`, `pilot-ergebnisse/`
- Prozessbeschreibungen werden heute analysiert (noch ausstehend)

### Nächste Schritte

- Analyse der Prozessbeschreibungen und ARIS-Modelle abschließen
- Erste vollständige Screens auf Basis der Pilotauswertung entwickeln
- Handlungsanweisungen für Design-Agent (Yves) und Fachlichkeits-Agent (Sebastian) erstellen
- Steuerungs- und Freigabe-Matrix für das Agenten-Team aufsetzen
- Direkte Kommunikation zwischen Cheko und Sebastian-Agent einrichten (läuft derzeit über Sarah)

### Herausforderung

Tiefere Screen-Ebenen sind in Figma nicht als eigenständige Komponenten definiert — manuell eingebettet. Erschwert die automatisierte Generierung. Lösung wird erarbeitet.

### Ungefährer Tokenaufwand

Größtes Thema — läuft den gesamten April. Tokenaufwand wird fortlaufend akkumuliert; manuelle Erfassung je Session.

---

## 2. Auswertung ILA-Pilot

**Ziel:** Vollständige quantitative und qualitative Auswertung des realen ILA-Piloten (133 Nutzer, 60 Tage) als Grundlage für die Weiterentwicklung.

### Fortschritt

Abgeschlossen. Drei Datenquellen ausgewertet:

- **Nutzerverhalten** (15.342 Zeilen): Nutzung, Rückkehrverhalten, Maßnahmen, Förderpläne, Jahrgänge
- **In-App-Feedback** (32 Einträge, 27 Freitexte): Bewertungen nach Seite/Schritt, thematische Cluster
- **Abschlussumfrage** (19 Teilnehmende): Bedienbarkeit, Fachpraxis, gewünschte Funktionen

Gesamtbericht erstellt (4 Kapitel, navigierbar), validiert und versandt.

**Zentrale Erkenntnisse:**
- Bedienbarkeit gut (Ø 3,46/4) — fachlicher Inhalt enttäuscht (Förderziele: Ø 2,15/4)
- Top-3-Probleme: Unterstützer-Feld zu eingeschränkt, Maßnahmen lückenhaft, keine Nachbearbeitung möglich
- Größter Wunsch Ausbaustufe 2: Kollegiums-Austauschfunktion (9 von 19 auf Rang 1)

### Nächste Schritte

Keine — abgeschlossen.

### Herausforderung

Keine — abgeschlossen.

### Ungefährer Tokenaufwand

Intensiv — ein Arbeitstag (KW 15). Hauptaufwand: iterative Datenanalyse, Fehlerkorrektur, Berichtsstrukturierung.

---

## 3. Analyse Erlass zum neuen Hessenauftritt

**Ziel:** Analyse des STK-Erlasses vom 23.03.2026 (neues Corporate Design Land Hessen) und Bewertung der Auswirkungen auf die ILA-Anwendung.

### Fortschritt

Abgeschlossen. Grundlage: Erlass + Hessen Corporate Design Manual V1.0k + Analyse der realen ILA-Anwendung (Screenshots).

**Zentrale Erkenntnisse:**
- ILA ist bereits nahezu CD-konform in der Grundstruktur — kein Redesign notwendig
- Konkrete Anpassungen: Hessenmarke einbinden, Schriftart (Hessen Gellix), Farbkalibrierung auf Hessen Blau #0A0076
- Offene politische Frage: darf das ila-Logo (Smile) als Ausnahme bestehen bleiben?
- Mit KI-Unterstützung ist eine schrittweise Anpassung deutlich beschleunigt möglich

Analyse-Dokument erstellt und versandt.

### Nächste Schritte

Keine — abgeschlossen. Entscheidung zum ila-Logo liegt beim HMKB.

### Herausforderung

Keine — abgeschlossen.

### Ungefährer Tokenaufwand

Mittel — Erlass-Lektüre und Screenshot-Analyse über eine Session.

---

## 4. Anforderungen an eine Corporate LLM im Ref. VI.3.1

**Ziel:** Erstellung eines Anforderungsdokuments für eine mögliche Ausschreibung zur Implementierung einer Corporate LLM (Large Language Model) inkl. Agentenstruktur für das Referat VI.3.1 des HMKB.

### Fortschritt

Noch nicht begonnen. Ordnerstruktur im Repository angelegt: `Anforderungen an eine Corporate LLM/`

### Nächste Schritte

- Inhaltliche Ausarbeitung des Dokuments beginnen
- Definition der Anforderungskategorien (Was ist eine Corporate LLM? Welche Anforderungen an Anbieter?)
- Beschreibung des konkreten Bedarfs für Referat VI.3.1

### Herausforderung

Noch offen — wird bei Beginn der Ausarbeitung definiert.

### Ungefährer Tokenaufwand

Noch nicht abschätzbar — Thema wurde noch nicht begonnen.

---

## 5. Allgemeine Unterstützung

**Ziel:** Unterstützung bei verschiedenen einzelnen Fragen und Aufgaben, die nicht einem der Hauptthemen zuzuordnen sind — z.B. konzeptionelle Diskussionen, Einschätzungen, Recherchen, Erklärungen.

### Fortschritt

Laufend. Beispiele dieser Woche:
- Erklärung Telegram-Sicherheit vs. WhatsApp vs. Signal
- Strukturierung und Formatdiskussion des Statusberichts
- Diskussion über Token-Erfassung und Berichtsformat

### Nächste Schritte

Fortlaufend nach Bedarf.

### Herausforderung

Keine.

### Ungefährer Tokenaufwand

Gering bis mittel je Woche — verteilt über mehrere kurze Interaktionen.

---

## Technische Infrastruktur (Überblick)

| Komponente | Status |
|---|---|
| Cheko (ILA-Hauptagent) | ✅ Betriebsbereit |
| Sebastians Agent (Bernd) | ✅ Betriebsbereit |
| Figma-Plugin | ✅ Läuft (v4, 155 Komponenten) |
| ILA-Repository | ✅ Aktuell |
| Semantische Suche | ⚠️ Teilweise (Torsten muss einrichten) |
| Direkte Agenten-Kommunikation Cheko ↔ Bernd | ⚠️ Noch über Sarah als Brücke |

---

*Nächste Aktualisierung: KW 16 | Erstellt mit: Cheko (ILA-Hauptagent)*
