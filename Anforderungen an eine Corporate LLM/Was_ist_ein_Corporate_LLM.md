# Anforderungen an eine Corporate LLM
## für das Referat IV. 2.1 des HMKB

*Erstellt: 2026-04-12 | Status: Entwurf*

---

## 1. Was ist ein Corporate LLM?

Ein Corporate LLM (Corporate Large Language Model — unternehmenseigenes großes Sprachmodell) ist kein eigenes KI-Modell, das von Grund auf neu trainiert wird. Es ist ein **privater, datenschutzkonformer KI-Arbeitsbereich für eine Organisation**, der auf bestehenden Sprachmodellen (z. B. von Anthropic, OpenAI oder europäischen Anbietern wie Mistral) aufsetzt.

Der entscheidende Unterschied zu allgemeinen KI-Tools: Das System antwortet nicht aus allgemeinem Internetwissen, sondern aus dem **eigenen Wissen der Organisation** — Erlasse, Prozessbeschreibungen, Handreichungen, häufige Fragen, interne Standards. Dieses Wissen wird indexiert und fließt automatisch in jede Anfrage ein.

| Merkmal | Bedeutung |
|---|---|
| Zentraler Zugang | Alle Mitarbeitenden arbeiten über eine einzige Oberfläche — kein Tool-Wildwuchs |
| Behördenwissen integriert | Interne Dokumente, Prozesse, Erlasse als Wissensgrundlage |
| Rollenbasierte Zugriffssteuerung | Wer darf was sehen und nutzen? Zentral steuerbar |
| Datenschutzkonform | EU-Hosting, DSGVO-konforme Verarbeitung, kein Training mit Behördendaten |
| Abteilungsspezifische Assistenten | Spezialisierte KI-Helfer für definierte Aufgaben möglich |

---

## 2. Warum kein Corporate LLM ein Problem ist

### Schatten-KI

Wenn keine offizielle Lösung bereitgestellt wird, nutzen Mitarbeitende trotzdem KI — unkontrolliert. Vertrauliche Daten, interne Prozesse und personenbezogene Informationen landen dann in fremden Systemen, häufig auf US-amerikanischen Servern, ohne Rechtsgrundlage und ohne Wissen der Behörde.

Bekanntes Beispiel: Samsung musste 2023 KI intern komplett verbieten, nachdem Mitarbeitende Quellcode und Produktionsdaten in ChatGPT eingegeben hatten.

### Datenschutzrechtliche Konsequenzen

Unkontrollierte KI-Nutzung mit Behördendaten ist eine DSGVO-relevante Datenverarbeitung. Mögliche Konsequenzen: Bußgelder bis zu 20 Millionen Euro, Haftungsrisiken, Vertrauensverlust.

### Fehlende Wirksamkeit

Ohne Einbettung in Prozesse und behördenspezifisches Wissen bleibt KI-Nutzung an der Oberfläche — E-Mails formulieren, Texte zusammenfassen. Messbarer Nutzen für die eigentliche Facharbeit entsteht erst, wenn das Systemwissen der Behörde integriert ist.

---

## 3. Datenschutz und rechtliche Anforderungen

Ein Corporate LLM im öffentlichen Sektor muss folgende Anforderungen erfüllen:

- **EU-Hosting:** Alle Daten werden ausschließlich auf europäischen Servern verarbeitet
- **Auftragsverarbeitungsvertrag (AVV):** Mit jedem KI-Anbieter nach Art. 28 DSGVO
- **Kein Modelltraining:** Eingaben dürfen nicht zur Verbesserung der Modelle verwendet werden
- **Granulare Zugriffssteuerung:** Berechtigungen auf Nutzer- und Gruppenebene
- **Protokollierung:** Nutzung nachvollziehbar und auditierbar
- **Löschkonzept:** Vollständige Datenlöschung auf Anfrage möglich

Zusätzlich im HMKB-Kontext:

- Personenbezogene Daten von Minderjährigen erfordern besondere Schutzmaßnahmen
- Dienstgeheimnisse und Amtsverschwiegenheit müssen technisch abgesichert sein
- Hessisches Datenschutzgesetz (HDSIG) gilt ergänzend zur DSGVO
- Mitbestimmungsrechte des Personalrats bei Einführung sind zu beachten

**Nicht geeignet für den Behördenkontext:**

| Tool | Problem |
|---|---|
| ChatGPT (Standard) | US-Server, kein AVV, mögliches Modelltraining |
| Microsoft Copilot (Standard) | Dokumentierte Sicherheitslücken |
| Private KI-Accounts der Mitarbeitenden | Keine Kontrolle, DSGVO-Problem |
| Whisperflow und ähnliche Spracheingabe-Tools | Machen dauerhaft Screenshots des gesamten Bildschirms |

---

## 4. Ausgangslage im Referat IV. 2.1

*Wird gemeinsam mit Sarah ausgearbeitet.*

Offene Fragen:

- Welche Aufgaben sind besonders zeitintensiv und wiederkehrend?
- Welche internen Wissensquellen (Erlasse, Handreichungen, Prozessbeschreibungen) könnten indexiert werden?
- Welche Mitarbeitenden nutzen bereits KI — und wie?
- Gibt es eine KI-Nutzungsrichtlinie im HMKB?

---

## 5. Anwendungsfälle für Referat IV. 2.1

*Folgt nach Abstimmung mit Sarah.*

---

## 6. Empfehlung weiteres Vorgehen

1. Bestandsaufnahme — Welche KI-Tools werden bereits genutzt?
2. Anforderungsdefinition — Welche Prozesse sollen unterstützt werden?
3. Marktanalyse — Welche Anbieter kommen für den öffentlichen Sektor in Frage?
4. Pilotbetrieb — Testbetrieb mit definierten Anwendungsfällen
5. Ausschreibung — Auf Basis der definierten Anforderungen

---

*Nächste Schritte: Abschnitte 4 und 5 gemeinsam mit Sarah ausarbeiten*
