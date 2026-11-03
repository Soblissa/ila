# Erste Analyse der Umfrage zum Rollout 2027

**Datenstand:** 03.11.2026  
**Quelldatei:** `Analyse_1_03.11.2026.csv`  
**Status:** Erstanalyse; deskriptiv, noch keine bereinigte oder gewichtete Endauswertung

## 1. Kurzfazit

1. **Die grundsätzliche Akzeptanz ist hoch.** 95,1 % der 490 Antwortenden erwarten, dass ein digitaler Förderplan die Förderarbeit erleichtert. 89,6 % sind motiviert, sich in die Anwendung einzuarbeiten, und 91,0 % bewerten die Diskussions- und Kommentarfunktion positiv.
2. **Die Einführung muss den Nutzen sichtbar und die Anwendung einfach machen.** Die Freitexte zeigen Informationsbedarf zu Funktionsumfang, Bedienung, Integration, Zeitplan und Testmöglichkeiten. Mehrere Personen kennen ila (diSAF) bisher kaum oder erstmals durch die Umfrage.
3. **Lernvideos und Webinare sind das stärkste Einführungsformat.** 78,4 % der 487 Personen mit mindestens einer Auswahl nennen dieses Format; 56,3 % wählen Schulungen.
4. **Eine offene Fragerunde allein erreicht voraussichtlich nur die Hälfte.** 241 Personen würden sie nutzen, 243 nicht. Sie sollte deshalb nur ein Bestandteil des Einführungsangebots sein.
5. **Die Geräteplanung unterscheidet sich deutlich nach Rolle.** Lehrkräfte erwarten vor allem die Nutzung privater Laptops; Mitglieder der Schulleitung vor allem die Nutzung von Schulrechnern.
6. **Beim Thema Vorbeugende Maßnahme (VM) sind Ressourcenmangel und lange, stark fallabhängige Laufzeiten zentral.** Die vorgegebenen Antwortkategorien zur Dauer bilden die Praxis nur unzureichend ab.
7. **Die exportierten Punktespalten sind nicht auswertbar.** Alle Punktwerte und Punktesummen stehen trotz vorhandener Antworten auf `0`. Die Analyse basiert deshalb auf den Antworttexten.

## 2. Datengrundlage und Vorgehen

- 706 Datensätze im Zeitraum 29.10. bis 03.11.2026
- 447 Datensätze als abgeschlossen markiert (63,3 %)
- 259 Datensätze nicht abgeschlossen (36,7 %)
- 415 Datensätze mit einer Antwort-Quote von mindestens 78,57 %
- alle 15 Schulamtsbezirke vertreten; zwischen 12 und 63 Nennungen je Bezirk
- 550 Einträge mit Schulname; 387 unterschiedliche Rohschreibweisen. Wegen Schreibvarianten wurde noch keine bereinigte Zahl unterschiedlicher Schulen gebildet
- 552 Angaben zur Rolle:
  - Lehrkraft: 343 (62,1 %)
  - Mitglied der Schulleitung: 205 (37,1 %)
  - Mitglied der Schulverwaltung: 4 (0,7 %)

Ausgewertet werden je Frage alle vorhandenen Antworten. Die jeweilige Bezugsgröße `n` wird deshalb separat angegeben. Bei Mehrfachauswahlfragen ist die Bezugsgröße die Zahl der Personen, die in dem jeweiligen Fragenblock mindestens eine Option ausgewählt haben. Die Ergebnisse sind nicht gewichtet und belegen keine Repräsentativität für alle hessischen Schulen.

## 3. Haltung zum digitalen Förderplan und zu ila

Positive Antworten fassen „Trifft absolut zu“ und „Trifft überwiegend zu“ zusammen.

| Aussage | n | absolut positiv | positiv | eher/absolut nicht positiv |
|---|---:|---:|---:|---:|
| Digitaler Förderplan erleichtert die Förderarbeit | 490 | 466 | 95,1 % | 4,9 % |
| Motivation zur Einarbeitung | 492 | 441 | 89,6 % | 10,4 % |
| Nutzen der Diskussions- und Kommentarfunktion | 488 | 444 | 91,0 % | 9,0 % |
| Eigener Zugriff für Sekretariate | 475 | 351 | 73,9 % | 26,1 % |
| Zugang über das Schulportal | 480 | 340 | 70,8 % | 29,2 % |

