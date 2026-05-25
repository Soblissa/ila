# Corporate LLM für ADO-basierte Entwicklungsprozesse
## Arbeitsentwurf mit Schwerpunkt ADO als Single Source of Truth

*Stand: 2026-05-25 | Arbeitsfassung zur iterativen Überarbeitung*

---

## 1. Ausgangslage

Sowohl die **LUSD** (Lehrer- und Schülerdatenbank Hessen) als auch **ila** werden in **Azure DevOps (ADO)** entwickelt. Die fachliche Grundlage bilden dabei die in ADO gepflegten Anforderungen.

Im praktischen Entwicklungsprozess entstehen aus diesen Anforderungen mehrere weitere Artefakte, insbesondere:
- **User Stories**
- **Akzeptanzkriterien**
- **Testfälle**
- perspektivisch auch Ansätze zur **Testautomatisierung**
- sowie mittelbar Dokumentation und Anwenderunterstützung

Der heutige Zustand ist in vielen Organisationen davon geprägt, dass diese Artefakte zwar eng zusammenhängen, aber oft mit hohem manuellem Aufwand erstellt, überarbeitet und aufeinander abgestimmt werden. Genau hier liegt ein relevanter Hebel für ein Corporate LLM (unternehmenseigenes großes Sprachmodell).

---

## 2. Strategischer Kern

Der zentrale Gedanke dieses Vorhabens lautet:

> **Azure DevOps wird zur führenden fachlichen Quelle im Entwicklungsprozess.**

Das bedeutet nicht, dass ADO die einzige Wissensquelle der Organisation ist. Relevante weitere Quellen wie Erlasse, Prozessbeschreibungen, bestehende Dokumentation oder Fachkonzepte bleiben notwendig.

Für den operativen Entwicklungsprozess soll jedoch gelten:

> **Was in ADO fachlich beschrieben und freigegeben ist, dient als maßgeblicher Ausgangspunkt für die Ableitung weiterer Entwicklungs- und Qualitätssicherungsartefakte.**

ADO wird damit zur **Single Source of Truth** im engeren Sinne des Entwicklungsprozesses.

---

## 3. Was mit „Single Source of Truth“ konkret gemeint ist

Im vorliegenden Kontext bedeutet **Single Source of Truth**:

- Anforderungen werden zentral in **ADO** gepflegt.
- Fachliche Änderungen werden dort strukturiert beschrieben.
- Aus diesen Inhalten werden weitere Artefakte systematisch abgeleitet.
- Änderungen an Anforderungen können gezielt auf ihre Auswirkungen in Test und Qualitätssicherung geprüft werden.

Die zentrale Annahme lautet:

**Je strukturierter und vollständiger Anforderungen in ADO vorliegen, desto besser lassen sich nachgelagerte Arbeitsschritte unterstützen, standardisieren und teilweise automatisieren.**

Damit verschiebt sich der Fokus weg von allgemeiner KI-Nutzung hin zu einem klaren Prozessnutzen:
- bessere Anforderungsqualität
- konsistentere Testbasis
- weniger manuelle Doppelarbeit
- bessere Nachvollziehbarkeit bei Änderungen

---

## 4. Hauptanwendungsfälle

Für das Vorhaben sind zunächst drei Hauptanwendungsfälle besonders relevant.

### 4.1 Unterstützung bei der Erstellung von Anforderungen für die Entwicklung

#### Ausgangsproblem
Die Erstellung fachlich tragfähiger Anforderungen ist aufwändig. Besonders kritisch sind dabei:
- unklare Formulierungen
- uneinheitliche Struktur
- fehlende Abgrenzungen
- unvollständige Akzeptanzkriterien
- zu wenig berücksichtigte Sonder- und Fehlerfälle

Diese Schwächen wirken sich direkt auf Entwicklung, Test und Abnahme aus.

#### Ziel
Ein Corporate LLM soll Mitarbeitende bei der Erstellung qualitativ hochwertiger Anforderungen in ADO unterstützen.

#### Konkret bedeutet das
Aus einer fachlichen Beschreibung oder einem ersten Entwurf kann das System Vorschläge erzeugen für:
- eine **sauber formulierte User Story**
- passende **Akzeptanzkriterien**
- eine erste Struktur der Anforderung
- fehlende fachliche Präzisierungen
- mögliche Sonderfälle und Fehlerfälle

#### Beispielhafte Unterstützung
Aus einer freien Beschreibung wie
> „Im BSLRR-Prozess sollen eingegebene Daten jederzeit gespeichert werden können“

würde das System einen strukturierten Vorschlag erzeugen für:
- User Story
- Akzeptanzkriterien
- fachliche Randbedingungen
- offene Rückfragen

#### Nutzen
- höhere Einheitlichkeit von Anforderungen
- weniger Nachschärfung zwischen Fachlichkeit und Entwicklung
- bessere Prüfbarkeit
- bessere Grundlage für nachgelagerte Testableitung

