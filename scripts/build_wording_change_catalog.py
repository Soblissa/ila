#!/usr/bin/env python3
import html, json, re, sys, zipfile
from collections import defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; WS=ROOT.parent
AUDIT=ROOT/'fachlichkeit/ui-textaudit-figma-2026-09-29.md'
OUTMD=ROOT/'fachlichkeit/ui-wording-umsetzungskatalog-figma-2026-09-30.md'
TEMPLATE=WS/'nextcloud-shared/ChekoWorkspace/40_Collabora-Vorlagen/01-Kurzbriefing.ott'
OUTODT=WS/'nextcloud-shared/ChekoWorkspace/10_Aktive-Themen/10_ILA-diSAF/50_Wording-Audit/diSAF_Figma-Wording-Umsetzungskatalog_2026-09-30.odt'
NODES=Path(sys.argv[1] if len(sys.argv)>1 else '/tmp/ila-figma-text-nodes.ndjson')

def clean(s): return s.strip().strip('`')
def pairs():
    result={}
    for line in AUDIT.read_text(encoding='utf-8').splitlines():
        if not (line.startswith('|') and line.endswith('|')): continue
        cells=[clean(x) for x in line.strip('|').split('|')]
        if all(re.fullmatch(r':?-{3,}:?',x) for x in cells): continue
        if len(cells)==3 and cells[0] not in {'Seite','Situation'}: result[cells[1]]=cells[2]
        elif len(cells)==2 and cells[0] not in {'Ist-Text','Situation','Perspektive'}: result[cells[0]]=cells[1]
    result['Wilkommen, Marc Czakay-Hänsel!']='Willkommen, [Nutzername]!'
    result['Willkommen Markus Czakay-Hänsel!']='Willkommen, [Nutzername]!'
    return result

PLACE=re.compile(r'lorem|blindtext|bal bla|typoblindtext',re.I)
GENERIC={'Action','Button','Label','Menu Item','Subtitle','Tag','Text-link','Title','[Name]','Placeholder Text Multiline'}
mapping=pairs(); groups=defaultdict(list)
for line in NODES.open(encoding='utf-8'):
    n=json.loads(line); old=n['text']; status='Umsetzbar'; category='Auditkorrektur'; target=mapping.get(old)
    if target and target.startswith(('Text fachlich','anwenderseitig')): status='Fachtext erforderlich'
    if not target and (PLACE.search(old) or old in GENERIC):
        target='Fachlich freigegebenen Zieltext einsetzen; Platzhalter darf nicht in einen freizugebenden Screen gelangen.'
        status='Fachtext erforderlich'; category='Platzhalter/Prototyprest'
    if not target: continue
    key=(n['page'],n['section'] or 'Ohne Section',n['frame'] or 'Ohne Screen/Frame',old,target,status,category)
    groups[key].append(n['node_id'])

pages=defaultdict(list)
for key,ids in groups.items(): pages[key[0]].append((key,ids))
lines=['# Figma-Wording: Umsetzungskatalog für die Entwicklung','',
'**Stand:** 2026-09-30  ','**Status:** Zur Prüfung  ',
'**Quelle:** `fachlichkeit/ui-textaudit-figma-2026-09-29.md` und Figma-Arbeitskopie `ila _ Design Specs`  ',
'**Prinzip:** Ein Eintrag beschreibt eine eindeutige Textänderung je Seite, Section und Screen/Frame. Wiederholte Komponenteninstanzen werden zusammengefasst; die Fundstellenzahl und Beispiel-Node-IDs bleiben erhalten.','',
'## Umsetzungshinweise','',
'- Texte möglichst zentral über Übersetzungsschlüssel oder gemeinsame Komponenten ändern.','- Status **Umsetzbar** kann direkt übernommen werden.','- Status **Fachtext erforderlich** blockiert nur die jeweilige Fundstelle; keinen Blindtext durch erfundenen Inhalt ersetzen.','- Nach Umsetzung gelten die Abnahmekriterien des Audits.','']
total=sum(len(v) for v in pages.values()); occurrences=sum(len(ids) for ids in groups.values())
lines += [f'**Umfang:** {total} eindeutige Änderungsgruppen mit {occurrences} Figma-Fundstellen auf {len(pages)} betroffenen Seiten.','']
counter=0
for page in sorted(pages):
    lines += [f'## {page}','']
    for key,ids in sorted(pages[page],key=lambda x:(x[0][1],x[0][2],x[0][3])):
        counter+=1; _,section,frame,old,target,status,category=key
        sample=', '.join(ids[:12])+(' …' if len(ids)>12 else '')
        lines += [f'### Änderung {counter:03d} — {category}',f'- **Section:** {section}',f'- **Screen/Frame:** {frame}',f'- **Status:** {status}',f'- **Ist:** `{old}`',f'- **Soll:** `{target}`',f'- **Fundstellen:** {len(ids)}',f'- **Node-IDs (Auszug):** `{sample}`','']
OUTMD.write_text('\n'.join(lines),encoding='utf-8')

def esc(s): return html.escape(s,quote=False)
body=['<text:p text:style-name="Title">Figma-Wording: Umsetzungskatalog</text:p>',
'<text:p text:style-name="Subtitle">Zur Prüfung · 30.09.2026</text:p>',
f'<text:p text:style-name="Lead">{total} eindeutige Änderungsgruppen · {occurrences} Fundstellen · {len(pages)} betroffene Seiten</text:p>']
for line in lines[lines.index('## Umsetzungshinweise'):]:
    if line.startswith('## '): body.append(f'<text:h text:style-name="Heading_20_1" text:outline-level="1">{esc(line[3:])}</text:h>')
    elif line.startswith('### '): body.append(f'<text:h text:style-name="Heading_20_2" text:outline-level="2">{esc(line[4:])}</text:h>')
    elif line.startswith('- '): body.append(f'<text:p text:style-name="Text_20_body">• {esc(re.sub(r"\*\*|`","",line[2:]))}</text:p>')
    elif line.strip(): body.append(f'<text:p text:style-name="Text_20_body">{esc(re.sub(r"\*\*|`","",line))}</text:p>')
body.append('<text:p text:style-name="FooterNote">Quelle: ila/fachlichkeit/ui-textaudit-figma-2026-09-29.md · Figma-Datei mGVoWdSLQzFABJlEzOQPRn</text:p>')
OUTODT.parent.mkdir(parents=True,exist_ok=True)
before=TEMPLATE.read_bytes()
with zipfile.ZipFile(TEMPLATE) as src, zipfile.ZipFile(OUTODT,'w') as dst:
    dst.writestr('mimetype','application/vnd.oasis.opendocument.text',compress_type=zipfile.ZIP_STORED)
    for info in src.infolist():
        if info.filename=='mimetype': continue
        data=src.read(info.filename)
        if info.filename=='content.xml':
            x=data.decode(); a=x.index('<office:text>')+len('<office:text>'); b=x.index('</office:text>'); data=(x[:a]+''.join(body)+x[b:]).encode()
        elif info.filename=='META-INF/manifest.xml': data=data.replace(b'application/vnd.oasis.opendocument.text-template',b'application/vnd.oasis.opendocument.text')
        dst.writestr(info,data)
assert TEMPLATE.read_bytes()==before
print(OUTMD); print(OUTODT)