### Auffällige Unterschiede nach Rolle

- **Erwartete Arbeitserleichterung:** Lehrkräfte 93,5 % positiv (`n=292`), Schulleitungsmitglieder 97,2 % (`n=180`).
- **Motivation zur Einarbeitung:** Lehrkräfte 87,0 % positiv (`n=292`), Schulleitungsmitglieder 94,0 % (`n=182`).
- **Sekretariatszugriff:** Lehrkräfte 80,6 % positiv (`n=279`), Schulleitungsmitglieder 64,2 % (`n=179`).
- **Schulportal-Zugang:** Lehrkräfte 74,1 % positiv (`n=286`), Schulleitungsmitglieder 64,6 % (`n=178`).

**Einordnung:** Der Kernnutzen wird sehr klar bejaht. Bei Zugriffswegen und Rollenrechten ist die Zustimmung geringer und die Perspektive der Schulleitung zurückhaltender. Diese Punkte sollten nicht aus dem Gesamtergebnis abgeleitet, sondern fachlich und rollenspezifisch geklärt werden.

## 4. Erwartete Gerätenutzung

| Gerät | n | positiv | eher/absolut nicht positiv |
|---|---:|---:|---:|
| privater Laptop | 464 | 75,9 % | 24,1 % |
| Schulrechner | 464 | 70,5 % | 29,5 % |
| schulisches Tablet (iPad) | 434 | 63,4 % | 36,6 % |
| Mobiltelefon | 421 | 43,5 % | 56,5 % |

Die Gesamtwerte verdecken starke Rollenunterschiede:

| Gerät | Lehrkräfte | Mitglieder der Schulleitung |
|---|---:|---:|
| Schulrechner | 52,8 % (`n=271`) | 96,0 % (`n=177`) |
| schulisches Tablet (iPad) | 61,0 % (`n=259`) | 67,7 % (`n=161`) |
| Mobiltelefon | 47,3 % (`n=260`) | 36,7 % (`n=147`) |
| privater Laptop | 84,1 % (`n=283`) | 61,6 % (`n=164`) |

**Einordnung:** Für Lehrkräfte ist der private Laptop derzeit der erwartete Hauptzugang. Das ist für Datenschutz, technische Unterstützung und die tatsächliche Verfügbarkeit dienstlicher Endgeräte relevant. Für Schulleitungen dominiert dagegen der Schulrechner.

## 5. Einführung und Unterstützung

Mehrfachauswahl, Bezugsgröße: 487 Personen mit mindestens einer Auswahl.

| Einführungshilfe | Nennungen | Anteil |
|---|---:|---:|
| Lernvideos / Webinare | 382 | 78,4 % |
| Schulungen | 274 | 56,3 % |
| Schulungsunterlagen | 177 | 36,3 % |
| KI Bot | 113 | 23,2 % |

### Offene Fragerunde vor dem Rollout

- Ja: 241 von 484 (49,8 %)
- Nein: 243 von 484 (50,2 %)

**Einordnung:** Lernvideos und Webinare sollten den Kern der Einführung bilden. Schulungen bleiben wichtig, während ein KI Bot allein nur eine Minderheit anspricht. Die exakt geteilte Nachfrage nach einer offenen Fragerunde spricht für ein freiwilliges Ergänzungsangebot, nicht für den einzigen Informationskanal.

## 6. Freitext zum Rollout

Zu Frage 8 liegen 83 Einträge vor. Nach Ausschluss von 26 inhaltsleeren Angaben wie „Nein“, „-“ oder „/“ bleiben 57 inhaltliche Rückmeldungen. Wiederkehrende Themen sind:

