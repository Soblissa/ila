# Corporate LLM für ADO-basierte Entwicklungsprozesse
## Arbeitsentwurf mit Schwerpunkt auf ila als Ausgangspunkt und der Übertragbarkeit auf die LUSD

*Stand: 2026-05-25 | Arbeitsfassung zur iterativen Überarbeitung*

---

# Teil 1: Einleitung

## 1. Einordnung eines Corporate LLM

Ein **Corporate LLM** (Corporate Large Language Model, unternehmenseigenes großes Sprachmodell) ist kein von Grund auf neu trainiertes eigenes Modell, sondern ein **privater, DSGVO-konformer KI-Arbeitsbereich**, der auf bestehenden Sprachmodellen aufsetzt und diese mit dem eigenen Organisationswissen verbindet. Grundlage dafür ist die Einbindung freigegebener interner Wissensquellen, die dem Modell als zusätzlicher Kontext bereitgestellt werden.

Der eigentliche Mehrwert liegt dabei nicht in einem allgemeinen KI-Chat, sondern in der Verbindung von Sprachmodell, organisationsspezifischem Wissen, klaren Rollen und definierten Anwendungsfällen.

Für den hier beschriebenen Anwendungsfall bedeutet das: Das Corporate LLM soll nicht allgemein beliebige Fragen beantworten, sondern gezielt den ADO-basierten Entwicklungsprozess rund um **ila** und perspektivisch auch die **LUSD** unterstützen.

---

# Teil 2: Anwendung und fachlicher Nutzen

## 2. Ausgangslage

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

## 3. Strategischer Kern

Der zentrale Gedanke dieses Vorhabens lautet:

> **Azure DevOps wird zur Single Source of Truth für die im Entwicklungsprozess von ila entstehenden Artefakte, insbesondere für User Stories, Akzeptanzkriterien und daraus abgeleitete Folgeartefakte.**

Das bedeutet im vorliegenden Kontext:
Alle relevanten Folgeartefakte, zum Beispiel Testfälle, Dokumentationsbausteine oder integrierte KI-basierte Anwenderunterstützung, werden aus den in ADO gepflegten User Stories und Akzeptanzkriterien abgeleitet.

Der stärkste Hebel liegt dabei nicht in der freien Ableitung beliebiger Inhalte aus Anforderungen, sondern in der systematischen Weiterverarbeitung der **Akzeptanzkriterien**.

Für den operativen Entwicklungsprozess soll daher gelten:

> **Was im ADO als User Story formuliert und in Akzeptanzkriterien konkretisiert ist, dient als maßgeblicher Ausgangspunkt für Testfälle und weitere Dokumentationsformen.**

ADO wird damit zur **Single Source of Truth** im engeren Sinne dieses Entwicklungsprozesses.

---

## 4. Zentrale Annahme

**Je klarer, strukturierter und vollständiger User Stories und insbesondere Akzeptanzkriterien in ADO vorliegen, desto besser lassen sich nachgelagerte Arbeitsschritte unterstützen, standardisieren und teilweise automatisieren.**

Damit liegt der Fokus weniger auf allgemeiner KI-Nutzung sondern auf einem klaren Prozessnutzen:
- bessere Qualität bei User Stories und Akzeptanzkriterien
- konsistentere Testbasis
- weniger manuelle Doppelarbeit
- bessere Nachvollziehbarkeit bei Änderungen

---

## 5. Hauptanwendungsfälle

Für das Vorhaben sind zunächst drei Hauptanwendungsfälle besonders relevant.

### 5.1 Unterstützung bei der Erstellung von User Stories

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

Im Fall von ila können solche vorgelagerten fachlichen Beschreibungen zum Beispiel aus Portfolios, Verordnungen oder anderen fachlichen Quellen stammen.

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

> Das Corporate LLM setzt **nicht** bei der Entstehung der fachlichen Anforderung an, sondern bei ihrer **Übersetzung in eine bearbeitbare User Story** für den weiteren Prozess in ADO, insbesondere für die anschließende Entwicklung der Akzeptanzkriterien als Grundlage für die Umsetzung.

---

### 5.2 Ableitung von Testfällen aus Akzeptanzkriterien

#### Ausgangsproblem
Testfälle werden häufig manuell aus Akzeptanzkriterien abgeleitet. Das ist fehleranfällig und stark von Erfahrung, Zeit und persönlicher Gründlichkeit abhängig.

