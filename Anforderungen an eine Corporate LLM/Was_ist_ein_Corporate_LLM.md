# Anforderungen an eine Corporate LLM
## Referat IV. 2.1 | HMKB

*Erstellt: 2026-04-12 | Aktualisiert: 2026-04-13 | Status: Entwurf*

---

## 1. Was ist ein Corporate LLM?

Ein **Corporate LLM** (Corporate Large Language Model — unternehmenseigenes großes Sprachmodell) ist kein eigenes KI-Modell das von Grund auf neu trainiert wird. Es ist ein **privater, DSGVO-konformer KI-Arbeitsbereich für eine Organisation**, der auf bestehenden Sprachmodellen (z. B. von Anthropic, OpenAI oder europäischen Anbietern wie Mistral) aufsetzt.

Das zugrunde liegende Sprachmodell bringt allgemeines Sprachverständnis und Grundwissen mit — erworben durch das Training auf großen Mengen öffentlicher Texte. Ein Corporate LLM erweitert das um das **eigene Wissen der Organisation**: Erlasse, Prozessbeschreibungen, Handreichungen, interne Standards. Dieses Wissen wird indexiert und fließt automatisch als zusätzlicher Kontext in jede Anfrage ein. Das Ergebnis ist eine Mischung aus beidem — wobei das Behördenwissen Vorrang hat und die Antwort in die richtige Richtung lenkt.

Analogie: Ein neuer Mitarbeiter bringt seine allgemeine Ausbildung mit. Dann bekommt er das Handbuch, die Erlasse und die internen Prozesse der Behörde. Ab dann arbeitet er mit beidem — aber die Hausregeln stechen das Schulbuchwissen.

| Merkmal | Bedeutung |
|---|---|
| Zentraler Zugang | Alle Mitarbeitenden nutzen eine einzige Oberfläche — kein Tool-Wildwuchs |
| Behördenwissen integriert | Interne Dokumente, Erlasse, Prozesse als Wissensgrundlage |
| Rollenbasierte Zugriffssteuerung | Wer darf was sehen und nutzen? Zentral steuerbar |
| DSGVO-konform | EU-Hosting, kein Training mit Behördendaten |
| Abteilungsspezifische Assistenten | Spezialisierte KI-Helfer für definierte Aufgaben möglich |
| Prompt-Bibliothek | Bewährte Arbeitsanweisungen zentral verfügbar — kein Prompt-Engineering nötig |

### Wie das Behördenwissen technisch eingebunden wird

Dokumente (PDF, Word, Excel, Markdown) werden in einer **Vektordatenbank** indexiert. Stellt eine Mitarbeiterin eine Frage, durchsucht das System automatisch diese Datenbank, zieht die relevanten Passagen heraus und gibt sie als Kontext an das Sprachmodell weiter.

**Vorteil:** Skaliert auf tausende Seiten. Es wird immer nur der für die Anfrage relevante Kontext geladen — nicht das gesamte Dokument.

**Unterstützte Formate:** PDF, Word, Excel, Markdown, Textdateien — auch handschriftliche Scans (via OCR).

---

## 2. Warum kein Corporate LLM ein Problem ist

### 2.1 Schatten-KI — der unsichtbare Risikofaktor

Wenn keine gute offizielle Lösung bereitgestellt wird, nutzen Mitarbeitende trotzdem KI — unkontrolliert. Vertrauliche Daten, Dienstgeheimnisse und personenbezogene Informationen landen dann in fremden Systemen, häufig auf US-amerikanischen Servern, ohne Rechtsgrundlage.

**Bekanntes Beispiel:** Samsung musste 2023 KI intern komplett verbieten, nachdem Mitarbeitende Quellcode und Produktionsdaten in ChatGPT eingegeben hatten. Das Verbot löste das Problem nicht — es verlagerte es in den Untergrund.

### 2.2 Fünf Hauptprobleme ohne Corporate LLM

| # | Problem | Folge |
|---|---|---|
| 1 | **Team nutzt KI nicht** | Potenzial bleibt ungenutzt, Führung und Mitarbeitende entkoppelt |
| 2 | **Schatten-KI** | Unkontrollierter Einsatz privater Accounts mit Dienstdaten |
| 3 | **Rechtliche Unsicherheit** | DSGVO-Risiken, fehlende Governance blockiert Innovation |
| 4 | **Falsche Lösungen** | Insellösungen die niemand nutzt (z.B. Microsoft Copilot: dokumentierte Sicherheitslücken, kaum Nutzung) |
| 5 | **Tool-Wildwuchs** | Ab 4+ Tools sinkt Produktivität durch Informationsüberflutung |

