# UI-Wording-Regeln — Version 1

**Stand:** 2026-04-01  
**Autor:** Cheko (ILA-Hauptagent)  
**Status:** Entwurf — zur Ergänzung durch Sebastian (Fachlichkeit) und Yves (Design)

---

## Zweck

Dieses Dokument legt fest, welche Sprache in der ILA-Anwendung verwendet wird — und welche nicht.

Es unterscheidet zwischen:
- **Technischer Bezeichnung** (intern, im Code und in Figma)
- **Anwender-Bezeichnung** (sichtbar in der Oberfläche)
- **Fachlicher Bezeichnung** (amtlich/pädagogisch korrekt)

---

## 1. Grundprinzipien

### 1.1 Sprache richtet sich nach der Zielgruppe
Die Anwendung wird von **Lehrkräften im sonderpädagogischen Kontext** genutzt.
Das bedeutet:
- Keine Verwaltungs-Bürokratie-Sprache, wenn es eine einfachere Alternative gibt
- Keine technischen Begriffe in der Oberfläche
- Fachbegriffe nur, wenn sie der Zielgruppe vertraut sind

### 1.2 Konsistenz vor Kreativität
Wenn ein Begriff einmal eingeführt ist, wird er konsequent verwendet.
Synonyme in der Oberfläche vermeiden — sie erzeugen Unsicherheit.

### 1.3 Aktiv statt passiv
- ✅ "Förderziel hinzufügen"
- ❌ "Hinzufügen von Förderzielen"

### 1.4 Kurz und handlungsorientiert
Besonders bei Buttons, Navigationspunkten und Überschriften:
- ✅ "Speichern"
- ❌ "Daten speichern und fortfahren"

---

## 2. Seitennamen — technisch vs. anwenderseitig

| Technischer Name (Figma) | Anwender-sichtbarer Name | Sichtbar? | Hinweise |
|---|---|---|---|
| Startseite | Startseite | ✅ ja | Direkter Begriff, passt |
| Schüler in Förderung | Meine Förderungen | ❓ klären | "Schüler in Förderung" ist intern klar, für Lehrkräfte ggf. zu abstrakt |
| Förderakte | Förderakte | ✅ ja | Amtlicher Begriff — vermutlich bekannt |
| Förderplan | Förderplan | ✅ ja | Amtlicher Begriff — vermutlich bekannt |
| Förderziel | Förderziel | ✅ ja | Amtlicher Begriff |
| Prozess: Neue Förderung | Neue Förderung anlegen | ✅ ja | "Prozess:" intern, nicht sichtbar |
| Prozess: Förderziele hinzufügen | Förderziele hinzufügen | ✅ ja | "Prozess:" intern, nicht sichtbar |
| FAQ | Häufige Fragen | ✅ ja | "FAQ" evtl. nicht für alle Zielgruppen vertraut |
| Nutzerfeedback | Rückmeldung geben | ✅ ja | "Nutzerfeedback" ist interner Begriff |

---

## 3. Komponentennamen — technisch vs. anwenderseitig

| Figma-Komponente | Was es zeigt | Anwender-Begriff | Hinweise |
|---|---|---|---|
| Card Target | Ein Förderziel | Förderziel | Karte ist nur das Container-Konzept |
| Card Skill | Eine Kompetenz | Kompetenz / Fertigkeit | Klären: Heißt es "Kompetenz" oder "Fertigkeit" im Fachkontext? |
| Card Category | Ein Förderbereich | Förderbereich | |
| List-Item Förderung | Eine laufende Förderung | Förderung | |
| List-Item Schüler | Ein Schüler | Schüler / Schülerin | Gendern klären |
| Accordion Item | Aufklappbarer Bereich | — (nicht direkt sichtbar) | |
| Modal Alert | Hinweisfenster | — je nach Inhalt benennen | |
| Modal Dialog | Bestätigungsfenster | — je nach Inhalt benennen | |
| Modal Stepper | Schritt-für-Schritt-Assistent | — je nach Kontext | |
| Modal Wizard | Mehrstufiger Assistent | — je nach Kontext | |
| Slot/User Feedback | Feedback-Formular | Rückmeldung | |
| Evaluation | Bewertung des Förderziels | Evaluation / Einschätzung | Klären: Welcher Begriff ist in der Schule üblich? |
| Notiz | Verlaufsdokumentation einer Maßnahme | "Verlauf" oder "Dokumentation" | ⚠️ **Bekanntes Problem:** "Notiz" zu offen — Pilotteilnehmer haben das Feld uneinheitlich genutzt. Fachlich korrekt: "Dokumentationseintrag". UI-Begriff offen, muss abgestimmt werden. |
| Tag | Markierung / Label | — je nach Kontext | |
| Badge | Status-Kennzeichnung | — je nach Kontext | |
| Snackbar | Kurze Statusmeldung | — nicht direkt sichtbar | |
| Notification | Benachrichtigung | Hinweis / Meldung | |

