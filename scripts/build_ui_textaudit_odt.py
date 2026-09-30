#!/usr/bin/env python3
"""Build an editable ODT review document from the Figma UI text audit.

The output is derived from the approved Collabora Kurzbriefing template. The
Markdown audit remains the versioned source of truth.
"""

from __future__ import annotations

import html
import re
import zipfile
from pathlib import Path


ILA_ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ILA_ROOT.parent
SOURCE = ILA_ROOT / "fachlichkeit" / "ui-textaudit-figma-2026-09-29.md"
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
    / "50_Wording-Audit"
    / "diSAF_Figma-Wording-Audit_2026-09-30.odt"
)


def inline_xml(value: str) -> str:
    """Render the small Markdown subset used by the audit as ODF inline XML."""
    tokens: list[str] = []

    def token(content: str) -> str:
        tokens.append(content)
        return f"@@TOKEN{len(tokens) - 1}@@"

    value = re.sub(
        r"`([^`]+)`",
        lambda match: token(f"„{html.escape(match.group(1), quote=False)}“"),
        value,
    )
    value = re.sub(
        r"\*\*([^*]+)\*\*",
        lambda match: token(html.escape(match.group(1), quote=False)),
        value,
    )
    escaped = html.escape(value, quote=False)
    for index, content in enumerate(tokens):
        escaped = escaped.replace(f"@@TOKEN{index}@@", content)
    return escaped


def paragraph(text: str, style: str = "Text_20_body") -> str:
    return f'<text:p text:style-name="{style}">{inline_xml(text)}</text:p>'


def heading(text: str, level: int) -> str:
    style = "Heading_20_1" if level <= 2 else "Heading_20_2"
    outline = 1 if level <= 2 else 2
    return (
        f'<text:h text:style-name="{style}" text:outline-level="{outline}">'
        f"{inline_xml(text)}</text:h>"
    )


def bullet(text: str) -> str:
    return (
        '<text:list text:style-name="List"><text:list-item>'
        f'{paragraph(text)}'
        "</text:list-item></text:list>"
    )


def table_xml(rows: list[list[str]], number: int) -> str:
    rendered = [f'<table:table table:name="AuditTable{number}">']
    width = max(len(row) for row in rows)
    rendered.append(f'<table:table-column table:number-columns-repeated="{width}"/>')
    for row in rows:
        rendered.append("<table:table-row>")
        for cell in row + [""] * (width - len(row)):
            rendered.append(
                '<table:table-cell office:value-type="string">'
                f'{paragraph(cell)}'
                "</table:table-cell>"
            )
        rendered.append("</table:table-row>")
    rendered.append("</table:table>")
    return "".join(rendered)


def markdown_body(markdown: str) -> str:
    lines = markdown.splitlines()
    out: list[str] = []
    table_rows: list[list[str]] = []
    table_number = 0

    def flush_table() -> None:
        nonlocal table_rows, table_number
        if table_rows:
            table_number += 1
            out.append(table_xml(table_rows, table_number))
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
        if stripped.startswith("### "):
            out.append(heading(stripped[4:], 3))
        elif stripped.startswith("## "):
            out.append(heading(stripped[3:], 2))
        elif re.match(r"^[-*] ", stripped):
            out.append(bullet(stripped[2:]))
        elif re.match(r"^\d+\. ", stripped):
            out.append(bullet(stripped))
        else:
            out.append(paragraph(stripped))
    flush_table()
    return "".join(out)


