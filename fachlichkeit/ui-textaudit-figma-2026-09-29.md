# UI-Textaudit Figma Design Specs

**Stand:** 2026-09-29
**Quelle:** Figma-Arbeitskopie `ila _ Design Specs`
**Datei-Key:** `mGVoWdSLQzFABJlEzOQPRn`
**Status:** Prüflauf abgeschlossen, Vorschläge noch nicht in Figma umgesetzt

## 1. Auftrag und Umfang

Geprüft wurden die Texte aller 34 Seiten der Figma-Arbeitskopie. Für die sprachliche Bewertung wurden die 15 funktionalen Seiten mit dem Präfix `📐` herangezogen. Interne Komponenten-, Ebenen- und Seitennamen sind nicht Teil des Wordings.

Der automatisierte Prüflauf hat auf den funktionalen Seiten erfasst:

- 80.254 Vorkommen von Textebenen einschließlich wiederverwendeter Komponenteninstanzen
- 1.243 unterschiedliche Texte nach Vereinheitlichung von Leerzeichen und Zeilenumbrüchen
- 87 unterschiedliche Texte mit direkter Sie-Ansprache
- 69 unterschiedliche Texte mit Ich-, Mein- oder Wir-Perspektive
- keine direkte Du-Ansprache
- 25 unterschiedliche Platzhalter- oder Blindtexte

Die hohen Vorkommenszahlen entstehen vor allem durch wiederverwendete Komponenten und Varianten. Für die Überarbeitung zählt daher der unterschiedliche Ausgangstext, nicht jede einzelne Instanz.

## 2. Verbindliches Prüfraster

| Situation | Perspektive | Beispiel |
|---|---|---|
| Persönliche Begrüßung | personalisiert | `Willkommen, [Nutzername]!` |
| Persönlicher Arbeitsbereich oder eigene Entität | Besitz aus Nutzersicht | `Mein Schüler`, `Meine Schüler`, `Meine Förderakten` |
| Handlungsanweisung oder Prozessfrage | direkte Sie-Ansprache | `Wählen Sie einen Förderbereich aus.` |
| Hilfe- oder FAQ-Frage | Ich-Perspektive zulässig | `Wie erstelle ich einen Förderplan?` |
| Persönliche Erklärung, Bestätigung oder Einwilligung | Ich-Perspektive | `Ich habe die Eltern informiert.` |
| Von der Lehrkraft verfasster Beispielinhalt | Ich-Perspektive zulässig | Freitext der Lehrkraft wird nicht redaktionell vereinheitlicht |
| Status-, Erfolgs- oder Fehlermeldung | neutrale Systemperspektive | `Der Förderplan wurde gespeichert.` |
| Redaktionelle Bitte des Produktteams | Wir-Perspektive ausnahmsweise zulässig | `Helfen Sie uns, die Anwendung zu verbessern.` |
| Schaltfläche | kurze Handlung ohne Anrede | `Speichern`, `Weiter`, `Später` |

## 3. Wichtigste Inkonsistenzen

### 3.1 Prozessfragen wechseln unnötig in die Ich-Perspektive

FAQ-Fragen dürfen die Frage der Nutzerin oder des Nutzers in der Ich-Perspektive wiedergeben. In geführten Prozessen soll die Anwendung dagegen direkt und konsequent mit „Sie“ ansprechen.

| Seite | Ist-Text | Vorschlag |
|---|---|---|
| Prozess: Förderakte anlegen | `Was möchte ich für Ellen Hannak tun?` | `Was möchten Sie für Ellen Hannak tun?` |
| Prozess: Förderakte anlegen | `Für wen möchte ich eine Förderakte anlegen?` | `Für wen möchten Sie eine Förderakte anlegen?` |
| Prozess: Förderziele hinzufügen | `In welchem Bereich möchte ich Ellen fördern?` | `In welchem Bereich möchten Sie Ellen fördern?` |
| Prozess: BSLRR | `Sind meine Angaben zu Anna vollständig?` | `Sind Ihre Angaben zu Anna vollständig?` |
| Prozess: BSLRR | `Welche bisherige Förderungen von Anna kann ich dokumentieren?` | `Welche bisherigen Förderungen von Anna möchten Sie dokumentieren?` |
| Förderziel | `Wie bewerte ich Ellens Fortschritt?` | `Wie bewerten Sie Ellens Fortschritt?` |
| Förderziel | `Wie begründe ich meine Bewertung für Ellen?` | `Wie begründen Sie Ihre Bewertung für Ellen?` |
| Prozess: Kenntnisgabe | `Wem habe ich den Förderplan für Ellen zur Kenntnis gegeben?` | `Wem haben Sie den Förderplan für Ellen zur Kenntnis gegeben?` |
| Meine Startseite | `Nein, mache ich später.` | `Später` oder `Nicht jetzt` |

### 3.2 „Meine …“ wird zu breit verwendet

Die Besitzperspektive ist für persönliche Bereiche und eigene Entitäten sinnvoll. Bei Feldbezeichnungen und fachlichen Inhalten ist die neutrale Bezeichnung kürzer und konsistenter.

