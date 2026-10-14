#!/usr/bin/env python3
"""Create a reproducible, size-diverse sample of primary-school forms."""

from __future__ import annotations

import argparse
import hashlib
import math
from collections import Counter, defaultdict
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo


HEADERS = [
    "SchulNr", "Schulname", "Schultyp", "Schulform", "Schulamt",
    "Rechtsstellung", "E-Mail-Adressen",
    "Anzahl Klassen (mit Vorklassen und ohne Vorlaufkurse)",
    "Kinder in Vorlaufkursen", "Anzahl Schülerinnen und Schüler",
    "Schülerinnen und Schüler in inklusiver Beschulung (IB)",
    "Schülerinnen und Schüler in vorbeugenden Maßnahmen (VM)",
    "Schülerinnen und Schüler in Intensivklassen oder -kursen",
    "Anzahl Lehrkräfte",
]

SIZE_LABELS = ["sehr klein", "klein", "mittel", "groß", "sehr groß"]


def stable_key(row: tuple) -> str:
    return hashlib.sha256(f"2025-26|{row[4]}|{row[0]}".encode()).hexdigest()


def target_count(n: int, minimum: int, maximum: int) -> int:
    if maximum == minimum:
        return 25
    return round(25 + 5 * (n - minimum) / (maximum - minimum))


def distribute(total: int, buckets: int = 5) -> list[int]:
    base, rest = divmod(total, buckets)
    order = [2, 1, 3, 0, 4]
    result = [base] * buckets
    for i in range(rest):
        result[order[i]] += 1
    return result


