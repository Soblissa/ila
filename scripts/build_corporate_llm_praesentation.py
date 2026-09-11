#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Baut die Präsentation "Corporate LLM für das HMKB — die Keller-KI".

Grundlage: Gesprächsprotokoll 29.08.2026 (memory/2026-09-07-0537.md),
Stand nach Klärung: SharePoint on-premise, Azure DevOps Server 2016 on-premise.

Vorlage: ila/pilot-ergebnisse/PowerPoint-Vorlage_HMKB.pptx
Ausgabe: ila/Anforderungen an eine Corporate LLM/Corporate_LLM_HMKB_Praesentation.pptx

Aufruf:  ~/.venvs/pptx/bin/python ila/scripts/build_corporate_llm_praesentation.py
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(BASE, "pilot-ergebnisse", "PowerPoint-Vorlage_HMKB.pptx")
OUTDIR = os.path.join(BASE, "Anforderungen an eine Corporate LLM")
OUTFILE = os.path.join(OUTDIR, "Corporate_LLM_HMKB_Praesentation.pptx")

# Hessen-Farben (STK-Erlass Corporate Design)
ROT = RGBColor(0xE1, 0x00, 0x1A)
DUNKELBLAU = RGBColor(0x1F, 0x3B, 0x63)
GRUEN = RGBColor(0x00, 0x7A, 0x33)
GRAU = RGBColor(0x59, 0x59, 0x59)
HELLGRAU = RGBColor(0xEF, 0xEF, 0xEF)
WEISS = RGBColor(0xFF, 0xFF, 0xFF)

LAYOUT_TITEL = 0        # Titelfolie - Standard
LAYOUT_TEXT = 3         # Standard-Textfolie
LAYOUT_NUR_TITEL = 6    # Textfolie nur Überschrift

prs = Presentation(TEMPLATE)
# Vorlagenfolien entfernen, nur Layouts behalten
for i in range(len(prs.slides) - 1, -1, -1):
    rid = prs.slides._sldIdLst[i].rId
    prs.part.drop_rel(rid)
    del prs.slides._sldIdLst[i]

SW = prs.slide_width
SH = prs.slide_height


def titelfolie(titel, untertitel):
    s = prs.slides.add_slide(prs.slide_layouts[LAYOUT_TITEL])
    s.placeholders[0].text = titel
    s.placeholders[1].text = untertitel
    return s


def textfolie(titel):
    s = prs.slides.add_slide(prs.slide_layouts[LAYOUT_TEXT])
    s.shapes.title.text = titel
    return s


def bullets(slide, items, size=16, idx=1):
    """items: Liste aus str oder (text, level) oder (text, level, bold)."""
    tf = slide.placeholders[idx].text_frame
    tf.clear()
    tf.word_wrap = True
    first = True
    for it in items:
        bold = False
        if isinstance(it, tuple):
            if len(it) == 3:
                text, level, bold = it
            else:
                text, level = it
        else:
            text, level = it, 0
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.text = text
        p.level = level
        for r in p.runs:
            r.font.size = Pt(size if level == 0 else size - 2)
            r.font.bold = bold
            r.font.color.rgb = DUNKELBLAU if bold else GRAU
        p.space_after = Pt(6)
    return tf


def leerflaeche(slide):
    """Platzhalter 1 entfernen, damit freie Flaeche entsteht."""
    ph = slide.placeholders[1]
    ph._element.getparent().remove(ph._element)