### 2.3 Fehlende Wirksamkeit ohne Prozesseinbettung

Ohne Integration in Behördenwissen und Arbeitsabläufe bleibt KI-Nutzung an der Oberfläche — Texte formulieren, zusammenfassen. Messbarer Nutzen für die eigentliche Facharbeit entsteht erst, wenn das Systemwissen der Organisation integriert ist.

---

## 3. Funktionsmodule eines Corporate LLM

### 3.1 Wissensdatenbank

Interne Dokumente werden indexiert und stehen als Wissensgrundlage zur Verfügung. Antworten basieren auf dem eigenen Behördenwissen, nicht auf allgemeinem Internetwissen. Quellenangabe bei Antworten möglich.

### 3.2 Agenten (spezialisierte KI-Assistenten)

Ein Agent ist mehr als ein KI-Modell mit Persona — er kombiniert:
- **Anweisungen** (Rolle, Verhalten)
- **Zugriff auf Teilmengen** des Behördenwissens
- **Skills** (z.B. Dokumenten-Erstellung, Websuche)
- **Prompt-Vorlagen** für wiederkehrende Aufgaben

Beispiel: Ein Sachbearbeitungs-Assistent der nur auf die für ihn freigegebenen Erlasse und Prozessbeschreibungen zugreift.

### 3.3 Prompt-Bibliothek mit Vorlagen

Zentrale Sammlung bewährter Arbeitsanweisungen. Mitarbeitende füllen nur noch Variablen aus — kein eigenes Prompt-Engineering nötig. Beispiel: Vorlage "Besprechungsprotokoll" → Mitarbeiterin füllt Datum, Teilnehmende, Punkte aus → fertiges Protokoll.

### 3.4 Abteilungsbereiche (Spaces)

Dedizierte Arbeitsbereiche pro Abteilung oder Thema. Jeder Bereich hat nur Zugriff auf das relevante Wissen — reduziert Rauschen, erhöht Qualität der Antworten.

### 3.5 Berechtigungsmanagement

Granulare Zugriffssteuerung: Wer darf welche Agenten, welches Wissen, welche Funktionen nutzen? Verhindert ungewollten Zugriff auf sensible Bereiche (z.B. Personalakten, Leitungsdokumente).

### 3.6 Modellauswahl

Zugang zu mehreren KI-Modellen über eine Oberfläche. Automatische Weiterleitung an das geeignetste Modell je nach Aufgabentyp möglich — wirtschaftlich und qualitätsorientiert.

### 3.7 Spracheingabe (optional)

Gesprochene Eingaben werden in kontextgerechten Text umgewandelt. Besonders wertvoll für Protokolle, Berichte und Notizen nach Besprechungen.

⚠️ **Datenschutzhinweis:** Manche bekannten Tools dieser Art (z.B. Whisperflow) machen dauerhaft Screenshots des gesamten Bildschirms. Im Behördenkontext nicht vertretbar. Nur DSGVO-konforme Lösungen mit EU-Hosting einsetzen.

---

## 4. Datenschutz und rechtliche Anforderungen

### 4.1 Technische Mindestanforderungen

| Anforderung | Beschreibung |
|---|---|
| EU-Hosting | Alle Daten ausschließlich auf europäischen Servern |
| AVV | Auftragsverarbeitungsvertrag mit allen KI-Anbietern (Art. 28 DSGVO) |
| Kein Modelltraining | Eingaben dürfen nicht zur Modellverbesserung verwendet werden |
| Zugriffsprotokollierung | Alle Zugriffe nachvollziehbar und auditierbar |
| Löschkonzept | Vollständige Datenlöschung auf Anfrage möglich |
| Rollenbasierte Rechtevergabe | Granulare Steuerung wer was sehen und nutzen darf |
| Keine Screenshots | Spracheingabe-Tools dürfen keine Screenshots erstellen |

### 4.2 Besonderheiten im HMKB-Kontext

- Personenbezogene Daten von Minderjährigen erfordern besondere Schutzmaßnahmen
- Dienstgeheimnisse und Amtsverschwiegenheit müssen technisch abgesichert sein
- Hessisches Datenschutzgesetz (HDSIG) gilt ergänzend zur DSGVO
- Mitbestimmungsrechte des Personalrats bei Einführung neuer IT-Systeme sind zu beachten