def build() -> None:
    template_hash_before = TEMPLATE.read_bytes()
    source_body = markdown_body(SOURCE.read_text(encoding="utf-8"))

    review_header = "".join(
        [
            paragraph("Wording-Audit der Figma Design Specs", "Title"),
            paragraph("Prüfdokument · Status: Zur Prüfung · 30.09.2026", "Subtitle"),
            paragraph(
                "Der Prüflauf zeigt keine direkte Du-Ansprache, aber erhebliche "
                "Inkonsistenzen bei Perspektive, Systemmeldungen, Terminologie, "
                "Platzhaltern sowie Rechtschreibung und Grammatik.",
                "Lead",
            ),
            heading("Management-Zusammenfassung", 2),
            paragraph(
                "Verifizierter Befund: 34 Figma-Seiten wurden eingelesen; 15 funktionale "
                "Seiten bildeten die sprachliche Prüfmenge. Erfasst wurden 80.254 "
                "Textebenen-Vorkommen und 1.243 unterschiedliche Texte. Gefunden wurden "
                "87 Texte mit direkter Sie-Ansprache, 69 Texte mit Ich-, Mein- oder "
                "Wir-Perspektive, keine direkte Du-Ansprache und 25 unterschiedliche "
                "Platzhalter- oder Blindtexte."
            ),
            paragraph(
                "Bewertung: Vor dem nächsten Nutzertest müssen Platzhalter, erkennbare "
                "Fehler, wechselnde Prozessperspektiven und vermenschlichte "
                "Systemmeldungen bereinigt werden.",
                "Callout",
            ),
            paragraph(
                "Annahme und Grenze: Der Audit bewertet sichtbare Texte der funktionalen "
                "Seiten. Interne Ebenen-, Komponenten- und Seitennamen wurden bewusst "
                "nicht redaktionell bewertet. Fachliche Leitbegriffe dürfen erst nach "
                "einer Entscheidung vereinheitlicht werden."
            ),
            heading("Offene Entscheidungen und Verantwortungen", 2),
            bullet(
                "Sarah / Fachentscheidung: Leitbegriff für Evaluation, Bewertung oder "
                "Einschätzung festlegen."
            ),
            bullet(
                "Sarah / Fachentscheidung: sichtbaren Statusbegriff für Aktiv oder In "
                "Durchführung festlegen."
            ),
            bullet("Sarah / Fachentscheidung: verbindliche Gendering-Regel festlegen."),
            bullet(
                "Fachlichkeit: Meine Förderakten und Meine Förderungen eindeutig "
                "voneinander abgrenzen."
            ),
            bullet(
                "Cheko: freigegebene Korrekturen anhand stabiler Figma-Node-IDs für die "
                "Umsetzung vorbereiten."
            ),
            heading("Vollständiger Auditbericht", 2),
        ]
    )

    source_links = "".join(
        [
            heading("Quellen und Nachvollziehbarkeit", 2),
            paragraph("Versionierte Hauptquelle: ila/fachlichkeit/ui-textaudit-figma-2026-09-29.md"),
            '<text:p text:style-name="Text_20_body">Repository: '
            '<text:a text:style-name="Link" xlink:type="simple" '
            'xlink:href="https://github.com/Soblissa/ila/blob/main/fachlichkeit/'
            'ui-textaudit-figma-2026-09-29.md" office:target-frame-name="_blank">'
            'UI-Textaudit auf GitHub</text:a></text:p>',
            '<text:p text:style-name="Text_20_body">Figma-Arbeitskopie: '
            '<text:a text:style-name="Link" xlink:type="simple" '
            'xlink:href="https://www.figma.com/design/mGVoWdSLQzFABJlEzOQPRn" '
            'office:target-frame-name="_blank">ila _ Design Specs</text:a></text:p>',
            paragraph(
                "Erstellt am 30.09.2026 · Verantwortlich: Cheko (ILA-Hauptagent) · "
                "Auditstand: 29.09.2026",
                "FooterNote",
            ),
        ]
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
                xml = xml[:start] + review_header + source_body + source_links + xml[end:]
                data = xml.encode("utf-8")
            elif info.filename == "meta.xml":
                xml = data.decode("utf-8")
                xml = xml.replace(
                    "[Thema]-Kurzbriefing",
                    "Wording-Audit der Figma Design Specs",
                )
                data = xml.encode("utf-8")
            elif info.filename == "META-INF/manifest.xml":
                xml = data.decode("utf-8").replace(
                    "application/vnd.oasis.opendocument.text-template",
                    "application/vnd.oasis.opendocument.text",
                )
                data = xml.encode("utf-8")
            target.writestr(info, data)

    if TEMPLATE.read_bytes() != template_hash_before:
        raise RuntimeError("Die Collabora-Vorlage wurde verändert.")

    print(OUTPUT)


if __name__ == "__main__":
    build()
