# ILA Agent Screen Builder — Figma-Plugin

Ein Figma-Plugin für das ILA-Pilotprojekt, das es KI-Agenten ermöglicht, Screens
automatisiert aus einer JSON-Spezifikation zu erstellen.

---

## Dateien

| Datei | Zweck |
|---|---|
| `manifest.json` | Plugin-Metadaten für Figma |
| `code.ts` | Haupt-Logik (TypeScript — Quelle) |
| `code.js` | Kompiliertes JS (von Figma ausgeführt) |
| `ui.html` | Plugin-Oberfläche (JSON-Eingabe + Feedback) |

---

## Installation (lokales privates Plugin)

1. Figma Desktop-App öffnen
2. Menü → **Plugins** → **Development** → **Import plugin from manifest…**
3. Diese `manifest.json` auswählen
4. Plugin erscheint unter **Plugins → Development → ILA Screen Builder**

> Kein Server, kein Backend. Läuft vollständig lokal in der Figma Desktop-App.

---

## Nutzung

### Via UI

Plugin öffnen → JSON einfügen → **„Screen erstellen"** klicken.

Mit dem **„Beispiel"**-Button wird ein Beispiel-JSON geladen.

### JSON-Format

```json
{
  "screen_name": "Foerderplan_Initial_V1",
  "page": "Agent-Entwürfe",
  "size": "desktop",
  "components": [
    { "name": "Navigation Bar Main", "x": 0, "y": 0 },
    { "name": "Input Text", "x": 40, "y": 100, "label": "Stärken" },
    { "name": "Button", "x": 40, "y": 260, "label": "Speichern" }
  ]
}
```

### Felder

| Feld | Pflicht | Beschreibung |
|---|---|---|
| `screen_name` | ✅ | Name des neuen Frames |
| `page` | ✅ | Zielseite (wird erstellt wenn nicht vorhanden) |
| `size` | — | `"desktop"` (1440×900, Standard) oder `"mobile"` (390×844) |
| `components` | ✅ | Liste der einzufügenden Komponenten |
| `components[].name` | ✅ | Exakter Komponentenname aus dem Design-System |
| `components[].x` | ✅ | X-Position im Frame (px) |
| `components[].y` | ✅ | Y-Position im Frame (px) |
| `components[].label` | — | Text-Inhalt (wird in den ersten TextNode der Komponente geschrieben) |

---

## Voraussetzungen & Libraries

Das Plugin sucht Komponenten **per Name** in dieser Reihenfolge:

1. Lokale Komponenten im aktuellen Figma-Dokument
2. Eingebundene Component-Sets (Varianten) im Dokument

**Wichtig:** Das Design-System muss als **lokale Library** im Figma-Dokument
eingebunden sein, in dem das Plugin läuft. Komponenten aus externen Team-Libraries
werden nur gefunden, wenn sie bereits im Dokument verwendet werden.

→ Empfehlung: Design-System-Datei öffnen, „Publish to Library" aktivieren,
und im Agent-Entwürfe-Dokument unter **Assets → Libraries** einbinden.

---

## Fehlerbehandlung

- Wenn eine Komponente per Name nicht gefunden wird: Fehlermeldung in der UI,
  restliche Komponenten werden trotzdem verarbeitet.
- Wenn die Zielseite nicht existiert: wird automatisch angelegt.
- Ungültiges JSON: Parsing-Fehler wird angezeigt, kein Frame wird erstellt.

---

## Entwicklung

### TypeScript kompilieren

```bash
# Einmalig: TypeScript-Compiler installieren
npm install -g typescript

# Kompilieren (im figma-plugin/ Verzeichnis)
tsc code.ts --target ES2017 --lib ES2017,DOM --outFile code.js
```

Oder mit dem offiziellen Figma Plugin Boilerplate:

```bash
npx create-figma-plugin . --name "ILA Screen Builder" --template ui
```

---

## Projektkontext

- **Projekt:** ILA-Pilotprojekt (Agenten-gestütztes UI/UX-Design)
- **Rolle:** Design-Agent-Interface
- **Author:** Cheko (ILA-Koordinations-Agent) `<cheko@ila-agent.local>`
- **Figma-Account:** Sarahs Professional Account (privates Plugin)
