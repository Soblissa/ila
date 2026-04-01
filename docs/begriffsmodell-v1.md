# Begriffsmodell ILA — Version 1

**Stand:** 2026-04-01  
**Autor:** Cheko (ILA-Hauptagent)  
**Grundlage:** Figma Design Specs (yIb1pCbdjaUqpnrPf0RMF1)  
**Status:** Entwurf — zur Ergänzung durch Sebastian (Fachlichkeit) und Yves (Design)

Kein Vollständigkeitsanspruch. Klein anfangen, mit dem Pilot wachsen.

---

## Begriffsmodell-Tabelle

| Begriff | Figma-Name | Fachbedeutung | Projektintern | Anwender-Begriff | Hinweise / Konflikte | Status |
|---|---|---|---|---|---|---|
| **Förderziel** | Card Target | Pädagogisch definiertes Lernziel für einen Schüler | Förderziel | Förderziel | Amtlicher Begriff — vermutlich direkt übertragbar | offen |
| **Förderung** | List-Item Förderung | Gesamtheit aller Maßnahmen für einen Schüler | Förderung | Förderung | Verhältnis zu "Förderplan" klären | offen |
| **Förderakte** | Förderakte (Seite) | Dokumentenmappe zum Schüler | Förderakte | Förderakte | Amtlicher Begriff — klären ob einheitlich verwendet | offen |
| **Förderplan** | Förderplan (Seite) | Offizielles Planungsdokument | Förderplan | Förderplan | Verhältnis zu "Förderakte" und "Förderung" klären | offen |
| **Förderbereich** | Card Category | Übergeordneter thematischer Bereich (z. B. Lesen, Rechnen) | Förderbereich | Förderbereich | Klären: Ist das ein amtlicher Begriff? | offen |
| **Kompetenz** | Card Skill | Konkrete Fähigkeit / Fertigkeit | Kompetenz | Kompetenz oder Fertigkeit? | Begriffe "Kompetenz" und "Fertigkeit" teils synonym — klären | offen |
| **Maßnahme** | Accordion-Item Eigene Maßnahme / Kurs | Konkrete pädagogische Aktivität zur Zielerreichung | Maßnahme | Maßnahme | "Kurs" vs. "eigene Maßnahme" — zwei Typen? Unterschied klären | offen |
| **Evaluation** | Evaluation (Component Set) / Slot/Wizard/Förderziel evaluieren | Bewertung des Förderziels nach Durchführungsphase | Evaluation | Evaluation oder Einschätzung? | Klären ob "Evaluation" für Lehrkräfte vertraut oder zu formal | offen |
| **Notiz** | Notiz (Component Set) | Freie Anmerkung zu einem Förderziel | Notiz | Notiz | Passt direkt — kein Konflikt | abgestimmt |
| **Lernausgangslage** | Schritt 2: Lernausgangslage | Feststellung des aktuellen Lernstands vor Zieldefinition | Lernausgangslage | Lernausgangslage | Amtlicher Fachbegriff — direkt übertragbar | offen |
| **Neue Förderung** | Prozess: Neue Förderung | Anlegen einer neuen Förderung für einen Schüler | Neue Förderung anlegen | Neue Förderung | 3-Schritte-Wizard: Schüler → Anlass → Zusammenfassung | offen |
| **Anlass** | Schritt 2: Anlass | Auslöser / Begründung für die Förderung | Anlass | Anlass | Klären: Ist "Anlass" der amtliche Begriff? | offen |
| **Feedback** | Slot/User Feedback / Nutzerfeedback | Rückmeldung der Lehrkraft zur Anwendung | Nutzerfeedback | Rückmeldung | "Feedback" vs. "Rückmeldung" — intern vs. Anwender unterscheiden | offen |
| **Status Förderziel** | `[in Planung]` / `[in Durchführung]` / `[abgeschlossen]` | Lebenszyklusphase eines Förderziels | in Planung / aktiv / abgeschlossen | In Planung / In Durchführung / Abgeschlossen | Klären ob "in Durchführung" für Lehrkräfte verständlich | offen |

---

## Noch nicht aufgenommen (nächste Version)

- Navigation-Elemente (Menüpunkte, Breadcrumbs)
- Systemfehlermeldungen
- Bestätigungstexte in Modals
- Gendering-Begriffe (Schüler/in, Lehrkraft)

---

## Wie dieses Dokument gepflegt wird

- **Cheko** trägt Figma-Namen ein und markiert Konflikte
- **Sebastian** ergänzt Fachbedeutung und klärt amtliche Begriffe
- **Yves** bestätigt Figma-Namen und Anwender-Begriff in der Oberfläche
- **Sarah** entscheidet bei strittigen Fällen
- Status wechselt von `offen` → `abgestimmt` sobald alle drei Seiten bestätigt haben
