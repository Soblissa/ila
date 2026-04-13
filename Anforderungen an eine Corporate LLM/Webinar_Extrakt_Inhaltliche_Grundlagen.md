# Inhaltliche Grundlagen: Corporate LLM
*Quelle: Webinar-Transkript (Everlast AI, April 2026)*
*Extrahiert und strukturiert von: Cheko — nur verwertbare Inhalte, kein Sales-Material*

---

## 1. Marktlage und Ausgangsproblem

### Stand 2026

KI ist in Unternehmen angekommen — aber meist ohne Wirkung:

- Durchschnittliche KI-Nutzung der Mitarbeitenden: **1,5 Stunden pro Woche**
- Ein Viertel der Mitarbeitenden nutzt KI am Arbeitsplatz **überhaupt nicht**
- Nur **14 % der Unternehmen** haben KI wirklich in Kernprozesse integriert
- **86 %** nutzen KI an der Oberfläche (Texte formulieren, zusammenfassen) — ohne messbaren Effekt
- **91 % der Unternehmen** sehen keinen messbaren Produktivitätseffekt durch KI

### Das eigentliche Problem: Schatten-KI

- **77 % der Mitarbeitenden** geben Unternehmensdaten in KI-Tools ein
- **82 % davon** über private, unkontrollierte Accounts
- **65 % der Organisationen** melden unautorisierte KI-Nutzung
- **43 % der Unternehmen** haben keine KI-Nutzungsrichtlinie

**Konsequenz:** Wenn keine gute offizielle Lösung existiert, nutzen Mitarbeitende trotzdem KI — unkontrolliert.

### Die fünf Hauptprobleme ohne Corporate LLM

| # | Problem | Beschreibung |
|---|---|---|
| 1 | **Team nutzt KI nicht** | Geschäftsführung nutzt KI, Mitarbeitende nicht — Potenzial bleibt ungenutzt |
| 2 | **Datenschutz und Schatten-KI** | Unkontrollierter Einsatz privater Accounts mit Unternehmensdaten |
| 3 | **Rechtliche Unsicherheit** | DSGVO-Risiken, fehlende Governance, Angst blockiert Innovation |
| 4 | **Schlechte oder falsche Lösungen** | Insellösungen die niemand nutzt (z.B. Microsoft Copilot: kaum Nutzung, dokumentierte Sicherheitslücken) |
| 5 | **Tool-Wildwuchs** | Ab 4+ Tools sinkt Produktivität durch Informationsüberflutung (BCG-Studie) |

---

## 2. Was ein Corporate LLM ist

**Definition:** Ein Corporate LLM ist kein eigenes KI-Modell. Es ist ein **privater, DSGVO-konformer KI-Arbeitsbereich** für eine Organisation, der auf bestehenden Sprachmodellen aufsetzt und das eigene Organisationswissen als Wissensgrundlage nutzt.

### Kernprinzip

Das System antwortet nicht aus allgemeinem Internetwissen, sondern aus dem **eigenen Wissen der Organisation** — Dokumente, Prozesse, FAQs, interne Standards — die automatisch in jede Anfrage einfließen.

### Abgrenzung zu allgemeinen KI-Tools

| Merkmal | ChatGPT / allgemeine Tools | Corporate LLM |
|---|---|---|
| Wissensgrundlage | Allgemeines Internetwissen | Eigenes Organisationswissen |
| Datenschutz | US-Server, unklare Datenverwendung | EU-Server, DSGVO-konform, kein Training |
| Zugriffsteuerung | Keine | Granular pro Nutzer/Gruppe |
| Integration | Keine | Tief in Prozesse eingebettet |
| Nutzung | Jeder für sich | Zentralisiert für alle |

---

## 3. Technische Architektur

### RAG (Retrieval-Augmented Generation — wissensgestützte Antwortgenerierung)

Das technische Kernprinzip:

1. **Input:** Interne Dokumente (PDF, Word, Excel, Markdown, sogar handschriftliche Scans)
2. **Embedding:** Dokumente werden durch ein Embedding-Modell in **Vektoren** (mathematische Darstellungen) umgewandelt
3. **Speicherung:** Vektoren landen in einer Vektordatenbank
4. **Anfrage:** Nutzer stellt Frage → System durchsucht Vektordatenbank semantisch
5. **Retrieval:** Relevanteste Textpassagen werden extrahiert
6. **Ausgabe:** LLM erhält Frage + extrahierte Passagen als Kontext → antwortet auf Basis des eigenen Wissens

**Vorteil gegenüber einfachem Dokumenten-Upload:** Skaliert auf tausende Seiten, da immer nur der relevante Kontext geladen wird — nicht das gesamte Dokument.

### Unterstützte Dokumentformate

Praktisch alle Formate: PDF, Word, Excel, Markdown, JSON, Textdateien, handschriftliche PDF-Scans (via OCR-Umwandlung in Markdown).

---

## 4. Funktionsmodule eines Corporate LLM

### 4.1 Modellauswahl und Auto-Select

- Zugang zu mehreren Modellen (OpenAI, Anthropic, Google Gemini, Mistral) über eine Oberfläche
- **Auto-Select:** System analysiert den Prompt und leitet automatisch zum geeignetsten Modell weiter — wirtschaftlich und qualitätsorientiert
- DSGVO-Konformität über AVV (Auftragsverarbeitungsvertrag) mit allen Anbietern, EU-Hosting

### 4.2 Wissensdatenbank (interne Suche)

