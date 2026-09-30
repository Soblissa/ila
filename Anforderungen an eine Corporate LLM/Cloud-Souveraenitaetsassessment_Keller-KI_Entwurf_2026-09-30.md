# Cloud-Souveränitätsassessment für die „Keller-KI“

**Stand:** 30.09.2026  
**Status:** Arbeitsentwurf zur Diskussion, keine abschließende Sicherheits-, Datenschutz- oder Vergabebewertung

## 1. Einordnung des vorgestellten Ansatzes

Die Beschreibung „48 Kriterien zur Bewertung von Cloud-Anbietern“ passt zum **Cloud Sovereignty Framework** der Europäischen Kommission. Die offizielle Umsetzungshilfe vom 01.06.2026 ordnet 48 Einzelkriterien acht Souveränitätszielen zu.

Das Framework liefert zwei getrennte Ergebnisse:

1. **SEAL (Sovereignty Effectiveness Assurance Level):** Mindestniveau von 0 bis 4. Maßgeblich ist das schwächste relevante Kriterium; gute Werte in anderen Bereichen gleichen eine kritische Lücke nicht aus.
2. **Sovereignty Score:** gewichteter Vergleichswert für Angebote, die das geforderte Mindestniveau bereits erreichen.

Die Anwendungsprüfung muss deshalb **vor** der Anbieterbewertung festlegen, welches Mindestniveau und welche Kriterien für den konkreten Einsatzzweck erforderlich sind.

## 2. Die 48 Kriterien

### SOV-1 Strategische Souveränität — 8 Kriterien, Gewicht 20 %

1. Kontrolle durch eine Rechtseinheit in der EU beziehungsweise im EWR
2. Risiko eines Kontroll- oder Eigentümerwechsels
3. Einfluss europäischer Beteiligter auf die Produktentwicklung
4. Finanzielle Unabhängigkeit von Kapital außerhalb der EU
5. Wirtschaftlicher Beitrag innerhalb der EU beziehungsweise des EWR
6. Beteiligung an strategischen EU-Programmen
7. Übereinstimmung mit europäischen Industrie- und Souveränitätsstrategien
8. Fortbetriebsfähigkeit bei Wegfall oder Unterbrechung externer Unterstützung

### SOV-2 Rechtliche und jurisdiktionelle Souveränität — 6 Kriterien, Gewicht 10 %

9. Primär anwendbare Rechtsordnung
10. Einfluss extraterritorialer Gesetze aus Drittstaaten
11. Rechtliche, vertragliche oder technische Zugriffswege aus Drittstaaten
12. Exportkontrollbeschränkungen
13. Herkunft der geistigen Eigentumsrechte
14. Rechtsordnung des Rechteinhabers

### SOV-3 Daten- und KI-Souveränität — 5 Kriterien, Gewicht 10 %

15. Kontrolle des Kunden über Verschlüsselungsschlüssel
16. Transparente Datenflüsse und Zugriffsprotokolle, einschließlich KI-Nutzung
17. Sichere Löschung mit überprüfbarem Löschungsnachweis
18. Ausschließliche Speicherung und Verarbeitung in EU beziehungsweise EWR
19. Entwicklung, Training, Betrieb und Steuerung der KI-Dienste unter europäischer Kontrolle

### SOV-4 Operative Souveränität — 6 Kriterien, Gewicht 15 %

20. Portabilität und Interoperabilität ohne Anbieterbindung
21. Betrieb ohne kritische Abhängigkeit von Stellen außerhalb der EU
22. Verfügbarkeit des benötigten Fachwissens innerhalb der EU
23. Support innerhalb der EU und unter europäischer Rechtsordnung
24. Vollständige Dokumentation und Wissenstransfer
25. Rechtsordnung und Kontrolle kritischer Unterauftragnehmer und Lieferanten

### SOV-5 Lieferkettensouveränität — 7 Kriterien, Gewicht 10 %

