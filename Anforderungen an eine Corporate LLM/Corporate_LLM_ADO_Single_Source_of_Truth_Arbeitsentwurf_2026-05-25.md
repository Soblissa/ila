# Corporate LLM für ADO-basierte Entwicklungsprozesse
## Arbeitsentwurf mit Schwerpunkt ADO als Single Source of Truth

*Stand: 2026-05-25 | Arbeitsfassung zur iterativen Überarbeitung*

---

## 1. Ausgangslage

**ila** ist ein Teil der **LUSD** (Lehrer- und Schülerdatenbank Hessen). Der Entwicklungsprozess läuft in **Azure DevOps (ADO)**.

Der fachliche Ablauf ist dabei grundsätzlich wie folgt:
1. Es gibt eine **fachliche Anforderung**.
2. Daraus wird eine **User Story** formuliert (PO und Fachlichkeit)
3. Diese User Story wird von den **UX-Kollegen** in Abstimmung mit den fachlichen Expertinnen und Experten in ein **Figma Design** übersetzt
4. Parallel werden durch Fachlichkeit / PO die **Akzeptanzkriterien** entwickelt
5. Die Akzeptanzkriterien werden von der Entwicklung umgesetzt.
6. Die **Testfälle** prüfen, ob die Akzeptanzkriterien erfüllt sind.

Ein Beispiel für diesen Ablauf ist:
- fachliche Anforderung: Die Lernausgangslage eines Kindes soll in einem Textfeld beschrieben werden können.
- User Story: *Als berechtigter Nutzer möchte ich für ein Kind die Lernausgangslage beschreiben, um die passende Förderung festlegen zu können.*

Wichtig ist dabei die saubere fachliche Trennung:
- Die User Story entsteht aus der **fachlichen Anforderung**.
- Die **Akzeptanzkriterien** basieren auf dem entwickelten Design und konkretisieren die User Story für die Entwicklung.
- Aus den **Akzeptanzkriterien** sollen die **Testfälle** abgeleitet werden.
- Aus den **Akzeptanzkriterien** sollen perspektivisch auch **Dokumentationsformen** abgeleitet werden.

Genau in dieser Prozesskette liegt ein relevanter Hebel für ein Corporate LLM (unternehmenseigenes großes Sprachmodell).

---

## 2. Strategischer Kern

Der zentrale Gedanke dieses Vorhabens lautet:

> **Azure DevOps wird zur führenden Quelle im Entwicklungsprozess von ila.**

Das bedeutet im vorliegenden Kontext:
Alle Artefakte werden aus den fachliche Anforderungen (User Stories / kzeptanzkriterien) im ADO abgeleitet

Der stärkste Hebel liegt dabei nicht in der freien Ableitung beliebiger Inhalte aus Anforderungen, sondern in der systematischen Weiterverarbeitung der **Akzeptanzkriterien**.

Für den operativen Entwicklungsprozess soll daher gelten:

> **Was im ADO als User Story formuliert und in Akzeptanzkriterien konkretisiert ist, dient als maßgeblicher Ausgangspunkt für Testfälle und weitere Dokumentationsformen.**

ADO wird damit zur **Single Source of Truth** im engeren Sinne dieses Entwicklungsprozesses.

---

## 3. Was mit „Single Source of Truth“ konkret gemeint ist

Im vorliegenden Kontext bedeutet **Single Source of Truth**:

- die fachliche Anforderung ist vorgelagert und entsteht außerhalb von ADO,
- in ADO wird daraus eine User Story erstellt,
- diese wird in Akzeptanzkriterien übersetzt,
- und die Akzeptanzkriterien bilden die verbindliche Grundlage für Test und Dokumentation.

Die zentrale Annahme lautet:

**Je strukturierter und vollständiger User Stories und insbesondere Akzeptanzkriterien in ADO vorliegen, desto besser lassen sich nachgelagerte Arbeitsschritte unterstützen, standardisieren und teilweise automatisieren.**

