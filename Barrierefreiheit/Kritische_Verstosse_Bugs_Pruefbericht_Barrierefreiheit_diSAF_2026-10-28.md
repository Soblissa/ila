# Kritische Verstöße und Bugs aus dem Prüfbericht zur Barrierefreiheit von diSAF

**Dokumentstatus:** Zur Prüfung  
**Dokumentstand:** 28.10.2026  
**Prüfzeitraum des Originalberichts:** 28.09.2026 bis 09.10.2026  
**Konformitätsziel:** WCAG 2.2 AA und EN 301 549 Version 3.2.1 (Web)  
**Quelle:** `Pruefbericht_Barrierefreiheit_diSAF_2026-10-09.pdf` (83 Seiten)

## Abgrenzung

Dieses Dokument führt ausschließlich die 14 Feststellungen auf, die im ursprünglichen Prüfbericht mit dem Schweregrad **Hoch** ausgewiesen sind. Enthalten sind 13 Verstöße und ein Bug. Feststellungen mit den Schweregraden Mittel oder Niedrig sowie Empfehlungen ohne Schweregrad sind nicht enthalten.

## Überblick

| Issue | Art | Feststellung | Gewerk | Berichtsseite |
|---:|---|---|---|---:|
| #6 | Bug | Unnötiger Einsatz von `role="application"` | Entwicklung | 9 |
| #11 | Verstoß | Nach Aktivierung von Nutzerprofil unklare Fokusverschiebung für die Screenreader-Nutzenden | Entwicklung | 12 |
| #14 | Verstoß | Schließen- und Zurück-Schalter für Screenreader unbeschriftet | Redaktion | 14 |
| #26 | Verstoß | Seitentitel vieler Seiten unverändert | Redaktion | 23 |
| #32 | Verstoß | Navigation außerhalb eines Dialogs möglich | Entwicklung | 27 |
| #42 | Verstoß | Switch-Elemente unzugänglich | Entwicklung | 33 |
| #59 | Verstoß | Links nicht als solche für Screenreader erkennbar | Entwicklung | 46 |
| #64 | Verstoß | Mehrere Phrasen sind für Screenreader-Nutzende zusammenhangslos platziert | Entwicklung | 47 |
| #65 | Verstoß | Kacheln im Dialog „Förderziele hinzufügen“ nicht semantisch ausgezeichnet | Entwicklung | 48 |
| #66 | Verstoß | Unbeschriftete Schalter für den Screenreader | Entwicklung | 49 |
| #81 | Verstoß | Unklares Interaktionsmuster für Screenreader-Nutzende | Entwicklung | 56 |
| #91 | Verstoß | Aufklapper der Kanban-Header nicht zugänglich | Entwicklung | 63 |
| #114 | Verstoß | Falsche Rolle bei der Auflistung der Notizen | Entwicklung | 74 |
| #124 | Verstoß | Jeweiliger Status in der Förder-Zusammenfassung nur visuell wahrnehmbar | Redaktion | 80 |

## #6 – Unnötiger Einsatz von `role="application"`

**Art:** Bug · **Schweregrad:** Hoch · **Gewerk:** Entwicklung · **Berichtsseite:** 9  
**Prüfschritt:** 9.4.1.2 Name, Rolle, Wert verfügbar

**Betroffene Seiten:** Willkommen Seite; Förderakte; Förderplan erstellen; Förderziel / Maßnahme planen; Förderziel starten / Evaluieren / Abschließen.

**Befund und erforderliche Korrektur:** Für die Hauptnavigation wird `role="application"` eingesetzt. Dadurch wird bei Screenreadern ein abweichender Interaktionsmodus erzwungen, obwohl kein vollständig selbst verwaltetes Anwendungs-Interaktionsmodell umgesetzt ist. Die Rolle ist zu entfernen.

## #11 – Nach Aktivierung von Nutzerprofil unklare Fokusverschiebung für die Screenreader-Nutzenden

**Art:** Verstoß · **Schweregrad:** Hoch · **Gewerk:** Entwicklung · **Berichtsseite:** 12  
**Prüfschritte:** 9.1.3.2 Sinnvolle Reihenfolge; 9.4.1.2 Name, Rolle, Wert verfügbar