| Ist-Text | Vorschlag |
|---|---|
| `Meine Notiz` | `Notiz` |
| `Meine Ergebnis` | `Ergebnis`; zusätzlich Grammatikfehler beheben |
| `Meine Begründung` | `Begründung` |
| `Meine Auswahl` | `Auswahl` |
| `Meine Dokumentation` | `Dokumentation` |
| `Meine Beschreibung der bisherigen Lernausgangslage von Anna` | `Bisherige Lernausgangslage von Anna` |

Bewusst erhalten bleiben sollen unter anderem `Meine Startseite`, `Meine Schüler`, `Meine Förderakten` und `Meine zuletzt bearbeiteten Förderakten`.

### 3.3 Systemmeldungen sprechen mit „wir“

Ein technisches System sollte bei Ergebnissen und Fehlern keine menschliche Absenderrolle behaupten. Die Wir-Perspektive bleibt nur bei klar redaktionellen Texten des Produktteams zulässig.

| Seite | Ist-Text | Vorschlag |
|---|---|---|
| Förderplan/Förderakte/Navigation | `Wir haben keine Förderziele für Ellen gefunden.` | `Für Ellen wurden keine Förderziele gefunden.` |
| Förderplan | `Wir können kein PDF erstellen.` | `Das PDF konnte nicht erstellt werden.` |
| Förderziel | `Wir haben keine Personen in unserer Datenbank gefunden.` | `Es wurden keine Personen gefunden.` |
| Förderziel | `Wir haben 1 mögliche Person in unserer Datenbank gefunden.` | `Eine mögliche Person wurde gefunden.` |
| Förderziel | `Wir haben 4 mögliche Personen in unserer Datenbank gefunden.` | `Vier mögliche Personen wurden gefunden.` |
| Förderziel | `Wir haben keine Vorschläge gefunden.` | `Es wurden keine Vorschläge gefunden.` |
| Förderziel | `Wir konnten mit keiner Maßnahme starten.` | `Keine Maßnahme konnte gestartet werden.` |
| Prozess: IFÖ | `Dazu legen wir Ihnen eine Förderakte an.` | `Dafür wird eine Förderakte angelegt.` |
| Nutzerfeedback | `Bitte nehmen Sie Kontakt mit mir auf` | `Bitte nehmen Sie Kontakt mit uns auf.` |

Die Formulierungen `Helfen Sie uns …`, `Wir sind auf Ihr Feedback angewiesen …` und `Wir werden uns … mit Ihnen in Verbindung setzen.` können im Nutzerfeedback bestehen bleiben, weil dort erkennbar das Produktteam spricht.

### 3.4 Persönliche Begrüßung

| Seite | Ist-Text | Verbindlicher Vorschlag |
|---|---|---|
| Meine Startseite | `Willkommen Markus Czakay-Hänsel!` | `Willkommen, [Nutzername]!` |

Der Name muss dynamisch aus dem angemeldeten Konto stammen. Ein fest eingetragener Beispielname darf nicht in der produktiven Variante verbleiben.

## 4. Rechtschreibung und Grammatik

| Ist-Text | Vorschlag |
|---|---|
| `Erstellen Sie jetzt ihre erste Förderakte und starten einen Förderprozess.` | `Erstellen Sie jetzt Ihre erste Förderakte und starten Sie eine Förderung.` |
| `Um ein PDF ihres Förderplans zu generieren, müssen Sie diesen zunächst speichern.` | `Um ein PDF Ihres Förderplans zu erstellen, speichern Sie den Förderplan zunächst.` |
| `Wollen Sie den Prozessfortschritt speichern bevor Sie diesen schließen?` | `Möchten Sie den Prozessfortschritt speichern, bevor Sie ihn schließen?` |
| `Ohne Speichern gehen alle Änderungen verloren. Wie wollen Sie weiter machen?` | `Ohne Speichern gehen alle Änderungen verloren. Wie möchten Sie fortfahren?` |
| `Sie können diese übernhemen oder… bal bla` | Text fachlich vervollständigen; mindestens `übernhemen` zu `übernehmen` korrigieren |
| `Klicken Sie auf eine der Maßnamen …` | `Wählen Sie eine Maßnahme aus …` |
| `Unterstüzung` | `Unterstützung` |
| `sonderpädaogischen` | `sonderpädagogischen` |
| `Förderprozess initieren` | anwenderseitig `Förderung starten` |
| `Maßnahmen des Nachteilsausgleich` | `Maßnahmen des Nachteilsausgleichs` |
| `Bitte geben Sie den Förderplan folgenden sorgeberechtigten Personen zur Kenntnis:` | `Bitte geben Sie den Förderplan den folgenden Sorgeberechtigten zur Kenntnis:` |
| `Meine Ergebnis` | `Mein Ergebnis` oder neutral `Ergebnis` |
| `SoPädFö` | `SöPädFö` |

## 5. Terminologie vereinheitlichen

