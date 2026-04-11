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

**Beschreibung:**
Agenten-gestützter UI/UX-Design-Pilot im sonderpädagogischen Kontext. Ziel ist die Entwicklung einer digitalen Förderplanungsanwendung (diSAF) mit KI-Unterstützung. Der Pilot wurde mit 133 Lehrkräften und Schulleitungsmitgliedern in hessischen Schulen durchgeführt.

**Aktivitäten (diese Woche):**
- Vollständige Auswertung der Pilotdaten (Nutzerverhalten, In-App-Feedback, Abschlussumfrage)
- Erstellung eines strukturierten Gesamtberichts (4 Kapitel, navigierbar)
- Bereinigung und Validierung aller Kennzahlen
- Export als Word-Dokument

**Output/Ergebnisse:**
- `pilot-ergebnisse/Pilotauswertung_Gesamtbericht_20260410.md` — vollständiger Analysebericht
- `pilot-ergebnisse/Pilotauswertung_Gesamtbericht_20260410.docx` — Word-Export
- `pilot-ergebnisse/Eigene_Massnahmen_235_eindeutig.md` — Liste der 235 eigenen Maßnahmen
- `pilot-ergebnisse/auswertung_basis.py` — validiertes Auswertungs-Script

**Zentrale Erkenntnisse:**
- 133 Nutzer, 60 Tage, Ø 7 Minuten Sitzungsdauer
- Bedienbarkeit gut (Ø 3,46/4) — fachlicher Inhalt enttäuscht (Förderziele: Ø 2,15/4)
- Top-3-Probleme: Unterstützer-Feld zu eingeschränkt, Maßnahmen lückenhaft, keine Nachbearbeitung möglich
- Größter Wunsch für Ausbaustufe 2: Kollegiums-Austauschfunktion (9 von 19 auf Rang 1)

**Nächste Schritte:**
- Figma-Screens auf Basis der Piloterkenntnisse entwickeln (geplant: KW 16)
- Handlungsanweisungen für Design-Agent (Yves) und Fachlichkeits-Agent (Sebastian) erstellen
- Steuerungs- und Freigabe-Matrix für das Agenten-Team aufsetzen

---

## 2. Analyse CD-Vorgaben Land Hessen

**Status:** ✅ Abgeschlossen

**Beschreibung:**
Analyse der Corporate-Design-Vorgaben des Landes Hessen als Grundlage für die visuelle Gestaltung der ILA-Anwendung.

**Ergebnis:**
Analyse abgeschlossen. Vorgaben sind dokumentiert und fließen in die Figma-Screens ein.

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
