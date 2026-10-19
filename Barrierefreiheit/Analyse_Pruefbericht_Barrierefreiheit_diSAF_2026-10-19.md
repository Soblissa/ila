# Analyse des Prüfberichts zur Barrierefreiheit von diSAF

**Stand:** 19.10.2026  
**Prüfzeitraum:** 28.09.2026 bis 09.10.2026  
**Konformitätsziel:** WCAG 2.2 AA und EN 301 549 Version 3.2.1 (Web)  
**Quelle:** `Pruefbericht_Barrierefreiheit_diSAF_2026-10-09.pdf` (83 Seiten)

## 1. Zusammenfassung

Der Prüfbericht weist für keinen der zwölf getesteten Dialoge Barrierefreiheit aus. Festgestellt wurden Barrieren für blinde, sehbehinderte, motorisch und kognitiv eingeschränkte Nutzende. Für Menschen mit Hörbeeinträchtigungen wurden in der geprüften Seitenauswahl keine Barrieren festgestellt.

Insgesamt enthält der Bericht **98 Feststellungen**: 72 Verstöße, 12 Bugs und 14 Empfehlungen. 14 sind hoch, 65 mittel und 8 niedrig gewichtet; 11 Empfehlungen haben keinen ausgewiesenen Schweregrad.

Die kritischsten Risiken liegen bei Screenreader-Semantik, zugänglichen Namen, Fokus- und Dialogsteuerung sowie nicht bedienbaren interaktiven Komponenten. Da sich viele Befunde auf wiederverwendete Komponenten beziehen, sollte die Behebung komponentenweit erfolgen und anschließend in allen zwölf geprüften Dialogen regressionsgetestet werden.

### Berichtseigenheiten

- Die Kennzahl „Gefundene Fehler: 72“ entspricht der Zahl der als „Verstoß“   bezeichneten Punkte. Zusätzlich sind 12 als „Bug“ und 14 als „Empfehlung“   bezeichnete Feststellungen enthalten.
- Die Gewichtung 14 hoch + 65 mittel + 8 niedrig umfasst 87 Feststellungen.   Elf Empfehlungen besitzen keinen Schweregrad.
- In der Detailauswertung ist #94 dem Gewerk „Struktur & Semantik“ zugeordnet;   die Management-Statistik führt dieses Gewerk nicht separat auf. #40 ist   zugleich Entwicklung und Design zugeordnet.

## 2. Sortierung nach Art

| Art | Anzahl | Bedeutung |
|---|---:|---|
| Verstoß | 72 | Muss für die angestrebte Konformität behoben werden. |
| Bug | 12 | Technischer Fehler; in der Detailauswertung ebenfalls gewichtet. |
| Empfehlung | 14 | Verbessert Zugänglichkeit bzw. Bedienkomfort; 3 davon sind mittel gewichtet. |

## 3. Sortierung nach Inhalt

| Inhaltsbereich | Anzahl | Zugehörige Issues |
|---|---:|---|
| Semantik, Struktur, Rollen und Beziehungen | 22 | #6, #8, #9, #17, #18, #36, #56, #58, #59, #61, #64, #65, #73, #78, #83, #90, #93, #94, #95, #103, #114, #116 |
| Tastatur, Fokus, Dialoge und Navigation | 24 | #10, #11, #12, #19, #20, #22, #24, #26, #27, #32, #34, #40, #42, #43, #44, #80, #81, #82, #91, #101, #104, #118, #119, #120 |
| Darstellung, Kontrast, Zoom und Benutzerpräferenzen | 19 | #21, #23, #25, #28, #29, #38, #39, #41, #46, #47, #48, #50, #53, #85, #86, #92, #102, #117, #122 |
| Formulare, Validierung und Statusmeldungen | 17 | #35, #45, #49, #52, #55, #69, #72, #74, #79, #87, #96, #99, #100, #105, #107, #115, #123 |
| Zugängliche Namen, Alternativtexte und Sprache | 16 | #7, #13, #14, #15, #30, #51, #54, #57, #66, #77, #84, #88, #97, #98, #121, #124 |

## 4. Priorisierung nach Schweregrad

Die Priorisierung übernimmt den Schweregrad des Prüfberichts. Innerhalb einer Stufe sind die Feststellungen nach Issue-Nummer sortiert. Auch niedrige Verstöße müssen für WCAG-Konformität behoben werden.