Typische Probleme sind:
- offensichtliche Fälle werden getestet, Randfälle fehlen
- Akzeptanzkriterien werden nicht vollständig in Testlogik übersetzt
- die Qualität der Testfälle schwankt
- bei Änderungen müssen Testfälle manuell gesucht und angepasst werden

#### Ziel
Ein Corporate LLM soll aus den in ADO hinterlegten Akzeptanzkriterien systematisch Testfälle ableiten, orientiert an einem eingespielten beziehungsweise überarbeiteten Testkonzept.

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

### 5.3 Perspektivisch: Unterstützung der Testautomatisierung

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

## 6. Zielbild des Prozesses

Das Zielbild ist ein Entwicklungsprozess, in dem ADO nicht nur Ablageort ist, sondern der **aktive Ausgangspunkt für die strukturierte Weiterverarbeitung von User Stories und Akzeptanzkriterien** sowie für daraus abgeleitete Artefakte in unterschiedlichen Formaten, zum Beispiel Testfälle, Dokumentationsbausteine oder eine integrierte KI-basierte Anwenderunterstützung.

Der wesentliche Mehrwert liegt darin, dass die Artefakte nicht isoliert entstehen, sondern in einer nachvollziehbaren Kette aufeinander aufbauen. Der relevante technische Einstiegspunkt des Corporate LLM liegt dabei nicht am Beginn der fachlichen Idee, sondern ab dem Moment, in dem eine User Story für den weiteren Entwicklungsprozess vorliegt.

---

## 7. Warum dieser Fokus für LUSD und ila sinnvoll ist

Der Schwerpunkt auf **ADO als Single Source of Truth** und auf die beschriebenen Anwendungsfälle ist für **ila** und perspektivisch auch für die **LUSD** besonders geeignet, weil hier ein klarer und messbarer Nutzen entsteht.

### 7.1 Direkte Hebelwirkung in ila
Bei ila sind User Stories, Design, Akzeptanzkriterien, Entwicklung und Test bereits eng miteinander verzahnt. Verbesserungen bei der Qualität und Weiterverarbeitung der Akzeptanzkriterien wirken sich deshalb unmittelbar auf Entwicklung, Test und Dokumentation aus.

### 7.2 Analyse- und Standardisierungspotenzial in der LUSD
Für die LUSD liegt der Nutzen zunächst stärker in der Analyse des bestehenden ADO-Bestands. Gerade dort kann ein Corporate LLM helfen, Muster in Akzeptanzkriterien zu erkennen, Unterschiede sichtbar zu machen und Empfehlungen für ein einheitlicheres Vorgehen abzuleiten.

### 7.3 Gemeinsamer Nutzen für beide Kontexte
Sowohl für ila als auch für die LUSD gilt: Der größte Nutzen entsteht dort, wo Akzeptanzkriterien nicht nur geschrieben, sondern systematisch weiterverarbeitet werden können, zum Beispiel für Testfälle, Dokumentationsformen oder perspektivisch für integrierte Anwenderunterstützung.

### 7.4 Anschlussfähigkeit für spätere Ausbaustufen
Wenn der Ansatz funktioniert, kann er später erweitert werden, zum Beispiel auf:
- Dokumentation
- Anwenderhilfen
- Change-Impact-Analysen
- integrierte Unterstützung direkt in ila
- übertragbare Standards für weitere Teilprodukte der LUSD

---

## 8. Erster Analyseauftrag für die LUSD

Für die **LUSD** kann nicht vorausgesetzt werden, dass die Inhalte in ADO bereits heute einheitlich, vollständig und in einer Form vorliegen, die sofort systematisch weiterverarbeitet werden kann. Gerade deshalb liegt ein wesentlicher erster Nutzen eines Corporate LLM in der **Analyse des bestehenden ADO-Bestands**.

Der erste Auftrag des Systems wäre damit nicht primär die direkte Standardisierung neuer Inhalte, sondern zunächst die strukturierte Auswertung dessen, was in der **LUSD** bereits vorhanden ist.

### 8.1 Ziel des ersten Analyseauftrags

