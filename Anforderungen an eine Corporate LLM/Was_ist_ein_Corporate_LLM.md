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

*Wird gemeinsam mit Sarah ausgearbeitet.*

Offene Fragen:

- Welche Aufgaben sind besonders zeitintensiv und wiederkehrend?
- Welche internen Wissensquellen (Erlasse, Handreichungen, Prozessbeschreibungen) könnten indexiert werden?
- Welche Mitarbeitenden nutzen bereits KI — und wie (auch privat)?
- Gibt es eine KI-Nutzungsrichtlinie im HMKB?
- Welche Datenschutzvorgaben gelten konkret für das Referat?

---

## 6. Anwendungsfälle für Referat IV. 2.1

*Folgt nach Abstimmung mit Sarah.*

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