---

### 4.2 Ableitung von Testfällen aus Anforderungen und Akzeptanzkriterien

#### Ausgangsproblem
Testfälle werden häufig manuell aus Anforderungen abgeleitet. Das ist fehleranfällig und stark von Erfahrung, Zeit und persönlicher Gründlichkeit abhängig.

Typische Probleme sind:
- offensichtliche Fälle werden getestet, Randfälle fehlen
- Akzeptanzkriterien werden nicht vollständig in Testlogik übersetzt
- die Qualität der Testfälle schwankt
- bei Änderungen müssen Testfälle manuell gesucht und angepasst werden

#### Ziel
Ein Corporate LLM soll aus den in ADO hinterlegten Anforderungen und Akzeptanzkriterien systematisch Testfälle vorschlagen.

#### Konkret bedeutet das
Das System kann zu einer Anforderung Testfälle ableiten für:
- **Normalfälle**
- **Sonderfälle**
- **Fehlerfälle**
- **Grenzfälle**
- gegebenenfalls Vorbedingungen und erwartete Ergebnisse

#### Nutzen
- höhere Testabdeckung
- konsistentere Testfallstruktur
- bessere Rückverfolgbarkeit zwischen Anforderung und Test
- Zeitersparnis bei der Erstformulierung von Testfällen

#### Besonderer Mehrwert
Wenn Anforderungen und Akzeptanzkriterien bereits in ADO sauber strukturiert vorliegen, entsteht eine direkte Linie:

**Anforderung in ADO → Akzeptanzkriterien → vorgeschlagene Testfälle**

Genau diese Kette ist für einen ADO-zentrierten KI-Einsatz besonders attraktiv.

---

### 4.3 Perspektivisch: Unterstützung der Testautomatisierung

#### Ausgangsproblem
Zwischen fachlicher Anforderung und automatisiertem Test liegt heute oft ein deutlicher Übersetzungsaufwand. Fachliche Aussagen müssen in technische Testlogik übertragen werden.

#### Ziel
Ein Corporate LLM soll perspektivisch helfen, die Brücke zwischen fachlich formulierten Anforderungen und einer möglichen Testautomatisierung zu verkürzen.

#### Konkret denkbare Unterstützung
Aus Anforderungen und Testfällen könnten vorbereitet oder vorgeschlagen werden:
- testbare Szenarien
- strukturierte Testfalllogiken
- Vorlagen für automatisierbare Testskripte
- Hinweise, welche Testfälle grundsätzlich für Automatisierung geeignet sind
- Markierung, wo menschliche Prüfung weiterhin erforderlich bleibt

#### Wichtige Einordnung
Das Ziel ist zunächst **nicht**, automatisierte Tests vollständig durch ein LLM erzeugen und ungeprüft ausführen zu lassen.

Realistisch und sinnvoll ist zunächst:
- **Unterstützung bei der Vorbereitung von Testautomatisierung**
- **Standardisierung von Testlogik**
- **Reduzierung manueller Übersetzungsarbeit**

#### Nutzen
- bessere Vorbereitung für automatisiertes Testen
- geringere manuelle Aufwände bei Standardfällen
- klarere Unterscheidung zwischen fachlich beschreibbaren und technisch komplexen Tests

---

## 5. Zielbild des Prozesses

Das Zielbild ist ein Entwicklungsprozess, in dem ADO nicht nur Ablageort von Anforderungen ist, sondern der **aktive Ausgangspunkt für Folgeprozesse**.

Ein mögliches Zielbild lautet:

```text
Fachliche Idee / Änderungsbedarf
        ↓
Corporate LLM unterstützt Formulierung in ADO
        ↓
Strukturierte User Story + Akzeptanzkriterien in ADO
        ↓
Corporate LLM leitet Testfälle ab
        ↓
Fachliche und technische Prüfung
        ↓
Entwicklung
        ↓
Perspektivisch Unterstützung bei Testautomatisierung
```

Der wesentliche Mehrwert liegt darin, dass die Artefakte nicht mehr isoliert entstehen, sondern in einer nachvollziehbaren Kette aufeinander aufbauen.

---

## 6. Voraussetzungen für den Ansatz

Damit dieser Ansatz tragfähig ist, müssen mehrere Bedingungen erfüllt sein.

### 6.1 Mindeststruktur in ADO
Die Anforderungen in ADO müssen so formuliert sein, dass sie systematisch ausgewertet werden können. Dazu gehören mindestens:
- fachliches Ziel
- betroffene Rolle oder Nutzergruppe
- gewünschtes Verhalten der Anwendung
- Akzeptanzkriterien
- erkennbare Sonder- oder Fehlerfälle