### 4.3 Nicht geeignet für den Behördenkontext

| Tool | Problem |
|---|---|
| ChatGPT (Standard-Account) | US-Server, kein AVV, mögliches Modelltraining |
| Microsoft Copilot (Standard) | Dokumentierte Sicherheitslücken, kaum messbarer Nutzen |
| Private KI-Accounts der Mitarbeitenden | Keine Kontrolle, DSGVO-Problem, Schatten-KI |
| Whisperflow und ähnliche Tools | Machen dauerhaft Screenshots des gesamten Bildschirms |

---

## 5. Ausgangslage im Referat IV. 2.1

### Die LUSD als Kernanwendung

Die **LUSD** (Lehrer- und Schülerdatenbank Hessen) ist die zentrale Schulverwaltungslösung für alle Schulen in Hessen. Sie verwaltet Schüler-, Unterrichts- und Leistungsdaten, Lehrereinsätze, Kursbelegungen, Zulassungen für Abschlüsse und liefert Grunddaten für Planung und Statistik.

Die LUSD ist über 20 Jahre gewachsen, wird kontinuierlich weiterentwickelt (3–4 Releases pro Jahr) und befindet sich aktuell im Umbau: Der ursprüngliche Monolith wird schrittweise in Microservices überführt.

**Charakteristika aus Nutzerperspektive:**
- Sehr komplex und für viele Nutzer schwer zugänglich
- Umfangreiche Funktionalität, die in der Breite kaum überblickbar ist
- Hoher Dokumentations- und Erklärungsaufwand bei jeder Änderung

### Wie Weiterentwicklung heute funktioniert

Die Weiterentwicklung der LUSD läuft über **Azure DevOps**. Der Prozess:

1. Mitarbeitende des Referats schreiben **Anwendungsanforderungen (AWA)** in Azure DevOps — strukturierte fachliche Beschreibungen dessen, was die Anwendung künftig können soll. Format und Qualität variieren je nach Team.
2. AWAs dienen als Grundlage für die Entwicklerinnen und Entwickler
3. Pro AWA wird **manuell ein Testfall** erstellt und manuell abgearbeitet
4. Aus umgesetzten AWAs entsteht (manuell) die **Verfahrensdokumentation** — als PDF gespeichert, durch Menschen aktualisiert
5. Aus der Verfahrensdokumentation entstehen (manuell) die **Anwenderhilfen** für Lehrkräfte und Schulleitungen

**Bekannte Schwachstellen im aktuellen Prozess:**

| Problem | Auswirkung |
|---|---|
| Testfälle werden manuell erstellt und abgearbeitet | Sehr fehleranfällig und aufwändig |
| Fehler im Testfall erfordern auch AWA-Anpassung | Hoher Rückkopplungsaufwand |
| Viele Fehler werden durch Testfälle nicht abgedeckt | Qualitätsrisiko bei Releases |
| Verfahrensdoku wird manuell aktualisiert | Verzögerungen, Inkonsistenzen |
| AWA-Format variiert je nach Team | Uneinheitliche Qualität als Entwicklungsgrundlage |
| KI wird im Referat noch nicht eingesetzt | Ungenutztes Effizienzpotenzial |

Ein erheblicher Teil der Referat-Kapazität fließt in diese Prozesskette. Jede AWA-Änderung zieht manuelle Nachpflege in Dokumentation, Testfällen und Hilfen nach sich.

---

## 6. Anwendungsfälle für Referat IV. 2.1

*Entwurf — zur Abstimmung mit Sarah*

### 6.1 AWA-Assistent

**Problem:** AWAs müssen strukturiert, vollständig und entwicklergerecht formuliert sein. Das erfordert Erfahrung und kostet Zeit.

**Lösung:** Ein KI-Agent der auf Basis einer fachlichen Beschreibung eine strukturierte AWA entwirft — inklusive Akzeptanzkriterien, Ausnahmebehandlung und Abgrenzung zu bestehenden Funktionen. Der Mitarbeitende prüft und finalisiert.

**Wissensbasis:** Bestehende AWAs, LUSD-Systemdokumentation, Fachbegriffe

---

### 6.2 Testfall-Generator

**Problem:** Pro AWA wird manuell ein Testfall erstellt und manuell abgearbeitet. Das ist fehleranfällig in beide Richtungen: Fehler im Testfall erfordern auch AWA-Anpassungen, und viele Fehler werden durch die Testfälle gar nicht abgedeckt. Das gefährdet die Release-Qualität.