- **Informationsdefizit:** Funktionsumfang, Aussehen, Zeitplan, Verbindung zum regionalen Beratungs- und Förderzentrum (rBFZ) und konkrete Nutzung sind für mehrere Personen noch unklar.
- **Einfachheit und Arbeitserleichterung:** Erwartet werden eine intuitive, unkomplizierte und tatsächlich zeitsparende Anwendung. Frühere Testerfahrungen werden teilweise kritisch beschrieben.
- **Schulung und Vorab-Erprobung:** Gewünscht werden Schulungen für ganze Kollegien, kurze Lernangebote, häufig gestellte Fragen (FAQ) und ein Testzugang vor dem Rollout.
- **Zugang und technische Einbindung:** Genannt werden Schulportal, iServ, Schul-ID, Hardwareausstattung und die Frage nach geeigneten Endgeräten.
- **Drucken und Aktenführung:** Förderpläne müssen weiterhin ausgedruckt und abgelegt werden können; auch die Qualität des Drucklayouts wird angesprochen.
- **Datenschutz und Elternbeteiligung:** Datenschutzkonformität sowie sprachliche und technische Hürden auf Elternseite werden als Bedingungen für den Erfolg genannt.
- **Fachliche Passung:** Einzelne Rückmeldungen fordern anpassbare Förderplanformate, ganztägige Betreuung, Arbeits- und Sozialverhalten sowie die Anschlussfähigkeit an bestehende schulische Verfahren.

## 7. Beratung durch das BFZ

Mehrfachauswahl, Bezugsgröße: 423 Personen mit mindestens einer Auswahl.

| Anlass | Nennungen | Anteil |
|---|---:|---:|
| Fortschreibung des individuellen Förderplans | 384 | 90,8 % |
| Bewertung einzelner Schülerleistungen | 375 | 88,7 % |
| Nachteilsausgleich | 353 | 83,5 % |
| Bestimmung des Entwicklungsstands und Gestaltung von Lernarrangements | 327 | 77,3 % |
| Beschaffung geeigneter Lehr-, Lern- und Hilfsmittel | 283 | 66,9 % |
| Schulanmeldung | 273 | 64,5 % |
| individuelles Kompetenz- und Entwicklungsprofil | 211 | 49,9 % |
| Kind-Umfeld-Analyse | 104 | 24,6 % |

**Einordnung:** Das BFZ wird vor allem bei der Fortschreibung von Förderplänen, der Bewertung von Schülerleistungen und beim Nachteilsausgleich einbezogen. Die Kind-Umfeld-Analyse ist deutlich seltener etabliert.

## 8. Abschlussgründe einer Vorbeugenden Maßnahme

Mehrfachauswahl, Bezugsgröße: 412 Personen mit mindestens einer Auswahl.

| Abschlussgrund | Nennungen | Anteil |
|---|---:|---:|
| Vorbeugende Maßnahme war erfolgreich | 367 | 89,1 % |
| Verfahren zur Feststellung eines Anspruchs auf sonderpädagogische Förderung startet | 317 | 76,9 % |
| Schulwechsel; anderes regionales BFZ zuständig | 279 | 67,7 % |
| Maßnahme nicht erfolgreich; weitere Förderung nicht sinnvoll | 76 | 18,4 % |
| Wechsel in eine andere Schulform an derselben Schule | 62 | 15,0 % |
| Andere | 13 | 3,2 % |

Zusätzlich wird im Freitext genannt, dass eine Maßnahme auch enden kann, wenn Eltern keine weitere Förderung wünschen.

## 9. Maßnahmen vor Beantragung einer Vorbeugenden Maßnahme

Mehrfachauswahl, Bezugsgröße: 419 Personen mit mindestens einer Auswahl.

| Maßnahme | Nennungen | Anteil |
|---|---:|---:|
| individualisierende und binnendifferenzierende Arbeitsformen | 409 | 97,6 % |
| umfassende Beratung und Information von Eltern und Schüler | 401 | 95,7 % |
| Zusammenarbeit mit dem BFZ | 363 | 86,6 % |
| Stütz- und Fördermaßnahmen in Kleingruppen oder Einzelförderung | 348 | 83,1 % |
| Nachteilsausgleich / Abweichung / Notenschutz | 346 | 82,6 % |
| Zusammenarbeit mit außerschulischen Fördereinrichtungen | 226 | 53,9 % |
| Zusammenarbeit mit der Schulpsychologie | 218 | 52,0 % |

**Einordnung:** Unterrichtliche Differenzierung und Elternberatung sind fast durchgängig vorgeschaltet. Schulpsychologie und außerschulische Fördereinrichtungen werden nur etwa halb so häufig genannt.

## 10. Beantragung und Dauer der Vorbeugenden Maßnahme

### Beantragung über wen? (`n=417`)

| Antwort | Anzahl | Anteil |
|---|---:|---:|
| Mitarbeiter des regionalen BFZ an der Schule | 231 | 55,4 % |
| sonderpädagogische Lehrkräfte an der Schule | 144 | 34,5 % |
| direkt bei der Leitung des regionalen BFZ | 31 | 7,4 % |
| Andere | 11 | 2,6 % |

