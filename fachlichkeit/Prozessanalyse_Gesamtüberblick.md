# Prozessanalyse: Individuelle Fördermaßnahmen in diSAF
*Erstellt: 2026-04-12 | Analysiert von: Cheko (ILA-Hauptagent)*
*Prämisse: Alle Prozesse ergeben zusammen eine Anwendung — nutzerfreundlich, barrierefrei, auf Basis des aktuellen Designs*

---

## 1. Überblick: Das Gesamtsystem

Die Anwendung diSAF bildet **einen zusammenhängenden Förderprozess** ab, der je nach Schüler-Situation unterschiedliche Pfade nimmt. Alle Prozesse teilen dieselben Kernelemente: Lernausgangslage → Förderziel → Maßnahmen → Evaluation → Entscheidung.

```
Schülerübersicht
    ↓
Förderung anlegen
    ↓
┌─────────────────────────────────────────────┐
│  Welcher Fördertyp?                          │
├─────────────────────────────────────────────┤
│ A) Allgemeine Schule (Regelfall)             │
│ B) bSLRR (Lesen/Rechtschreiben/Rechnen)     │
│ C) Vorbeugende Maßnahme BFZ (VM)            │
│ D) SOPÄDFÖ inklusive Beschulung (IB)        │
│ E) SOPÄDFÖ Förderschule (FS)                │
└─────────────────────────────────────────────┘
    ↓
Förderziel → Maßnahmen → Evaluation
    ↓
Entscheidung: Weiterführen / Abschließen / Eskalieren
```

---

## 2. Prozesse im Einzelnen

### 2.1 Individuelle Fördermaßnahmen Allgemeine Schule (Hauptprozess)

**Was es ist:** Der Standardprozess für alle Schülerinnen und Schüler mit Förderbedarf an allgemeinen Schulen. Ausgangspunkt für alle anderen Prozesse.

**Auslöser (eines von vielen):**
- Schüler von Nichtversetzung bedroht
- Schüler zeigt Leistungsversagen
- Schüler besonders/hochbegabt
- Vorbeugende Maßnahme läuft bereits
- Förderung SOPÄDFÖ nicht mehr nötig

**Beteiligte Rollen:**

| Rolle | Aufgabe |
|---|---|
| Schulleitung (allg. Schule) | Verantwortlich, beschließt |
| Klassenleitung / Tutor/in | Führt aus (Hauptakteur in der App) |
| Fachlehrkraft | Führt aus, wirkt mit |
| Klassenkonferenz | Entscheidet |
| Eltern | Wirken mit, werden informiert |
| Schüler/in | Wirkt mit |

**Schritte:**
1. Schülerübersicht aufrufen (aktive / keine Förderung)
2. Entwicklungsstand und Lernausgangslage bestimmen
3. Förderziel anlegen
4. Förderziel bearbeiten (Ziel beschreiben + Maßnahmen)
5. Förderplan anlegen
6. Bestehende Förderziele dem Plan zuordnen
7. Förderplan-Klassenkonferenz-Termin zuordnen
8. Förderplan beschließen (→ Status: Beschlossen)
9. Förderplan vorstellen (Eltern + Schüler)
10. Schüler fördern und Maßnahmen dokumentieren
11. Klassenkonferenz zur Evaluation vorbereiten
12. Förderziel evaluieren (→ Status: Abgeschlossen)
13. **Entscheidung:** Weiter fördern / Eskalieren / Abschließen

**Statusmodell Förderziel:**
```
Neu – angelegt (grau)
  → Beschlossen (blau)
    → Kenntnis genommen (blau)
      → Maßnahmen aktiv (blau)
        → Zu evaluieren (blau)
          → Abgeschlossen (grün)
```

**Statusmodell Förderplan:**
```
Neu – angelegt (grau) → Beschlossen (blau) → Kenntnis genommen (blau) → Beendet (grün)
```

**Entscheidungspunkte mit Ausgängen:**

| Entscheidung | Mögliche Ausgänge |
|---|---|
| Über weitere Förderung entscheiden | Weiterfördern (Schleife) / bSLRR-Verfahren / Vorbeugende Maßnahme BFZ / SOPÄDFÖ-Verfahren / Abschließen |

---

### 2.2 Verfahren bSLRR (Besondere Schwierigkeiten Lesen / Rechtschreiben / Rechnen)

**Was es ist:** Spezialisiertes Verfahren für Schüler mit LRS oder Dyskalkulie. Kann aus dem Allgemeinen Prozess, SOPÄDFÖ-IB oder SOPÄDFÖ-FS heraus gestartet werden.