---

## 4. Aktions-Wording (Buttons, Links, Trigger)

### Grundregeln
- Imperativ (Befehlsform): "Speichern", "Hinzufügen", "Abschließen"
- Keine Passivkonstruktionen
- Maximal 3 Wörter — je kürzer, desto besser
- Keine Abkürzungen

### Häufige Aktionen

| Aktion | ✅ Empfohlen | ❌ Vermeiden |
|---|---|---|
| Datensatz anlegen | "Hinzufügen" / "Anlegen" | "Neu erstellen", "Eingabe starten" |
| Datensatz speichern | "Speichern" | "Daten sichern", "Bestätigen und speichern" |
| Prozess abschließen | "Abschließen" | "Fertigstellen", "Prozess beenden" |
| Schritt weiter | "Weiter" | "Nächster Schritt", "Fortfahren" |
| Schritt zurück | "Zurück" | "Vorheriger Schritt", "Korrigieren" |
| Löschen | "Löschen" | "Entfernen", "Verwerfen" |
| Abbrechen | "Abbrechen" | "Schließen", "Zurück ohne Speichern" |
| Bearbeiten | "Bearbeiten" | "Ändern", "Editieren" |

---

## 5. Überschriften und Seitentitel

### Grundregeln
- Überschriften beschreiben, was der Nutzer **tut** oder **sieht** — nicht was das System tut
- Keine technischen IDs oder internen Bezeichnungen
- Kein Doppelpunkt am Ende von Überschriften

### Beispiele

| Kontext | ✅ Empfohlen | ❌ Vermeiden |
|---|---|---|
| Seite mit Förderziel-Details | "Förderziel" | "Förderziel-Detail", "Card Target View" |
| Prozess Neue Förderung, Schritt 1 | "Schüler auswählen" | "Schritt 1: Schülersuche", "Suche starten" |
| Leerer Zustand (keine Einträge) | "Noch keine Förderziele vorhanden" | "Empty State", "Keine Daten" |
| Fehlermeldung | "Bitte gib einen Wert ein" | "Fehler: Pflichtfeld leer", "Validation Error" |

---

## 6. Statusbezeichnungen (Lebenszyklus Förderziel)

Der Lebenszyklus eines Förderziels hat drei Zustände — sowohl technisch als auch für Anwender:

| Technisch (Figma) | Anwender-sichtbar | Hinweis |
|---|---|---|
| `[in Planung]` | "In Planung" | Passt direkt |
| `[in Durchführung]` | "Aktiv" oder "In Durchführung" | Klären: Ist "in Durchführung" für Lehrkräfte verständlich? |
| `[abgeschlossen]` | "Abgeschlossen" | Passt direkt |

---

## 7. Gendern und Anrede

**Offen — muss mit Sebastian und Sarah geklärt werden:**
- Schüler/Schülerin vs. Schüler:in vs. Lernende:r
- Lehrkraft vs. Lehrer/Lehrerin
- Anrede in Systemnachrichten (du vs. Sie)

---

## 8. Offene Fragen (für Sebastian und Yves)

- [ ] Heißt es "Kompetenz" oder "Fertigkeit" im amtlichen Kontext?
- [ ] Ist "in Durchführung" für Lehrkräfte vertraut, oder besser "Aktiv"?
- [ ] Welche Gendering-Regel gilt im HMKB-Kontext?
- [ ] Heißt es "Evaluation" oder "Einschätzung" in der Schule?
- [ ] Ist "FAQ" für die Zielgruppe verständlich, oder besser "Häufige Fragen"?
- [ ] Wie heißt der Anwender-Begriff für die "Förderakte" — ist das amtlich etabliert?