Die elf Freitexte unter „Andere“ nennen überwiegend Schulleitung, Inklusionsbeauftragte oder schulinterne Weiterleitungswege zum BFZ.

### Durchschnittliche Dauer (`n=399`)

| Antwort | Anzahl | Anteil |
|---|---:|---:|
| bis zu einem Schuljahr | 212 | 53,1 % |
| anderes | 147 | 36,8 % |
| bis zu einem halben Jahr | 35 | 8,8 % |
| bis zu drei Monaten | 5 | 1,3 % |

136 Personen haben die Auswahl „anderes“ erläutert. Sehr häufig werden mehrere Schuljahre, die gesamte Grundschulzeit oder eine rein fallabhängige Dauer genannt. Die bestehenden Kategorien bilden diese Praxis daher nicht ausreichend ab.

## 11. Freitext zur Vorbeugenden Maßnahme

Zu Frage 14 liegen 50 Einträge vor; 36 davon enthalten nach Ausschluss inhaltsleerer Angaben eine fachliche Aussage. Das deutlichste Thema ist die **Ressourcenlage**: Mindestens 16 der 36 inhaltlichen Rückmeldungen benennen zu wenige BFZ-Stunden, zu wenig sonderpädagogisches Personal, fehlende Zuständigkeit oder zu wenig Zeit und Unterstützung. Weitere Themen:

- Anträge und Abläufe werden als aufwendig erlebt.
- Gewünscht werden mehr Vereinheitlichung und klarere Informationen zu Maßnahmen und Antragszeitpunkten.
- Rollen, Verlässlichkeit und aktive Unterstützung durch BFZ-Kräfte werden unterschiedlich erlebt.
- Vorbeugende Maßnahmen laufen teilweise parallel zu den vorgelagerten Maßnahmen oder enden faktisch erst mit Schulwechsel beziehungsweise Feststellungsverfahren.

## 12. Erste Konsequenzen für den Rollout

1. **Vor dem Rollout einen anschaulichen Systemüberblick veröffentlichen:** Funktionsumfang, Rollen, Zeitplan, rBFZ-Anbindung, Druckansicht und konkrete Arbeitsabläufe zeigen.
2. **Einführung mehrgleisig aufbauen:** kurze Lernvideos/Webinare als Standard, ergänzende Schulungen, kompakte Unterlagen und eine freiwillige offene Fragerunde.
3. **Testzugang oder geführte Demonstration anbieten:** Ein Teil der Befragten kann Nutzen und Bedienbarkeit ohne konkreten Einblick noch nicht belastbar bewerten.
4. **Geräte- und Zugangskonzept rollenspezifisch prüfen:** besonders die hohe erwartete Nutzung privater Laptops durch Lehrkräfte und die starke Nutzung von Schulrechnern durch Schulleitungen.
5. **Druck- und Aktenprozess ausdrücklich absichern:** Ausdruck, Layout und Ablage sind keine Nebenthemen, sondern Teil des realen Arbeitsprozesses.
6. **VM-Dauerkategorien für die nächste Befragung überarbeiten:** mindestens „länger als ein Schuljahr“, „mehrere Schuljahre“ und „fallabhängig“ ergänzen.
7. **Ressourcenthema getrennt vom Software-Rollout behandeln:** ila kann Abläufe unterstützen, löst aber den mehrfach genannten Mangel an BFZ-Stunden und sonderpädagogischem Personal nicht.

## 13. Grenzen der Erstanalyse

- keine Bereinigung uneinheitlicher Schulnamen
- keine Gewichtung nach Schulamtsbezirk, Schulgröße oder Rolle
- kleine Fallzahl für die Schulverwaltung (`n=4`), daher keine belastbare eigene Teilgruppenanalyse
- unterschiedliche Bezugsgrößen durch Teilabbrüche und fehlende Antworten
- Mehrfachauswahlfragen erlauben keine Aussage über Prioritäten zwischen gleichzeitig gewählten Optionen
- qualitative Themen sind eine erste inhaltliche Bündelung, noch keine vollständige systematische Codierung
- Exportfehler oder Fehlkonfiguration bei sämtlichen Punktespalten; diese wurden nicht verwendet