Das Corporate LLM soll den vorhandenen ADO-Bestand der LUSD systematisch auswerten, um insbesondere die vorhandenen **Akzeptanzkriterien** besser zu verstehen. Dabei soll es:
- wiederkehrende Muster in Akzeptanzkriterien erkennen,
- Unterschiede in Formulierungsweisen und Detaillierungsgraden sichtbar machen,
- typische Strukturen von Akzeptanzkriterien identifizieren,
- Lücken, Unschärfen und Inkonsistenzen erkennen,
- häufige fachliche oder sprachliche Schwächen benennen,
- und daraus Empfehlungen für eine künftig bessere Strukturierbarkeit ableiten.

Gerade bei der LUSD ist das relevant, weil von einem historisch gewachsenen Bestand mit unterschiedlichen Autoren, unterschiedlichen fachlichen Zuschnitten und unterschiedlichen Qualitätsniveaus auszugehen ist.

### 8.2 Konkrete Fragestellungen für die Analyse

Ein erster Analyseauftrag an ein Corporate LLM könnte für die LUSD zum Beispiel lauten:
- Welche Typen von Akzeptanzkriterien kommen im ADO-Bestand der LUSD wiederholt vor?
- Welche Formulierungen oder Muster werden häufig verwendet?
- Welche Bestandteile sind regelmäßig vorhanden und welche fehlen oft?
- Wie stark unterscheiden sich Akzeptanzkriterien zwischen Themenfeldern oder Teams?
- Welche Formulierungen eignen sich als gute Vorlage für künftige Akzeptanzkriterien?
- Wo gibt es auffällige Unschärfen, Widersprüche oder Auslassungen?

### 8.3 Erwarteter Nutzen dieses ersten Schritts

Dieser erste Analyseschritt hätte für die LUSD mehrere Vorteile:
- Der vorhandene ADO-Bestand wird überhaupt erst systematisch durchschaubar.
- Gute Muster in Akzeptanzkriterien können identifiziert und für die weitere Arbeit nutzbar gemacht werden.
- Schwächen im Bestand werden nicht nur vermutet, sondern konkret benannt.
- Empfehlungen für ein einheitlicheres Vorgehen können auf realem Material aufsetzen.
- Die spätere Ableitung von Testfällen, Dokumentationsformen oder weiteren Unterstützungsleistungen kann auf einer belastbareren Grundlage erfolgen.

### 8.4 Bedeutung für das weitere Vorgehen

Für die LUSD sollte das Corporate LLM daher zunächst nicht so gedacht werden, als läge bereits ein sauber standardisierter ADO-Bestand vor. Realistischer und fachlich sinnvoller ist ein zweistufiges Vorgehen:

1. **Analyse des bestehenden ADO-Bestands der LUSD mit Schwerpunkt auf den Akzeptanzkriterien**
2. **Ableitung von Empfehlungen, Standards und späteren Unterstützungsfunktionen**

Menschliche Prüfung bleibt dabei zwingend erforderlich. Das Corporate LLM soll Muster erkennen, Vorschläge machen und Auffälligkeiten sichtbar machen, aber keine fachliche Bewertung oder Freigabe ersetzen.

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

# Teil 3: Technische Umsetzung und Voraussetzungen

## 10. Technische Zielarchitektur

Für den vorliegenden Anwendungsfall genügt kein allgemeiner KI-Chat. Erforderlich ist eine technisch und organisatorisch abgesicherte Plattform, die in den bestehenden Entwicklungsprozess eingebettet werden kann.

Ausgangspunkt ist dabei die Annahme, dass rund **60 Mitarbeitende** mit der LUSD arbeiten und perspektivisch ganz oder teilweise von einer solchen Lösung profitieren könnten. Nicht alle werden dieselben Funktionen benötigen. Daraus folgt, dass die Lösung sowohl skalierbar als auch rollenbasiert aufgebaut sein muss.

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

---

## 11. Betriebsvarianten, Hardware und Hosting

### 11.1 Variante A: Hosting und Betrieb in eigener Verantwortung

Eine mögliche Variante ist, dass Hosting und Betrieb durch den Auftraggeber selbst oder durch einen von ihm gesteuerten Dienstleister erfolgen.

Vorteile:
- höhere Steuerbarkeit
- größere technische Unabhängigkeit
- flexible Auswahl von Komponenten

Nachteile:
- höherer Betriebsaufwand
- mehr Eigenverantwortung für Sicherheit, Wartung und Skalierung
- zusätzlicher Bedarf an technischem Know-how