Damit verschiebt sich der Fokus weg von allgemeiner KI-Nutzung hin zu einem klaren Prozessnutzen:
- bessere Qualität bei User Stories und Akzeptanzkriterien
- konsistentere Testbasis
- weniger manuelle Doppelarbeit
- bessere Nachvollziehbarkeit bei Änderungen

---

## 4. Hauptanwendungsfälle

Für das Vorhaben sind zunächst drei Hauptanwendungsfälle besonders relevant.

### 4.1 Unterstützung bei der Erstellung von User Stories

#### Ausgangsproblem
Fachliche Anforderungen entstehen zunächst außerhalb von ADO. Sie werden von den beteiligten Personen beschrieben, diskutiert und fachlich eingeordnet. Für die weitere Bearbeitung im Entwicklungsprozess müssen diese Anforderungen in eine verständliche und einheitliche **User Story** übersetzt werden.

Gerade an dieser Stelle können Probleme entstehen:
- uneinheitliche Formulierungen
- unklare Zielbeschreibung
- fehlender Nutzerbezug
- unpräziser fachlicher Nutzen
- zu frühe Vermischung von Fachlichkeit und Lösungsidee

Diese Schwächen wirken sich direkt auf die nachgelagerte Entwicklung von Design, Akzeptanzkriterien, Test und Abnahme aus.

#### Ziel
Ein Corporate LLM soll dabei unterstützen, aus einer fachlich beschriebenen Anforderung eine **klar formulierte User Story** im vereinbarten Format zu erstellen.

#### Konkret bedeutet das
Aus einer fachlichen Beschreibung oder einem ersten Entwurf kann das System Vorschläge erzeugen für:
- eine **sauber formulierte User Story**
- eine sprachliche Strukturierung der fachlichen Beschreibung
- die Benennung des relevanten Nutzers oder der relevanten Rolle
- die präzise Formulierung des fachlichen Nutzens
- offene Rückfragen zur fachlichen Schärfung

#### Beispielhafte Unterstützung
Aus einer freien fachlichen Beschreibung wie
> „Die Lernausgangslage eines Kindes soll in einem Textfeld beschrieben werden können“

würde das System einen strukturierten Vorschlag erzeugen für:
- eine User Story im vereinbarten Format
- fachliche Randbedingungen
- offene Klärungspunkte

Zum Beispiel:
> *Als berechtigter Nutzer möchte ich für ein Kind die Lernausgangslage beschreiben, um die passende Förderung festlegen zu können.*

#### Nutzen
- höhere Einheitlichkeit bei User Stories
- klarerer Übergang von Fachlichkeit in den Entwicklungsprozess
- weniger sprachliche Unschärfen
- bessere Grundlage für die anschließende Entwicklung von Design und Akzeptanzkriterien

Wichtig ist dabei:

> Das Corporate LLM setzt **nicht** bei der Entstehung der fachlichen Anforderung an, sondern bei ihrer **Übersetzung in eine bearbeitbare User Story** für den weiteren Prozess in ADO.

---

### 4.2 Ableitung von Testfällen aus Akzeptanzkriterien

#### Ausgangsproblem
Testfälle werden häufig manuell aus Akzeptanzkriterien abgeleitet. Das ist fehleranfällig und stark von Erfahrung, Zeit und persönlicher Gründlichkeit abhängig.

Typische Probleme sind:
- offensichtliche Fälle werden getestet, Randfälle fehlen
- Akzeptanzkriterien werden nicht vollständig in Testlogik übersetzt
- die Qualität der Testfälle schwankt
- bei Änderungen müssen Testfälle manuell gesucht und angepasst werden

#### Ziel
Ein Corporate LLM soll aus den in ADO hinterlegten Akzeptanzkriterien systematisch Testfälle vorschlagen.