26. Herkunft wesentlicher physischer Komponenten
27. Herstellungs- und Montagestandorte der Hardware
28. Herkunft und Rechtsordnung von Firmware und eingebettetem Code
29. Herkunft und Entwicklung der Software
30. Kontrolle über Paketierung, Verteilung und Aktualisierung der Software
31. Kritische Einzelabhängigkeiten von Anbietern, Einrichtungen oder proprietärer Technik außerhalb der EU
32. Transparenz und Prüfbarkeit der vollständigen Liefer- und Unterlieferantenkette

### SOV-6 Technologische Souveränität — 5 Kriterien, Gewicht 15 %

33. Offene, dokumentierte und nicht proprietäre Schnittstellen
34. Nutzung öffentlich geregelter und breit etablierter offener Standards
35. Verfügbarkeit der Software unter offenen Lizenzen einschließlich Prüf-, Änderungs- und Weitergaberechten
36. Transparenz der Architektur, Datenflüsse und Abhängigkeiten
37. Europäische Unabhängigkeit bei Hochleistungsrechnern, Beschleunigern und Software-Ökosystemen

### SOV-7 Sicherheits- und Compliance-Souveränität — 7 Kriterien, Gewicht 15 %

38. Anerkannte Sicherheitszertifizierungen und Prüfberichte
39. Nachgewiesene Einhaltung einschlägiger EU-Regelungen
40. Sicherheitsüberwachung und Behandlung von Vorfällen innerhalb der EU
41. Direkter Kundenzugriff auf Sicherheitsprotokolle, Warnungen und Überwachung
42. Transparente und fristgerechte Meldung von Sicherheitsvorfällen
43. Unabhängigkeit bei Entwicklung, Prüfung und Einspielung von Sicherheitsaktualisierungen
44. Möglichkeit unabhängiger Sicherheits- und Compliance-Prüfungen

### SOV-8 Ökologische Nachhaltigkeit — 4 Kriterien, Gewicht 5 %

45. Energieeffizienz und messbare Verbesserungsziele
46. Wiederverwendung, Aufarbeitung und Recycling der Hardware
47. Transparente Berichterstattung zu Emissionen, Wasser- und Ressourcenverbrauch
48. Nutzung erneuerbarer oder CO₂-armer Energie

## 3. Anwendungsassessment für die Keller-KI

### Schritt A — Schutzbedarf und Einsatzgrenzen bestimmen

| Prüffeld | Vorläufige Einordnung Phase 1 | Klärungsbedarf |
|---|---|---|
| Zweck | Interner Wissens-, AWA- und Testfallassistent | Verbindliche Liste der freigegebenen Anwendungsfälle |
| Nutzerkreis | Rund 60 berechtigte HMKB-/LUSD-Beteiligte | Rollen, Administration und externe Dienstleister |
| Daten | Interne Fach- und Projektdokumente | Schutzbedarfsfeststellung pro Dokumentenklasse |
| Personenbezogene Daten | Technisch möglich, für Phase 1 zunächst auszuschließen | Verbindliche Upload-Regeln und technische Filter |
| Schülerdaten / besondere Kategorien | Nicht für Phase 1 vorgesehen | Explizites Verbot, Kontrollen und Behandlung von Fehl-Uploads |
| Datenquellen | Manueller Export und kontrollierter Import | Freigabe- und Aktualisierungsprozess |
| Systemanbindung | Keine Live-Anbindung an ADO oder SharePoint | Phase 2 separat bewerten |
| Kritikalität | Unterstützendes System, kein führendes Fachverfahren | Zulässige Ausfallzeit und Wiederanlaufziel festlegen |
| Entscheidungswirkung | Ergebnisse werden von Menschen geprüft und übernommen | Keine automatisierten Verwaltungsentscheidungen |
| Modellnutzung | Lokal betriebenes Sprachmodell mit lokaler Wissensdatenbank | Keine Nutzung der Eingaben für externes Training sicherstellen |
| Protokollierung | Erforderlich für Zugriffe, Administration und KI-Nutzung | Aufbewahrung, Auswertung und Datenschutz festlegen |
| Betriebsort | EU-Rechenzentrum außerhalb des Hessennetzes vorgesehen | Anbieter, Standorte, Backups und Supportorte nachweisen |