### 11.2 Variante B: Hosting und Betrieb durch die HZD

Da die bestehende Infrastruktur derzeit durch die **HZD** (Hessische Zentrale für Datenverarbeitung) bereitgestellt wird, ist eine zweite, naheliegende Variante das Hosting und der Betrieb durch die HZD.

Vorteile:
- bessere Anschlussfähigkeit an die bestehende Infrastruktur
- Einbettung in vorhandene Betriebs- und Sicherheitsstrukturen
- naheliegende Betriebsform im Behördenkontext

Nachteile:
- stärkere Abhängigkeit von bestehenden Rahmenbedingungen
- geringere technische Beweglichkeit bei Architektur und Komponentenwahl
- zusätzlicher Abstimmungsbedarf mit dem Betreiber

### 11.3 Hardware und Skalierung

Für eine erste belastbare Lösung mit etwa 60 potenziellen Nutzerinnen und Nutzern erscheint bei Nutzung gehosteter Sprachmodelle folgende Größenordnung realistisch:
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

Ein vollständiger **Eigenbetrieb lokaler Modelle** wäre technisch deutlich aufwändiger. Dafür wären zusätzlich erforderlich:
- GPU-Server mit hohem VRAM
- eigener Modellbetrieb
- zusätzliche Betriebs- und Wartungskompetenz
- aufwändigeres Performance- und Lastmanagement

Für den fachlichen Einstieg in den beschriebenen Anwendungsfall erscheint dies derzeit nicht verhältnismäßig.

---

## 12. Datenschutz und Informationssicherheit

Im beschriebenen Kontext ist Datenschutz kein Nebenaspekt, sondern eine zentrale Voraussetzung.

Zu berücksichtigen sind insbesondere:
- **EU-Hosting** oder gleichwertig rechtskonforme Betriebsform
- **AVV** mit eingesetzten Anbietern
- **kein Training mit Organisationsdaten**
- **Datenminimierung** bei allen eingebundenen Quellen
- **rollenbasierte Zugriffskontrolle**
- **Auditierbarkeit und Protokollierung**
- **Trennung von Test- und Produktivumgebung**
- klar geregelte Zuständigkeiten für Betrieb, Administration und Freigaben

Gerade im LUSD-Kontext ist zusätzlich zu beachten, dass mit sensiblen schulischen Daten gearbeitet wird und die Lösung daher nur auf klar freigegebene Inhalte zugreifen darf.

---

## 13. Agenten und Funktionsmodule

Für dieses Vorhaben sind **Agenten** sinnvoll, allerdings nicht als frei agierende Systeme, sondern als **klar begrenzte Spezial-Assistenten**.

Sinnvolle Module wären insbesondere:

### 13.1 User-Story-Assistent
- Eingabe: fachlich beschriebene Anforderung außerhalb von ADO
- Ausgabe: strukturierte User Story im vereinbarten Format für ADO

### 13.2 Akzeptanzkriterien-Assistent
- Eingabe: User Story
- Ausgabe: strukturierte Akzeptanzkriterien, Sonderfälle, Fehlerfälle, offene Rückfragen

### 13.3 Testfall-Assistent
- Eingabe: Akzeptanzkriterien
- Ausgabe: Testfälle mit Testschritten und erwarteten Ergebnissen

### 13.4 Dokumentations-Assistent
- Eingabe: Akzeptanzkriterien und umgesetzte Funktion
- Ausgabe: Entwürfe für Anwenderhilfe, Kurzbeschreibung, Release-Hinweise oder weitere Dokumentationsformen

### 13.5 Impact-Assistent
- Eingabe: geänderte User Story oder geänderte Akzeptanzkriterien
- Ausgabe: Hinweise auf betroffene Testfälle, Dokumentationsbausteine und Folgeprüfungen

Wichtig ist dabei: Diese Assistenten sollen **Vorschläge erzeugen**, aber keine fachliche oder organisatorische Freigabe ersetzen.

---

## 14. Weitere technische Voraussetzungen aus der LUSD-Perspektive

Die im Repo vorliegenden LUSD-Unterlagen zeigen, dass die technische Lösung folgende Besonderheiten des Fachkontextes berücksichtigen muss:

### 14.1 Rollen und Berechtigungen
Die LUSD arbeitet bereits heute mit einem differenzierten Rollen- und Berechtigungskonzept. Daraus folgt für ein Corporate LLM:
- rollenbasierter Zugriff auf Funktionen und Inhalte
- restriktive Vergabe von Berechtigungen
- Trennung unterschiedlicher Nutzergruppen
- Zugriff nur auf freigegebene Inhalte

### 14.2 Kontextabhängige Anwenderunterstützung
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

### 14.3 Heterogene Dokumentbestände
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

### 14.4 Technische Muss-Anforderungen
Aus dem beschriebenen Vorhaben ergeben sich mindestens folgende Muss-Anforderungen:
- **Quellenbezug pro Antwort**
- **Anbindung an ADO**
- **Anbindung an freigegebene Dokumentenquellen**
- **semantische Suche**
- **Versionierung**
- **API-Schnittstellen** für die Integration in bestehende Systeme

### 14.5 Sinnvolle Zusatzanforderungen
Zusätzlich sinnvoll wären:
- mehrere Modelloptionen über eine Oberfläche
- Vorlagenbibliothek für wiederkehrende Aufgaben
- Feedbackfunktion zur Bewertung von Vorschlägen
- Export in nutzbare Formate, zum Beispiel Word, Markdown oder Testfalltabellen
- Freigabe- und Prüfschritte für erzeugte Inhalte
- Bereichs- oder Mandantentrennung bei unterschiedlichen Nutzergruppen

---

# Teil 4: Empfehlungen und Vorgehen

## 15. Empfehlungen für das weitere Vorgehen

Für die erste Pilotierung erscheint folgender Zuschnitt sinnvoll:

### 15.1 Pilotfokus Stufe 1
**Analyse des bestehenden ADO-Bestands mit Schwerpunkt auf Akzeptanzkriterien, zunächst vor allem für die LUSD**

Warum?
- realistischer Einstieg in einen historisch gewachsenen Bestand
- gute Grundlage für spätere Standards
- direkte Sicht auf Muster, Schwächen und Unterschiede

### 15.2 Pilotfokus Stufe 2
**Ableitung von Testfällen aus freigegebenen Akzeptanzkriterien**

Warum?
- direkt anschlussfähig
- gut prüfbar
- messbarer Qualitätsgewinn
- Akzeptanzkriterien sind der entscheidende fachliche Bezugspunkt für die Umsetzung in Code

### 15.3 Perspektive Stufe 3
**Ableitung weiterer Artefakte aus Akzeptanzkriterien, insbesondere Dokumentationsformen und perspektivisch Unterstützung bei Testautomatisierung**

Warum?
- fachlich folgerichtig
- anschlussfähig an den bestehenden Entwicklungsprozess
- sinnvoll erst dann, wenn Analyse und Struktur der Akzeptanzkriterien belastbarer geworden sind

---

## 16. Technische Empfehlung

Für den beschriebenen Anwendungsfall erscheint folgende technische Linie am sinnvollsten:

> **Keine isolierte KI-Einzellösung, sondern eine abgesicherte Plattform mit ADO-Anbindung, Dokumentenindex, rollenbasiertem Zugriff und klar begrenzten Spezial-Assistenten.**

Der Einstieg sollte dabei **nicht** über lokalen Vollbetrieb großer Modelle erfolgen, sondern über eine kontrollierte Plattformarchitektur mit extern betriebenem, datenschutzkonform eingebundenem Sprachmodell oder alternativ über eine durch die HZD betriebene Lösung, sofern diese die fachlichen und technischen Anforderungen erfüllt.

So bleibt der Fokus auf dem eigentlichen Nutzen:
- bessere User Stories
- bessere Akzeptanzkriterien
- bessere Testfälle
- bessere Dokumentationsgrundlagen

---

## 17. Offene Fragen für die nächste Iteration

1. Wie sehen die derzeitigen Anforderungen in ADO konkret aus?
2. Wie stark unterscheiden sich User Stories und Akzeptanzkriterien aktuell zwischen Teams?
3. Gibt es bereits wiederkehrende Muster für gute Anforderungen?
4. Wie werden Testfälle derzeit dokumentiert und gepflegt?
5. Welche Teile der Testfallableitung wären kurzfristig realistisch standardisierbar?
6. Welche Form von Testautomatisierung ist überhaupt perspektivisch im Zielbild enthalten?
7. Soll der erste Pilot eher an **ila** oder eher an einem übergreifenden LUSD-Prozess ansetzen?
