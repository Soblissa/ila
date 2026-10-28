#!/usr/bin/env python3
"""Erzeugt das Collabora-ODT mit den 14 hoch gewichteten Prüfbericht-Befunden."""

from __future__ import annotations

import html
import re
import zipfile
from pathlib import Path


ILA_ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ILA_ROOT.parent
SOURCE = (
    ILA_ROOT
    / "Barrierefreiheit"
    / "Kritische_Verstosse_Bugs_Pruefbericht_Barrierefreiheit_diSAF_2026-10-28.md"
)
TEMPLATE = (
    WORKSPACE
    / "nextcloud-shared"
    / "ChekoWorkspace"
    / "40_Collabora-Vorlagen"
    / "01-Kurzbriefing.ott"
)
OUTPUT = (
    WORKSPACE
    / "nextcloud-shared"
    / "ChekoWorkspace"
    / "10_Aktive-Themen"
    / "10_ILA-diSAF"
    / "30_Barrierefreiheit"
    / "diSAF_Kritische-Verstoesse-und-Bugs_Pruefbericht-Barrierefreiheit_2026-10-28.odt"
)


def inline_xml(value: str) -> str:
    tokens: list[str] = []

    def hold(content: str) -> str:
        tokens.append(content)
        return f"@@TOKEN{len(tokens) - 1}@@"

    value = re.sub(
        r"`([^`]+)`",
        lambda match: hold(f"„{html.escape(match.group(1), quote=False)}“"),
        value,
    )
    value = re.sub(
        r"\*\*([^*]+)\*\*",
        lambda match: hold(html.escape(match.group(1), quote=False)),
        value,
    )
    escaped = html.escape(value, quote=False)
    for index, content in enumerate(tokens):
        escaped = escaped.replace(f"@@TOKEN{index}@@", content)
    return escaped


def paragraph(value: str, style: str = "Text_20_body") -> str:
    return f'<text:p text:style-name="{style}">{inline_xml(value)}</text:p>'


def heading(value: str, level: int) -> str:
    style = "Heading_20_1" if level <= 2 else "Heading_20_2"
    outline = 1 if level <= 2 else 2
    return (
        f'<text:h text:style-name="{style}" text:outline-level="{outline}">'
        f"{inline_xml(value)}</text:h>"
    )


def table_xml(rows: list[list[str]], number: int) -> str:
    output = [f'<table:table table:name="BefundTable{number}">']
    width = max(len(row) for row in rows)
    output.append(f'<table:table-column table:number-columns-repeated="{width}"/>')
    for row_number, row in enumerate(rows):
        output.append("<table:table-row>")
        for cell in row + [""] * (width - len(row)):
            output.append(
                '<table:table-cell office:value-type="string">'
                f"{paragraph(cell)}"
                "</table:table-cell>"
            )
        output.append("</table:table-row>")
    output.append("</table:table>")
    return "".join(output)


def markdown_body(markdown: str) -> str:
    lines = markdown.splitlines()
    output: list[str] = []
    table_rows: list[list[str]] = []
    table_number = 0

    def flush_table() -> None:
        nonlocal table_number, table_rows
        if table_rows:
            table_number += 1
            output.append(table_xml(table_rows, table_number))
            table_rows = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("# "):
            continue
        if stripped.startswith("|") and stripped.endswith("|"):
            cells = [cell.strip() for cell in stripped.strip("|").split("|")]
            if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
                continue
            table_rows.append(cells)
            continue
        flush_table()
        if not stripped:
            continue
        if stripped.startswith("## "):
            output.append(heading(stripped[3:], 2))
        else:
            output.append(paragraph(stripped))
    flush_table()
    return "".join(output)


def build() -> None:
    template_before = TEMPLATE.read_bytes()
    body = markdown_body(SOURCE.read_text(encoding="utf-8"))
    header = "".join(
        [
            paragraph(
                "Kritische Verstöße und Bugs aus dem Prüfbericht zur Barrierefreiheit von diSAF",
                "Title",
            ),
            paragraph("Status: Zur Prüfung · 28.10.2026", "Subtitle"),
            paragraph(
                "Ausschließlich die 14 Feststellungen des ursprünglichen Prüfberichts mit dem Schweregrad Hoch: 13 Verstöße und ein Bug.",
                "Lead",
            ),
        ]
    )
    footer = paragraph(
        "Erstellt am 28.10.2026 · Verantwortlich: Cheko (ILA-Hauptagent) · Quellenstand: Prüfbericht vom 09.10.2026",
        "FooterNote",
    )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(TEMPLATE, "r") as source, zipfile.ZipFile(OUTPUT, "w") as target:
        target.writestr(
            "mimetype",
            "application/vnd.oasis.opendocument.text",
            compress_type=zipfile.ZIP_STORED,
        )
        for info in source.infolist():
            if info.filename == "mimetype":
                continue
            data = source.read(info.filename)
            if info.filename == "content.xml":
                xml = data.decode("utf-8")
                xml = xml.replace(
                    'xmlns:xlink="http://www.w3.org/1999/xlink"',
                    'xmlns:xlink="http://www.w3.org/1999/xlink" '
                    'xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0"',
                )
                start = xml.index("<office:text>") + len("<office:text>")
                end = xml.index("</office:text>")
                xml = xml[:start] + header + body + footer + xml[end:]
                data = xml.encode("utf-8")
            elif info.filename == "meta.xml":
                xml = data.decode("utf-8").replace(
                    "[Thema]-Kurzbriefing",
                    "Kritische Verstöße und Bugs – Prüfbericht Barrierefreiheit diSAF",
                )
                data = xml.encode("utf-8")
            elif info.filename == "META-INF/manifest.xml":
                xml = data.decode("utf-8").replace(
                    "application/vnd.oasis.opendocument.text-template",
                    "application/vnd.oasis.opendocument.text",
                )
                data = xml.encode("utf-8")
            target.writestr(info, data)

    if TEMPLATE.read_bytes() != template_before:
        raise RuntimeError("Die Collabora-Vorlage wurde verändert.")
    print(OUTPUT)


if __name__ == "__main__":
    build()
