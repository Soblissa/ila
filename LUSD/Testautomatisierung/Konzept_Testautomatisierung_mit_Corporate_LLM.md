# Konzept: Testautomatisierung mit Corporate LLM
## LUSD / ila | Referat IV. 2.1 | HMKB

*Stand: 2026-07-30 | Arbeitsentwurf*

---

## 1. Ausgangslage

### 1.1 Was die Machbarkeitsstudie gezeigt hat

Die Machbarkeitsstudie des Test Center Hessen (TCH) vom Juli 2026 hat untersucht, ob die Webapplikation LUSD technisch automatisiert getestet werden kann. Das Ergebnis: **Grundsätzlich ja — aber mit erheblichem manuellem Übersetzungsaufwand.**

Der Prototyp wurde mit Eclipse, Java, Maven, Selenium und TestNG auf einem einzelnen Funktionslaptop entwickelt. Die einfachen Testfälle liefen nach Optimierung stabil. Dabei wurden drei zentrale Lücken sichtbar:

1. **Fachliche Testfälle → technische Skripte:** Die Übersetzung von fachlich beschriebenen Testfällen (in AzureDevOps) in ausführbare Automatisierungsskripte bleibt ein manueller Schritt — und ist fehleranfällig.
2. **Testdatenmanagement:** Ohne Strategie zur Datenverwaltung ist keine wiederholbare Testausführung möglich.
3. **Infrastruktur:** Der aktuelle Betrieb auf einem einzelnen Laptop ist nicht skalierbar und nicht teamfähig.

Hinzu kommt: Komplexe Testfälle (SAP-Datenabgleich, Datei-Downloads, Drag-&-Drop-Interaktionen) sind mit reinem Selenium nicht sinnvoll automatisierbar.

Die Machbarkeitsstudie hat empfohlen, vor einer weiteren Umsetzung grundlegende Fragen zu Infrastruktur, Verantwortlichkeiten und Testziel zu klären.

### 1.2 Was das Corporate-LLM-Konzept bereits beschreibt

Das im Referat IV. 2.1 erarbeitete Corporate-LLM-Konzept (ADO als Single Source of Truth, Stand: 2026-05-25) beschreibt eine Prozesslogik, die direkt an die Schwachstellen der Machbarkeitsstudie anschließt:

> **User Story → Akzeptanzkriterien in ADO → Testfälle → perspektivisch Testautomatisierung**

Das Corporate LLM soll dabei nicht frei agieren, sondern strukturiert aus den Akzeptanzkriterien ableiten. Die Testautomatisierung wird im bestehenden Konzept explizit als Stufe 3 (Perspektive) beschrieben — also als das, was nach Analyse und Testfall-Ableitung folgt.

Dieses Konzept schließt genau dort an.

---

## 2. Zielbild

Das Ziel ist eine **dreistufige Prozesskette**, in der das Corporate LLM die Brücke zwischen fachlicher Beschreibung und ausführbarem Test schlägt:

```
Fachliche Anforderung (Mensch)
    ↓
[C-LLM: User-Story-Assistent]
    → strukturierte User Story in ADO
    ↓
[C-LLM: Akzeptanzkriterien-Assistent]
    → Normalfall, Sonderfall, Fehlerfall
    ↓
[C-LLM: Testfall-Assistent]
    → prüfbare Testfälle mit Testschritten und erwartetem Ergebnis
    ↓
[C-LLM: Automatisierungsassistent]  ← NEU (Gegenstand dieses Konzepts)
    → Einschätzung der Automatisierbarkeit
    → Testskript-Vorlagen (Selenium/TestNG)
    → Markierung was manuell bleiben muss
    ↓
Testausführung (Mensch + automatisiertes Skript)
```

**Kein Schritt ersetzt die menschliche Freigabe.** Das Corporate LLM erzeugt Vorschläge — Testanalysten prüfen, korrigieren und freigeben.

---

## 3. Anwendungsfälle im Detail

### 3.1 Einschätzung der Automatisierbarkeit

**Problem:** Nicht jeder Testfall eignet sich für Selenium. Das musste in der Machbarkeitsstudie mühsam manuell bewertet werden.

**Lösung:** Der C-LLM-Automatisierungsassistent bewertet jeden Testfall auf Basis seiner Akzeptanzkriterien und Testschritte automatisch:

| Kriterium | Automatisierbar? |
|---|---|
| Reine Klickstrecken, Navigationsaufrufe | ✅ gut geeignet |
| Formularfelder füllen, Datensätze anlegen/bearbeiten/löschen | ✅ gut geeignet |
| Tabellenprüfungen (Spalten, Filter, Sortierung) | ⚠️ komplex, hoher Aufwand |
| Tooltips / Kurzinfos | ⚠️ nur indirekt (Attribute, nicht visuell) |
| Datei-Downloads + Inhaltsvergleich | ❌ nicht mit Selenium |
| Drag-&-Drop-Interaktionen | ❌ technisch nicht sinnvoll |
| SAP-Datenabgleich / externe Systeme | ❌ anderes Tooling erforderlich |

**Ausgabe:** Pro Testfall eine klare Ampelbewertung + Begründung. Damit kann das Team priorisieren, was automatisiert wird und was manuell bleibt.

---

### 3.2 Testskript-Vorlagen generieren

**Problem:** Die Übersetzung von fachlichen Testschritten in Selenium-Java-Code ist heute eine manuelle Kompetenzaufgabe.

**Lösung:** Für als automatisierbar bewertete Testfälle generiert das C-LLM eine Testskript-Vorlage im TCH-Framework-Format (Eclipse/Java/Maven/Selenium/TestNG). Die Vorlage enthält:

- Grundstruktur der Testklasse (Java/TestNG)
- Seitenelement-Referenzen auf Basis der bekannten LUSD-HTML-Struktur (eindeutige IDs, iFrame-Handling)
- Platzhalter für Login, Navigation, Dateneingabe
- Wait-Mechanismen (explizite Waits für Ladezeiten)
- Testdaten-Parametrisierung (damit Testläufe wiederholbar sind)

**Wichtig:** Die Vorlage ist kein fertiges Skript. Sie ist ein strukturierter Ausgangspunkt, den ein Testautomatisierer anpasst und freigibt.

---

### 3.3 Hybrid-Tests (Kombination manuell + automatisiert)

**Problem:** Einige Testfälle sind zu 80% automatisierbar, brechen aber an einer Stelle ab (z.B. Datei-Download).

**Lösung:** Das C-LLM identifiziert den Übergabepunkt und erzeugt einen geteilten Testplan:
- Automatisierter Teil: Skript läuft bis zum kritischen Schritt
- Manueller Teil: Anweisung was der Mensch dann prüft
- Automatisierter Abschluss: Skript übernimmt wieder danach

Das entspricht dem Vorgehen, das die Machbarkeitsstudie als "Kombination/Aufsplitterung" beschreibt — jetzt systematisch unterstützt statt manuell entschieden.

---

### 3.4 Testdatenmanagement

**Problem:** Testfall 4 der Machbarkeitsstudie hat gezeigt: Wenn Branchen angelegt und nicht vollständig gelöscht werden, scheitert der nächste Testlauf. Kein gelöstes Problem.

**Lösung:** Das C-LLM analysiert jeden Testfall auf Nebeneffekte (Side Effects):
- Welche Daten werden angelegt?
- Welche werden nicht automatisch zurückgesetzt?
- Was muss vor/nach dem Testlauf bereinigt werden?

Ausgabe: Pro Testfall eine Checkliste für Setup (Vorbedingungen) und Teardown (Nachbedingungen). Grundlage für eine spätere Testumgebungs-Reset-Strategie.

---

## 4. Abgrenzung: Was das C-LLM nicht leistet

Es ist wichtig zu benennen, was dieses Konzept bewusst *nicht* vorsieht:

| Nicht vorgesehen | Warum |
|---|---|
| Vollautomatische Testgenerierung ohne menschliche Prüfung | Qualitätsrisiko — fachliche Akzeptanzkriterien müssen stimmen |
| Ersatz für die Testumgebungs-Infrastruktur | Azure Pipelines / virtuelle Maschinen müssen separat beschafft werden |
| Automatische Ausführung ohne freigegebenen Test-User | Laut Machbarkeitsstudie: dedizierter Benutzer notwendig |
| Selenium-Code für Drag-&-Drop, Datei-Downloads, externe Tools | Technisch außerhalb des Browser-DOMs — nicht lösbar |
| Vollständige SAP-Integration | Erfordert anderes Tooling (z.B. API-Tests, andere Frameworks) |

---

## 5. Voraussetzungen

### 5.1 Was bereits vorhanden ist (laut Machbarkeitsstudie)

- ✅ TCH-Testautomationsframework (Eclipse, Java, Maven, Selenium, TestNG)
- ✅ Testfälle in AzureDevOps beschrieben und strukturiert
- ✅ Nachweis: LUSD ist grundsätzlich automatisierbar
- ✅ Erfahrung mit iFrame-Handling, Wait-Mechanismen, einfachen Workflows

### 5.2 Was noch fehlt (Klärungsbedarf laut Machbarkeitsstudie)