def tabelle(slide, daten, left, top, width, height, kopf_farbe=DUNKELBLAU,
            size=12, spaltenbreiten=None):
    rows, cols = len(daten), len(daten[0])
    gf = slide.shapes.add_table(rows, cols, left, top, width, height)
    tbl = gf.table
    if spaltenbreiten:
        for i, w in enumerate(spaltenbreiten):
            tbl.columns[i].width = w
    for r, zeile in enumerate(daten):
        for c, wert in enumerate(zeile):
            cell = tbl.cell(r, c)
            cell.text = str(wert)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            cell.margin_left = Inches(0.08)
            cell.margin_right = Inches(0.08)
            cell.margin_top = Inches(0.03)
            cell.margin_bottom = Inches(0.03)
            para = cell.text_frame.paragraphs[0]
            para.font.size = Pt(size)
            if r == 0:
                para.font.bold = True
                para.font.color.rgb = WEISS
                cell.fill.solid()
                cell.fill.fore_color.rgb = kopf_farbe
            else:
                para.font.color.rgb = GRAU
                cell.fill.solid()
                cell.fill.fore_color.rgb = WEISS if r % 2 else HELLGRAU
    return tbl


def kasten(slide, left, top, width, height, titel, zeilen, farbe,
           titel_size=14, text_size=12):
    from pptx.enum.shapes import MSO_SHAPE
    sh = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    sh.fill.solid()
    sh.fill.fore_color.rgb = WEISS
    sh.line.color.rgb = farbe
    sh.line.width = Pt(1.5)
    sh.shadow.inherit = False
    tf = sh.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.16)
    tf.margin_right = Inches(0.16)
    tf.margin_top = Inches(0.12)
    p = tf.paragraphs[0]
    p.text = titel
    p.alignment = PP_ALIGN.LEFT
    p.runs[0].font.size = Pt(titel_size)
    p.runs[0].font.bold = True
    p.runs[0].font.color.rgb = farbe
    for z in zeilen:
        p = tf.add_paragraph()
        p.text = z if z else "\u00a0"
        for r in p.runs:
            r.font.size = Pt(text_size)
            r.font.color.rgb = GRAU
        p.space_before = Pt(4)
    return sh


def notiz(slide, text):
    slide.notes_slide.notes_text_frame.text = text


# ---------------------------------------------------------------- Folie 1
s = titelfolie(
    "Eine eigene KI für das HMKB",
    "Corporate LLM im Eigenbetrieb — was mit und was ohne die HZD möglich ist\n"
    "Referat IV. 2.1  ·  Stand: 11.09.2026",
)
notiz(s, "Einstieg: Wir sprechen über eine KI, die dem HMKB gehört und im eigenen Haus "
         "läuft. Kein Cloud-Dienst, keine Daten bei Dritten. Die zentrale Frage ist nicht "
         "'geht das technisch', sondern 'wie weit kommen wir ohne die HZD'.")

# ---------------------------------------------------------------- Folie 2
s = textfolie("Worum es geht")
bullets(s, [
    ("Die Ausgangslage", 0, True),
    ("Testfälle werden heute händisch pro AWA erstellt — fehleranfällig und langsam", 1),
    ("Verfahrensdokumentation wird händisch gepflegt und als PDF abgelegt", 1),
    ("Wissen über die LUSD steckt in Köpfen, ADO-Tickets und SharePoint-Dokumenten", 1),
    ("", 0),
    ("Der Vorschlag", 0, True),
    ("Ein Corporate LLM — eine Sprach-KI, die dem HMKB gehört und im Eigenbetrieb läuft", 1),
    ("Alle Daten bleiben im Haus. Kein Cloud-Anbieter, keine Weitergabe an Dritte", 1),
    ("Budgetrahmen: maximal 100.000 € über zwei Jahre", 1),
    ("", 0),
    ("Der Kern dieser Präsentation", 0, True),
    ("Es gibt einen Weg, der sofort funktioniert — ganz ohne die HZD", 1),
    ("Und einen Vollausbau, der ohne die HZD nicht geht", 1),
], size=15)
notiz(s, "Wichtig: nicht mit Technik einsteigen. Der Schmerz ist bekannt — händische "
         "Testfälle und Doku. Die Frage ans Referat lautet später: wollen wir Phase 1 "
         "starten, ohne auf die HZD zu warten?")

