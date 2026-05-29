# Hessische Anforderungen an Barrierefreiheit

Stand: 2026-05-29  
Kontext: erster Überblick für das ila-Repo mit Fokus auf Anforderungen für öffentliche Stellen in Hessen, insbesondere für digitale Anwendungen, Webanwendungen, Dokumente und IKT-Produkte (Informations- und Kommunikationstechnik-Produkte).

---

## 1. Worum es hier geht

Für ila als Teil der LUSD ist Barrierefreiheit kein optionales Qualitätsthema, sondern eine rechtliche und fachliche Anforderung.

Maßgeblich sind für Hessen insbesondere:

- das **Hessische Behinderten-Gleichstellungsgesetz (HessBGG)**
- die **Hessische Verordnung über barrierefreie Informationstechnik (BITV HE 2019)**
- die darin herangezogene **EN 301 549** als europäische Norm
- praktisch umgesetzt in der Regel über die **WCAG 2.1, mindestens Konformitätsstufe AA**

Die hessischen Anforderungen betreffen nicht nur klassische Websites, sondern grundsätzlich auch:

- Webanwendungen
- mobile Anwendungen (Apps)
- Software
- digitale Verwaltungsverfahren
- Dokumente, insbesondere PDF- und Word-Dateien
- weitere IKT-Produkte öffentlicher Stellen

---

## 2. Zentrale rechtliche Anforderungen in Hessen

### 2.1 HessBGG und BITV HE

Nach den Informationen des Landeskompetenzzentrums für Barrierefreie IT Hessen (LBIT) gilt in Hessen die **BITV HE** als maßgebliche Verordnung für barrierefreie Informationstechnik auf Landesebene.

Sie stützt sich auf § 14 HessBGG und legt die Anforderungen an die Barrierefreiheit von IKT-Produkten öffentlicher Stellen fest.

### 2.2 EN 301 549 als technischer Maßstab

Die hessische Verordnung verweist auf die **EN 301 549**. Darin sind die konkreten Anforderungen an barrierefreie Gestaltung digitaler Produkte beschrieben.

Für Hessen gilt dabei mindestens:

- **Konformität auf Stufe AA**

Das ist für praktische Umsetzungen besonders wichtig, weil damit die WCAG-Anforderungen (Web Content Accessibility Guidelines, internationale Richtlinien für barrierefreie Webinhalte) faktisch der zentrale Umsetzungsmaßstab werden.

### 2.3 Erklärung zur Barrierefreiheit und Feedback-Mechanismus

Für einzelne IKT-Produkte öffentlicher Stellen sind zusätzlich erforderlich:

- eine **Erklärung zur Barrierefreiheit**
- ein **Feedback-Mechanismus**, über den Barrieren gemeldet werden können

Das ist keine Nebensache, sondern ein explizit genannter Bestandteil der hessischen Anforderungen.

---

## 3. Was das praktisch für ila bedeutet

Für ila als digitale Fachanwendung im öffentlichen Kontext bedeutet das mindestens:

### 3.1 Für Webanwendung und Oberfläche

Die Anwendung muss so gestaltet sein, dass sie mit assistiven Technologien nutzbar ist. Dazu gehören insbesondere:

- vollständige oder weitgehend vollständige **Tastaturbedienbarkeit**
- sinnvolle **Fokusführung** und klar sichtbarer Fokus
- ausreichende **Farbkontraste**
- verständliche **Struktur und Navigation**
- korrekte technische Auszeichnung von Bedienelementen, Rollen und Zuständen
- keine Information ausschließlich über Farbe
- Formulare, Hinweise und Fehlermeldungen müssen verständlich und zugänglich sein
- kompatible Nutzung mit **Screenreadern**

### 3.2 Für Dokumente

Wenn ila oder die LUSD Dokumente bereitstellt oder erzeugt, müssen auch diese barrierefrei gedacht werden.

Wichtige Anforderungen laut hessischen Informationsseiten:

- Dokumente müssen **strukturiert** sein, also mit echten Überschriften, Absätzen und Listen arbeiten
- Bilder und grafische Inhalte brauchen **Alternativtexte**
- PDF-Dokumente dürfen keine reinen Bild-PDFs sein
- PDF-Dokumente sollen für **Screenreader lesbar** sein
- als Standard für barrierefreie PDFs wird **PDF/UA** genannt
- Word-Dokumente sollten bereits in der Erstellung barrierefrei aufgebaut werden, weil das die Grundlage für barrierefreie PDFs ist

