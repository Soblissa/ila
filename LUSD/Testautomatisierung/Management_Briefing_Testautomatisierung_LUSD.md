# Testautomatisierung LUSD — Management Briefing
## Wo stehen wir, was ist möglich, wie können wir KI einsetzen?

*Stand: 2026-07-30 | Zielgruppe: Projektleitung, Entscheidungsträger*

---

## Das Wichtigste vorab

Die gute Nachricht: **LUSD kann automatisiert getestet werden.** Das ist keine Annahme — das wurde in einer Machbarkeitsstudie des Test Center Hessen (TCH) praktisch bewiesen.

Die nüchterne Einschätzung: **Automatisierung alleine löst das Problem nicht.** Der eigentliche Engpass ist der manuelle Aufwand zwischen fachlicher Anforderung und ausführbarem Test. Genau hier kann ein KI-gestützter Agent (auf Basis des Corporate LLM) gezielt helfen.

Dieses Dokument erklärt — ohne Technikjargon — den aktuellen Stand, was möglich ist, und was wir als nächstes tun sollten.

---

## 1. Was ist Softwaretesting überhaupt?

Jedes Mal wenn LUSD eine neue Version bekommt, muss geprüft werden: Funktioniert noch alles? Hat die neue Funktion etwas Altes kaputt gemacht?

Heute passiert das manuell: Eine Testanalystin öffnet den Browser, klickt eine Liste von Testschritten durch und notiert ob das Ergebnis stimmt. Bei der LUSD gibt es sehr viele Testfälle — das kostet viel Zeit und ist fehleranfällig.

**Testautomatisierung** bedeutet: Ein Computerprogramm übernimmt dieses Durchklicken. Es öffnet den Browser, klickt, tippt, prüft — und meldet sofort wenn etwas nicht stimmt. Ohne Mensch, in Sekunden.

Das Werkzeug das dabei eingesetzt wird heißt **Selenium** — eine weitverbreitete, kostenlose Software die Webbrowser fernsteuern kann. Stellen Sie sich vor, jemand sitzt unsichtbar am Computer und klickt genau das durch was der Test vorschreibt — das ist Selenium.

---

## 2. Was die Machbarkeitsstudie herausgefunden hat

Das Test Center Hessen (TCH) hat im Juni/Juli 2026 einen Prototyp entwickelt und fünf Testfälle untersucht. Das Ergebnis:

### Was funktioniert gut ✅

- LUSD ist technisch gut für Automatisierung geeignet — die Programmstruktur der Weboberfläche ist klar aufgebaut
- Einfache Abläufe (Seiten aufrufen, Formulare ausfüllen, Datensätze anlegen/bearbeiten/löschen) lassen sich stabil automatisieren
- Ein Testfall lief zehn Mal hintereinander ohne einen einzigen Fehler durch

### Was schwierig ist ⚠️

- LUSD lädt manchmal langsam — das Automatisierungsskript muss "warten lernen", sonst bricht es ab, obwohl die Anwendung korrekt funktioniert. Das ist lösbar, braucht aber Sorgfalt.
- Manche Prüfungen (z.B. kleine Hilfetexte die per Mausberührung erscheinen) können nicht direkt getestet werden — technische Eigenheit des Browsers

### Was nicht automatisierbar ist ❌

- Testfälle die externe Programme brauchen (z.B. SAP-Datenabgleich, Excel-Vergleiche, Datei-Downloads) — das Werkzeug Selenium kann nur *innerhalb* des Browsers arbeiten, nicht darüber hinaus
- Sehr lange Testfälle mit über 100 Schritten und vagen Anweisungen wie "Verändern Sie beliebig die Ansicht" — das kann kein Automatisierungsskript interpretieren

### Der aktuelle Engpass

Die Studie zeigt: Der größte Aufwand entsteht **nicht** beim eigentlichen Ausführen der Tests — sondern beim Übersetzen fachlicher Testbeschreibungen in ausführbare Programme. Das macht heute ein Mensch manuell, Schritt für Schritt. Das ist zeitintensiv, fehleranfällig und hängt am Wissen einzelner Personen.

Dazu kommt: Der gesamte Prototyp liegt auf dem Laptop einer einzelnen Mitarbeiterin. Kein Teamzugriff, keine zentrale Ablage. Das ist kein nachhaltiger Zustand.