#### Konkret bedeutet das
Das System kann zu einem Satz von Akzeptanzkriterien Testfälle ableiten für:
- **Normalfälle**
- **Sonderfälle**
- **Fehlerfälle**
- **Grenzfälle**
- gegebenenfalls Vorbedingungen und erwartete Ergebnisse

Dabei geht es nicht um freie Testformulierung, sondern um die strukturierte Übersetzung der bereits entwickelten Akzeptanzkriterien in prüfbare Testlogik.

#### Nutzen
- höhere Testabdeckung
- konsistentere Testfallstruktur
- bessere Rückverfolgbarkeit zwischen Akzeptanzkriterium und Testfall
- Zeitersparnis bei der Erstformulierung von Testfällen

#### Besonderer Mehrwert
Wenn User Story und Akzeptanzkriterien bereits in ADO sauber strukturiert vorliegen, entsteht eine direkte Linie:

**User Story → Akzeptanzkriterien in ADO → vorgeschlagene Testfälle**

Für die eigentliche Testableitung sind dabei die **Akzeptanzkriterien** der entscheidende Bezugspunkt.

Perspektivisch gilt dasselbe auch für Dokumentationsformen: Auch sie sollten nicht frei formuliert, sondern möglichst aus den Akzeptanzkriterien abgeleitet werden.

---

### 4.3 Perspektivisch: Unterstützung der Testautomatisierung

#### Ausgangsproblem
Zwischen Akzeptanzkriterien, Testfall und automatisiertem Test liegt heute oft ein deutlicher Übersetzungsaufwand. Fachliche Aussagen müssen in technische Testlogik übertragen werden.

#### Ziel
Ein Corporate LLM soll perspektivisch helfen, die Brücke zwischen fachlich formulierten Anforderungen und einer möglichen Testautomatisierung zu verkürzen.

#### Konkret denkbare Unterstützung
Aus Akzeptanzkriterien und Testfällen könnten vorbereitet oder vorgeschlagen werden:
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

Das Zielbild ist ein Entwicklungsprozess, in dem ADO nicht nur Ablageort ist, sondern der **aktive Ausgangspunkt für die strukturierte Weiterverarbeitung von User Stories und Akzeptanzkriterien**.

Ein mögliches Zielbild lautet:

```text
Fachliche Anforderung
        ↓
Corporate LLM unterstützt die Formulierung der User Story in ADO
        ↓
UX übersetzt die User Story in ein Figma Design
        ↓
Fachlichkeit / PO entwickeln parallel die Akzeptanzkriterien
        ↓
Corporate LLM leitet aus den Akzeptanzkriterien Testfälle ab
        ↓
Entwicklung setzt Akzeptanzkriterien um
        ↓
Test prüft Akzeptanzkriterien
        ↓
Perspektivisch Ableitung von Dokumentationsformen und Unterstützung bei Testautomatisierung
```

Der wesentliche Mehrwert liegt darin, dass die Artefakte nicht isoliert entstehen, sondern in einer nachvollziehbaren Kette aufeinander aufbauen.

Der relevante technische Einstiegspunkt des Corporate LLM liegt dabei nicht am Beginn der fachlichen Idee, sondern ab dem Moment, in dem eine User Story für den weiteren Entwicklungsprozess vorliegt.

---

## 6. Voraussetzungen für den Ansatz

Damit dieser Ansatz tragfähig ist, müssen mehrere Bedingungen erfüllt sein.

### 6.1 Mindeststruktur in ADO
Die Inhalte in ADO müssen so formuliert sein, dass sie systematisch ausgewertet werden können. Dazu gehören mindestens:
- User Story im vereinbarten Format
- Akzeptanzkriterien
- erkennbare Sonder- oder Fehlerfälle

### 6.2 Einheitlicheres Vorgehen bei User Stories und Akzeptanzkriterien
Wenn User Stories und Akzeptanzkriterien sehr unterschiedlich formuliert werden, sinkt die Qualität der automatischen Unterstützung. Deshalb wäre mittelfristig ein Mindeststandard sinnvoll.

