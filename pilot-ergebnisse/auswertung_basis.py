"""
ILA Pilotauswertung — Basis-Script
===================================
Single Source of Truth für alle Kennzahlen.
Immer dieses Script verwenden, niemals ad-hoc auswerten.

Wichtige Filterregeln (NICHT weglassen!):
1. Nutzer-IDs die mit '=' beginnen = Excel-Formelartefakt → IMMER herausfiltern
2. FP-ID-Spalte (row[19]) ist in JEDER Zeile befüllt → NICHT für FP-Nutzer-Zählung verwenden
3. Für FP-Nutzer-Zählung: Spalte 'FP erstellt durch' (row[20]) + 'FP erstellt am' (row[21]) verwenden
4. Für eindeutige FP-IDs: nur wenn row[20] (Ersteller) vorhanden
"""

import openpyxl
from collections import defaultdict, Counter
from datetime import datetime
import statistics

DATEI = 'Pilotauswertungen_Arbeitsdatei_Analysedatei_Chefkoch.xlsm'

def parse_ts(val):
    if val is None: return None
    if isinstance(val, datetime): return val
    if isinstance(val, str):
        for fmt in ('%Y-%m-%d %H:%M', '%Y-%m-%d %H:%M:%S', '%Y-%m-%d'):
            try: return datetime.strptime(val.strip(), fmt)
            except: pass
    return None

def is_artefakt(val):
    """Excel-Formelreste herausfiltern — IMMER anwenden auf Nutzer-IDs und FP-IDs"""
    return isinstance(val, str) and val.startswith('=')

def lade_daten(pfad):
    wb = openpyxl.load_workbook(pfad, keep_vba=True)
    ws = wb['Nutzerverhalten Report']
    rows = []
    for row in ws.iter_rows(min_row=4, values_only=True):
        u = row[2]
        if u is None: continue
        if is_artefakt(u): continue  # ← Formelartefakt raus
        rows.append(row)
    return rows

def berechne_kennzahlen(rows):
    alle_user = set()
    user_fp_erstellt = set()
    fp_ids = set()
    foerderungen = set()
    user_foerderung = defaultdict(set)
    user_massnahme = defaultdict(list)
    massnahmen_katalog = 0
    massnahmen_eigene = 0
    massnahmen_ausgewaehlt = set()
    massnahmen_aktiviert = set()
    massnahmen_deaktiviert = set()
    user_dates = defaultdict(set)
    user_day_ts = defaultdict(lambda: defaultdict(list))
    ts_cols = [3, 4, 13, 14, 15, 16, 17, 21, 25]

    for row in rows:
        u = row[2]
        alle_user.add(u)

        fid = row[1]
        fp_durch = row[20]  # FP erstellt durch — maßgeblich für FP-Nutzer!
        fp_am = row[21]     # FP erstellt am
        fp_id = row[19]
        massnahme = row[11]
        m_typ = row[12]

        if fid and not is_artefakt(str(fid)):
            foerderungen.add(fid)
            user_foerderung[u].add(fid)

        # FP: NUR via fp_durch + fp_am zählen (nicht via fp_id-Spalte!)
        if fp_durch and fp_am and not is_artefakt(str(fp_durch)):
            user_fp_erstellt.add(u)
            if fp_id and not is_artefakt(str(fp_id)):
                fp_ids.add(fp_id)

        if massnahme:
            user_massnahme[u].append(massnahme)
            if m_typ == 'Katalog': massnahmen_katalog += 1
            elif m_typ == 'Eigene': massnahmen_eigene += 1

        if row[15]: massnahmen_ausgewaehlt.add(u)
        if row[16]: massnahmen_aktiviert.add(u)
        if row[17]: massnahmen_deaktiviert.add(u)

        for col in ts_cols:
            ts = parse_ts(row[col])
            if ts:
                user_dates[u].add(ts.date())
                user_day_ts[u][ts.date()].append(ts)

    return {
        'alle_user': alle_user,
        'user_fp_erstellt': user_fp_erstellt,
        'fp_ids': fp_ids,
        'foerderungen': foerderungen,
        'user_foerderung': user_foerderung,
        'user_massnahme': user_massnahme,
        'massnahmen_katalog': massnahmen_katalog,
        'massnahmen_eigene': massnahmen_eigene,
        'massnahmen_ausgewaehlt': massnahmen_ausgewaehlt,
        'massnahmen_aktiviert': massnahmen_aktiviert,
        'massnahmen_deaktiviert': massnahmen_deaktiviert,
        'user_dates': user_dates,
        'user_day_ts': user_day_ts,
    }