**Startereignisse:**
- Aus allgemeinem Förderprozess
- Aus SOPÄDFÖ inklusive Beschulung
- Aus SOPÄDFÖ Förderschule

**Beteiligte Rollen:** Klassenleitung (Hauptakteur), Klassenkonferenz, Eltern, Schüler/in

**Schritte:**
1. Antrag Förderplan bSLRR stellen (durch Eltern oder Schüler — Papierdokument)
2. Individuellen Förderplan bSLRR anlegen
3. Antrag erfassen (in diSAF)
4. Bisherige Förderung bSLRR beschreiben
5. Entwicklungsstand und Lernausgangslage beschreiben
6. Fördermaßnahmen bSLRR benennen
7. → Rückgabe an allgemeinen Förderprozess

**Besonderheit:** Antrag ist nicht immer erforderlich. Drei gesetzliche Phasen (VOGSV):
- Nachteilsausgleich (§7 Abs. 2)
- Abweichung Leistungsfeststellung (§7 Abs. 3)
- Abweichung Leistungsbewertung / Notenschutz (§7 Abs. 4)

---

### 2.3 Vorbeugende Maßnahmen BFZ — Durchführen

**Was es ist:** Sonderpädagogische Beratung und Förderung an allgemeinen Schulen als vorbeugende Maßnahme, bevor ein formeller SOPÄDFÖ-Anspruch festgestellt wird.

**Schritte:**
1. Vorbeugende Maßnahme anlegen
2. Förderart auswählen (Beratung oder Förderangebot)
3. Beratungsanlass beschreiben
4. Anmeldung sonderpädagogische Unterstützung vorbereiten
5. Zustimmung einholen
6. Bisherige Förderung zusammenfassen
7. Sonderpädagogische Unterstützung beauftragen (BFZ)
8. Beauftragung prüfen
9. Vorbeugende Maßnahme in Durchführung nehmen

---

### 2.4 Vorbeugende Maßnahmen BFZ — Abschließen

**Was es ist:** Beendigung der vorbeugenden Maßnahme, wenn Förderung nicht mehr erforderlich oder SOPÄDFÖ-Anspruch festgestellt wurde.

**Schritte:**
1. Individuelle Förderung SOPÄDFÖ abschließen

**Einfachster Prozess im System — ein einziger Schritt.**

---

### 2.5 Entscheidungsverfahren SOPÄDFÖ — FDS beauftragen

**Was es ist:** Formelles Verfahren zur Feststellung eines Anspruchs auf sonderpädagogische Förderung (SOPÄDFÖ) nach § 9 VOSB. Beginnt mit der Einholung einer förderdiagnostischen Stellungnahme (FDS).

**Schritte:**
1. In-Betracht-kommenden Anspruch prüfen
2. Eltern beraten
3. Förderdiagnostische Stellungnahme (FDS) beauftragen
4. Über weitere Förderung entscheiden
5. Auftrag FDS annehmen oder ablehnen
6. Externe Beauftragung FDS prüfen und entscheiden
7. Förderschullehrkraft rBFZ mit FDS-Erstellung beauftragen
8. FDS extern beauftragen (falls intern nicht möglich)
9. Externen Auftrag annehmen oder ablehnen
10. Externe Lehrkraft für FDS beauftragen

**Komplexeste Beauftragungslogik im System** — mehrere Entscheidungspunkte mit Rückschleifen.

---

### 2.6 SOPÄDFÖ nach Feststellung — Inklusive Beschulung (IB)

**Was es ist:** Sonderpädagogische Förderung nach festgestelltem Anspruch an einer allgemeinen Schule.

**Startbedingung (beide müssen erfüllt sein):**
- Eltern einverstanden mit Art, Umfang und Organisation
- Anspruch auf SOPÄDFÖ festgestellt

**Schritte:**
1. Dokumente verwalten
2. Lernausgangslage eruieren und evaluieren
3. Individuelle Förderplanung bereitstellen
4. Förderziel erfassen und bearbeiten
5. Förderziele beschließen
6. Förderplanung vorstellen (Eltern)
7. Schüler fördern und dokumentieren
8. Förderziel evaluieren

**Entscheidungspunkte mit Ausgängen:**

| Entscheidung | Ausgänge |
|---|---|
| Nach Evaluierung Lernausgangslage | Anpassen / bSLRR-Verfahren / Nicht aktiv → Planung bereitstellen / Weiteres SOPÄDFÖ-Verfahren / Ausreichend |