### Priorität 1 – kritisch (14)

| Issue | Art | Feststellung | Gewerk | Inhaltsbereich |
|---:|---|---|---|---|
| #6 | Bug | Unnötiger Einsatz von role="application" | Entwicklung | Semantik, Struktur, Rollen und Beziehungen |
| #11 | Verstoß | Nach Aktivierung von Nutzerprofil unklare Fokusverschiebung für die Screenreader-Nutzenden | Entwicklung | Tastatur, Fokus, Dialoge und Navigation |
| #14 | Verstoß | Schließen- und Zurück-Schalter für Screenreader unbeschriftet | Redaktion | Zugängliche Namen, Alternativtexte und Sprache |
| #26 | Verstoß | Seitentitel vieler Seiten unverändert | Redaktion | Tastatur, Fokus, Dialoge und Navigation |
| #32 | Verstoß | Navigation außerhalb eines Dialogs möglich | Entwicklung | Tastatur, Fokus, Dialoge und Navigation |
| #42 | Verstoß | Switch-Elemente unzugänglich | Entwicklung | Tastatur, Fokus, Dialoge und Navigation |
| #59 | Verstoß | Links nicht als solche für Screenreader erkennbar | Entwicklung | Semantik, Struktur, Rollen und Beziehungen |
| #64 | Verstoß | Mehrere Phrasen sind für Screenreader-Nutzende zusammenhangslos platziert | Entwicklung | Semantik, Struktur, Rollen und Beziehungen |
| #65 | Verstoß | Kacheln im Dialog "Förderziele hinzufügen" nicht semantisch ausgezeichnet | Entwicklung | Semantik, Struktur, Rollen und Beziehungen |
| #66 | Verstoß | Unbeschriftete Schalter für den Screenreader | Entwicklung | Zugängliche Namen, Alternativtexte und Sprache |
| #81 | Verstoß | Unklares Interaktionsmuster für Screenreader-Nutzende | Entwicklung | Tastatur, Fokus, Dialoge und Navigation |
| #91 | Verstoß | Aufklapper der Kanban-Header nicht zugänglich | Entwicklung | Tastatur, Fokus, Dialoge und Navigation |
| #114 | Verstoß | Falsche Rolle bei der Auflistung der Notizen | Entwicklung | Semantik, Struktur, Rollen und Beziehungen |
| #124 | Verstoß | Jeweiliger Status in der Förder-Zusammenfassung nur visuell wahrnehmbar | Redaktion | Zugängliche Namen, Alternativtexte und Sprache |

### Priorität 2 – wesentlich (65)

