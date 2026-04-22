# Anforderungsbeschreibung: Kalender, Erinnerung, Aufgaben
*ILA / diSAF — Funktionsbereich Zeitplanung & Aufgabenmanagement*
*Erstellt: 2026-04-21 | Autor: Cheko (ILA-Hauptagent)*

---

## 1. Überblick

Dieser Funktionsbereich ergänzt das Kernmodul (individuelle und sonderpädagogische Förderung) um zeitbezogene Unterstützung für Lehrkräfte. Ziel ist es, förderrelevante Termine, Fristen und Aufgaben direkt im System verwaltbar zu machen — ohne Medienbruch zu externen Kalender-Apps.

---

## 2. Kalender

### 2.1 Grundfunktionen (Basics)

- **Termin anlegen**: Titel, Datum, Uhrzeit, Ort (optional), Beschreibung (optional)
- **Termin bearbeiten und löschen**
- **Einladen**: andere Lehrkräfte oder Unterstützer (z.B. BFZ-Lehrkraft, Eltern) zu einem Termin einladen
- **Ansichten**: Tagesansicht, Wochenansicht, Monatsansicht
- **Navigation**: vor/zurück, Sprung auf "Heute"
- **Termin-Typen**: unterscheidbar nach Kategorie (z.B. Elterngespräch, Förderstunde, Konferenz, Frist)

### 2.2 Fachspezifische Anforderungen

- **Verknüpfung mit Förderung**: Termin kann einem Schüler und/oder einer laufenden Förderung zugeordnet werden
- **Wiederholende Termine**: z.B. "wöchentliche Leseförderung, dienstags" als Serie anlegen
- **Schuljahresrahmen**: Schulferien und Zeugnistermine als hinterlegter Rahmenkalender (schulspezifisch konfigurierbar)
- **Fälligkeiten aus Förderung**: Evaluationstermine werden automatisch als Kalendereinträge erzeugt, wenn ein Förderziel angelegt wird

---

## 3. Erinnerungen

### 3.1 Grundfunktionen (Basics)

- **Erinnerung zu Terminen**: konfigurierbar (z.B. 1 Tag vorher, 1 Stunde vorher)
- **Anzeige auf der Startseite**: aktuelle und anstehende Erinnerungen als sichtbarer Block / Badge beim App-Start
- **Push-Notification** (sofern technisch verfügbar) oder In-App-Hinweis
- **Erinnerung als gelesen markieren / wegklicken**
- **Erinnerung wiederholen**: "Erinnere mich morgen nochmal"

### 3.2 Fachspezifische Anforderungen

- **Automatische Fälligkeits-Erinnerungen**: Das System erinnert automatisch, wenn…
  - eine Evaluation eines Förderziels fällig ist
  - ein Nachteilsausgleich ausläuft
  - eine BSLRR-Frist abläuft
  - ein Förderplan-Druck noch aussteht
- **Konfigurierbar**: Vorlaufzeit pro Erinnerungstyp einstellbar (Standard-Vorschlag wird mitgeliefert)
- **Rollenbezug**: Erinnerungen sind personalisiert — jede Lehrkraft sieht nur ihre eigenen

---

## 4. Aufgaben

### 4.1 Grundfunktionen (Basics)

- **Aufgabe anlegen**: Titel, Beschreibung (optional), Fälligkeitsdatum (optional)
- **Aufgabe bearbeiten und löschen**
- **Status**: offen → in Bearbeitung → erledigt
- **Aufgaben-Liste**: gefiltert nach Status, nach Schüler, nach Fälligkeitsdatum
- **Aufgabe als erledigt markieren** (mit einem Klick)

### 4.2 Fachspezifische Anforderungen

- **Verknüpfung mit Schüler oder Förderung**: Aufgabe kann direkt an einem Schüler oder einem konkreten Förderziel hängen
- **Zuweisung an Kollegin/Kollegen**: Aufgabe kann einer anderen Lehrkraft zugewiesen werden (passt zum gewünschten kollegialen Austausch)
- **Typische Aufgaben-Vorlagen** (optional, als Schnellauswahl):
  - Elterngespräch führen
  - Kollegin informieren
  - BFZ kontaktieren
  - Nachteilsausgleich beantragen
  - Evaluation durchführen

---

## 5. Integration & Querverbindungen

| Ausgangspunkt | Erzeugt automatisch |
|---|---|
| Förderziel angelegt | Evaluationstermin im Kalender |
| Nachteilsausgleich gesetzt | Fristenhinweis als Erinnerung |
| Aufgabe zugewiesen | Benachrichtigung an zugewiesene Lehrkraft |
| Termin heute | Anzeige auf Startseite |

---

## 6. Nicht in Scope (bewusste Abgrenzung)

- Keine Synchronisation mit externen Kalender-Apps (Outlook, Google Calendar) — in dieser Version
- Kein schülerübergreifender Redaktionskalender / Schulkalender als Planungswerkzeug
- Keine Eltern-Kommunikationsfunktion über den Kalender

---

## 7. Offene Fragen

- Sollen Erinnerungen auch per E-Mail verschickt werden können?
- Wie werden Vertretungen abgebildet — übernimmt die Vertretungslehrkraft auch die Erinnerungen?
- Wer pflegt den Schuljahresrahmen (Ferien, Zeugnistermine) — Schuladmin oder zentral?

---

## 8. Anbindung an externe Kalender- und E-Mail-Accounts

### 8.1 Kalender-Anbindung

Standard-Protokoll für Kalender-Integration ist **CalDAV / iCal** — kompatibel mit Outlook, Google Calendar und Apple Calendar.

**Variante 1 — iCal-Feed (empfohlen für erste Ausbaustufe)**
- ILA stellt einen iCal-Feed bereit (read-only)
- Lehrkraft abonniert diesen Feed in ihrem eigenen Kalender-Client
- Einfach umzusetzen, keine Schreibrechte auf externe Systeme nötig
- Datenschutzfreundlich steuerbar (siehe 8.3)

**Variante 2 — Bidirektionale Sync via CalDAV**
- ILA und externer Kalender synchronisieren in beide Richtungen
- Änderungen von beiden Seiten möglich
- Höherer Implementierungsaufwand, mehr Fehlerquellen
- Empfehlung: erst in einer späteren Ausbaustufe prüfen

### 8.2 E-Mail-Anbindung

- **Erinnerungen per E-Mail**: Technisch einfach — SMTP-Versand an eine hinterlegte Adresse pro Nutzerin, keine tiefere Integration nötig
- **Erweiterte Mail-Integration** (Inbox lesen, Aufgaben aus Mails erzeugen o.ä.): Nicht empfohlen — zu hoher Aufwand, zu hohes Datenschutzrisiko im Schulkontext

### 8.3 Datenschutz-Hinweis (kritisch im Schulkontext)

Sobald Schülerdaten in externe Dienste fließen (Google, Apple, Microsoft), ist eine **Auftragsverarbeitungsvereinbarung (AVV)** mit dem jeweiligen Anbieter erforderlich — und in der Regel schulrechtlich zu genehmigen.

**Empfehlung**: iCal-Feed nur mit abstrakten Termintiteln befüllen (z.B. "Evaluation fällig" statt "Evaluation Max Mustermann") — damit sind keine personenbezogenen Daten im externen Kalender, die AVV-Pflicht entfällt.

Diese Entscheidung sollte mit dem Datenschutzbeauftragten der Schule bzw. des Schulträgers abgestimmt werden.

---
*Dokument-Status: Entwurf — zur Abstimmung mit Sarah*