**Lösung:** Ein KI-Agent der aus einer fertigen AWA systematisch Testfälle generiert — Normalfall, Sonderfall, Fehlerfall, Grenzfall. Die Vollständigkeit ist strukturell höher als bei manueller Erstellung. Grundlage für strukturiertes Testen und perspektivisch für Testautomatisierung.

**Wissensbasis:** AWA, LUSD-Prozessbeschreibungen, bestehende Testfälle als Muster

---

### 6.3 Verfahrensdokumentation-Generator

**Problem:** Nach Umsetzung einer AWA muss die Verfahrensdokumentation manuell aktualisiert werden. Das passiert verzögert oder unvollständig.

**Lösung:** Aus umgesetzten AWAs wird automatisch ein Entwurf der aktualisierten Verfahrensdokumentation erstellt. Ändert sich eine AWA, wird der betroffene Dokumentationsabschnitt automatisch zur Überarbeitung markiert und ein neuer Entwurf vorgeschlagen.

**Wissensbasis:** AWAs, bestehende Verfahrensdokumentation, Dokumentationsstandards

---

### 6.4 Anwenderhilfen-Generator

**Problem:** Anwenderhilfen für Lehrkräfte und Schulleitungen werden manuell aus der Verfahrensdokumentation abgeleitet. Sprache und Detailtiefe sind oft nicht nutzergerecht.

**Lösung:** Aus der Verfahrensdokumentation werden nutzergerechte Hilfen in einfacher Sprache generiert — angepasst an die Zielgruppe (Lehrkraft, Schulleitung, Schulverwaltung). Bei Änderungen automatischer Hinweis auf betroffene Hilfetexte.

**Wissensbasis:** Verfahrensdokumentation, bestehende Anwenderhilfen, Zielgruppenprofil

---

### 6.5 LUSD-Wissensassistent

**Problem:** Die LUSD ist komplex. Viele Fragen zu Funktionen, Prozessen und Abhängigkeiten können nur von wenigen Personen mit tiefem Systemwissen beantwortet werden.

**Lösung:** Ein KI-Assistent der auf Basis der indexierten LUSD-Systemdokumentation, AWAs und Verfahrensdokumentation Fragen beantwortet — intern für das Referat, perspektivisch auch für Schulen.

**Wissensbasis:** LUSD-Dokumentation, AWAs, Verfahrensdokumentation, FAQ

---

### 6.6 Change-Impact-Analyse

**Problem:** Eine neue oder geänderte AWA kann bestehende Funktionen, Dokumentation und Hilfen betreffen. Das wird heute manuell geprüft.

**Lösung:** Beim Eingang einer neuen AWA prüft ein Agent automatisch: Welche bestehenden Funktionen sind betroffen? Welche Dokumentationsabschnitte müssen überarbeitet werden? Welche Testfälle müssen angepasst werden?

**Wissensbasis:** Alle bestehenden AWAs, Verfahrensdokumentation, Funktionsregister

---

### Gesamtbild: Der KI-gestützte AWA-Prozess

```
Fachliche Anforderung (Mensch)
    ↓
[AWA-Assistent] → strukturierte AWA
    ↓
[Testfall-Generator] → Testfälle
    ↓
Entwicklung (Mensch)
    ↓
[Verfahrensdoku-Generator] → aktualisierte Dokumentation
    ↓
[Anwenderhilfen-Generator] → nutzergerechte Hilfen
    ↓
[Änderung einer AWA] → [Change-Impact-Analyse] → automatischer Update-Vorschlag
```

*Offene Fragen zur Konkretisierung: Format bestehender AWAs, Umfang der vorhandenen Dokumentation, Datenschutzeinstufung der LUSD-Inhalte*

---

## 7. Implementierung und Kosten

*Folgt nach Abschluss der Anforderungsanalyse.*

---

## 8. Empfehlung weiteres Vorgehen

1. **Bestandsaufnahme** — Welche KI-Tools werden bereits genutzt (inkl. privat)?
2. **Anforderungsdefinition** — Welche Prozesse und Wissensquellen sollen eingebunden werden?
3. **Marktanalyse** — Welche Anbieter kommen für den öffentlichen Sektor in Frage?
4. **Pilotbetrieb** — Testbetrieb mit einem definierten Anwendungsfall
5. **Ausschreibung** — Auf Basis der definierten Anforderungen

---

*Abschnitte 5, 6 und 7 folgen in Abstimmung mit Sarah*