---

### 2.7 SOPÄDFÖ nach Feststellung — Förderschule (FS)

**Was es ist:** Strukturell identisch mit 2.6 (Inklusive Beschulung), aber im Kontext Förderschule.

**Schritte (analog IB):**
1. Dokumente verwalten (FS)
2. Lernausgangslage eruieren und evaluieren (FS)
3. Förderplanung bereitstellen (FS)
4. Förderziel erfassen und bearbeiten (FS)
5. Förderziele beschließen (FS)
6. Förderplanung vorstellen (FS)
7. Förderung dokumentieren (FS)
8. Förderziel evaluieren (FS)

---

## 3. Was die Prozesse gemeinsam haben — Design-Implikationen

### 3.1 Geteilte Kernelemente (überall vorhanden)

| Element | Beschreibung | Design-Anforderung |
|---|---|---|
| **Lernausgangslage** | Startpunkt jeder Förderung | Klares, strukturiertes Eingabeformular |
| **Förderziel** | Zentrale Einheit, trägt den Status | Status immer sichtbar, visuell unterscheidbar |
| **Maßnahmen** | Pro Förderziel, aus Katalog oder frei | Katalog + Freitexteingabe, beides möglich |
| **Evaluation** | Abschluss jedes Zyklus | Einfache, geführte Bewertungseingabe |
| **Entscheidung** | Weiter / Eskalieren / Abschließen | Klare Handlungsoptionen nach Evaluation |
| **Statusverlauf** | Förderziel und Förderplan haben Status | Statusanzeige prominent, durchgängig |
| **Rollenbasierung** | Wer darf was? | Rechtemodell muss UI-Logik steuern |

### 3.2 Geteilte Probleme aus dem Piloten

- **Unterstützer-Feld:** Nur Vater/Mutter — entspricht nicht der Realität (BFZ, Förderschullehrkraft, externe Stellen)
- **Maßnahmen zu abstrakt:** Entsprechen eher Zielen, nicht konkreten Handlungen
- **Keine Nachbearbeitung:** Gespeicherte Inhalte nicht editierbar — widerspricht dem Prozess (Fortschreibung ist vorgesehen)
- **Vorklasse fehlt:** Jahrgang 0 hat meiste Einträge, aber kaum Förderpläne
- **Keine Verlaufshistorie sichtbar:** Statuswechsel nicht nachvollziehbar für Lehrkraft

### 3.3 Prozessübergänge — kritisch für die UX

Mehrere Prozesse **rufen sich gegenseitig auf**. Das bedeutet für die Anwendung:

- Nahtloser Übergang zwischen Prozessen ohne Neueinstieg
- Kontext (Schülerdaten, bestehende Förderungen) muss automatisch übernommen werden
- Nutzer muss immer wissen, in welchem Prozess er sich befindet
- Rückkehr zum vorherigen Prozess muss klar möglich sein

### 3.4 Barrierefreiheit — was die Prozesse verlangen

- Alle Statuswechsel müssen für Screenreader erkennbar sein (nicht nur Farbe)
- Pflichtfelder müssen klar ausgewiesen sein (Unterstützer-Pflichtfeld war UX-Problem)
- Formulare müssen vollständig per Tastatur bedienbar sein (Tastatursteuerung ist in Design Specs dokumentiert)
- Zeitdruck-Situationen vermeiden: Keine Timeouts bei Formulareingaben

---

## 4. Offene Punkte und Widersprüche

| Punkt | Beschreibung |
|---|---|
| **Begrifflichkeit** | "Förderplan" darf laut Prozess nicht verwendet werden — muss "Förderung" heißen. In der Anwendung noch nicht vollständig umgesetzt. |
| **Status "Beschlossen"** | Statusmodell im Prozess kennt "Beschlossen" — App bildet das noch nicht ab |
| **Vorklasse** | Kein eigener Prozess für Vorklasse — größter Nutzungsanteil ohne Prozessgrundlage |
| **Antrag bSLRR** | Papierdokument als Input — kein digitaler Antragsprozess vorhanden |
| **Externe Beauftragung FDS** | Komplexer Entscheidungsbaum, noch nicht in App abgebildet |
| **Evaluation Klassenkonferenz** | Termin-Zuordnung vorgesehen — unklar wie das in der App umgesetzt ist |

---

*Nächste Schritte: Analyse als Grundlage für neue Figma-Screens verwenden*
*Alle beschriebenen Prozesse liegen als EPK-Diagramme und Aufgabenbeschreibungen in `ila/fachlichkeit/`*