| Issue | Art | Feststellung | Gewerk | Inhaltsbereich |
|---:|---|---|---|---|
| #8 | Bug | Unzulässige Verschachtelung identischer & falscher Rollen für Auflistung Förderakten & Förderprozess-Auswahl | Entwicklung | Semantik, Struktur, Rollen und Beziehungen |
| #9 | Empfehlung | Generische Elemente mit ARIA-Labels | Entwicklung | Semantik, Struktur, Rollen und Beziehungen |
| #10 | Verstoß | Navigation einblenden / ausblenden Funktionalität hat keinen Einfluss auf Screenreader-Nutzende | Entwicklung | Tastatur, Fokus, Dialoge und Navigation |
| #12 | Verstoß | Wichtige Seitenregionen sind nicht definiert | Entwicklung | Tastatur, Fokus, Dialoge und Navigation |
| #13 | Verstoß | Diagramm "meine Schüler" nicht für Screenreader-Nutzende zugänglich | Entwicklung | Zugängliche Namen, Alternativtexte und Sprache |
| #15 | Verstoß | Logo zur Startseite interaktiv implementieren und mit Beschreibung ausstatten | Redaktion | Zugängliche Namen, Alternativtexte und Sprache |
| #17 | Empfehlung | Listen mit list-style: none (Safari-Bug) | Design | Semantik, Struktur, Rollen und Beziehungen |
| #18 | Bug | Navigation ohne Listenauszeichnung | Entwicklung | Semantik, Struktur, Rollen und Beziehungen |
| #20 | Verstoß | Aktiver Eintrag der Navigation nicht zugänglich | Entwicklung | Tastatur, Fokus, Dialoge und Navigation |
| #21 | Verstoß | Blaue Tastatur-Fokus-Farbe gegenüber hellen Hintergrundfarben nicht ausreichend kontrastierend | Design | Darstellung, Kontrast, Zoom und Benutzerpräferenzen |
| #23 | Verstoß | Graphen-Erklärungstext Farbe ohne ausreichenden Kontrast | Design | Darstellung, Kontrast, Zoom und Benutzerpräferenzen |
| #28 | Bug | Schriftgrößen in absoluten Pixel-Werten definiert | Design | Darstellung, Kontrast, Zoom und Benutzerpräferenzen |
| #29 | Bug | Zeilenhöhen in absoluten Pixel-Werten definiert | Design | Darstellung, Kontrast, Zoom und Benutzerpräferenzen |
| #30 | Verstoß | "Suchphrasen-Inhalt entfernen"-Schalter unbeschriftet | Redaktion | Zugängliche Namen, Alternativtexte und Sprache |
| #34 | Verstoß | Dialoge ohne Beschriftung | Redaktion | Tastatur, Fokus, Dialoge und Navigation |
| #35 | Verstoß | Statusmeldung unterhalb Suchfeld für Screenreader optimieren | Entwicklung | Formulare, Validierung und Statusmeldungen |
| #36 | Empfehlung | Ungültige ARIA-ID-Referenzen | Entwicklung | Semantik, Struktur, Rollen und Beziehungen |
| #40 | Verstoß | Schritt-Navigation optimieren | Entwicklung, Design | Tastatur, Fokus, Dialoge und Navigation |
| #41 | Verstoß | Radio Buttons nicht verlässlich visuell wahrnehmbar | Design | Darstellung, Kontrast, Zoom und Benutzerpräferenzen |
| #43 | Verstoß | Schalter "Kalender umschalten" nicht zugänglich | Entwicklung | Tastatur, Fokus, Dialoge und Navigation |
| #44 | Verstoß | Schalter zum Ein- und Ausklappen der Schritt-Navigation unbeschriftet | Redaktion | Tastatur, Fokus, Dialoge und Navigation |
| #45 | Verstoß | Formularelemente der Antragstellung optimieren | Redaktion | Formulare, Validierung und Statusmeldungen |
| #46 | Verstoß | Auswahl der Monate im Kalender-Widget bei starker Vergrößerung unnötig ausgeblendet | Design | Darstellung, Kontrast, Zoom und Benutzerpräferenzen |
| #47 | Verstoß | Inhalte brechen im Dialog der Förderbereiche nicht um | Design | Darstellung, Kontrast, Zoom und Benutzerpräferenzen |
| #48 | Verstoß | Zahlen in der Schritt-Navigation ohne ausreichenden Kontrast | Design | Darstellung, Kontrast, Zoom und Benutzerpräferenzen |
| #49 | Verstoß | Datums-Auswahl-Feld nicht programmatisch ermittelbar als fehlerhaft ausgezeichnet | Entwicklung | Formulare, Validierung und Statusmeldungen |
| #51 | Verstoß | Englischsprachige Schalter-Beschriftungen übersetzen | Redaktion | Zugängliche Namen, Alternativtexte und Sprache |
| #53 | Verstoß | Rahmenfarbe der Formularfelder mit nur unzureichendem Kontrast | Design | Darstellung, Kontrast, Zoom und Benutzerpräferenzen |
| #54 | Bug | Beschriftung des iframe-HTML-Elements | Redaktion | Zugängliche Namen, Alternativtexte und Sprache |
| #55 | Verstoß | Nach "Weiter"-Navigation gibt es keine Rückmeldung durch den Screenreader | Entwicklung | Formulare, Validierung und Statusmeldungen |
| #56 | Verstoß | Kalenderansicht nicht zugänglich für Screenreader | Entwicklung | Semantik, Struktur, Rollen und Beziehungen |
| #57 | Verstoß | Einzelne Schalter im WYSIWYG-Editor für Screenreader nicht ausgezeichnet | Entwicklung | Zugängliche Namen, Alternativtexte und Sprache |
| #69 | Verstoß | Statusmeldung zur Toggle-Selektion muss von Screenreadern angesagt werden | Entwicklung | Formulare, Validierung und Statusmeldungen |
| #72 | Verstoß | Anzahl der ausgewählten Förderziele wird nicht direkt vom Screenreader angesagt | Entwicklung | Formulare, Validierung und Statusmeldungen |
| #73 | Verstoß | Visuell ausgeblendete Phrasen werden vom Screenreader vorgelesen | Entwicklung | Semantik, Struktur, Rollen und Beziehungen |
| #74 | Verstoß | Anzahl der Maßnahmen wird per Screenreader nach Aktivierung der Toggles nicht angesagt | Entwicklung | Formulare, Validierung und Statusmeldungen |
| #77 | Verstoß | HTML-Element in Text-Beschriftung enthalten | Redaktion | Zugängliche Namen, Alternativtexte und Sprache |
| #78 | Verstoß | Aufklapper als Listenboxen ausgezeichnet | Entwicklung | Semantik, Struktur, Rollen und Beziehungen |
| #79 | Bug | Formularfelder ohne programmatische Beschriftung | Entwicklung | Formulare, Validierung und Statusmeldungen |
| #80 | Verstoß | Tastatur-fokussierbare Elemente können hinter Alarm-Meldung verschwinden | Entwicklung | Tastatur, Fokus, Dialoge und Navigation |
| #82 | Verstoß | Tastatur-Falle in den Maßnahmen | Entwicklung | Tastatur, Fokus, Dialoge und Navigation |
| #83 | Bug | Seite hat mehrere Header im Inhaltsbereich | Redaktion | Semantik, Struktur, Rollen und Beziehungen |
| #84 | Bug | Sichtbarer Text der Schritt-Navigation nicht im zugänglichen Namen enthalten | Redaktion | Zugängliche Namen, Alternativtexte und Sprache |
| #86 | Verstoß | Warnmeldung überlagert Schalter auf schmalen Viewports bzw. stark vergrößerten Ansichten | Design | Darstellung, Kontrast, Zoom und Benutzerpräferenzen |
| #87 | Verstoß | Fehlerhafte Formularfelder nicht programmatisch auslesbar | Entwicklung | Formulare, Validierung und Statusmeldungen |
| #88 | Verstoß | Schalter zum Leeren der Textareas für Screenreader nicht beschriftet | Redaktion | Zugängliche Namen, Alternativtexte und Sprache |
| #90 | Bug | Listenstruktur: Ungültige Kind-Elemente | Entwicklung | Semantik, Struktur, Rollen und Beziehungen |
| #92 | Verstoß | Text-Hervorhebung ohne ausreichendes Kontrastverhältnis | Design | Darstellung, Kontrast, Zoom und Benutzerpräferenzen |
| #93 | Verstoß | Unnötige Link-Auszeichnung eines nicht-interaktiven Elements | Entwicklung | Semantik, Struktur, Rollen und Beziehungen |
| #94 | Bug | Aufklapper nicht zugänglich | Struktur & Semantik | Semantik, Struktur, Rollen und Beziehungen |
| #95 | Verstoß | Auflistung der Attribute nicht zugänglich | Entwicklung | Semantik, Struktur, Rollen und Beziehungen |
| #96 | Verstoß | Fehlermeldungen müssen semantisch als solche ausgezeichnet werden | Entwicklung | Formulare, Validierung und Statusmeldungen |
| #97 | Verstoß | Emojis im Feedback-Dialog nicht zugänglich | Entwicklung | Zugängliche Namen, Alternativtexte und Sprache |
| #99 | Verstoß | Sichtbare und programmatisch ermittelbare Beschriftungen für Formularelemente einfügen | Entwicklung | Formulare, Validierung und Statusmeldungen |
| #101 | Verstoß | Fokus des "Feedback"-Schalters bei geöffnetem "Förderziele hinzufügen" Dialog nicht erkennbar | Design | Tastatur, Fokus, Dialoge und Navigation |
| #102 | Verstoß | Inhalte brechen im Dialog "Förderziele hinzufügen" nicht um | Design | Darstellung, Kontrast, Zoom und Benutzerpräferenzen |
| #104 | Verstoß | Schalter "Filtern", "Weiter" und "Zurück" nicht zugänglich | Entwicklung | Tastatur, Fokus, Dialoge und Navigation |
| #105 | Verstoß | Fehlermeldungen nicht semantisch mit den jeweiligen Fehlerfeldern verknüpft | Entwicklung | Formulare, Validierung und Statusmeldungen |
| #107 | Verstoß | Nach dem Hinzufügen einer "eigenen Maßnahme" erhält der Screenreader kein Feedback über den Erfolg der Maßnahme | Entwicklung | Formulare, Validierung und Statusmeldungen |
| #115 | Verstoß | Dropdowns nicht semantisch umgesetzt | Entwicklung | Formulare, Validierung und Statusmeldungen |
| #117 | Verstoß | Schriftfarbe über hellblauen Kästchen ohne ausreichenden Kontrast | Design | Darstellung, Kontrast, Zoom und Benutzerpräferenzen |
| #118 | Verstoß | Dialog "Evaluation erstellen" nicht als Modaldialog umgesetzt | Entwicklung | Tastatur, Fokus, Dialoge und Navigation |
| #119 | Verstoß | Tastatur-fokussierbare Elemente im Dialog können von der schwebenden Action-Bar überdeckt werden | Design | Tastatur, Fokus, Dialoge und Navigation |
| #121 | Bug | Fehlende zugängliche Beschriftung | Redaktion | Zugängliche Namen, Alternativtexte und Sprache |
| #123 | Verstoß | Fehlerfall muss programmatisch auslesbar sein | Entwicklung | Formulare, Validierung und Statusmeldungen |