# ---------------------------------------------------------------- Folie 3
s = textfolie("Was eine „Keller-KI\u201c ist")
leerflaeche(s)
top = Inches(1.35)
h = Inches(1.55)
w = Inches(2.15)
gap = Inches(0.18)
left = Inches(0.5)
for titel, zeilen, farbe in [
    ("Das Modell", ["Die Sprach-KI selbst.", "Läuft lokal auf eigener", "Hardware — offline."], DUNKELBLAU),
    ("Die Oberfläche", ["Ein Browser-Fenster,", "wie man es von", "Chatdiensten kennt."], DUNKELBLAU),
    ("Die Wissens-\ndatenbank", ["Eigene Dokumente,", "durchsuchbar gemacht.", "AWAs, Handbücher, Doku."], GRUEN),
    ("Die Agenten", ["Vorkonfigurierte Helfer", "für wiederkehrende", "Aufgaben."], GRUEN),
]:
    kasten(s, left, top, w, h, titel, zeilen, farbe, titel_size=13, text_size=11)
    left += w + gap

tabelle(s, [
    ["Baustein", "Software", "Lizenzkosten"],
    ["Modellbetrieb", "Ollama", "0 € — Open Source"],
    ["Benutzeroberfläche", "Open WebUI", "0 € — Open Source"],
    ["Wissensdatenbank", "Qdrant (Vektordatenbank)", "0 € — Open Source"],
    ["Dokumentensuche", "RAG-Verfahren", "0 € — Open Source"],
], Inches(0.5), Inches(3.15), Inches(9.0), Inches(1.9), size=12,
   spaltenbreiten=[Inches(2.6), Inches(3.6), Inches(2.8)])
notiz(s, "RAG = die KI schlägt in den eigenen Dokumenten nach, bevor sie antwortet. "
         "Dadurch erfindet sie deutlich weniger. Alle vier Bausteine sind Open Source — "
         "es fallen keine Lizenzkosten an, nur Hardware und Arbeit.")

# ---------------------------------------------------------------- Folie 4
s = textfolie("Hardware und Modellauswahl")
leerflaeche(s)
kasten(s, Inches(0.5), Inches(1.35), Inches(4.3), Inches(1.5),
       "Hardware-Empfehlung",
       ["NVIDIA RTX A6000 Ada, 48 GB Grafikspeicher",
        "in einem Dell PowerEdge Server",
        "15.000 – 20.000 € einmalig"], DUNKELBLAU, titel_size=14, text_size=12)
kasten(s, Inches(5.2), Inches(1.35), Inches(4.3), Inches(1.5),
       "Was die Hardware leistet",
       ["Modelle bis 32 Milliarden Parameter",
        "10 – 20 gleichzeitige Nutzer",
        "bei rund 60 Berechtigten insgesamt"], GRUEN, titel_size=14, text_size=12)

tabelle(s, [
    ["Modell", "Herkunft", "Qualität Deutsch", "Einordnung"],
    ["Mistral Small 3.2 (24B)", "Frankreich", "Gut", "1. Wahl — EU-Anbieter, Apache 2.0"],
    ["Qwen 2.5 (32B)", "China", "Sehr gut", "2. Wahl — beste Qualität"],
    ["Llama 4 Scout", "USA", "Befriedigend", "Rückfalloption"],
], Inches(0.5), Inches(3.15), Inches(9.0), Inches(1.6), size=12,
   spaltenbreiten=[Inches(2.5), Inches(1.5), Inches(1.7), Inches(3.3)])

tb = s.shapes.add_textbox(Inches(0.5), Inches(4.85), Inches(9.0), Inches(0.4)).text_frame
tb.word_wrap = True
p = tb.paragraphs[0]
p.text = ("Mehrere Modelle laufen parallel auf derselben Hardware und lassen sich "
          "per Klick wechseln. Die Entscheidung ist nicht endgültig.")
