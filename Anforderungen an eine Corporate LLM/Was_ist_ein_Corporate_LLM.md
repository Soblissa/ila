# Anforderungen an eine Corporate LLM
## für das Referat VI 3.1 des HMKB

*Erstellt: 2026-04-12 | Analysiert von: Cheko (ILA-Hauptagent)*
*Grundlage: Fachliche Recherche und eigene Einordnung*
*Status: Entwurf - Anwendungsfälle folgen in Abstimmung mit Sarah*

---

## 1. Was ist ein Corporate LLM?

Ein Corporate LLM (Corporate Large Language Model - unternehmenseigenes großes Sprachmodell) ist **kein eigenes KI-Modell**, das von Grund auf neu trainiert wird. Es ist ein **privater, datenschutzkonformer KI-Arbeitsbereich für eine Organisation**, der auf bestehenden Sprachmodellen (z. B. von Anthropic, OpenAI, Google oder europäischen Anbietern wie Mistral) aufsetzt.

### Was ein Corporate LLM ausmacht

| Merkmal | Erklärung |
|---|---|
| **Zentraler Zugang** | Alle Mitarbeitenden arbeiten über eine einzige Oberfläche mit KI - kein Tool-Wildwuchs, keine Schatten-Systeme |
| **Firmenwissen integriert** | Interne Dokumente, Prozesse, Produkte, FAQs fließen automatisch in jede Anfrage ein |
| **Rollenbasierte Zugriffssteuerung** | Wer darf welches Wissen sehen? Wer darf welche KI-Funktionen nutzen? Alles zentral steuerbar |
| **Datenschutzkonform** | Betrieb auf europäischen Servern, DSGVO-konforme Verarbeitung, keine Weitergabe an KI-Anbieter für Trainingszwecke |
| **Mehrere Modelle, eine Oberfläche** | Wechsel zwischen Modellen je nach Aufgabe - ohne separate Accounts oder Tools |
| **Agentenstruktur möglich** | Spezialisierte KI-Assistenten für einzelne Abteilungen oder Prozesse |

### Wie das Firmenwissen technisch funktioniert (RAG)

Interne Dokumente (PDFs, Word, Excel, Markdown) werden in sogenannte **Vektoren** (mathematische Darstellungen von Textinhalten) umgewandelt und in einer Datenbank gespeichert. Stellt eine Nutzerin eine Frage, durchsucht das System automatisch diese Vektordatenbank, zieht die relevantesten Textpassagen heraus und gibt sie als Kontext an das Sprachmodell weiter. Das Modell antwortet dann nicht aus allgemeinem Internetwissen, sondern auf Basis des eigenen Firmenwissens.

Dieser Ansatz heißt **RAG** (Retrieval-Augmented Generation - wissensgestützte Antwortgenerierung) und ist der technische Kern jedes Corporate LLM.

---

## 2. Warum kein Corporate LLM ein Problem ist

### 2.1 Schatten-KI — das unterschätzte Risiko

Wenn keine offizielle, datenschutzkonforme Lösung bereitgestellt wird, nutzen Mitarbeitende trotzdem KI — unkontrolliert. Vertrauliche Daten, interne Prozesse und personenbezogene Informationen landen dann in fremden Systemen, häufig auf US-amerikanischen Servern, ohne Rechtsgrundlage und ohne Wissen der Organisation.

Ein bekanntes Beispiel: Samsung musste 2023 KI intern komplett verbieten, nachdem Mitarbeitende Quellcode und Produktionsdaten in ChatGPT eingegeben hatten. Das Problem hat sich seitdem nicht verbessert, sondern verstärkt.

### 2.2 Datenschutzrechtliche Konsequenzen

Unkontrollierte KI-Nutzung mit Unternehmensdaten ist eine **DSGVO-relevante Datenverarbeitung**. Mögliche Konsequenzen:

- Bußgelder bis zu 20 Millionen Euro oder 4 % des weltweiten Jahresumsatzes
- Verlust des Vertrauens von Kunden und Partnern
- Haftungsrisiken für Führungskräfte

### 2.3 Produktivitätsverlust durch Tool-Wildwuchs

Ohne zentralen Rahmen entstehen Insellösungen, die nicht miteinander kommunizieren. Doppelarbeit bei Prompts und Wissen, unkontrollierte Qualitätsschwankungen und Überforderung durch zu viele parallele Tools sind die typischen Folgen.

### 2.4 Fehlende Wirksamkeit ohne Einbettung in Prozesse

KI-Tools werden häufig nur an der Oberfläche genutzt (E-Mails formulieren, Texte zusammenfassen) — ohne messbaren Effekt auf die eigentliche Arbeit. Ein Corporate LLM schafft erst die Grundlage für echten, nachhaltigen Nutzen, weil es Firmenwissen und Prozesse direkt einbettet.

---

## 3. Datenschutz und rechtliche Anforderungen

### 3.1 Grundanforderungen

Ein Corporate LLM im öffentlichen Sektor (und damit auch im HMKB) muss folgende Anforderungen erfüllen:

- **EU-Hosting**: Alle Daten werden ausschließlich auf europäischen Servern verarbeitet
- **Auftragsverarbeitungsvertrag (AVV)**: Mit jedem eingesetzten KI-Anbieter muss ein AVV nach Art. 28 DSGVO geschlossen sein
- **Keine Nutzung für Modelltraining**: Eingaben dürfen nicht zur Verbesserung der KI-Modelle verwendet werden
- **Rollenbasierte Zugriffssteuerung**: Wer sieht welche Daten? Berechtigungen müssen granular steuerbar sein
- **Protokollierung**: Nutzung muss nachvollziehbar und auditierbar sein
- **Löschkonzept**: Daten müssen auf Anfrage vollständig gelöscht werden können

### 3.2 Besonderheiten im öffentlichen Sektor

Im Bereich Schulverwaltung und Bildung kommen zusätzliche Anforderungen hinzu:

- **Personenbezogene Daten von Minderjährigen** erfordern besondere Schutzmaßnahmen
- **Dienstgeheimnisse und Amtsverschwiegenheit** müssen technisch abgesichert sein
- **Hessisches Datenschutzgesetz (HDSIG)** gilt ergänzend zur DSGVO
- Ggf. **Mitbestimmungsrechte** des Personalrats bei Einführung neuer IT-Systeme

### 3.3 Abgrenzung: Was ein C-LLM nicht ist

| Nicht geeignet | Warum |
|---|---|
| ChatGPT (Standard-Account) | US-Server, kein AVV, Training mit Eingaben möglich |
| Microsoft Copilot (Standard) | Sicherheitslücken dokumentiert, kein messbarer Nutzennachweis |
| Whisperflow und ähnliche | Macht Screenshots vom gesamten System, keine Transparenz über Datenweitergabe |
| Private KI-Accounts der Mitarbeitenden | Keine Kontrolle, DSGVO-Problem, Schatten-KI |

---

## 4. Technische Kernfunktionen eines Corporate LLM

### 4.1 Wissensdatenbank (RAG)
Interne Dokumente werden indexiert und stehen als Wissensquelle zur Verfügung. Antworten basieren auf dem eigenen Firmenwissen, nicht auf allgemeinem Internetwissen.

### 4.2 Agenten
Spezialisierte KI-Assistenten für definierte Aufgaben (z. B. Förderplan-Assistent, Sachbearbeitungs-Assistent). Können auf Teilmengen des Wissens, bestimmte Modelle und spezifische Fähigkeiten (Skills) beschränkt werden.

### 4.3 Prompt-Bibliothek
Zentrale Sammlung bewährter Arbeitsanweisungen (Prompts) für wiederkehrende Aufgaben. Mitarbeitende müssen keine eigenen Prompts formulieren - sie wählen aus vorgefertigten Vorlagen.

### 4.4 Berechtigungsmanagement
Zugriffssteuerung auf Gruppenebene: Wer darf welche Agenten, welches Wissen, welche Modelle nutzen? Abteilungsbezogene Spaces (Arbeitsbereiche) möglich.

### 4.5 Mehrmodell-Unterstützung
Zugang zu verschiedenen KI-Modellen (Claude, GPT, Gemini, Mistral) über eine einzige Oberfläche. Automatische Weiterleitung an das geeignetste Modell je nach Aufgabentyp möglich.

### 4.6 Spracheingabe (optional)
Gesprochene Eingaben werden in kontextgerechten Text umgewandelt (Transkription). Besonders wertvoll für Protokolle, Berichte und Notizen nach Gesprächen — spart Tippzeit und senkt die Hemmschwelle zur Nutzung. Wichtig: Nur DSGVO-konforme Lösungen mit EU-Hosting einsetzen. Einige bekannte Tools dieser Art (z. B. Whisperflow) machen dauerhaft Screenshots des gesamten Bildschirms — das ist im Behördenkontext nicht vertretbar.

---

## 5. Ausgangslage im Referat VI 3.1

*Dieser Abschnitt wird gemeinsam mit Sarah ausgearbeitet.*

Folgende Fragen sind zu klären:

- Welche Aufgaben im Referat sind besonders zeitintensiv und wiederkehrend?
- Welche internen Wissensquellen (Erlasse, Handreichungen, Prozessbeschreibungen) könnten indexiert werden?
- Welche Mitarbeitenden nutzen bereits KI - und wie?
- Gibt es bereits eine KI-Nutzungsrichtlinie im HMKB?
- Welche Datenschutzvorgaben gelten konkret für das Referat?

---

## 6. Anwendungsfälle für Referat VI 3.1

*Folgt nach Abstimmung mit Sarah - dieser Abschnitt wird gemeinsam entwickelt.*

---

## 7. Empfehlung für das weitere Vorgehen

1. **Bestandsaufnahme** - Welche KI-Tools werden im Referat bereits genutzt? (inkl. private Accounts)
2. **Anforderungsdefinition** - Welche Prozesse sollen durch ein C-LLM unterstützt werden?
3. **Marktanalyse** - Welche Anbieter kommen für den öffentlichen Sektor in Frage?
4. **Pilotbetrieb** - Kleiner Testbetrieb mit definierten Anwendungsfällen vor Volleinführung
5. **Ausschreibung** - Auf Basis der definierten Anforderungen

---

*Nächste Schritte: Abschnitte 5 und 6 gemeinsam mit Sarah ausarbeiten*
*Erstellt mit: Cheko (ILA-Hauptagent) | Grundlage: Webinar-Transkript + eigene fachliche Einordnung*