---

## 3. Wo das Corporate LLM ansetzt

Das Referat IV. 2.1 arbeitet bereits an einem Corporate LLM-Konzept — einem KI-gestützten Arbeitsassistenten der auf dem eigenen Behördenwissen aufsetzt und den Entwicklungsprozess in Azure DevOps (ADO) unterstützt.

Dieses Konzept beschreibt eine Prozesskette:

```
Fachliche Anforderung
    → strukturierte User Story in ADO
    → Akzeptanzkriterien
    → Testfälle
    → Testautomatisierung
```

**Testautomatisierung ist der letzte Schritt dieser Kette.** Und genau hier kann ein KI-Agent den größten manuellen Engpass übernehmen.

---

## 4. Was ein KI-Agent konkret tun kann

### 4.1 Einschätzen: Was lässt sich automatisieren?

Heute bewertet ein Mensch manuell ob ein Testfall für Automatisierung geeignet ist. Das kostet Zeit und erfordert technisches Spezialwissen.

Ein KI-Agent liest den Testfall in ADO und gibt sofort eine Einschätzung:

- 🟢 **Gut geeignet** — einfache Klickabläufe, Formulare, Standardworkflows
- 🟡 **Bedingt geeignet** — komplex, hoher Aufwand, nur teilweise sinnvoll
- 🔴 **Nicht geeignet** — externe Systeme, Downloads, vage Testbeschreibungen

Das Ergebnis: Das Team weiß sofort worauf es sich konzentrieren soll. Keine Zeit mehr für Testfälle die sowieso nicht automatisierbar sind.

---

### 4.2 Vorbereiten: Testskript-Vorlagen erstellen

Für alle grün bewerteten Testfälle erstellt der Agent eine **Vorlage** für das Automatisierungsskript. Diese Vorlage enthält:

- Die richtige Grundstruktur für das eingesetzte Werkzeug (TCH-Framework)
- Die wichtigsten Aktionsschritte bereits vorstrukturiert
- Platzhalter für Login, Navigation, Dateneingabe
- Eingebaute Wartemechanismen für LUSD-Ladezeiten

Ein Testautomatisierer nimmt diese Vorlage, prüft sie, passt sie an und gibt sie frei. **Der Mensch bleibt zuständig — aber startet von einem fertigen Entwurf statt von einem leeren Blatt.**

---

### 4.3 Absichern: Testdaten-Checklisten

Ein bekanntes Problem: Wenn ein Test Daten anlegt und nicht vollständig aufräumt, schlägt der nächste Testlauf fehl. Das wurde in der Machbarkeitsstudie konkret beobachtet.

Der Agent analysiert jeden Testfall und erstellt eine Checkliste:
- Was muss vor dem Test vorbereitet sein?
- Was muss nach dem Test aufgeräumt werden?

So werden Testläufe wiederholbar — unabhängig davon wer sie ausführt.

---

### 4.4 Kombinieren: Wo Mensch und Maschine sich ergänzen

Manche Testfälle sind zu 80% automatisierbar — brechen aber an einer Stelle ab (z.B. wenn eine Datei heruntergeladen und manuell geprüft werden muss).

Der Agent erkennt diesen Punkt und erstellt einen geteilten Testplan:
- Automatisierter Teil bis Schritt X
- Klare Anweisung was der Mensch dann prüft
- Automatisierter Abschluss danach

Das Ergebnis: Auch komplexe Tests werden effizienter — ohne dass man sie komplett manuell durchführen muss.

---

## 5. Was noch nicht gelöst ist

Der KI-Agent kann die fachliche Arbeit unterstützen. Aber einige organisatorische und technische Fragen müssen vorher beantwortet sein:

| Offene Frage | Warum wichtig |
|---|---|
| Auf welcher Testumgebung laufen die Tests? | Heute: ein einzelner Laptop — das skaliert nicht |
| Gibt es eine zentrale Infrastruktur (Server, Cloud)? | Voraussetzung für Teambetrieb und regelmäßige Testläufe |
| Wer ist dauerhaft für die Tests verantwortlich? | Ohne feste Zuständigkeit kein nachhaltiger Betrieb |
| Wie werden Testergebnisse zurückgemeldet? | Ohne Rückmeldung kein Nutzen |
| Wie wird die Testumgebung nach Testläufen zurückgesetzt? | Voraussetzung für wiederholbare Tests |
| Wo liegt der Source Code? | Aktuell nur auf dem Laptop einer Mitarbeiterin — Risiko |