### 6.3 Menschliche Prüfung bleibt zwingend
Das LLM darf Vorschläge machen, aber keine fachliche Freigabe ersetzen. Verantwortung bleibt bei den fachlich zuständigen Personen.

### 6.4 Rückverfolgbarkeit
Es muss nachvollziehbar bleiben:
- aus welcher User Story und welchen Akzeptanzkriterien ein Testfall abgeleitet wurde,
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
Fachliche Anforderung, User Story, Akzeptanzkriterien und Testfälle gehören bereits heute zusammen. Das Vorhaben baut also auf einem bestehenden Arbeitszusammenhang auf und erfindet keinen künstlichen KI-Fall.

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
**Unterstützung bei der Erstellung von User Stories auf Basis fachlicher Anforderungen sowie bei der Formulierung von Akzeptanzkriterien in ADO**

Warum?
- höchster Hebel am Anfang der Kette
- direkte Verbesserung der Eingangsqualität
- gute Voraussetzung für alles Weitere

### Pilotfokus Stufe 2
**Ableitung von Testfällen aus freigegebenen Akzeptanzkriterien**

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

Ein Corporate LLM entfaltet im vorliegenden Kontext seinen größten Nutzen nicht als allgemeiner Chat-Assistent, sondern als **prozessnahes Arbeitswerkzeug im ADO-basierten Entwicklungsprozess von ila**.

Der strategisch sinnvollste Einstieg ist daher:

> **ADO als Single Source of Truth für den Zusammenhang von User Story, Akzeptanzkriterien und daraus abgeleiteten Testfällen zu stärken.**

Damit entsteht ein klarer, fachlich anschlussfähiger und schrittweise ausbaubarer Anwendungsrahmen.

Die eigentliche Stärke des Vorhabens liegt nicht im Sprachmodell an sich, sondern in der besseren Verbindung von:
- User Story
- Akzeptanzkriterien
- Testlogik
- perspektivisch Dokumentationsformen und Testautomatisierung

---

## 10. Technische Anforderungen an ein Corporate LLM

Für den vorliegenden Anwendungsfall genügt kein allgemeiner KI-Chat. Erforderlich ist eine technisch und organisatorisch abgesicherte Plattform, die in den bestehenden Entwicklungsprozess eingebettet werden kann.

Ausgangspunkt ist dabei die Annahme, dass rund **60 Mitarbeitende** mit der LUSD arbeiten und perspektivisch ganz oder teilweise von einer solchen Lösung profitieren könnten. Nicht alle werden dieselben Funktionen benötigen. Daraus folgt, dass die Lösung sowohl skalierbar als auch rollenbasiert aufgebaut sein muss.

### 10.1 Zielarchitektur

Für den beschriebenen Einsatzfall werden mindestens vier technische Bausteine benötigt:

1. **LLM-Zugriffsschicht**  
   Zugriff auf ein oder mehrere Sprachmodelle über eine kontrollierte und datenschutzkonforme Schnittstelle.

2. **Wissensschicht**  
   Anbindung an freigegebene Quellen, insbesondere:
   - **Azure DevOps (ADO)**
   - freigegebene LUSD-Dokumentation
   - Anleitungen
   - Release-Informationen
   - Rollen- und Berechtigungskonzepte
   - weitere freigegebene Fachunterlagen

3. **Anwendungslogik**  
   Fachliche Vorlagen und Workflows für klar definierte Aufgaben, zum Beispiel:
   - fachlich beschriebene Anforderungen in User Stories überführen
   - Akzeptanzkriterien strukturieren
   - Testfälle aus Akzeptanzkriterien ableiten
   - Dokumentationsformen vorbereiten

4. **Sicherheits- und Rechteebene**  
   Rollenbasierte Zugriffskontrolle, Protokollierung, Bereichstrennung und kontrollierter Zugriff auf Quellen.

### 10.2 Hardware und Betriebsmodell