p.runs[0].font.size = Pt(11)
p.runs[0].font.italic = True
p.runs[0].font.color.rgb = GRAU
notiz(s, "Mistral ist die politisch und rechtlich sauberste Wahl: EU-Anbieter, freie "
         "Apache-Lizenz. Qwen ist qualitativ besser, kommt aber aus China — das kann "
         "in der Behörde eine Diskussion auslösen. Deshalb: beide installieren, "
         "Referat entscheidet nach eigenem Test.")

# ---------------------------------------------------------------- Folie 5
s = textfolie("Kosten über zwei Jahre")
leerflaeche(s)
tabelle(s, [
    ["Posten", "Betrag"],
    ["Hardware (Server inkl. Grafikkarte)", "15.000 – 20.000 €"],
    ["Einrichtung und Konfiguration", "18.000 – 30.000 €"],
    ["Betrieb und Wartung (24 Monate)", "15.000 – 27.000 €"],
    ["Puffer", "5.000 – 10.000 €"],
    ["Gesamt", "53.000 – 87.000 €"],
], Inches(1.2), Inches(1.4), Inches(7.6), Inches(2.8), size=14,
   spaltenbreiten=[Inches(5.0), Inches(2.6)])

kasten(s, Inches(1.2), Inches(4.35), Inches(7.6), Inches(0.85),
       "Ergebnis",
       ["Der Budgetrahmen von 100.000 € wird in jeder Variante eingehalten — "
        "auch im oberen Kostenszenario bleibt Luft."], GRUEN, titel_size=14, text_size=12)
notiz(s, "Keine Lizenzkosten, weil der gesamte Software-Stack Open Source ist. "
         "Der größte Posten ist Arbeitszeit, nicht Technik. Nach zwei Jahren gehört "
         "die Hardware dem HMKB — keine wiederkehrende Abo-Gebühr.")

# ---------------------------------------------------------------- Folie 6
s = textfolie("Die entscheidende Hürde: das Hessennetz")
bullets(s, [
    ("Alle HMKB-Fachsysteme laufen im Hessennetz — einem geschlossenen Behördennetz.", 0, True),
    ("", 0),
    ("Was das konkret bedeutet", 0, True),
    ("SharePoint läuft on-premise bei der HZD — von außen nicht erreichbar", 1),
    ("Azure DevOps Server 2016 läuft ebenfalls on-premise bei der HZD", 1),
    ("Eine Live-Anbindung von außen ist damit technisch ausgeschlossen. Ohne Ausnahme.", 1),
    ("", 0),
    ("Was das nicht bedeutet", 0, True),
    ("Die Keller-KI selbst funktioniert vollständig — sie braucht keinen Netzzugang "
     "zu diesen Systemen, um zu arbeiten", 1),
    ("Nur der automatische Datenfluss in beide Richtungen entfällt", 1),
    ("", 0),
    ("Der Vollausbau ist deshalb kein Antrag auf eine Firewall-Regel, sondern "
     "perspektivisch eine Kooperation mit der HZD.", 0, True),
], size=14)
notiz(s, "Das ist die Folie, auf der die ehrliche Einordnung passiert. Nicht "
         "beschönigen: eine einfache Netzwerkfreigabe ist es nicht. Auch kleine "
         "Freigaben durchlaufen bei der HZD lange Genehmigungsprozesse — "
         "IT-Sicherheitskonzept, Datenschutzfolgeabschätzung. Beantragen heißt nicht "
         "durchsetzen. Deshalb bauen wir Phase 1 so, dass sie ohne die HZD trägt.")

# ---------------------------------------------------------------- Folie 7
s = textfolie("Zwei Wege — mit und ohne HZD")
leerflaeche(s)