### Priorität 3 – nachgelagert (8)

| Issue | Art | Feststellung | Gewerk | Inhaltsbereich |
|---:|---|---|---|---|
| #19 | Verstoß | URL verlinken | Redaktion | Tastatur, Fokus, Dialoge und Navigation |
| #22 | Verstoß | Graph tastaturfokussierbar ohne Ergebnis auf Interaktion hin | Entwicklung | Tastatur, Fokus, Dialoge und Navigation |
| #24 | Verstoß | Fokus geht nach Interaktion mit dem Element zum Ausklappen der Navigation verloren | Entwicklung | Tastatur, Fokus, Dialoge und Navigation |
| #27 | Verstoß | Tastatur-Fokus teilweise von ausgeklappter Navigation überlagert | Design | Tastatur, Fokus, Dialoge und Navigation |
| #52 | Verstoß | Beschriftung von Formularfeldern resilient definieren | Entwicklung | Formulare, Validierung und Statusmeldungen |
| #98 | Verstoß | Schließen-Schalter des Feedback-Dialogs missverständlich beschriftet | Redaktion | Zugängliche Namen, Alternativtexte und Sprache |
| #116 | Verstoß | Überschrift fragmentiert | Redaktion | Semantik, Struktur, Rollen und Beziehungen |
| #122 | Verstoß | Selektierter Eintrag in Combobox mit zu geringem Kontrast der Hervorhebung | Design | Darstellung, Kontrast, Zoom und Benutzerpräferenzen |

