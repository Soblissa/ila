# agent-ila — Arbeitsordner ILA-Pilot

**Verantwortlich:** Cheko (ILA-Hauptagent)  
**Stand:** 2026-04-01

---

## Ordnerstruktur

| Ordner | Zweck |
|---|---|
| `00_inbox/` | Neue Anforderungen, noch nicht bearbeitet |
| `01_fachlichkeit/` | Fachliche Unterlagen von Sebastian / Fachlichkeits-Agent |
| `02_design/` | Screen-Entwürfe von Yves / Design-Agent |
| `03_review/` | Fertige Screens zur Freigabe durch Sarah |
| `04_metrics/` | Erfolgsmessung (Time-to-Draft, Rework, Akzeptanz) |
| `99_archive/` | Abgeschlossene Screens mit Metadaten |

---

## Workflow

1. Anforderung landet in `00_inbox/`
2. Fachliche Klärung → `01_fachlichkeit/`
3. Design-Auftrag → `02_design/`
4. Qualitäts-Check durch Cheko
5. Review-Vorbereitung → `03_review/`
6. Sarah entscheidet
7. Abschluss → `99_archive/` + Metriken in `04_metrics/`
