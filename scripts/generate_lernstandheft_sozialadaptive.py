#!/usr/bin/env python3
"""Erstellt ein Lernstandsheft für sozialadaptive Kompetenzen aus Excel."""

from __future__ import annotations

import argparse
from collections import OrderedDict
from itertools import count
from pathlib import Path

import openpyxl
from docx import Document
from docx.enum.section import WD_SECTION_START
from docx.enum.table import WD_ALIGN_VERTICAL, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor


W14 = "http://schemas.microsoft.com/office/word/2010/wordml"
BLUE = "1F457A"
MID_BLUE = "2E74B5"
LIGHT_BLUE = "E8EEF7"
LIGHT_GRAY = "F5F6F8"
GREEN = "E2F5E3"
YELLOW = "FFF8D6"
RED = "FFE4E7"

MAIN_CONFIG = {
    "Lebenspraktische Kompetenzen": ("1", "4472C4"),
    "Soziale Kompetenzen": ("2", "70AD47"),
    "Schulische Kompetenz": ("3", "7030A0"),
}

CHECKBOX_IDS = count(100000)


def rgb(hex_color: str) -> RGBColor:
    value = hex_color.lstrip("#")
    return RGBColor(int(value[0:2], 16), int(value[2:4], 16), int(value[4:6], 16))