### 3.3 Für Entwicklungs- und Betriebsprozesse

Barrierefreiheit darf nicht erst am Ende geprüft werden. Sie muss in Anforderungen, Design, Entwicklung, Tests und Abnahme eingehen.

Für ila heißt das sehr konkret:

- Barrierefreiheit muss schon in **User Stories** und **Akzeptanzkriterien** auftauchen
- Designs müssen früh auf Tastaturbedienbarkeit, Fokus, Kontrast und Struktur geprüft werden
- Testfälle müssen Barrierefreiheitsanforderungen mitprüfen
- erzeugte Dokumente und Hilfetexte müssen ebenfalls berücksichtigt werden

---

## 4. Besonders relevante Punkte aus hessischer Sicht

Aus den hessischen Quellen lassen sich für unser Umfeld vor allem diese Punkte ableiten:

1. **Barrierefreiheit betrifft nicht nur Webseiten**, sondern auch Fachverfahren, Webanwendungen, Dokumente und Software.
2. **AA-Niveau ist Mindeststandard**.
3. **Erklärung zur Barrierefreiheit** und **Feedback-Möglichkeit** müssen mitgedacht werden.
4. **Dokumente** sind ausdrücklich Teil der Anforderungen, nicht nur die Oberfläche.
5. Eine vollständige Bewertung gelingt nicht über Bauchgefühl oder einzelne Checklisten, sondern nur über einen **vollständigen Barrierefreiheitstest** gegen die geltenden Kriterien.

---

## 5. Relevanz für ila

Für das ila-Projekt sollten daraus mindestens folgende Arbeitsaufträge abgeleitet werden:

### Kurzfristig

- Prüfen, welche Teile von ila rechtlich und fachlich unter die hessischen Barrierefreiheitsanforderungen fallen
- Prüfen, ob es bereits bestehende Anforderungen oder Prüfstände im LUSD-/HMKB-/HZD-Kontext gibt
- Barrierefreiheit als festen Punkt in Anforderungen, UX und Test verankern
- Dokumenterzeugung und Exportfunktionen gesondert betrachten

### Fachlich / UX

- Wording, Navigation, Fokusführung und Fehlermeldungen auf Barrierefreiheit prüfen
- Farb- und Kontrastsystem prüfen
- Screenreader- und Tastatur-Nutzung als festen Prüffall aufnehmen

### Technisch

- Komponentenbibliothek und Frontend auf semantische und assistive Nutzbarkeit prüfen
- Formulare, Dialoge, Tabellen und Statusanzeigen besonders prüfen
- PDF- und Word-Exporte auf Barrierefreiheit mitdenken

### Organisatorisch

- Klären, wer für Erklärung zur Barrierefreiheit, Pflege, Feedback-Kanal und Nachweis verantwortlich ist
- Klären, wie Barrierefreiheit dokumentiert und getestet wird

---

## 6. Empfohlene nächste Dateien in diesem Ordner

Sinnvoll wären als Nächstes:

- `Checkliste_Barrierefreiheit_ila.md`
- `Barrierefreiheit_offene_Fragen_fuer_LUSD_HMKB_HZD.md`
- `Barrierefreiheit_Dokumente_PDF_Word.md`
- `Barrierefreiheit_Testfaelle_ila.md`

---

## 7. Quellen

1. LBIT Hessen, **Allgemeine Anforderungen der barrierefreien IT**  
   <https://lbit.hessen.de/oeffentliche-stellen/allgemeine-anforderungen-der-barrierefreien-it>

2. LBIT Hessen, **Nationale Gesetzgebung**  
   <https://lbit.hessen.de/oeffentliche-stellen/gesetze-richtlinien/bundesgesetze>

3. LBIT Hessen, **Themenseite barrierefreie Dokumente**  
   <https://lbit.hessen.de/service-beratung/dokumente>

4. LBIT Hessen, **Erklärung zur Barrierefreiheit**  
   <https://lbit.hessen.de/erklaerung-zur-barrierefreiheit>

---

## 8. Kurzfazit

Für Hessen ist klar: Öffentliche digitale Angebote und zugehörige Dokumente müssen barrierefrei gestaltet werden. Für ila bedeutet das, dass Barrierefreiheit künftig nicht nur als Designfrage, sondern als durchgehende Anforderung in **Fachlichkeit, UX, Entwicklung, Test, Dokumentation und Betrieb** behandelt werden muss.
