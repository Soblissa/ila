# Statusreport — KI-gestützte Arbeitsvorhaben
*Referat VI 3.1 | HMKB*
*Erstellt: 2026-04-11 | KW 15/2026*

---

## Übersicht

| # | Thema | Status |
|---|---|---|
| 1 | KI-Pilot ILA | 🟡 Laufend |
| 2 | Analyse CD-Vorgaben Land Hessen | ✅ Abgeschlossen |
| 3 | Datenanalyse & Gesamtauswertung Pilot ILA | ✅ Abgeschlossen |
| 4 | Anforderungen an eine Corporate LLM (Referat VI 3.1) | 🔵 In Vorbereitung |

---

## 1. KI-Pilot ILA

**Status:** 🟡 Laufend

**Ziel:**
Nachweis, dass ein KI-Agent neue Figma-Screens schneller und mindestens gleichwertig erstellen kann wie ein menschlicher Designer — auf Basis des bestehenden Design-Systems der Anwendung diSAF.

**Bisherige Leistungen (Stand KW 14):**
- Cheko (ILA-Hauptagent) vollständig eingerichtet und betriebsbereit
- Figma-Plugin entwickelt: generiert Screens direkt in Figma, 155 Komponenten analysiert und erfasst
- Erste Screen-Generierung erfolgreich (Navigation, Heading, Struktur)
- ARIS-Prozessmodelle gelesen und dokumentiert, Begriffsmodell angelegt
- Sebastians Agent (Bernd, @FelgesBot) eingerichtet und gepairt
- 19 App-Screenshots der Testumgebung dokumentiert, vollständiger Workflow erfasst
- Repo-Struktur aufgebaut: `agent-ila/`, `pilot-ergebnisse/`, `fachlichkeit/`, `docs/`

**Aktivitäten KW 15:**
- Vollständige Auswertung der Pilotdaten (Nutzerverhalten, In-App-Feedback, Abschlussumfrage)
- Erstellung eines strukturierten Gesamtberichts (4 Kapitel, navigierbar, Word-Export)
- Bereinigung und Validierung aller Kennzahlen, Erstellung validiertes Auswertungs-Script

**Output/Ergebnisse:**
- `pilot-ergebnisse/Pilotauswertung_Gesamtbericht_20260410.md/.docx` — vollständiger Analysebericht
- `pilot-ergebnisse/Eigene_Massnahmen_235_eindeutig.md` — Liste der 235 eigenen Maßnahmen
- `pilot-ergebnisse/auswertung_basis.py` — validiertes Auswertungs-Script
- `fachlichkeit/screenshots/` — 19 App-Screenshots mit Walkthrough-Dokumentation
- `docs/` — Begriffsmodell, UI-Wording, Figma-Plugin-Anforderungen, Agentenkommunikation

**Zentrale Erkenntnisse aus der Pilotauswertung:**
- 133 Nutzer, 60 Tage, Ø 7 Minuten Sitzungsdauer
- Bedienbarkeit gut (Ø 3,46/4) — fachlicher Inhalt enttäuscht (Förderziele: Ø 2,15/4)
- Top-3-Probleme: Unterstützer-Feld zu eingeschränkt, Maßnahmen lückenhaft, keine Nachbearbeitung möglich
- Größter Wunsch für Ausbaustufe 2: Kollegiums-Austauschfunktion (9 von 19 auf Rang 1)

**Aktuelle Herausforderung:**
Tiefere Screen-Ebenen sind in Figma nicht als eigenständige Komponenten definiert — manuell eingebettet. Erschwert automatisierte Generierung. Lösung in Erarbeitung.

**Nächste Schritte:**
- Figma-Screens auf Basis der Piloterkenntnisse entwickeln (KW 16)
- Fachliche Anforderungen von Sebastian ins Repo
- Handlungsanweisungen für Design-Agent (Yves) und Fachlichkeits-Agent (Sebastian) erstellen
- Steuerungs- und Freigabe-Matrix für das Agenten-Team aufsetzen
- Direkte Kommunikation Cheko ↔ Bernd einrichten (läuft derzeit über Sarah als Brücke)

---

## 2. Analyse CD-Vorgaben Land Hessen / Figma Design Specs

**Status:** ✅ Abgeschlossen

**Beschreibung:**
Analyse der Figma Design Specs der ILA-Anwendung sowie der Corporate-Design-Vorgaben des Landes Hessen als Grundlage für die KI-gestützte Screen-Generierung.

**Ergebnisse:**
- 24 Figma-Seiten analysiert und dokumentiert (9 Screen-Seiten, 9 Komponenten-Seiten, 6 sonstige)
- 9 Hauptflows erfasst: Neue Förderung, Förderziele, Evaluation, Förderplan, Notizen, Feedback u.a.
- 155 Komponenten aus dem Design-System erfasst und in Plugin integriert
- Responsive-Strategie dokumentiert: S/M/L-Größen je Screen
- Bekannte Node-IDs der Kernkomponenten dokumentiert (Navigation Bar, Task List Item, Notiz)
- CD-Vorgaben sind in Figma-Datei umgesetzt und fließen in die Screen-Generierung ein

**Output:**
- `docs/figma-analyse-design-specs-2026-03-31.md` — vollständige Analyse
- `docs/ui-wording-regeln-v1.md` — Sprach- und Benennungsregeln
- `docs/begriffsmodell-v1.md` — fachliches Begriffsmodell

---

## 3. Datenanalyse & Gesamtauswertung Pilot ILA

**Status:** ✅ Abgeschlossen

**Beschreibung:**
Vollständige quantitative und qualitative Auswertung der drei Datenquellen aus dem ILA-Piloten: Nutzungsverhalten (Sheet 1), In-App-Feedback (Sheet 2) und Abschlussumfrage (CSV).

**Ergebnis:**
Gesamtbericht erstellt, validiert und im Repository abgelegt. Word-Export verfügbar. Alle Kennzahlen auf Datenfehler geprüft und bereinigt.

---

## 4. Anforderungen an eine Corporate LLM für das Referat VI 3.1 des HMKB

**Status:** 🔵 In Vorbereitung

**Beschreibung:**
Erstellung eines Anforderungsdokuments für eine mögliche Ausschreibung zur Implementierung einer Corporate LLM (Large Language Model, großes Sprachmodell) inkl. Agentenstruktur für das Referat VI 3.1. Das Dokument beschreibt unter anderem: Was ist eine Corporate LLM, wie müsste eine solche für das Referat aussehen, und welche Anforderungen sind an Anbieter zu stellen.

**Aktivitäten:**
- Thema definiert, Ordnerstruktur im Repository angelegt
- Inhaltliche Ausarbeitung beginnt in KW 15

**Nächste Schritte:**
- Inhaltliche Ausarbeitung des Dokuments
- Definition der Anforderungskategorien
- Abstimmung mit Sarah über Zielgruppe und Detailtiefe

---

## KI-Nutzung

| Kennzahl | Wert |
|---|---|
| Modell | Claude Sonnet 4.6 (Anthropic) |
| Session KW 15 | laufend |
| Cache-Hit-Rate | ~100% (effiziente Nutzung durch Kontext-Caching) |
| Token-Erfassung | Manuell je Session — keine automatische Akkumulation über Sessions |

*Hinweis: OpenClaw speichert Token-Verbräuche nicht automatisch über Sessions hinweg. Auf Wunsch kann ein manuelles Token-Log eingerichtet werden.*

---

*Nächste Aktualisierung: KW 16 | Erstellt mit: Cheko (ILA-Hauptagent)*