### Schritt B — Vorläufiges Anforderungsniveau

Für die beschriebene **Phase 1 ohne Schüler- und sonstige besonders schützenswerte personenbezogene Daten** ist als Arbeitshypothese mindestens **SEAL-2 (Datensouveränität)** anzusetzen. Für den Regelbetrieb im Umfeld des HMKB ist **SEAL-3 (digitale Resilienz)** das sinnvollere Ziel, soweit der Markt und das Budget dies ermöglichen.

**SEAL-4** ist für den geplanten Technikaufbau voraussichtlich nicht realistisch: Selbst bei europäischem Betrieb bleiben kritische Abhängigkeiten von nicht-europäischer Hardware, insbesondere Grafikbeschleunigern, und möglicherweise von nicht-europäischen KI-Modellen bestehen.

Die Einstufung ändert sich wesentlich, sobald eine der folgenden Erweiterungen hinzukommt:

- Verarbeitung echter Schüler-, Personal- oder Falldaten
- Live-Anbindung an ADO, SharePoint oder weitere Systeme im Hessennetz
- Nutzung als führendes oder entscheidungsrelevantes System
- automatisierte Übernahme von Ergebnissen ohne menschliche Prüfung
- besonders hohe Verfügbarkeits- oder Geheimschutzanforderungen

Diese Ausbaustufe ist als eigenes Assessment zu behandeln und spricht eher für einen Betrieb in der VerfahrensCloud Hessen, im Hessennetz oder in einer vergleichbar kontrollierten privaten Umgebung.

## 4. Mindestanforderungen vor einer Anbieterbewertung

Folgende Punkte sollten als Ausschlusskriterien behandelt werden, nicht nur als verrechenbare Pluspunkte:

1. Vertragspartner und anwendbares Recht in EU beziehungsweise EWR
2. Speicherung, Verarbeitung, Protokolle, Backups und reguläre Supportzugriffe ausschließlich in EU beziehungsweise EWR
3. Vollständige Liste aller Unterauftragnehmer und Betriebsstandorte
4. Keine Nutzung von HMKB-Daten zum Training allgemeiner Modelle
5. Mandantentrennung und rollenbasierte Zugriffssteuerung
6. Verschlüsselung bei Speicherung und Übertragung; Regelung zur Schlüsselkontrolle
7. Nachvollziehbare und überprüfbare Löschung einschließlich Backups
8. Kundenzugriff auf Zugriffs-, Administrations- und Sicherheitsprotokolle
9. Definierte Meldewege und Reaktionszeiten für Sicherheitsvorfälle
10. Export der Daten, Wissensbestände, Konfigurationen und Protokolle in dokumentierten Formaten
11. Vertraglich geregelter Exit einschließlich Löschung, Übergabe und Fortbetriebsunterstützung
12. Aktuelles C5-Testat Typ 2 für den tatsächlich angebotenen Dienst und Betriebsumfang
13. Geeigneter Nachweis eines Informationssicherheitsmanagementsystems, beispielsweise ISO/IEC 27001 auf Basis von IT-Grundschutz oder ein gleichwertiger Nachweis
14. Prüf- und Auditrechte für HMKB beziehungsweise beauftragte unabhängige Stellen
15. Technische Sicherheitsprüfung der Anwendungsschicht zusätzlich zur Prüfung des Cloud-Anbieters

## 5. Vorläufige Bewertung der geplanten Keller-KI

Eine belastbare Punktzahl ist ohne konkreten Anbieter und dessen Nachweise nicht möglich. Für die bisher geplante Architektur ergibt sich dennoch ein erstes Profil:

| Bereich | Vorläufige Tendenz | Begründung |
|---|---|---|
| Strategisch | offen | Anbieter, Eigentümerstruktur und Fortbetriebsmodell fehlen |
| Rechtlich | offen | Vertragspartner, Konzernstruktur und Drittstaatenzugriffe fehlen |
| Daten und KI | mittel bis gut gestaltbar | Lokaler Modellbetrieb und lokale Wissensdatenbank helfen; Schlüsselkontrolle, Logs und Löschung sind noch zu definieren |
| Operativ | mittel | Offener Software-Stack ist portierbar; Betrieb, Support und Wissenstransfer sind noch nicht geregelt |
| Lieferkette | begrenzt | Abhängigkeit von NVIDIA-Hardware und weiteren nicht-europäischen Komponenten |
| Technologie | gut gestaltbar | Offene Komponenten und dokumentierte Schnittstellen sind möglich; Modelllizenz und tatsächliche Austauschbarkeit müssen geprüft werden |
| Sicherheit und Compliance | offen | C5 Typ 2, Zertifizierungen, Überwachung, Vorfallmanagement und Auditrechte sind anbieterspezifisch |
| Nachhaltigkeit | offen | Erst mit Rechenzentrumsdaten und Anbieterberichten bewertbar |

### Vorläufiges Fazit

Die Keller-KI ist für ein kontrolliertes Pilotvorhaben grundsätzlich cloudfähig, wenn Phase 1 konsequent von personenbezogenen und besonders schützenswerten Daten getrennt wird. Der entscheidende Engpass ist nicht das Sprachmodell, sondern der nachweisbare Betriebsrahmen: Rechtsordnung, Datenorte, Support, Unterauftragnehmer, Sicherheitsnachweise, Protokollzugriff und Exit-Fähigkeit.

## 6. Benötigte Nachweise für das echte Assessment

- Name und genaue Leistungsbeschreibung des Cloud-Anbieters
- Rechts- und Konzernstruktur
- Liste der Rechenzentrums-, Backup- und Supportstandorte
- Liste der Unterauftragnehmer
- C5-Prüfbericht Typ 2 einschließlich Geltungsbereich, Zeitraum und Abweichungen
- ISO-Zertifikate einschließlich Geltungsbereich
- Auftragsverarbeitungsvertrag und technische-organisatorische Maßnahmen
- Architektur- und Datenflussdarstellung
- Verschlüsselungs- und Schlüsselkonzept
- Rollen- und Berechtigungskonzept
- Protokollierungs- und Überwachungskonzept
- Lösch- und Aufbewahrungskonzept
- Notfall-, Wiederanlauf- und Exit-Konzept
- Lizenz- und Herkunftsnachweise für Modelle und Softwarekomponenten
- Energie- und Nachhaltigkeitskennzahlen des Rechenzentrums

## 7. Quellen

- Europäische Kommission: Cloud Sovereignty Framework – Implementation Guidance, 01.06.2026: <https://commission.europa.eu/document/download/2ad80a48-166f-4c77-a513-80c53ca2a128_en?filename=Cloud+Sovereignty+Framework+-+Implementation+guidance.pdf>
- Europäische Kommission: Sovereignty Assessment Calculator, 01.06.2026: <https://commission.europa.eu/document/download/3acb8fe8-8a4a-4339-ae74-f56138d913d1_en?filename=Annex%20-%20Sovereignty%20assessment%20calculator.xlsx>
- HZD: Reif für die Cloud? – Cloud-Readiness-Assessments: <https://hzd.hessen.de/medienraum/publikationen/hzd-inform/inform-1-23/magazin-reif-fuer-die-cloud>
- HZD: Support in Sachen Sicherheit – externe Cloud-Nutzung und C5 Typ 2: <https://hzd.hessen.de/support-in-sachen-sicherheit>
- BSI: C5 – Antworten zum Mindeststandard für externe Cloud-Dienste: <https://www.bsi.bund.de/DE/Themen/Oeffentliche-Verwaltung/Mindeststandards/Externe_Cloud-Dienste/FAQ_MST_Externe_Cloud-Dienste/faq_mst_Externe_Cloud-Dienste_node.html>