Bevor das C-LLM produktiv eingesetzt werden kann, müssen diese offenen Punkte beantwortet sein:

| # | Frage | Verantwortlich |
|---|---|---|
| 1 | Auf welcher Testumgebung laufen die automatisierten Tests? (HZD / Marburg) | HMKB / HZD |
| 2 | Stehen virtuelle Maschinen mit RDP oder Azure Pipelines zur Verfügung? | HZD |
| 3 | Wer ist der dedizierte Test-User für Automatisierung? | Projektleitung |
| 4 | Wer führt Tests aus und überwacht sie dauerhaft? | Testmanagement |
| 5 | Wie werden Testergebnisse zurückgemeldet (ADO-Integration)? | Projektleitung / HZD |
| 6 | Welche Testfälle sollen in Stufe 1 automatisiert werden? | Testmanagement + Fachlichkeit |
| 7 | Wie wird die Testumgebung nach Testläufen zurückgesetzt? | HZD |
| 8 | Wo liegt der Source Code? (aktuell: Funktionslaptop Helene Lesko) | TCH |

### 5.3 Was das Corporate LLM benötigt

- **ADO-Anbindung:** Zugriff auf User Stories und Akzeptanzkriterien (lesend)
- **LUSD-Wissensbasis:** Indexierte LUSD-Dokumentation, Anleitungen, Release-Informationen
- **Testfall-Muster:** Bestehende Testfälle als Lerngrundlage für den Assistenten
- **TCH-Framework-Dokumentation:** Damit generierte Skript-Vorlagen zum verwendeten Stack passen

---

## 6. Stufenplan

### Stufe 1 — Grundlagen (Voraussetzung: Infrastruktur-Fragen beantwortet)

- [ ] C-LLM-Automatisierungsassistent mit LUSD-Testfall-Muster trainieren
- [ ] Automatisierbarkeits-Bewertung für bestehende Testfälle durchführen
- [ ] Prioritätenliste: Welche ~20 Testfälle werden als erstes automatisiert?
- [ ] Testdaten-Checklisten für diese 20 Testfälle erstellen

### Stufe 2 — Pilotbetrieb

- [ ] Skript-Vorlagen für die 20 priorisierten Testfälle generieren
- [ ] Testanalysten prüfen, korrigieren, finalisieren
- [ ] Testläufe auf zentrale Infrastruktur (VM / Azure Pipelines) übertragen
- [ ] Ergebnis-Rückmeldung in ADO etablieren

### Stufe 3 — Ausbau

- [ ] Hybrid-Test-Konzept für komplexe Fälle umsetzen
- [ ] Testdaten-Reset-Strategie mit HZD klären und umsetzen
- [ ] Weitere Testfälle systematisch nachziehen
- [ ] Bewertung: Welches Tooling braucht es für SAP-Datenabgleich / Datei-Tests?

---

## 7. Nutzen im Überblick

| Heute (manuell) | Mit C-LLM-Unterstützung |
|---|---|
| Testfälle manuell aus Anforderungen ableiten — fehleranfällig | C-LLM generiert Testfallvorschläge aus Akzeptanzkriterien |
| Automatisierbarkeit manuell pro Testfall bewerten | Systematische Ampelbewertung durch C-LLM |
| Testskripte von Grund auf manuell schreiben | C-LLM generiert strukturierte Skript-Vorlagen |
| Side Effects manuell identifizieren | C-LLM analysiert Setup/Teardown-Bedarf |
| Testdaten-Probleme erst beim Ausführen bemerkt | Vorab-Checkliste verhindert Fehlerläufe |
| Wissen konzentriert auf wenige Personen | Prozess dokumentiert und übertragbar |

---

## 8. Zusammenhang mit dem Gesamtkonzept

Dieses Konzept ist kein isolierter Ansatz, sondern **Stufe 3 des Corporate-LLM-Konzepts für das Referat IV. 2.1**:

```
Stufe 1: Analyse des ADO-Bestands (Akzeptanzkriterien verstehen)
Stufe 2: Testfall-Ableitung aus Akzeptanzkriterien
Stufe 3: Unterstützung der Testautomatisierung  ←  Dieses Dokument
```

Die Grundlage für alle drei Stufen ist dieselbe: **ADO als Single Source of Truth.** Wer gute Akzeptanzkriterien schreibt, bekommt bessere Testfälle — und aus besseren Testfällen entstehen bessere Automatisierungsskripte. Die Qualität propagiert durch die gesamte Kette.

---

*Nächste Schritte: Klärung der offenen Infrastruktur-Fragen (Abschnitt 5.2), dann Pilotstart mit Stufe 1.*