**Betroffene Seiten:** Willkommen Seite; Antrag, bisherige Förderungen sowie Rechtsbezug und Maßnahmen im Prozess „Besondere Schwierigkeiten im Lesen, Rechtschreiben oder Rechnen feststellen“; Förderakte; Förderplan erstellen; Förderziel / Maßnahme planen; Förderziel starten / Evaluieren / Abschließen.

**Befund und erforderliche Korrektur:** Nach Aktivierung des Schalters „Benutzerprofil“ wird der Fokus an das Ende des DOM auf einen als Menü gekennzeichneten Bereich verlagert. Die Fokusverlagerung und die Semantik sind verwirrend. Das Konstrukt ist entweder als Dialog oder als klassisches Menü umzusetzen. Der auslösende Schalter benötigt `aria-controls` und `aria-expanded`; der zugehörige Bereich sollte im DOM direkt nach dem Schalter stehen. Die Abmeldefunktion ist als Link oder Schalter umzusetzen.

## #14 – Schließen- und Zurück-Schalter für Screenreader unbeschriftet

**Art:** Verstoß · **Schweregrad:** Hoch · **Gewerk:** Redaktion · **Berichtsseite:** 14  
**Prüfschritt:** 9.1.1.1a Alternativtexte für Bedienelemente

**Betroffene Seiten:** Förderakte Anlegen Dialog; Antrag, bisherige Förderungen sowie Rechtsbezug und Maßnahmen im Prozess „Besondere Schwierigkeiten im Lesen, Rechtschreiben oder Rechnen feststellen“; Förderziele hinzufügen Dialog / Förderbereich wählen; Förderziele hinzufügen Dialog / Lernausgangslage bestimmen.

**Befund und erforderliche Korrektur:** Die Schalter zum Schließen des Dialogs „Förderakte anlegen“ und zum Zurück-Navigieren sind für Screenreader unbeschriftet. Vorhandene `aria-label`-Attribute sind leer. Die Schalter müssen sprechend beschriftet werden.

## #26 – Seitentitel vieler Seiten unverändert

**Art:** Verstoß · **Schweregrad:** Hoch · **Gewerk:** Redaktion · **Berichtsseite:** 23  
**Prüfschritt:** 9.2.4.2 Sinnvolle Dokumenttitel

**Betroffene Seiten:** Willkommen Seite; Feedback-Dialog; Förderakte Anlegen Dialog; Antrag, bisherige Förderungen sowie Rechtsbezug und Maßnahmen im Prozess „Besondere Schwierigkeiten im Lesen, Rechtschreiben oder Rechnen feststellen“; Förderziele hinzufügen Dialog / Förderbereich wählen; Förderziele hinzufügen Dialog / Lernausgangslage bestimmen; Förderplan erstellen; Förderziel / Maßnahme planen; Förderziel starten / Evaluieren / Abschließen.

**Befund und erforderliche Korrektur:** Der Seitentitel bleibt in allen Ansichten unverändert „ILA“. Seitentitel müssen den individuellen Inhalt der jeweiligen Seite beschreiben und anschließend den Anbieter nennen.

## #32 – Navigation außerhalb eines Dialogs möglich

**Art:** Verstoß · **Schweregrad:** Hoch · **Gewerk:** Entwicklung · **Berichtsseite:** 27  
**Prüfschritt:** 9.1.3.2 Sinnvolle Reihenfolge

**Betroffene Seite:** Förderakte Anlegen Dialog.

**Befund und erforderliche Korrektur:** Nach der Auswahl eines Schülers bzw. einer Schülerin verliert der Screenreader den Fokus und springt an den Seitenanfang. Der eingeblendete Bereich am Ende des DOM ist nicht mehr als Modaldialog identifizierbar. Solange der Dialog geöffnet ist, muss der Fokus im Dialog verbleiben. Der Prüfbericht nennt als einfachste Umsetzung ein `<dialog>`-Element in Verbindung mit `showModal()`.

## #42 – Switch-Elemente unzugänglich

**Art:** Verstoß · **Schweregrad:** Hoch · **Gewerk:** Entwicklung · **Berichtsseite:** 33  
**Prüfschritte:** 9.1.3.1h Beschriftung von Formularelementen programmatisch ermittelbar; 9.1.4.11 Kontraste von Grafiken und grafischen Bedienelementen ausreichend; 9.2.1.1 Ohne Maus nutzbar