def drucke_bericht(k):
    print("=" * 60)
    print("ILA PILOTAUSWERTUNG — VERIFIKATION KERNZAHLEN")
    print("=" * 60)

    print(f"\n[ NUTZER ]")
    print(f"  Eindeutige Nutzer (bereinigt): {len(k['alle_user'])}")

    print(f"\n[ FÖRDERUNGEN ]")
    print(f"  Eindeutige Förderungen: {len(k['foerderungen'])}")
    fc = [len(v) for v in k['user_foerderung'].values()]
    print(f"  Ø pro Nutzer: {statistics.mean(fc):.1f} | Max: {max(fc)}")

    print(f"\n[ MASSNAHMEN ]")
    gesamt_m = k['massnahmen_katalog'] + k['massnahmen_eigene']
    print(f"  Zeilen gesamt: {gesamt_m}")
    print(f"  Katalog: {k['massnahmen_katalog']} ({k['massnahmen_katalog']/gesamt_m*100:.0f}%)")
    print(f"  Eigene:  {k['massnahmen_eigene']} ({k['massnahmen_eigene']/gesamt_m*100:.0f}%)")
    ohne_m = set(k['user_foerderung'].keys()) - set(k['user_massnahme'].keys())
    print(f"  Nutzer ohne Maßnahme (trotz Förderung): {len(ohne_m)}")
    nur_ausgewaehlt = k['massnahmen_ausgewaehlt'] - k['massnahmen_aktiviert']
    print(f"  Nutzer ausgewählt aber nie aktiviert: {len(nur_ausgewaehlt)}")
    print(f"  Nutzer mit deaktivierten Maßnahmen: {len(k['massnahmen_deaktiviert'])}")

    print(f"\n[ FÖRDERPLÄNE ]  ← via 'FP erstellt durch', NICHT fp_id-Spalte!")
    mit_fp = len(k['user_fp_erstellt'])
    ohne_fp = len(k['alle_user']) - mit_fp
    print(f"  Eindeutige FP-IDs: {len(k['fp_ids'])}")
    print(f"  Nutzer MIT FP: {mit_fp} ({mit_fp/len(k['alle_user'])*100:.0f}%)")
    print(f"  Nutzer OHNE FP: {ohne_fp} ({ohne_fp/len(k['alle_user'])*100:.0f}%)")

    print(f"\n[ RÜCKKEHRVERHALTEN ]")
    dist = Counter(len(d) for d in k['user_dates'].values())
    einmal = dist[1]
    mehr = len(k['alle_user']) - einmal
    print(f"  Nur 1 Tag: {einmal} ({einmal/len(k['alle_user'])*100:.1f}%)")
    print(f"  Rückkehrer (>1 Tag): {mehr} ({mehr/len(k['alle_user'])*100:.1f}%)")
    for tage in sorted(dist.keys()):
        print(f"    {tage} Tag(e): {dist[tage]} Nutzer")

    print(f"\n[ SITZUNGSDAUER PRO TAG ]")
    spannen = []
    for u, tage in k['user_day_ts'].items():
        for tag, tss in tage.items():
            tss.sort()
            spannen.append((tss[-1] - tss[0]).total_seconds() / 60)
    print(f"  Nutzer-Tage analysiert: {len(spannen)}")
    print(f"  Median: {statistics.median(spannen):.0f} Min | Ø: {statistics.mean(spannen):.0f} Min")

if __name__ == '__main__':
    import os
    pfad = os.path.join(os.path.dirname(__file__), DATEI)
    rows = lade_daten(pfad)
    k = berechne_kennzahlen(rows)
    drucke_bericht(k)