def assign_size_bands(rows: list[tuple]) -> list[tuple[tuple, int]]:
    ordered = sorted(rows, key=lambda r: (r[9], r[0]))
    n = len(ordered)
    return [(row, min(4, (index * 5) // n)) for index, row in enumerate(ordered)]


def select_for_district(rows: list[tuple], target: int) -> list[tuple[tuple, int]]:
    banded = assign_size_bands(rows)
    buckets: dict[int, list[tuple]] = defaultdict(list)
    for row, band in banded:
        buckets[band].append(row)
    quotas = distribute(target)
    selected: list[tuple[tuple, int]] = []
    for band in range(5):
        candidates = sorted(buckets[band], key=stable_key)
        selected.extend((row, band) for row in candidates[:quotas[band]])

    # If a district has private schools, ensure at least one is represented while
    # preserving the size band and total count.
    if any(r[5] == "privat" for r in rows) and not any(r[5] == "privat" for r, _ in selected):
        private = sorted((x for x in banded if x[0][5] == "privat"), key=lambda x: stable_key(x[0]))[0]
        same_band_public = [x for x in selected if x[1] == private[1] and x[0][5] != "privat"]
        if same_band_public:
            selected.remove(sorted(same_band_public, key=lambda x: stable_key(x[0]))[-1])
            selected.append(private)
    return sorted(selected, key=lambda x: (x[1], x[0][9], x[0][0]))


def add_table(ws, name: str) -> None:
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions
    tab = Table(displayName=name, ref=ws.dimensions)
    tab.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showRowStripes=True)
    ws.add_table(tab)
    for cell in ws[1]:
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill("solid", fgColor="1F4E78")
        cell.alignment = Alignment(wrap_text=True, vertical="top")
    for col in range(1, ws.max_column + 1):
        values = [str(ws.cell(r, col).value or "") for r in range(1, min(ws.max_row, 250) + 1)]
        ws.column_dimensions[get_column_letter(col)].width = min(45, max(10, max(map(len, values)) + 2))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--sample-factor", type=float, default=1.0)
    args = parser.parse_args()

    source = load_workbook(args.source, read_only=True, data_only=True)["Schulliste"]
    rows = [tuple(r) for r in source.iter_rows(min_row=4, max_col=14, values_only=True) if r[0] is not None]
    filtered = [r for r in rows if "Grund" in str(r[3])]
    by_district: dict[str, list[tuple]] = defaultdict(list)
    for row in filtered:
        by_district[str(row[4])].append(row)
    sizes = [len(v) for v in by_district.values()]
    targets = {
        district: math.ceil(target_count(len(items), min(sizes), max(sizes)) * args.sample_factor)
        for district, items in by_district.items()
    }
    selected = {district: select_for_district(items, targets[district]) for district, items in by_district.items()}

    wb = Workbook()
    ws = wb.active
    ws.title = "Auswahl"
    ws.append(HEADERS + ["Größenklasse im Schulamtsbezirk", "Auswahlkriterium"])
    for district in sorted(selected):
        for row, band in selected[district]:
            ws.append(list(row) + [SIZE_LABELS[band], "geschichtete Auswahl nach Schulgröße"])
    add_table(ws, "AuswahlGSchulen")

    overview = wb.create_sheet("Bezirksübersicht")
    overview.append(["Schulamt", "G-Schulen gesamt", "Auswahl", "Anteil", "kleinste Schule", "größte Schule", "Schultypen in Auswahl", "Rechtsstellungen in Auswahl"])
    for district in sorted(by_district):
        chosen = [r for r, _ in selected[district]]
        overview.append([
            district, len(by_district[district]), len(chosen), len(chosen) / len(by_district[district]),
            min(r[9] for r in chosen), max(r[9] for r in chosen),
            ", ".join(sorted({str(r[2]) for r in chosen})),
            ", ".join(sorted({str(r[5]) for r in chosen})),
        ])
    for cell in overview["D"][1:]: cell.number_format = "0.0%"
    add_table(overview, "Bezirksuebersicht")

    all_g = wb.create_sheet("Alle Grundschulformen")
    all_g.append(HEADERS)
    for row in sorted(filtered, key=lambda r: (str(r[4]), r[9], r[0])): all_g.append(row)
    add_table(all_g, "AlleGSchulen")

    method = wb.create_sheet("Methodik")
    notes = [
        ("Quelle", args.source.name),
        ("Filter", "Langbezeichnung der Schulform enthält Grund; damit werden reine und kombinierte Grundschulformen erfasst."),
        ("Enthaltene Schultypen", ", ".join(sorted({str(r[2]) for r in filtered}))),
        ("Grundgesamtheit", f"{len(filtered)} Schulen in {len(by_district)} Schulamtsbezirken."),
        ("Auswahlumfang", f"Ausgangsquote je Schulamtsbezirk 25 bis 30 Schulen, linear nach Anzahl der gefilterten Schulen skaliert; angewendeter Faktor {args.sample_factor:g}. Ungerade Ergebnisse werden aufgerundet. Insgesamt {sum(map(len, selected.values()))} Schulen."),
        ("Diversität", "Je Schulamtsbezirk fünf gleich große Größenklassen anhand der Anzahl Schülerinnen und Schüler; annähernd gleiche Auswahlzahl aus jeder Größenklasse."),
        ("Reproduzierbarkeit", "Deterministische Auswahl anhand Schulamt und Schulnummer; bei unveränderten Eingangsdaten entsteht dieselbe Auswahl."),
        ("Private Schulen", "Wenn in einem Bezirk vorhanden, wird mindestens eine private Schule berücksichtigt, ohne Größenklasse oder Gesamtquote zu verändern."),
        ("Größenkennzahl", "Anzahl Schülerinnen und Schüler, Spalte J der Quelldatei."),
    ]
    for key, value in notes: method.append([key, value])
    method.column_dimensions["A"].width = 24
    method.column_dimensions["B"].width = 110
    for row in method.iter_rows():
        row[0].font = Font(bold=True)
        row[1].alignment = Alignment(wrap_text=True, vertical="top")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    wb.save(args.output)
    print(args.output)
    print("filtered", len(filtered), "selected", sum(len(v) for v in selected.values()))


if __name__ == "__main__":
    main()