kasten(s, Inches(0.45), Inches(1.3), Inches(4.4), Inches(3.55),
       "Phase 1 — sofort startbar",
       ["Abhängig von der HZD:  nein",
        "",
        "KI-Server läuft außerhalb des Hessennetzes,",
        "in einem EU-Rechenzentrum, DSGVO-konform",
        "",
        "Dokumente werden manuell exportiert und in",
        "die Wissensdatenbank geladen",
        "",
        "Alle Agenten laufen vollständig:",
        "AWA-Assistent, Testfall-Generator,",
        "Wissensassistent",
        "",
        "Ergebnisse werden manuell in ADO eingetragen",
        "— so wie heute, nur erheblich schneller"], GRUEN, titel_size=15, text_size=11)

kasten(s, Inches(5.15), Inches(1.3), Inches(4.4), Inches(3.55),
       "Phase 2 — Vollausbau",
       ["Abhängig von der HZD:  ja",
        "",
        "KI-Server steht physisch im Hessennetz",
        "",
        "Live-Zugriff auf Azure DevOps und SharePoint",
        "in beide Richtungen",
        "",
        "Mitarbeitende öffnen die KI direkt im Browser",
        "am HessenPC — keine Installation nötig",
        "",
        "Voraussetzung: eigener Serverraum beim HMKB",
        "oder Kooperation mit der HZD",
        "",
        "Zeitpunkt offen — politisch, nicht technisch"], ROT, titel_size=15, text_size=11)

tb = s.shapes.add_textbox(Inches(0.45), Inches(4.95), Inches(9.1), Inches(0.4)).text_frame
tb.word_wrap = True
p = tb.paragraphs[0]
p.text = "Phase 1 liefert rund 80 % des Nutzens — und ist vollständig unabhängig lieferbar."
p.alignment = PP_ALIGN.CENTER
p.runs[0].font.size = Pt(13)
p.runs[0].font.bold = True
p.runs[0].font.color.rgb = DUNKELBLAU
notiz(s, "Kernbotschaft der Präsentation. Phase 1 ist kein Kompromiss und keine "
         "Notlösung, sondern ein vollwertiger erster Schritt. Phase 2 ist ein Ziel, "
         "kein Versprechen — sie hängt an einer Entscheidung, die weder das Referat "
         "noch wir allein treffen können.")

# ---------------------------------------------------------------- Folie 8
s = textfolie("Was sich konkret ändert")
leerflaeche(s)
tb = s.shapes.add_textbox(Inches(0.5), Inches(1.25), Inches(9.0), Inches(0.45)).text_frame
p = tb.paragraphs[0]
p.text = "Von der AWA zum Testfall — in 30 Sekunden"
p.runs[0].font.size = Pt(17)
p.runs[0].font.bold = True
p.runs[0].font.color.rgb = DUNKELBLAU

schritte = [
    ("1", "Mitarbeiterin öffnet die AWA in Azure DevOps"),
    ("2", "Agent liest die AWA und die LUSD-Dokumente aus der Wissensdatenbank"),
    ("3", "Agent erzeugt Normalfall, Sonderfall und Fehlerfall automatisch"),
    ("4", "Mensch prüft das Ergebnis und gibt es frei"),
]
top = Inches(1.85)
for nr, text in schritte:
    kasten(s, Inches(0.5), top, Inches(9.0), Inches(0.55),
           "Schritt " + nr + "   ·   " + text, [], DUNKELBLAU,
           titel_size=12)
    top += Inches(0.68)

kasten(s, Inches(0.5), Inches(4.65), Inches(4.3), Inches(0.62),
       "Heute:  2 – 3 Stunden händisch", [], GRAU, titel_size=13)
kasten(s, Inches(5.2), Inches(4.65), Inches(4.3), Inches(0.62),
       "Künftig:  30 Sekunden + Freigabe", [], GRUEN, titel_size=13)
notiz(s, "Konkretes Beispiel statt abstrakter Nutzenversprechen. Wichtig betonen: "
         "Der Mensch prüft und gibt frei. Die KI ersetzt niemanden, sie nimmt die "
         "stumpfe Vorarbeit ab. Dieser Anwendungsfall funktioniert auch in Phase 1 — "
         "die AWA wird dann exportiert statt live gelesen.")