### Priorität 4 – Empfehlungen ohne Schweregrad (11)

| Issue | Art | Feststellung | Gewerk | Inhaltsbereich |
|---:|---|---|---|---|
| #7 | Empfehlung | Beschriftung des Schalters Benutzerprofil konsistent beschriften | Redaktion | Zugängliche Namen, Alternativtexte und Sprache |
| #25 | Empfehlung | Ladeanzeige sollte auf Browser-Einstellungen reagieren | Design | Darstellung, Kontrast, Zoom und Benutzerpräferenzen |
| #38 | Empfehlung | Icon externer Links im Hochkontrast-Modus kaum visuell wahrnehmbar | Design | Darstellung, Kontrast, Zoom und Benutzerpräferenzen |
| #39 | Empfehlung | Icons im Hochkontrast-Modus ausgeblendet | Design | Darstellung, Kontrast, Zoom und Benutzerpräferenzen |
| #50 | Empfehlung | Status der Auswahl der Radio-Buttons im Hochkontrast-Modus ausgeblendet | Design | Darstellung, Kontrast, Zoom und Benutzerpräferenzen |
| #58 | Empfehlung | Voller Umfang des WYSIWYG-Editor nicht für Screenreader zugänglich | Entwicklung | Semantik, Struktur, Rollen und Beziehungen |
| #61 | Empfehlung | Überschrift erster Ebene nach Erwähnung der Klassenzugehörigkeit | Entwicklung | Semantik, Struktur, Rollen und Beziehungen |
| #85 | Empfehlung | Toggle UI Elemente im Hochkontrastmodus ausgeblendet | Design | Darstellung, Kontrast, Zoom und Benutzerpräferenzen |
| #100 | Empfehlung | Kontaktmöglichkeit per autocomplete erweitern | Entwicklung | Formulare, Validierung und Statusmeldungen |
| #103 | Empfehlung | Ungültige ARIA-ID-Referenzen | Entwicklung | Semantik, Struktur, Rollen und Beziehungen |
| #120 | Empfehlung | Schalter "Förderziel öffnen" als Link umgesetzt | Entwicklung | Tastatur, Fokus, Dialoge und Navigation |