#### Empfohlener Einstieg

Für den vorliegenden Anwendungsfall ist ein Einstieg mit **gehosteten Sprachmodellen** und einer eigenen, abgesicherten Fachlogik am sinnvollsten.

In diesem Fall wird keine große eigene KI-Hardware für das Sprachmodell benötigt. Benötigt wird vielmehr Infrastruktur für:
- Anwendungsschicht
- Benutzerverwaltung
- Dokumentenverarbeitung
- Indexierung und semantische Suche
- Datenhaltung
- Protokollierung und Monitoring

Für eine erste belastbare Lösung mit etwa 60 potenziellen Nutzerinnen und Nutzern erscheint folgende Größenordnung realistisch:
- **1-2 Anwendungsserver**
- **1 Datenbankserver**
- **1 Such- oder Indexierungsdienst**
- gesicherter Dateispeicher für Dokumente, Indizes und Protokolle
- Trennung von Test- und Produktivumgebung

Als grobe Ausgangsgröße erscheint für die Anwendungsschicht eine Ausstattung in der Größenordnung von etwa:
- **8-16 vCPU**
- **32-64 GB RAM**
pro Instanz sinnvoll.

Eine **GPU** ist in diesem Modell nicht zwingend erforderlich, solange das eigentliche Sprachmodell extern und rechtskonform betrieben wird.

#### Nicht empfohlener Einstieg

Ein vollständiger **Eigenbetrieb lokaler Modelle** wäre technisch deutlich aufwändiger. Dafür wären zusätzlich erforderlich:
- GPU-Server mit hohem VRAM
- eigener Modellbetrieb
- zusätzliche Betriebs- und Wartungskompetenz
- aufwändigeres Performance- und Lastmanagement

Für den fachlichen Einstieg in den beschriebenen Anwendungsfall erscheint dies nicht verhältnismäßig.

### 10.3 Agenten und Funktionsmodule

Für dieses Vorhaben sind **Agenten** sinnvoll, allerdings nicht als frei agierende Systeme, sondern als **klar begrenzte Spezial-Assistenten**.

Sinnvolle Module wären insbesondere:

#### User-Story-Assistent
- Eingabe: fachlich beschriebene Anforderung außerhalb von ADO
- Ausgabe: strukturierte User Story im vereinbarten Format für ADO

#### Akzeptanzkriterien-Assistent
- Eingabe: User Story
- Ausgabe: strukturierte Akzeptanzkriterien, Sonderfälle, Fehlerfälle, offene Rückfragen

#### Testfall-Assistent
- Eingabe: Akzeptanzkriterien
- Ausgabe: Testfälle mit Testschritten und erwarteten Ergebnissen

#### Dokumentations-Assistent
- Eingabe: Akzeptanzkriterien und umgesetzte Funktion
- Ausgabe: Entwürfe für Anwenderhilfe, Kurzbeschreibung, Release-Hinweise oder weitere Dokumentationsformen

#### Impact-Assistent
- Eingabe: geänderte User Story oder geänderte Akzeptanzkriterien
- Ausgabe: Hinweise auf betroffene Testfälle, Dokumentationsbausteine und Folgeprüfungen

Wichtig ist dabei: Diese Assistenten sollen **Vorschläge erzeugen**, aber keine fachliche oder organisatorische Freigabe ersetzen.

### 10.4 Anforderungen aus der LUSD-Perspektive

Die im Repo vorliegenden LUSD-Unterlagen zeigen, dass die technische Lösung folgende Besonderheiten des Fachkontextes berücksichtigen muss:

#### Rollen und Berechtigungen
Die LUSD arbeitet bereits heute mit einem differenzierten Rollen- und Berechtigungskonzept. Daraus folgt für ein Corporate LLM:
- rollenbasierter Zugriff auf Funktionen und Inhalte
- restriktive Vergabe von Berechtigungen
- Trennung unterschiedlicher Nutzergruppen
- Zugriff nur auf freigegebene Inhalte