### 5.1 Förderung statt Förderprozess

`Förderprozess` kann intern zur Modellierung verwendet werden. In der sichtbaren Oberfläche soll für den fachlichen Vorgang grundsätzlich `Förderung` stehen, sofern nicht ausdrücklich der technische Ablauf gemeint ist.

### 5.2 Meine Förderakten als zentraler persönlicher Bereich

`Meine Förderakten` bezeichnet den persönlichen Hub. `Meine Förderungen` darf nur bestehen bleiben, wenn tatsächlich eine davon getrennte Liste von Förderungen gemeint ist. Andernfalls ist die Bezeichnung auf `Meine Förderakten` zu vereinheitlichen.

### 5.3 Evaluation, Bewertung und Einschätzung

Aktuell werden `Evaluation`, `Bewertung` und `Einschätzung` nebeneinander verwendet. Fachlich muss ein Leitbegriff festgelegt werden. Bis zur Entscheidung dürfen die Begriffe nicht automatisch gegeneinander ersetzt werden.

### 5.4 Statusbezeichnungen

`In Durchführung` und `Aktiv` werden für denselben oder einen sehr ähnlichen Zustand verwendet. Es ist ein gemeinsamer sichtbarer Statusbegriff festzulegen.

### 5.5 Gendering

Die Datei mischt unter anderem:

- `Schüler/-innen`
- `Schüler:innen`
- `Schülerinnen und Schüler`
- `Schüler`

Die Gendering-Regel ist noch fachlich zu entscheiden. Diese offene Entscheidung blockiert die übrige Wording-Überarbeitung nicht.

## 6. Platzhalter und Prototypreste

Auf funktionalen Seiten wurden 25 unterschiedliche Platzhalter- oder Blindtexte gefunden. Dazu gehören:

- `Lorem ipsum …`
- `Blindtext` und längere Typoblindtexte
- `Label`, `Button`, `Subtitle`, `Tag`, `Action`, `Title`, `Menu Item`, `Text-link`
- `[Name]`
- `Sie können diese übernhemen oder… bal bla`
- `Lorem ipsum was erwartet mich hier`

Vor einer Freigabe ist je Fundstelle zu unterscheiden:

1. Reine Design-Anmerkung außerhalb eines Screens: darf im Arbeitsbereich bleiben, aber nicht in einem produktiven Screen erscheinen.
2. Sichtbarer Platzhalter in einem Screen: durch finalen Text oder einen eindeutigen dynamischen Platzhalter ersetzen.
3. Beispielinhalt für Freitext: als solcher kennzeichnen und fachlich plausibel formulieren.

Besonders betroffen sind Förderakte, Förderplan, Förderziel, Navigation, BSLRR, VM BFZ und Meine Startseite.

## 7. Dialoge, Hinweise und Schaltflächen

- Bestätigungsfragen einheitlich mit `Möchten Sie …?` statt wechselnd `Wollen Sie …?` formulieren.
- Schaltflächen als kurze Handlung benennen: `Speichern`, `Weiter`, `Archivieren`, `Später`.
- Auf Schaltflächen keine Ich-Sätze verwenden.
- Vollständige Hinweis- und Fehlersätze mit Satzzeichen abschließen.
- Für Auslassungen das Zeichen `…` verwenden, nicht drei Punkte `...`.
- Platzhalter in Eingabefeldern knapp halten und nicht mit einer vollständigen Anleitung überladen.

## 8. Priorisierung der Überarbeitung

### Priorität 1 — vor jedem Nutzertest

- Platzhalter, Blindtexte und unvollständige Sätze entfernen
- Rechtschreib- und Grammatikfehler korrigieren
- Prozessfragen von Ich- auf Sie-Perspektive umstellen
- Systemmeldungen neutral formulieren
- dynamische Begrüßung umsetzen

### Priorität 2 — fachliche Konsistenz

- `Förderung` und `Förderprozess` abgrenzen
- `Evaluation`, `Bewertung` und `Einschätzung` festlegen
- `In Durchführung` und `Aktiv` vereinheitlichen
- `Meine Förderakten` und `Meine Förderungen` abgrenzen

### Priorität 3 — redaktioneller Feinschliff

- Satzlängen reduzieren
- Platzhalter vereinheitlichen
- Zeichensetzung und Auslassungszeichen vereinheitlichen
- Hilfetexte auf Verständlichkeit prüfen

## 9. Abnahmekriterien

Die Wording-Überarbeitung ist abgeschlossen, wenn:

- keine direkte Du-Ansprache vorkommt,
- Prozessfragen konsequent die Sie-Perspektive verwenden,
- Ich- und Mein-Formulierungen nur in den definierten Ausnahmen stehen,
- Systemmeldungen neutral formuliert sind,
- alle Platzhalter und Blindtexte aus freizugebenden Screens entfernt sind,
- die offenen Leitbegriffe fachlich entschieden und anschließend einheitlich verwendet werden,
- Rechtschreibung, Grammatik und Zeichensetzung geprüft sind.
