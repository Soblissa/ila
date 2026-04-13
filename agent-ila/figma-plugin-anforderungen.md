# Figma-Plugin: Anforderungen

**Stand:** 2026-03-23  
**Autor:** Cheko (ILA-Hauptagent)  
**Status:** Entwurf — zur Freigabe durch Sarah, zur Umsetzung durch Torsten

---

## Zweck

Das Plugin verbindet den ILA-Agenten-Workflow mit Figma.  
Es übersetzt strukturierte Agenten-Ausgaben (Wireframes, Screen-Beschreibungen) in echte Figma-Objekte — direkt in der Sandbox-Datei (Testumgebung, die vom Live-System getrennt ist).

---

## Kontext

- **Figma-Account:** Sarah (Soblissa), Professional-Plan
- **Figma-Umgebung:** Sandbox (Kopie der Produktiv-Instanz — kein Risiko für Live-Daten)
- **Agenten-Seite:** ILA-Hauptagent (Cheko) gibt strukturierten Input, Design-Agent führt aus
- **Plugin-Typ:** Privates Plugin (nicht öffentlich in der Community)

---

## Kernfunktionen (Muss)

### 1. Frame erstellen (Rahmen/Screen anlegen)
- Neuen Frame auf einer definierten Seite anlegen
- Größe und Name per Parameter übergeben
- Standardgröße: 1440 × 900 px (Desktop) und 390 × 844 px (Mobile)

### 2. Komponenten einfügen (Design-Bausteine platzieren)
- Komponenten aus dem lokalen Design-System abrufen
- Komponenten per Name ansprechen (z. B. "Button/Primary", "Input/Text")
- Komponenten an definierten Positionen im Frame platzieren

### 3. Text setzen
- Textinhalte in bestehende Textfelder (Text-Layer) schreiben
- Textstile (Schriftart, Größe, Gewicht) aus dem Design-System übernehmen

### 4. Layout-Struktur aufbauen
- Auto-Layout (automatische Ausrichtung von Elementen) anwenden
- Abstände und Ausrichtung per Parameter setzen

### 5. Ausgabe exportieren
- Fertigen Frame als PNG (Bilddatei) oder PDF exportieren
- Datei lokal oder im Repo ablegen

---

## Eingabeformat (wie der Agent das Plugin steuert)

Das Plugin soll eine **JSON-Datei** (strukturierte Datenbeschreibung) als Eingabe akzeptieren.  
Beispielstruktur:

```json
{
  "screen_name": "Bearbeitungsansicht_Formular_V1",
  "page": "Agent-Entwürfe",
  "size": "desktop",
  "components": [
    { "name": "Header/Default", "x": 0, "y": 0 },
    { "name": "Input/Text", "x": 40, "y": 100, "label": "Vorname" },
    { "name": "Input/Text", "x": 40, "y": 160, "label": "Nachname" },
    { "name": "Button/Primary", "x": 40, "y": 260, "label": "Speichern" }
  ]
}
```

---

## Technische Rahmenbedingungen

- **Sprache:** TypeScript (Microsofts erweiterte Version von JavaScript — Figma-Standard für Plugins)
- **Figma Plugin API** (offizielle Schnittstelle von Figma für Plugin-Entwicklung): Lese- und Schreibzugriff auf alle Layer (Ebenen) und Nodes (Objekte im Figma-Baum)
- **Kein Server nötig:** Das Plugin läuft lokal in der Figma Desktop-App
- **Figma Desktop-App** erforderlich (Plugin-Entwicklung läuft nicht im Browser)

---

## Nicht im Scope (Umfang) dieses Pilots

- Kein KI-Modell im Plugin selbst — die Intelligenz liegt beim Agenten, das Plugin ist nur der "Arm"
- Kein Schreiben in die Produktiv-Figma-Datei
- Keine automatische Veröffentlichung in der Figma Community

---

## Abgrenzung: Wer macht was

| Aufgabe | Zuständigkeit |
|---|---|
| Screen-Konzept und Inhalt | ILA-Hauptagent (Cheko) |
| JSON-Ausgabe erzeugen | ILA-Hauptagent / Design-Agent |
| Plugin entwickeln | Torsten |
| Plugin in Figma ausführen | Design-Agent (Yves) |
| Ergebnis reviewen | Sarah |

---

## Nächste Schritte

1. Torsten prüft technische Umsetzbarkeit (insbesondere Komponenten per Name ansprechen)
2. Einigung auf JSON-Format (kann noch angepasst werden)
3. Minimal-Version bauen: erst nur Frame + 1 Komponente einfügen
4. Schrittweise Erweiterung nach erstem Testlauf