**Betroffene Seiten:** Rechtsbezug und Maßnahmen im Prozess „Besondere Schwierigkeiten im Lesen, Rechtschreiben oder Rechnen feststellen“; Förderziele hinzufügen Dialog / Lernausgangslage bestimmen.

**Befund und erforderliche Korrektur:** Toggle-Elemente lassen sich nur per Maus, nicht zuverlässig per Screenreader oder Tastatur umschalten; bei Enter oder Escape springen sie unmittelbar zurück, bei Leertaste kann zusätzlich die Seite scrollen. Der Prüfbericht empfiehlt die Umstellung auf Standard-Checkboxen mit `role="switch"` und die Verknüpfung der sichtbaren Beschriftung über `for`. Ergänzende Beschreibungen sind über `aria-describedby` zu verknüpfen. Der Kontrast des deselektierten Zustands und des Fokus muss mindestens 3:1 betragen.

## #59 – Links nicht als solche für Screenreader erkennbar

**Art:** Verstoß · **Schweregrad:** Hoch · **Gewerk:** Entwicklung · **Berichtsseite:** 46  
**Prüfschritt:** 9.4.1.2 Name, Rolle, Wert verfügbar

**Betroffene Seite:** Rechtsbezug und Maßnahmen im Prozess „Besondere Schwierigkeiten im Lesen, Rechtschreiben oder Rechnen feststellen“.

**Befund und erforderliche Korrektur:** Die Links zu Rechtsquellen sind als Schaltflächen umgesetzt und für Screenreader nicht als Links erkennbar. Dadurch wird das Öffnen einer neuen Seite nicht erwartbar angekündigt. Die Schaltflächen sind in reguläre `<a href="…">`-Elemente umzuwandeln.

## #64 – Mehrere Phrasen sind für Screenreader-Nutzende zusammenhangslos platziert

**Art:** Verstoß · **Schweregrad:** Hoch · **Gewerk:** Entwicklung · **Berichtsseite:** 47  
**Prüfschritt:** 9.1.3.2 Sinnvolle Reihenfolge

**Betroffene Seite:** Förderakte.

**Befund und erforderliche Korrektur:** Screenreader geben Bestätigungsfragen zum Löschen oder Archivieren eines Förderziels ohne zugehörige Bestätigungsschalter aus. Sind die Inhalte visuell ausgeblendet, müssen sie auch für Screenreader ausgeblendet werden. Existieren Bestätigungsschalter, müssen diese auch für Screenreader verfügbar sein.

## #65 – Kacheln im Dialog „Förderziele hinzufügen“ nicht semantisch ausgezeichnet

**Art:** Verstoß · **Schweregrad:** Hoch · **Gewerk:** Entwicklung · **Berichtsseite:** 48  
**Prüfschritt:** 9.4.1.2 Name, Rolle, Wert verfügbar

**Betroffene Seite:** Förderziele hinzufügen Dialog / Förderbereich wählen.

**Befund und erforderliche Korrektur:** Die Auswahlkacheln im Schritt „Förderbereich wählen“ sind nicht als interaktive Elemente ausgezeichnet. Sie sind als Schalter oder – zur Abbildung des Auswahlstatus – als Radio-Buttons umzusetzen. Die Rolle `application` sowie die bisherige Tabellenbeschreibung sind zu entfernen. Die Struktur sollte als reguläre Liste statt über `role="row"` abgebildet werden.

## #66 – Unbeschriftete Schalter für den Screenreader

**Art:** Verstoß · **Schweregrad:** Hoch · **Gewerk:** Entwicklung · **Berichtsseite:** 49  
**Prüfschritte:** 9.1.1.1a Alternativtexte für Bedienelemente; 9.4.1.2 Name, Rolle, Wert verfügbar

**Betroffene Seiten:** Förderakte; Förderziele hinzufügen Dialog / Förderbereich wählen; Förderziele hinzufügen Dialog / Lernausgangslage bestimmen.

