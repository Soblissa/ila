# Figma Design Specs — Analyse

**Stand:** 2026-03-31  
**Autor:** Cheko (ILA-Hauptagent)  
**Quelle:** Figma-Datei `ila _ Design Specs` (Key: `yIb1pCbdjaUqpnrPf0RMF1`)  
**Letztes Update der Datei:** 2026-03-25

---

## 1. Übersicht der Haupt-Flows

| Flow | Beschreibung | Screens |
|---|---|---|
| **Neue Förderung anlegen** | 3-Schritte-Wizard: Schüler suchen → Anlass → Zusammenfassung | ~36 Frames (S/M/L × 4 Zustände) |
| **Förderziele hinzufügen** | 3-Schritte-Stepper: Förderbereich → Lernausgangslage → Zusammenfassung | je Schritt 3–5 Größen |
| **Förderziel bearbeiten** | Maßnahmen hinzufügen/bearbeiten/löschen — 3 Lebenszyklus-Zustände | S/M/L × Zustand |
| **Förderziel evaluieren** | Ergebnis → Verlauf → Begründung → Abschließen | vollständig ausgearbeitet |
| **Notizen verwalten** | Hinzufügen/Bearbeiten/Löschen im Modal | S/M/L |
| **Förderplan bearbeiten** | Formular mit Stärken, Texteingaben | S/M/L |
| **Nutzerfeedback** | Emoji-Rating → Freitext → optionale Kontaktangabe | 7 Modal-Zustände |
| **Startseite / Dashboard** | Überblick, FAQ, Widget-Board | S/M/L + Edgecases |
| **Schüler in Förderung** | Listenansicht, Filterung nach Schule/Klasse | S/M/L |

---

## 2. Seitenstruktur der Figma-Datei

**24 Seiten gesamt:**

### Screen-Seiten (📐 — ausgearbeitete Screens)
- 📐 🟢 Startseite
- 📐 🟢 Schüler in Förderung
- 📐 🟢 FAQ
- 📐 🟢 Förderakte
- 📐 🟢 Förderplan
- 📐 🟢 Förderziel
- 📐 🟢 Nutzerfeedback
- 📐 🟢 Prozess: Neue Förderung
- 📐 🟢 Prozess: Förderziele hinzufügen

### Komponenten-Seiten (🧩 — Design-System-Bausteine)
- 🧩 Actions
- 🧩 Tags
- 🧩 Form Inputs
- 🧩 Menus
- 🧩 Cards
- 🧩 Indicators
- 🧩 Accordion Items
- 🧩 List Items
- 🧩 Modals

---

## 3. Komponenten-Übersicht (Design-System)

### 🧩 Actions
- Button Floating
- Button (Standard)
- Button Icon
- Links

### 🧩 Tags
- Tag, Tag Name, Tag Number, Tag Select, Tag Filter, Tag Avatar

### 🧩 Form Inputs
- Input Text (5 Varianten)
- Input Select
- Input Multiselect
- Input Checkbox + Extended
- Input Radio + Extended
- Input Search
- Toggle

### 🧩 Menus
- Menu Flyout
- Menu Select
- Menu Items (intern)

### 🧩 Cards
- Card Target (4 Varianten)
- Card Target Select (4 Varianten)
- Card Target Compact (2 Varianten)
- Card Skill
- Card Category

### 🧩 Indicators
- Badge (3 Varianten)
- Snackbar
- Notification

### 🧩 Accordion Items
- Board, Standard, Support, Task
- Accordion Header Support

### 🧩 List Items
- List-Item Förderung
- List-Item Schüler

### 🧩 Modals
- Modal Alert
- Modal Dialog
- Modal Page
- Modal Page: Action
- Modal Stepper
- Modal Wizard
- Building Blocks (Basis-Elemente)
- Alle mit responsivem Verhalten (S/M/L)

---

## 4. Zustände und Varianten (wiederkehrende Muster)