def set_cell_bg(cell, fill: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    old = tc_pr.find(qn("w:shd"))
    if old is not None:
        tc_pr.remove(old)
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    tc_pr.append(shd)


def set_cell_margins(cell, top=90, start=90, bottom=90, end=90) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_mar = tc_pr.find(qn("w:tcMar"))
    if tc_mar is None:
        tc_mar = OxmlElement("w:tcMar")
        tc_pr.append(tc_mar)
    for side, value in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = tc_mar.find(qn(f"w:{side}"))
        if node is None:
            node = OxmlElement(f"w:{side}")
            tc_mar.append(node)
        node.set(qn("w:w"), str(value))
        node.set(qn("w:type"), "dxa")


def set_table_borders(table) -> None:
    tbl_pr = table._tbl.tblPr
    existing = tbl_pr.find(qn("w:tblBorders"))
    if existing is not None:
        tbl_pr.remove(existing)
    borders = OxmlElement("w:tblBorders")
    for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
        border = OxmlElement(f"w:{side}")
        border.set(qn("w:val"), "single")
        border.set(qn("w:sz"), "4")
        border.set(qn("w:space"), "0")
        border.set(qn("w:color"), "B7BEC8")
        borders.append(border)
    tbl_pr.append(borders)


def set_table_grid(table, widths_cm: list[float]) -> None:
    tbl_grid = table._tbl.tblGrid
    for child in list(tbl_grid):
        tbl_grid.remove(child)
    for width in widths_cm:
        grid_col = OxmlElement("w:gridCol")
        grid_col.set(qn("w:w"), str(int(width * 567)))
        tbl_grid.append(grid_col)
    for row in table.rows:
        for index, cell in enumerate(row.cells):
            cell.width = Cm(widths_cm[index])


def repeat_table_header(row) -> None:
    tr_pr = row._tr.get_or_add_trPr()
    tbl_header = OxmlElement("w:tblHeader")
    tbl_header.set(qn("w:val"), "true")
    tr_pr.append(tbl_header)


def prevent_row_split(row) -> None:
    tr_pr = row._tr.get_or_add_trPr()
    cant_split = OxmlElement("w:cantSplit")
    tr_pr.append(cant_split)


def keep_with_next(paragraph) -> None:
    p_pr = paragraph._p.get_or_add_pPr()
    keep = OxmlElement("w:keepNext")
    keep.set(qn("w:val"), "true")
    p_pr.append(keep)


def add_checkbox(cell, title: str) -> None:
    paragraph = cell.paragraphs[0]
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.paragraph_format.space_after = Pt(0)

    sdt = OxmlElement("w:sdt")
    sdt_pr = OxmlElement("w:sdtPr")

    alias = OxmlElement("w:alias")
    alias.set(qn("w:val"), title)
    sdt_pr.append(alias)

    tag = OxmlElement("w:tag")
    tag.set(qn("w:val"), title)
    sdt_pr.append(tag)

    sdt_id = OxmlElement("w:id")
    sdt_id.set(qn("w:val"), str(next(CHECKBOX_IDS)))
    sdt_pr.append(sdt_id)

    checkbox = OxmlElement("w14:checkbox")
    checked = OxmlElement("w14:checked")
    checked.set(qn("w14:val"), "0")
    checked_state = OxmlElement("w14:checkedState")
    checked_state.set(qn("w14:val"), "2612")
    checked_state.set(qn("w14:font"), "MS Gothic")
    unchecked_state = OxmlElement("w14:uncheckedState")
    unchecked_state.set(qn("w14:val"), "2610")
    unchecked_state.set(qn("w14:font"), "MS Gothic")
    checkbox.extend([checked, checked_state, unchecked_state])
    sdt_pr.append(checkbox)
    sdt.append(sdt_pr)

    sdt_content = OxmlElement("w:sdtContent")
    run = OxmlElement("w:r")
    run_pr = OxmlElement("w:rPr")
    fonts = OxmlElement("w:rFonts")
    fonts.set(qn("w:ascii"), "MS Gothic")
    fonts.set(qn("w:hAnsi"), "MS Gothic")
    size = OxmlElement("w:sz")
    size.set(qn("w:val"), "22")
    run_pr.extend([fonts, size])
    run.append(run_pr)
    text = OxmlElement("w:t")
    text.text = "☐"
    run.append(text)
    sdt_content.append(run)
    sdt.append(sdt_content)
    paragraph._p.append(sdt)


def read_stage(ws) -> OrderedDict:
    expected = [
        "Sozialadaptive Kompetenzen",
        "Kompetenzbereich",
        "Erfahrungsfeld",
        "Kompetenz",
        "Kompetenz (Der Schüler...)",
        "Erfüllt/nicht erfüllt",
    ]
    headers = [cell.value for cell in ws[1]]
    if headers != expected:
        raise ValueError(f"Unerwartete Spalten in {ws.title}: {headers}")

    structured: OrderedDict = OrderedDict()
    for row in ws.iter_rows(min_row=2, values_only=True):
        main, area, field, formal, observation, _ = row
        if not any(value is not None for value in row):
            continue
        if not all((main, area, field, formal, observation)):
            raise ValueError(f"Unvollständige Kompetenzzeile in {ws.title}: {row}")
        structured.setdefault(main, OrderedDict()).setdefault(area, OrderedDict()).setdefault(field, []).append(
            (str(formal).strip(), str(observation).strip())
        )
    return structured


def add_heading(document: Document, text: str, level: int, color: str | None = None) -> None:
    paragraph = document.add_heading(text, level=level)
    keep_with_next(paragraph)
    if color:
        for run in paragraph.runs:
            run.font.color.rgb = rgb(color)


def add_competency_table(document: Document, competencies: list[tuple[str, str]]) -> None:
    widths = [9.2, 1.5, 1.7, 1.7, 3.8]
    headers = ["Kompetenz / Beobachtung", "Erfüllt", "Teilweise", "Nicht erfüllt", "Bemerkung"]
    table = document.add_table(rows=1, cols=5)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    set_table_borders(table)
    set_table_grid(table, widths)
    repeat_table_header(table.rows[0])

    for index, (cell, header) in enumerate(zip(table.rows[0].cells, headers)):
        cell.text = header
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        set_cell_bg(cell, BLUE)
        set_cell_margins(cell)
        paragraph = cell.paragraphs[0]
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        paragraph.paragraph_format.space_after = Pt(0)
        for run in paragraph.runs:
            run.font.name = "Aptos"
            run.font.size = Pt(8)
            run.font.bold = True
            run.font.color.rgb = RGBColor(255, 255, 255)

    for row_index, (formal, observation) in enumerate(competencies):
        row = table.add_row()
        prevent_row_split(row)
        for cell in row.cells:
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            set_cell_margins(cell)

        text_cell = row.cells[0]
        set_cell_bg(text_cell, LIGHT_BLUE if row_index % 2 else "FFFFFF")
        paragraph = text_cell.paragraphs[0]
        paragraph.paragraph_format.space_after = Pt(2)
        run = paragraph.add_run(f"Der Schüler {observation}")
        run.font.name = "Aptos"
        run.font.size = Pt(9)
        run.font.bold = True
        detail = text_cell.add_paragraph()
        detail.paragraph_format.space_after = Pt(0)
        detail_run = detail.add_run(formal)
        detail_run.font.name = "Aptos"
        detail_run.font.size = Pt(8)
        detail_run.font.italic = True
        detail_run.font.color.rgb = RGBColor(89, 89, 89)

        for col_index, (fill, label) in enumerate(
            ((GREEN, "Erfüllt"), (YELLOW, "Teilweise erfüllt"), (RED, "Nicht erfüllt")), start=1
        ):
            set_cell_bg(row.cells[col_index], fill)
            add_checkbox(row.cells[col_index], label)

        set_cell_bg(row.cells[4], LIGHT_BLUE if row_index % 2 else "FFFFFF")

    document.add_paragraph().paragraph_format.space_after = Pt(2)


def create_document(workbook_path: Path, output_path: Path) -> tuple[int, int]:
    workbook = openpyxl.load_workbook(workbook_path, data_only=True)
    stages = OrderedDict(
        (
            ("Einschulung", read_stage(workbook["Kompetenzen Einschulung"])),
            ("Mittelstufe", read_stage(workbook["Kompetenzen Mittelstufe"])),
        )
    )

    document = Document()
    section = document.sections[0]
    section.top_margin = Cm(1.8)
    section.bottom_margin = Cm(1.8)
    section.left_margin = Cm(1.8)
    section.right_margin = Cm(1.8)

    styles = document.styles
    styles["Normal"].font.name = "Aptos"
    styles["Normal"].font.size = Pt(9.5)
    for style_name, size, color in (
        ("Title", 25, BLUE),
        ("Heading 1", 18, BLUE),
        ("Heading 2", 15, BLUE),
        ("Heading 3", 12, MID_BLUE),
        ("Heading 4", 10, MID_BLUE),
    ):
        style = styles[style_name]
        style.font.name = "Aptos Display"
        style.font.size = Pt(size)
        style.font.color.rgb = rgb(color)
        style.font.bold = True
        style.paragraph_format.space_before = Pt(8)
        style.paragraph_format.space_after = Pt(4)

    header = section.header.paragraphs[0]
    header.text = "Lernstandsheft · Sozialadaptive Kompetenzen"
    header.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    for run in header.runs:
        run.font.name = "Aptos"
        run.font.size = Pt(8)
        run.font.color.rgb = rgb(MID_BLUE)

    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    footer.add_run("Seite ")
    page_field = OxmlElement("w:fldSimple")
    page_field.set(qn("w:instr"), "PAGE")
    footer._p.append(page_field)
    for run in footer.runs:
        run.font.name = "Aptos"
        run.font.size = Pt(8)

    # Titelseite
    title = document.add_paragraph(style="Title")
    title.paragraph_format.space_before = Pt(80)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title.add_run("Lernstandsheft\nSozialadaptive Kompetenzen")
    subtitle = document.add_paragraph()
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub_run = subtitle.add_run("Einschulung und Mittelstufe")
    sub_run.font.name = "Aptos Display"
    sub_run.font.size = Pt(16)
    sub_run.font.color.rgb = rgb(MID_BLUE)
    document.add_paragraph("")
    document.add_paragraph("")
    for label in ("Name", "Geburtsdatum", "Klasse / Stufe", "Schule", "Beobachtungszeitraum"):
        paragraph = document.add_paragraph()
        paragraph.paragraph_format.space_after = Pt(12)
        run = paragraph.add_run(f"{label}:  ")
        run.bold = True
        paragraph.add_run("____________________________________________")
    document.add_paragraph("")
    legend = document.add_paragraph()
    legend.alignment = WD_ALIGN_PARAGRAPH.CENTER
    legend_run = legend.add_run("Legende:  ☒ erfüllt   ·   ☒ teilweise erfüllt   ·   ☒ nicht erfüllt")
    legend_run.font.size = Pt(10)
    legend_run.font.italic = True

    total_competencies = 0
    total_tables = 0
    for stage, main_areas in stages.items():
        document.add_page_break()
        add_heading(document, stage, 1)
        intro = document.add_paragraph(
            "Bitte je Kompetenz genau einen Lernstand markieren. Ergänzende Beobachtungen "
            "können im Bemerkungsfeld dokumentiert werden."
        )
        intro.paragraph_format.space_after = Pt(8)

        for main_area, competency_areas in main_areas.items():
            number, color = MAIN_CONFIG.get(main_area, ("", BLUE))
            add_heading(document, f"{number}. {main_area}" if number else main_area, 2, color)
            for competency_area, experience_fields in competency_areas.items():
                add_heading(document, competency_area, 3)
                for experience_field, competencies in experience_fields.items():
                    add_heading(document, experience_field, 4)
                    add_competency_table(document, competencies)
                    total_competencies += len(competencies)
                    total_tables += 1

    document.core_properties.title = "Lernstandsheft – Sozialadaptive Kompetenzen"
    document.core_properties.subject = "Kompetenzbogen für Einschulung und Mittelstufe"
    document.core_properties.author = "Cheko"
    document.core_properties.keywords = "Lernstand, sozialadaptive Kompetenzen, Einschulung, Mittelstufe"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    document.save(output_path)
    return total_competencies, total_tables


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("excel", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    competencies, tables = create_document(args.excel, args.output)
    print(f"Gespeichert: {args.output}")
    print(f"Kompetenzen: {competencies}")
    print(f"Tabellen: {tables}")
    print(f"Kontrollkästchen: {competencies * 3}")


if __name__ == "__main__":
    main()