### 6.2 Einheitlicheres Vorgehen bei User Stories und Akzeptanzkriterien
Wenn Teams Anforderungen sehr unterschiedlich formulieren, sinkt die Qualität der automatischen Unterstützung. Deshalb wäre mittelfristig ein Mindeststandard sinnvoll.

### 6.3 Menschliche Prüfung bleibt zwingend
Das LLM darf Vorschläge machen, aber keine fachliche Freigabe ersetzen. Verantwortung bleibt bei den fachlich zuständigen Personen.

### 6.4 Rückverfolgbarkeit
Es muss nachvollziehbar bleiben:
- aus welcher ADO-Anforderung ein Testfall abgeleitet wurde,
- welche Version zugrunde lag,
- und ob der Vorschlag durch Menschen angepasst wurde.

### 6.5 Klare Begrenzung des Systems
Das LLM darf keine neue Fachlichkeit erfinden. Es soll strukturieren, ableiten, auf Lücken hinweisen und Vorschläge formulieren, aber nicht eigenständig fachpolitische Entscheidungen treffen.

---

## 7. Warum dieser Fokus sinnvoll ist

Der Schwerpunkt auf **ADO als Single Source of Truth** und auf die drei Hauptanwendungsfälle ist für einen Einstieg besonders geeignet, weil hier ein klarer, messbarer Nutzen entsteht.

### 7.1 Direkte Hebelwirkung
Eine bessere Anforderung wirkt sich unmittelbar auf Entwicklung, Test und Qualität aus.

### 7.2 Gute fachliche Anschlussfähigkeit
User Stories, Akzeptanzkriterien und Testfälle gehören bereits heute zusammen. Das Vorhaben baut also auf einem bestehenden Arbeitszusammenhang auf und erfindet keinen künstlichen KI-Fall.

### 7.3 Begrenzter und nachvollziehbarer Startpunkt
Statt ein Corporate LLM zunächst als allgemeines Wissenssystem für alles zu denken, beginnt man mit einem klar umrissenen Prozessschritt mit hohem Nutzen.

### 7.4 Anschlussfähigkeit für spätere Ausbaustufen
Wenn der Ansatz funktioniert, kann er später erweitert werden, zum Beispiel auf:
- Dokumentation
- Anwenderhilfen
- Change-Impact-Analysen
- integrierte Unterstützung direkt in ila

---

## 8. Vorläufige Empfehlung für das weitere Vorgehen

Für die erste Pilotierung erscheint folgender Zuschnitt sinnvoll:

### Pilotfokus Stufe 1
**Unterstützung bei der Erstellung von User Stories und Akzeptanzkriterien in ADO**

Warum?
- höchster Hebel am Anfang der Kette
- direkte Verbesserung der Eingangsqualität
- gute Voraussetzung für alles Weitere

### Pilotfokus Stufe 2
**Ableitung von Testfällen aus freigegebenen Anforderungen**

Warum?
- direkt anschlussfähig
- gut prüfbar
- messbarer Qualitätsgewinn

### Perspektive Stufe 3
**Vorbereitung von Testautomatisierung**

Warum?
- fachlich attraktiv, aber komplexer
- sinnvoll erst dann, wenn Anforderungs- und Testfallqualität stabiler geworden sind

---

## 9. Vorläufige Schlussfolgerung

Ein Corporate LLM entfaltet im vorliegenden Kontext seinen größten Nutzen nicht als allgemeiner Chat-Assistent, sondern als **prozessnahes Arbeitswerkzeug im ADO-basierten Entwicklungsprozess**.

Der strategisch sinnvollste Einstieg ist daher:

> **ADO als Single Source of Truth für Anforderungen stärken und darauf aufbauend KI-Unterstützung für User Stories, Akzeptanzkriterien und Testfälle etablieren.**

Damit entsteht ein klarer, fachlich anschlussfähiger und schrittweise ausbaubarer Anwendungsrahmen.

Die eigentliche Stärke des Vorhabens liegt nicht im Sprachmodell an sich, sondern in der besseren Verbindung von:
- Anforderung
- Qualitätskriterium
- Testlogik
- perspektivisch Testautomatisierung

---

## 10. Offene Fragen für die nächste Iteration

1. Wie sehen die derzeitigen Anforderungen in ADO konkret aus?
2. Wie stark unterscheiden sich User Stories und Akzeptanzkriterien aktuell zwischen Teams?
3. Gibt es bereits wiederkehrende Muster für gute Anforderungen?
4. Wie werden Testfälle derzeit dokumentiert und gepflegt?
5. Welche Teile der Testfallableitung wären kurzfristig realistisch standardisierbar?
6. Welche Form von Testautomatisierung ist überhaupt perspektivisch im Zielbild enthalten?
7. Soll der erste Pilot eher an **ila** oder eher an einem übergreifenden LUSD-Prozess ansetzen?