**Breakpoints (Bildschirmgrößen) je Screen:**
- `ila-S` — Smartphone
- `ila-M` — Tablet
- `ila-L` — Desktop
- `ila-XL` — Großbildschirm (vereinzelt)
- `iFö-` — Prefix für Förder-spezifische Screens

**Inhaltliche Zustände je Screen:**
- Initial (leer)
- Befüllt / Recurring
- Fehler / Validierung
- Edgecase (Grenzfall, z. B. maximale Ausprägung)

**Förderziel-Lebenszyklus:**
- `[in Planung]` → `[in Durchführung]` → `[abgeschlossen]`

**Barrierefreiheit:**
- Tastatursteuerung für alle kritischen Flows dokumentiert (Accordion, Modals, Kacheln)

---

## 5. Namenskonvention (für Plugin-Entwicklung relevant)

Format: `{Prefix}-{Größe}/{Seite}/{Zustand}`

Beispiele:
- `ila-L/Förderplan/Initial`
- `iFö-M/Förderplan/Stärken/Gespeichert`
- `ila-S/Förderziele hinzufügen/Schritt 1 Förderbereich`

→ Stabile, maschinenlesbare Benennung — Plugin kann Frames zuverlässig per Name ansprechen.

---

## 6. Besonderheiten

- **Building Blocks** auf jeder Screen-Seite: lokale Atom-Komponenten (kleinste Bausteine) direkt neben den Screens
- **Connector Lines** (Verbindungspfeile): zeigen Flow-Logik zwischen Screens — für Plugin nicht relevant
- **Specs-Frames**: Maßvorgaben direkt in der Datei (Cards, List Items) — nützlich für Layout-Konfiguration im Plugin
- **Responsives Verhalten**: auf jeder Seite als eigener Abschnitt dokumentiert mit Breakpoint-Sheet

---

## 7. Bewertung für Plugin-Tauglichkeit

### Sehr gut geeignet (MVP)
| Screen | Begründung |
|---|---|
| `iFö-L/Förderplan/Initial` | Einfachster Screen, klare Input-Felder, wenig Zustandskomplexität |
| `ila-L/Neue Förderung/Schülersuche 1` | Klarer Wizard-Einstieg, standardisierte Struktur |
| `ila-L/Förderungen` | Einfache Listenansicht |

### Gut geeignet, aber komplexer
- Förderziel `[in Planung]` — viele Zustände, aber klar benannt
- Evaluation — vollständig ausgearbeitet, gute Komponentenbasis

### Für MVP vorerst auslassen
- Tastatursteuerungs-Flows — sehr detailliert, nicht für ersten Plugin-Bau nötig
- Responsives Verhalten (Breakpoint-Sheets) — Dokumentations-Frames, kein Inhalt
- Nutzerfeedback-Modal — zu viele Zustände für Erstversion
- Modals allgemein — 5 Typen, komplex

---

## 8. Empfehlung für Plugin-MVP

**Einstiegspunkt:** `iFö-L/Förderplan/Initial`

Begründung:
- Einfachste, sauberste Struktur
- Enthält Form Inputs und Button — die zwei häufigsten Komponenten
- Kein komplexes Zustandsmanagement
- Direkt testbar nach erstem Plugin-Build

**Komponenten für MVP:**
1. `Input Text` (aus 🧩 Form Inputs)
2. `Button` (aus 🧩 Actions)
3. `Navigation Bar Main` (Header — taucht auf jedem Screen auf)

Mit diesen drei Komponenten lässt sich der erste Screen vollständig aufbauen.

---

## 9. Figma API-Zugriff

- **Datei-Key:** `yIb1pCbdjaUqpnrPf0RMF1`
- **Token:** in `/etc/openclaw/users/user1.env` als `FIGMA_TOKEN` hinterlegt
- **Getesteter Zugriff:** erfolgreich (2026-03-31)