**Befund und erforderliche Korrektur:** Mehrere Symbolschalter besitzen keine zugängliche Beschriftung. Sie müssen sprechend beschriftet werden. Der Accordion-Trigger ist zusätzlich als `<button type="button">` umzusetzen, damit Semantik und Interaktionsverhalten übereinstimmen.

## #81 – Unklares Interaktionsmuster für Screenreader-Nutzende

**Art:** Verstoß · **Schweregrad:** Hoch · **Gewerk:** Entwicklung · **Berichtsseite:** 56  
**Prüfschritt:** 9.4.1.2 Name, Rolle, Wert verfügbar

**Betroffene Seite:** Förderplan erstellen.

**Befund und erforderliche Korrektur:** Die Auswahl sorgeberechtigter Personen ist mit einer Datumsabfrage in einer Listbox kombiniert. Dieses Interaktionsmuster funktioniert für Screenreader nicht und ist nicht etabliert. Der Prüfbericht fordert eine funktionierende Alternative, beispielsweise Checkboxen, die nach Auswahl ein Datumsfeld einblenden. Falls keine Auswahl erforderlich ist, kann auf die Listbox beziehungsweise Radio-Buttons verzichtet werden.

## #91 – Aufklapper der Kanban-Header nicht zugänglich

**Art:** Verstoß · **Schweregrad:** Hoch · **Gewerk:** Entwicklung · **Berichtsseite:** 63  
**Prüfschritte:** 9.1.3.2 Sinnvolle Reihenfolge; 9.2.4.3 Schlüssige Reihenfolge bei der Tastaturbedienung; 9.4.1.2 Name, Rolle, Wert verfügbar

**Betroffene Seite:** Förderakte.

**Befund und erforderliche Korrektur:** Die Kanban-Header „In Planung“, „In Durchführung“ und „Abgeschlossen“ sind immer per Tastatur fokussierbar, obwohl das Ein- und Ausklappen nur auf schmalen Viewports verfügbar ist. Die Elemente dürfen nur dann fokussierbar sein, wenn die Funktion tatsächlich angeboten wird. Da sie nicht als Schalter ausgezeichnet sind, können Screenreader-Nutzende die Bereiche nicht öffnen und deren Inhalte nicht erreichen. Die Aufklappfunktion muss semantisch und per Tastatur zugänglich umgesetzt werden.

## #114 – Falsche Rolle bei der Auflistung der Notizen

**Art:** Verstoß · **Schweregrad:** Hoch · **Gewerk:** Entwicklung · **Berichtsseite:** 74  
**Prüfschritt:** 9.4.1.2 Name, Rolle, Wert verfügbar

**Betroffene Seite:** Förderziel starten / Evaluieren / Abschließen.

**Befund und erforderliche Korrektur:** Notizen zu einer gestarteten Maßnahme werden im Quellcode als Listbox dargestellt. Dadurch werden die Schalter „Bearbeiten“ und „Löschen“ von Screenreadern nicht korrekt erkannt. Die Listbox ist durch eine klassische `<ul>`-/`<li>`-Struktur zu ersetzen.

## #124 – Jeweiliger Status in der Förder-Zusammenfassung nur visuell wahrnehmbar

**Art:** Verstoß · **Schweregrad:** Hoch · **Gewerk:** Redaktion · **Berichtsseite:** 80  
**Prüfschritt:** 9.1.1.1b Alternativtexte für Grafiken und Objekte

**Betroffene Seiten:** Förderakte; Förderplan erstellen.

**Befund und erforderliche Korrektur:** In „Schritt 7/7: Zusammenfassung“ wird der jeweilige Status ausschließlich über ein grünes Häkchen oder rotes Kreuz dargestellt. Die Bedeutung ist programmatisch nicht auslesbar. Der Status ist als zugängliche Beschriftung bereitzustellen; der Prüfbericht nennt hierfür ein `aria-label` am jeweiligen SVG-Element.

## Quellenhinweis

Alle Feststellungen, Zuordnungen, Prüfschritte, betroffenen Seiten und Korrekturhinweise wurden ausschließlich aus dem ursprünglichen Prüfbericht `Pruefbericht_Barrierefreiheit_diSAF_2026-10-09.pdf` übernommen oder knapp zusammengefasst. Die im Bericht verwendete Produktbezeichnung „ILA“ wurde in Befundtexten nicht fachlich umgedeutet.