- Ordnerstruktur pro Bereich (z.B. Geschäftsführung, HR, Fachbereiche)
- Aktivierbare Wissenssuche pro Anfrage
- Quellenangabe bei Antworten (welches Dokument, welcher Abschnitt)
- Skaliert auf organisationsweites Wissen

### 4.3 Agenten

Ein **Agent** ist mehr als ein KI-Modell mit Persona. Vollständig konfigurierbar:

| Konfigurationselement | Beschreibung |
|---|---|
| System-Prompt | Grundanweisung und Rolle des Agenten |
| Begrüßungsnachricht | Selbstvorstellung des Agenten |
| Prompt-Beispiele | Vorschläge für häufige Anfragen |
| Wissenszugriff | Welche Teile der Wissensdatenbank darf der Agent nutzen? |
| Skills | Spezialfähigkeiten (z.B. PDF-Generierung, Python-Code, Websuche) |
| Modell | Welches Sprachmodell wird verwendet? |
| Temperature | Wie deterministisch/kreativ sollen Antworten sein? |

**Stärke:** Kombination aus Agentic Framework + Skills + internem Wissen = qualitativ hochwertige, kontextspezifische Ausgaben.

### 4.4 Prompt- und Skill-Bibliothek

- Zentrale Sammlung aller Prompts und Skills — kein Chaos mit Links, Docs oder GitHub
- Kategorisierbar nach Bereichen (HR, Fachbereich, Verwaltung etc.)
- **Prompt-Templates mit Variablen:** Nutzer füllt nur noch Variablen aus, kein eigenes Prompt-Engineering nötig
- Beispiel: Template "Tagesbericht" → Nutzer gibt Felder ein → fertiger formatierter Bericht

### 4.5 Spaces (Arbeitsbereiche pro Abteilung)

- Dedizierte Arbeitsbereiche pro Abteilung oder Thema
- Jeder Space hat nur Zugriff auf das relevante Wissen → reduziert "Rauschen"
- **Bewertungsfunktion:** System bewertet den eigenen Wissenskontext und zeigt Lücken auf (z.B. fehlende Styleguides, unvollständige Prozessbeschreibungen)

### 4.6 Berechtigungsmanagement

- Zugriffssteuerung auf Gruppenebene
- Pro Gruppe konfigurierbar: Agenten / Spaces / Prompts / Skills / Dateien
- Verhindert ungewollten Zugriff auf sensible Bereiche (z.B. Geschäftsführungsunterlagen für alle sichtbar)

### 4.7 Bildgenerierung (Atelier)

- Dedizierte Oberfläche für Bild- (und perspektivisch Video-) Generierung
- Prompt-Optimierung durch KI
- Negativprompt (was soll nicht erscheinen)
- Referenzbild-Funktion für Variationen

### 4.8 Spracheingabe (ergänzend)

- Sprache statt Tippen: 150–200 Wörter/Minute gesprochen vs. 40–50 getippt
- App-Kontext wird erkannt → automatisch formatierte Ausgabe (Mail-Format in Gmail, Bullet-Points in Docs)
- **Datenschutzproblem bekannter Tools:** Manche Tools (z.B. Whisperflow) machen dauerhaft Screenshots des gesamten Bildschirms → im Behördenkontext nicht vertretbar
- Anforderung: EU-Hosting, keine Screenshots, DSGVO-konform

---

## 5. Implementierungsansatz

### Erfolgsfaktoren

1. **Wissen explizit machen:** Implizites Organisationswissen muss dokumentiert und strukturiert werden, bevor es indexiert werden kann
2. **Goldstandard-Dokumente:** Saubere, gut strukturierte Quelldokumente liefern bessere Ergebnisse
3. **Schrittweise einführen:** Mit einem Anwendungsfall starten, nicht mit allem auf einmal
4. **Mitarbeitende einbinden:** System muss besser sein als Schatten-KI — sonst nutzen Mitarbeitende weiter private Accounts
5. **Governance etablieren:** Richtlinie zur KI-Nutzung, klare Regeln wer was darf

### Empfohlene Einführungsreihenfolge

1. Bestandsaufnahme (welche KI-Tools werden bereits genutzt, auch privat)
2. Anforderungen definieren (welche Prozesse, welche Fachbereiche)
3. Wissen aufbereiten (relevante Dokumente, Prozessbeschreibungen)
4. Pilotbetrieb mit einem Anwendungsfall
5. Schrittweise ausweiten

---

## 6. Datenschutz-Checkliste (technische Mindestanforderungen)

| Anforderung | Beschreibung |
|---|---|
| EU-Hosting | Alle Daten ausschließlich auf europäischen Servern |
| AVV | Auftragsverarbeitungsvertrag mit allen KI-Anbietern (Art. 28 DSGVO) |
| Kein Modelltraining | Eingaben dürfen nicht für Modellverbesserung verwendet werden |
| Zugriffsprotokollierung | Alle Zugriffe nachvollziehbar und auditierbar |
| Löschkonzept | Vollständige Datenlöschung auf Anfrage möglich |
| Rollenbasierte Rechtevergabe | Granulare Steuerung wer was sehen und nutzen darf |
| Keine Screenshots | Spracheingabe-Tools dürfen keine Screenshots erstellen |

---

*Dieses Dokument enthält ausschließlich übertragbare Fachinhalte aus dem Webinar. Produktnamen, Preisangaben und Sales-Inhalte wurden weggelassen.*