# ---------------------------------------------------------------- Folie 9
s = textfolie("Geprüft und verworfen")
bullets(s, [
    ("Diese Wege haben wir untersucht und wieder verworfen — der Vollständigkeit halber:", 0, False),
    ("", 0),
    ("Server bei der HZD aufstellen (Colocation)", 0, True),
    ("Technisch elegant, politisch aussichtslos: fremder Server im eigenen Netz, "
     "den die HZD nicht kontrolliert. Dazu Präzedenzfall-Sorge und Eigeninteresse "
     "an eigener KI-Infrastruktur.", 1),
    ("", 0),
    ("Anbindung über Microsoft Azure / Service Principal", 0, True),
    ("Würde funktionieren, wenn die Systeme in der Microsoft-Cloud lägen. "
     "Tun sie nicht — SharePoint und Azure DevOps Server 2016 laufen on-premise.", 1),
    ("", 0),
    ("KI lokal auf den Endgeräten installieren", 0, True),
    ("Der HessenPC lässt keine Software-Installation zu. Ausgeschlossen.", 1),
    ("", 0),
    ("Zugriff über HessenAccess (VPN)", 0, True),
    ("Interessant: Wer über HessenAccess verbunden ist, ist faktisch im Hessennetz "
     "und könnte einen internen KI-Server per Browser erreichen. Setzt aber Phase 2 "
     "voraus — der Server muss erst drin stehen.", 1),
], size=13)
notiz(s, "Diese Folie schafft Vertrauen. Sie zeigt: wir haben nicht nur einen Weg "
         "gefunden, sondern vier geprüft. Wer im Referat kritisch ist, findet hier "
         "seine Einwände bereits behandelt.")

# ---------------------------------------------------------------- Folie 10
s = textfolie("Offene Fragen und nächste Schritte")
bullets(s, [
    ("Zu klären mit dem HMKB", 0, True),
    ("Hat das HMKB einen eigenen Serverraum mit Rack-Infrastruktur — oder läuft "
     "alles über die HZD?", 1),
    ("Wer verwaltet die Microsoft-Tenants des HMKB: das Haus selbst oder die HZD?", 1),
    ("Wer ist der IT-Ansprechpartner für dieses Vorhaben?", 1),
    ("Besteht eine Ausschreibungspflicht?", 1),
    ("Gibt es bereits eine KI-Nutzungsrichtlinie im Haus?", 1),
    ("Wurde das Vorhaben mit dem Datenschutzbeauftragten besprochen?", 1),
    ("Bis wann soll das Angebot vorliegen?", 1),
    ("", 0),
    ("Vorschlag für das weitere Vorgehen", 0, True),
    ("Entscheidung des Referats: Phase 1 starten, ohne auf die HZD zu warten", 1),
    ("Parallel klären, ob Phase 2 mittelfristig realistisch ist", 1),
    ("Nach den Antworten: verbindliches Angebot mit Zeitplan", 1),
], size=14)
notiz(s, "Abschluss mit einer konkreten Entscheidungsfrage, nicht mit einem "
         "Ausblick. Das Referat soll heute nicht Phase 2 beschließen — es soll "
         "entscheiden, ob Phase 1 beginnen darf.")

# ---------------------------------------------------------------- Folie 11
s = titelfolie("Die Kernaussage in einem Satz",
               "Wir können sofort anfangen — ohne die HZD, innerhalb des Budgets, "
               "mit rund 80 % des Nutzens.\nAlles Weitere ist eine politische "
               "Entscheidung, keine technische.")
notiz(s, "Schlussfolie. Bewusst kurz halten und stehen lassen.")

os.makedirs(OUTDIR, exist_ok=True)
prs.save(OUTFILE)
print("Gespeichert:", OUTFILE)
print("Folien:", len(prs.slides.__iter__.__self__._sldIdLst))