#### Kontextabhängige Anwenderunterstützung
Die LUSD verfügt bereits über:
- Online-Hilfen pro Webseite
- Anleitungen
- FAQs
- Support- und Helpdesk-Strukturen
- Fortbildungsangebote

Das Corporate LLM sollte diese Struktur nicht ersetzen, sondern sinnvoll ergänzen. Antworten sollten deshalb möglichst:
- kontextbezogen,
- rollenbezogen,
- quellenbezogen
- und anschlussfähig an bestehende Hilfestrukturen
sein.

#### Heterogene Dokumentbestände
Im LUSD-Bestand liegen bereits unterschiedliche Dokumenttypen vor, darunter:
- PDF
- Word
- Excel
- Textdateien
- Release-Dokumente
- Anleitungen

Die Plattform muss deshalb in der Lage sein:
- unterschiedliche Dokumenttypen zu verarbeiten,
- Inhalte zu indexieren,
- Metadaten zu verwalten,
- Versionen zu unterscheiden,
- und nach Thema, Zielgruppe oder Dokumenttyp zu filtern.

### 10.5 Technische Muss-Anforderungen

Aus dem beschriebenen Vorhaben ergeben sich mindestens folgende Muss-Anforderungen:

- **EU-Hosting** oder gleichwertig rechtskonforme Betriebsform
- **AVV** mit eingesetzten Anbietern
- **kein Training mit Organisationsdaten**
- **rollenbasierte Zugriffskontrolle**
- **Quellenbezug pro Antwort**
- **Anbindung an ADO**
- **Anbindung an freigegebene Dokumentenquellen**
- **semantische Suche**
- **Versionierung**
- **Auditierbarkeit und Protokollierung**
- **Trennung von Test- und Produktivumgebung**
- **API-Schnittstellen** für die Integration in bestehende Systeme

### 10.6 Sinnvolle Zusatzanforderungen

Zusätzlich sinnvoll wären:
- mehrere Modelloptionen über eine Oberfläche
- Vorlagenbibliothek für wiederkehrende Aufgaben
- Feedbackfunktion zur Bewertung von Vorschlägen
- Export in nutzbare Formate, zum Beispiel Word, Markdown oder Testfalltabellen
- Freigabe- und Prüfschritte für erzeugte Inhalte
- Bereichs- oder Mandantentrennung bei unterschiedlichen Nutzergruppen

### 10.7 Technische Empfehlung

Für den beschriebenen Anwendungsfall erscheint folgende technische Linie am sinnvollsten:

> **Keine isolierte KI-Einzellösung, sondern eine abgesicherte Plattform mit ADO-Anbindung, Dokumentenindex, rollenbasiertem Zugriff und klar begrenzten Spezial-Assistenten.**

Der Einstieg sollte dabei **nicht** über lokalen Vollbetrieb großer Modelle erfolgen, sondern über eine kontrollierte Plattformarchitektur mit extern betriebenem, datenschutzkonform eingebundenem Sprachmodell.

So bleibt der Fokus auf dem eigentlichen Nutzen:
- bessere User Stories
- bessere Akzeptanzkriterien
- bessere Testfälle
- bessere Dokumentationsgrundlagen

---

## 11. Offene Fragen für die nächste Iteration

1. Wie sehen die derzeitigen Anforderungen in ADO konkret aus?
2. Wie stark unterscheiden sich User Stories und Akzeptanzkriterien aktuell zwischen Teams?
3. Gibt es bereits wiederkehrende Muster für gute Anforderungen?
4. Wie werden Testfälle derzeit dokumentiert und gepflegt?
5. Welche Teile der Testfallableitung wären kurzfristig realistisch standardisierbar?
6. Welche Form von Testautomatisierung ist überhaupt perspektivisch im Zielbild enthalten?
7. Soll der erste Pilot eher an **ila** oder eher an einem übergreifenden LUSD-Prozess ansetzen?