## 5. Empfohlene Umsetzungsreihenfolge

1. **Kritische Barrieren schließen:** alle 14 hoch gewichteten Feststellungen    bearbeiten und separat mit Tastatur sowie JAWS/NVDA prüfen.
2. **Basiskomponenten sanieren:** Navigation, Dialog, Schalter/Switch, Aufklapper,    Link, Listen-/Kachelstruktur und zugängliche Beschriftungen zentral korrigieren.
3. **Formulare und Rückmeldungen konsolidieren:** Fehlerzustände, Fehlermeldungen,    Statusmeldungen und Feldbeschriftungen als einheitliches Muster umsetzen.
4. **Visuelle Barrieren beheben:** Fokusindikatoren, Text-/Grafikkontraste,    Hochkontrastmodus, Vergrößerung und Umbruch prüfen.
5. **Abschlussprüfung durchführen:** alle zwölf Dialoge und übertragbare Vorkommen    außerhalb der Stichprobe erneut testen; erst danach Konformität bewerten.

## 6. Kritische Feststellungen im Überblick

- **#6 – Unnötiger Einsatz von role="application"** (Bug; Entwicklung; Semantik, Struktur, Rollen und Beziehungen)
- **#11 – Nach Aktivierung von Nutzerprofil unklare Fokusverschiebung für die Screenreader-Nutzenden** (Verstoß; Entwicklung; Tastatur, Fokus, Dialoge und Navigation)
- **#14 – Schließen- und Zurück-Schalter für Screenreader unbeschriftet** (Verstoß; Redaktion; Zugängliche Namen, Alternativtexte und Sprache)
- **#26 – Seitentitel vieler Seiten unverändert** (Verstoß; Redaktion; Tastatur, Fokus, Dialoge und Navigation)
- **#32 – Navigation außerhalb eines Dialogs möglich** (Verstoß; Entwicklung; Tastatur, Fokus, Dialoge und Navigation)
- **#42 – Switch-Elemente unzugänglich** (Verstoß; Entwicklung; Tastatur, Fokus, Dialoge und Navigation)
- **#59 – Links nicht als solche für Screenreader erkennbar** (Verstoß; Entwicklung; Semantik, Struktur, Rollen und Beziehungen)
- **#64 – Mehrere Phrasen sind für Screenreader-Nutzende zusammenhangslos platziert** (Verstoß; Entwicklung; Semantik, Struktur, Rollen und Beziehungen)
- **#65 – Kacheln im Dialog "Förderziele hinzufügen" nicht semantisch ausgezeichnet** (Verstoß; Entwicklung; Semantik, Struktur, Rollen und Beziehungen)
- **#66 – Unbeschriftete Schalter für den Screenreader** (Verstoß; Entwicklung; Zugängliche Namen, Alternativtexte und Sprache)
- **#81 – Unklares Interaktionsmuster für Screenreader-Nutzende** (Verstoß; Entwicklung; Tastatur, Fokus, Dialoge und Navigation)
- **#91 – Aufklapper der Kanban-Header nicht zugänglich** (Verstoß; Entwicklung; Tastatur, Fokus, Dialoge und Navigation)
- **#114 – Falsche Rolle bei der Auflistung der Notizen** (Verstoß; Entwicklung; Semantik, Struktur, Rollen und Beziehungen)
- **#124 – Jeweiliger Status in der Förder-Zusammenfassung nur visuell wahrnehmbar** (Verstoß; Redaktion; Zugängliche Namen, Alternativtexte und Sprache)