Diese Fragen sind nicht Aufgabe des KI-Agenten — sie müssen organisatorisch und mit der HZD (Hessische Zentrale für Datenverarbeitung) geklärt werden.

---

## 6. Empfehlung

### Kurzfassung

> **Den KI-Agenten jetzt vorbereiten — aber erst einsetzen wenn die Infrastruktur steht.**

Beides gleichzeitig anzugehen macht Sinn: Während die Infrastruktur-Fragen mit der HZD geklärt werden, kann der Agent bereits auf LUSD-Testfälle vorbereitet und erprobt werden.

---

### Die drei Schritte

**Schritt 1 — Sofort: Infrastruktur klären (ohne KI)**

Die offenen Fragen aus Abschnitt 5 sind die Grundvoraussetzung. Ohne zentrale Testumgebung, festen Test-User und klare Verantwortlichkeiten ist jede weitere Arbeit auf Sand gebaut.
→ *Zuständig: Projektleitung, HZD*

**Schritt 2 — Parallel: Agenten vorbereiten**

Den C-LLM-Automatisierungsassistenten mit LUSD-Testfällen aus ADO vertraut machen. Erste Automatisierbarkeits-Bewertungen durchführen. Prioritätenliste: Welche 20 Testfälle werden zuerst automatisiert?
→ *Zuständig: Testmanagement + C-LLM-Team*

**Schritt 3 — Sobald Infrastruktur steht: Pilotbetrieb**

Der Agent generiert Skript-Vorlagen für die priorisierten Testfälle. Testanalysten prüfen und geben frei. Erste automatisierte Testläufe auf zentraler Infrastruktur.
→ *Zuständig: TCH + Testmanagement*

---

### Was wir gewinnen

| Heute | Mit KI-Agent |
|---|---|
| Testfall-Übersetzung: Stunden pro Testfall | Skript-Vorlage: Minuten, dann Mensch prüft |
| Automatisierbarkeit: manuell bewertet | Sofort-Einschätzung durch Agenten |
| Testdaten-Probleme: beim Ausführen entdeckt | Vorab-Checkliste verhindert Fehlerläufe |
| Wissen bei einzelnen Personen | Prozess dokumentiert, übertragbar |
| Code auf einem Laptop | Zentral, teamfähig, versioniert |

Der langfristige Gewinn: **Schnellere Releases mit höherer Qualität.** Jede neue LUSD-Version kann zuverlässiger getestet werden — ohne dass der manuelle Testaufwand proportional mitwächst.

---

## 7. Einordnung: Was KI kann und was nicht

Zum Abschluss eine ehrliche Einordnung — weil Erwartungen hier oft zu hoch oder zu niedrig angesetzt werden:

**KI kann:**
- Strukturierte Aufgaben mit klaren Regeln schneller und konsistenter erledigen als Menschen
- Aus vorhandenen Testfällen systematisch Vorlagen ableiten
- Muster erkennen und auf Vollständigkeit prüfen
- Den menschlichen Experten entlasten — nicht ersetzen

**KI kann nicht:**
- Fachliches Urteilsvermögen ersetzen ("Ist dieser Test fachlich korrekt?")
- Entscheiden was getestet werden soll
- Außerhalb des Browsers arbeiten (SAP, Excel, externe Systeme)
- Ohne saubere Akzeptanzkriterien in ADO gute Ergebnisse liefern

Der entscheidende Satz aus dem Corporate-LLM-Konzept gilt hier genauso:

> *Der Mensch bringt Fachurteil und Freigabe — der Agent übernimmt Strukturierung, Vollständigkeit und Konsistenz.*

---

*Dokument erstellt auf Basis der Machbarkeitsstudie Testautomatisierung LUSD (TCH, Juli 2026) und des Corporate-LLM-Konzepts für das Referat IV. 2.1 (Stand: Mai 2026).*
