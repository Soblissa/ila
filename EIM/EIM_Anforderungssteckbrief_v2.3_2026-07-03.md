# Anforderungssteckbrief und Absichtserklärung (LoI)
## Zur Integration in die zentrale Enterprise Identity Management (EIM) Plattform

- **Version:** 2.3
- **Datum:** 03. Juli 2026
- **Status:** Final – Hosting-Kategorien, M2M-Klarstellung, hybrides Rechtemodell, SLA-Abgrenzung, Nomenklatur
- **Bezugsdokument:** Fachkonzept EIM v1.15, Integrationsleitfaden v1.1
- **Herausgeber:** Hessische Zentrale für Datenverarbeitung (HZD), Projektleitung Enterprise Identity Management
- **Quelle:** von Sarah übermittelt am 11.09.2026 (Telegram)

---

## Präambel

Das Projekt „Enterprise Identity Management" (EIM) der HZD schafft die zukunftssichere, mandantenfähige Identitäts-Plattform für die bestehende HZD-Infrastruktur sowie für moderne Cloud-Architekturen (u. a. kompatibel zum D-Stack).

Geboten werden:
- zentrales Single Sign-On (SSO)
- Multi-Faktor-Authentifizierung (MFA)
- automatisiertes Berechtigungsmanagement (IGA)

Durch offene Standards (OIDC/SAML, SCIM) sollen Fachverfahren nahtlos in das föderale Ökosystem (u. a. Deutsche Verwaltungscloud – DVC) integrierbar sein.

Der Steckbrief dient der gemeinsamen Architekturplanung, der Zuweisung zum passenden Identity Broker (Sicherheitszone) und der Priorisierung des Verfahrens für das technische Onboarding.

---

## Einordnung in den Onboarding-Prozess

Diese Absichtserklärung ist die **erste Stufe** des EIM-Anbindungsprozesses. Sie dient der fachlichen Vorqualifizierung und Ressourcenplanung.

| Schritt | Dokument | Wer | Wann |
|---|---|---|---|
| 1. Absichtserklärung | Dieses Dokument (LoI) | Fachverfahrensleitung | Vor Planungsbeginn |
| 2. Technisches Onboarding | Digitales Onboarding-Formular im EIM-Portal | Technical Owner | Nach Priorisierung durch EIM |
| 3. Data Sharing Agreement | DSA (digitale Zeichnung im Portal) | Data Owner + EIM | Vor Go-Live |

---

## TEIL 1: Allgemeine Informationen zum Fachverfahren

| Eigenschaft | Angabe des Fachverfahrens |
|---|---|
| Name der Anwendung / des Fachverfahrens | [Bitte eintragen] |
| Kurzbeschreibung (Zweck der Anwendung) | [1–2 Sätze eintragen] |
| Fachverantwortliche(r) (Data Owner) | [Name, Abteilung, E-Mail] |
| Technischer Ansprechpartner (Technical Owner) | [Name, Firma/Abteilung, E-Mail] |
| Schutzbedarf der Anwendung (nach BSI) | [ ] Normal  [ ] Hoch  [ ] Sehr Hoch |
| Testumgebung (DEV/QS/Staging) vorhanden | [ ] Ja  [ ] Nein, nur produktive Umgebung verfügbar |

### Architektur-Kategorie (Hosting)

*Hinweis des EIM-Teams: Die Auswahl bestimmt, wie das EIM-Team das Fachverfahren technisch anbindet. Intern gehostete Anwendungen (HZD-Rechenzentrum) können bei Bedarf über den „EIM-Proxy" minimalinvasiv angebunden werden – das bestehende Login bleibt dabei funktional, eine schrittweise Modernisierung wird unterstützt. Bei extern gehosteten Anwendungen (SaaS) muss der Hersteller die benötigten Standards nativ mitbringen. Bei Unsicherheit: die Kategorie wählen, die der aktuellen Betriebssituation am nächsten kommt – Details klärt das EIM-Team im anschließenden Onboarding-Gespräch.*

- [ ] **Moderne Fachverfahren (Cloud-native):** Von der HZD (oder einem Partner) gehostet, Betrieb auf einer standardisierten, DVC-konformen Cloud-Plattform (z. B. souveräne Container/Kubernetes-Infrastruktur).
- [ ] **Klassische Fachverfahren (On-Premises):** Von der HZD gehostet, Betrieb im klassischen internen Rechenzentrum (virtuelle Server / Bare Metal).
- [ ] **In Modernisierung (Übergangsphase):** Aktuell klassisch (On-Premises), Migration in moderne Cloud-Architekturen in Planung oder bereits begonnen.
- [ ] **Externe Fachverfahren (SaaS):** Cloud-Dienst eines externen Drittanbieters außerhalb der HZD (z. B. WebEx, ServiceNow).

*Wichtiger Arbeitsauftrag: Vorab mit dem Software-Hersteller klären, ob das Produkt OIDC oder SAML 2.0 nativ unterstützt. Da die Anwendung außerhalb der HZD-Infrastruktur läuft, kann das EIM-Team keinen vorgeschalteten Login-Proxy bereitstellen – die Unterstützung muss nativ vom Hersteller kommen.*

---

## TEIL 2: Nutzergruppen & Zugriffswege (Zero Trust)

*Wer meldet sich zukünftig an dieser Anwendung an und von wo? Auf Basis dieser Angaben ordnet das EIM-Team das Fachverfahren der passenden Sicherheitszone zu (interner Broker oder Public-Broker).*

- [ ] **Interne Nutzer (Corporate Network):** Zugriff durch HZD-/Landes-Beschäftigte primär aus dem abgesicherten internen Behördennetz.
- [ ] **Interne Nutzer (Internet / BYOD):** Zugriff durch Beschäftigte auch von außerhalb des Behördennetzes (Home-Office ohne VPN, privates Endgerät). *Löst im EIM automatisch Zero-Trust-Schutz mit zwingender MFA aus.*
- [ ] **Externe Nutzer (Bürger / Unternehmen):** Zugriff durch externe Personen ohne HZD-Konto (z. B. via BundID, Unternehmenskonto).
- [ ] **Föderale Partner / Andere Behörden:** Zugriff aus anderen Kommunen/Ländern (z. B. via NdB, eKom21).
- [ ] **Maschinen / APIs:** Technische Service-Accounts für automatisierte Hintergrundprozesse.

**Erwartete Nutzeranzahl (ca.):** ______________

---

## TEIL 3: Authentifizierung & IT-Sicherheit (Access Management)

### 3.1 Präferiertes Authentifizierungsprotokoll

- [ ] **OpenID Connect (OIDC) / OAuth 2.0** — bevorzugter, zukunftssicherer Standard der HZD
- [ ] **SAML 2.0** — für klassische Bestandsanwendungen
- [ ] **Andere / Unbekannt** — erfordert individuelle Prüfung durch das EIM-Team. Unterstützt eine intern gehostete Anwendung keines der genannten Protokolle, kann sie in einer Übergangsphase über den EIM-Proxy betrieben werden. Bei externen SaaS-Diensten ist das nicht möglich.

### 3.2 Gewünschte Vertrauensstufe (Trust Level)

*Die Vertrauensstufe bestimmt, wie stark die Identität der Nutzer geprüft wird – und damit auch, ob MFA erforderlich ist. Der Broker erzwingt die gewählte Stufe automatisch; bei Zugriff aus unsicheren Netzen (z. B. Home-Office/BYOD) kann er die Stufe dynamisch anheben (Step-Up), ohne dass die Anwendung angepasst werden muss.*

- [ ] **Bronze (Einstieg / Übergangsbetrieb):** Benutzername & Passwort oder nahtloses Windows-SSO. Kein zweiter Faktor. Für unkritische Anwendungen mit Schutzbedarf „Normal".
- [ ] **Silber (Empfohlener Standard / Dynamischer Zero-Trust-Schutz):** Nahtlose Anmeldung ohne erneute Passworteingabe im Behördennetz (Desktop-SSO über bestehende Windows-Infrastruktur). Bei Zugriff aus dem Internet (Home-Office/BYOD) erzwingt der Broker automatisch MFA (z. B. FIDO2). Standard für die meisten Fachanwendungen.
- [ ] **Gold (Höchstes Sicherheitsniveau):** Zwingende MFA bei jedem Login, unabhängig vom Standort. Für Anwendungen mit Schutzbedarf „Hoch" oder personenbezogenen Daten besonderer Kategorien.
- [ ] **Nur Maschinen-/API-Zugriff (M2M):** Keine menschlichen Nutzer. Authentifizierung System-zu-System über sichere API-Tokens (z. B. OAuth 2.0 Client Credentials oder zertifikatsbasiert / mTLS). Konkrete Absicherung wird im technischen Onboarding individuell festgelegt.
- [ ] **Perspektivisch gewünscht (Transformationspfad):** Start mit Bronze, perspektivisch Wechsel auf Silber oder Gold. *Hochstufung ist jederzeit formlos beim EIM-Team beantragbar – ohne Änderung an der Anwendung.*

### 3.3 Datenschutz & Datensparsamkeit

- [ ] **Privacy by Design (PPID) – empfohlen:** Das Fachverfahren verarbeitet aus Datenschutzgründen keine echten Personendaten und erhält vom EIM bei der Anmeldung nur eine eindeutige, nicht-rückverfolgbare Pseudonym-ID (PPID). *Standardmodus der EIM-Plattform, erfüllt die DSGVO-Anforderung zur Datensparsamkeit.*
- [ ] **Klardaten:** Das Fachverfahren benötigt zwingend echte Personendaten (Name, E-Mail, AD-Kennung) im Token zur internen Verarbeitung. *Erfordert eine Begründung im Rahmen des Data Sharing Agreements.*

---

## TEIL 4: Berechtigungsmanagement (Identity Governance / IGA)

### 4.1 Rollen- und Rechteverwaltung

- [ ] **Zentral (via EIM):** Das EIM übergibt bei der Anmeldung direkt die übergeordneten Fach-Rollen (z. B. „Sachbearbeiter", „Leser") im OIDC/SAML-Token an die Applikation.
- [ ] **Dezentral (in der App):** Das EIM prüft nur die Identität (reiner Login). Feingranulare Rechte vergeben Administratoren weiterhin innerhalb des Fachverfahrens.
- [ ] **Hybrides Modell (Grob- und Feinrechte):** Das EIM übergibt eine Basis-Berechtigung (z. B. „App-Zugang gestattet"), die tiefere feingranulare Berechtigungsvergabe erfolgt dezentral in der Anwendung.

### 4.2 Automatisierte Provisionierung (JML-Prozess)

- [ ] **Echtzeit-Provisionierung (SCIM / REST-API) – empfohlen:** Die EIM IGA-Engine legt Nutzerkonten vollautomatisiert über eine standardisierte Schnittstelle an, aktualisiert sie bei Änderungen und sperrt sie beim Austritt sofort („Not-Aus"). Sicherster Modus.
- [ ] **Just-in-Time (JIT):** Nutzerkonten werden beim *ersten* erfolgreichen SSO-Login über das EIM automatisch in der App erstellt. *Mindestvoraussetzung für direkte OIDC/SAML-Integrationen. Bestandskonten aus dem AD können beim ersten SSO-Login automatisch mit der neuen EIM-Identität verknüpft werden.*
- [ ] **Manuell / Bestand (Übergangsbetrieb):** Die Anwendung pflegt Konten vollständig selbst (manuell oder per eigenem AD/LDAP-Sync). *Historische Altanwendungen über den EIM-Proxy können in der Übergangsphase weiterhin auf manuellen oder lokalen AD-Syncs basieren. Die automatische Kontosperrung beim Mitarbeiteraustritt greift hier in der Regel nicht. Technische Service-Accounts für APIs werden generell gesondert über das EIM-Portal registriert.*

---

## TEIL 5: Zeitplan & Verbindliche Absichtserklärung

- **Gewünschter Start der Test-Integration (Quartal/Jahr):** ______________
- **Geplanter produktiver Go-Live (Quartal/Jahr):** ______________

Wir beabsichtigen, das oben genannte Fachverfahren an die EIM-Plattform der HZD anzubinden. Uns ist bewusst, dass dieser Steckbrief der initialen Ressourcenplanung sowie der Zuweisung der korrekten Architektur-Zonen durch das EIM-Projekt dient.

### Mitwirkungspflichten & Aufgabenteilung

1. **Schnittstellen-Integration:** Das EIM-Projekt stellt die Identitäts-Plattform, die Login-Masken sowie standardisierte Schnittstellen (Tokens) zur Verfügung. **Die Auswertung dieser Tokens und die informationstechnische Durchsetzung der Zugriffsrechte obliegen der jeweiligen Fachanwendung selbst.**
2. **Netzwerk / Firewalls:** Etwaige notwendige Firewall-Freischaltungen – beispielsweise damit die EIM IGA-Engine eine On-Premises-Anwendung für die automatisierte SCIM-Provisionierung netzwerktechnisch erreichen darf – sind rechtzeitig durch die Fachverfahrensverantwortlichen beim IT-Betrieb zu beantragen.
3. **Data Sharing Agreement (DSA):** Vor der produktiven Freischaltung ist ein DSA zwischen Fachverfahren und EIM-Projekt digital zu zeichnen. Das DSA regelt, welche Identitätsattribute an das Fachverfahren übermittelt werden und unter welchen Bedingungen. *Bei Wahl des datensparsamen Standard-Modus „PPID" (Teil 3.3) ist das DSA ein stark vereinfachter Freigabeprozess, da keine Klardaten fließen.*

Zugesichert wird, für die Phase der Anbindung und der abschließenden Integrationstests ausreichend technische und fachliche Ansprechpartner bereitzustellen. Etwaige Entwicklungsaufwände zur Anpassung der eigenen Applikation an die EIM-Standardschnittstellen (OIDC/SAML, SCIM) erfolgen in der Verantwortung und aus dem Budget des Fachverfahrens.

___________________________________________________________
*Datum, Ort / Unterschrift Fachverantwortliche(r) (Data Owner)*

**Bitte senden Sie den ausgefüllten Steckbrief an:** [E-Mail-Adresse / Link zum EIM-Portal eintragen]

---

## Nächste Schritte nach Eingang der Absichtserklärung

1. **Bewertung & Priorisierung** (EIM-Team, ~5 AT): Zuordnung zur Sicherheitszone, Abgleich mit der Rollout-Roadmap, Rückmeldung mit voraussichtlichem Onboarding-Zeitfenster.
2. **Technisches Onboarding-Formular** (Technical Owner, ~0,5 AT): Im EIM-Onboarding-Portal werden technische Details erfasst (Redirect-URIs, benötigte Attribute, Scopes, Grant-Typen). Details im *EIM-Integrationsleitfaden für Fachverfahren*.
3. **Automatische Provisionierung** (System): Nach Genehmigung wird der OIDC/SAML-Client automatisch in der Testumgebung angelegt.
4. **Integration & Test** (Technical Owner): Das Entwicklungsteam konfiguriert die Schnittstelle (OIDC/SAML) und testet den Login-Flow.
5. **DSA & Go-Live** (Data Owner, ~0,5 AT): Data Sharing Agreement zeichnen, Go-Live-Freigabe erteilen.

**Typische Netto-Bearbeitungszeit des EIM-Teams für ein Standard-Onboarding:** ≤ 3 Arbeitstage *(exklusive Test- und Integrationszeiten auf Seiten des Fachverfahrens)*

---

## Anhang: Vorlage Begleit-E-Mail für den Versand an die Fachverfahren

**Betreff:** Einladung zur EIM-Integration: Zukunftssicheres Log-in & Identity Management für Ihr Fachverfahren

Sehr geehrte(r) [Name],

Ihr Fachverfahren [Name der App] leistet einen wichtigen Beitrag in unserer Anwendungslandschaft. Mit dem Projekt „Enterprise Identity Management (EIM)" bauen wir aktuell die zentrale Identitäts-Infrastruktur der HZD auf, um Logins, IT-Sicherheit und die Benutzerverwaltung landesweit zukunftssicher zu standardisieren.

Unsere Plattform bildet dabei einen wesentlichen Baustein, um den gestiegenen Sicherheitsanforderungen gerecht zu werden und unseren Fachverfahren eine nahtlose Interoperabilität im föderalen Ökosystem (u. a. Deutsche Verwaltungscloud – DVC) zu ermöglichen.

Wir möchten Ihnen die Möglichkeit bieten, Ihr Fachverfahren frühzeitig an die neue EIM-Plattform anzubinden. Für Sie als Verfahrensverantwortlicher bietet das erhebliche Vorteile:

- **Sicherheit & DVC-Bereitschaft:** zentral BSI-konforme Sicherheit (MFA, Zero-Trust für Remote-Zugriffe via BYOD) und offene Standards (OIDC), die für moderne, föderale Cloud-Architekturen gefordert werden.
- **Weniger Support-Aufwand:** das zeitraubende manuelle Anlegen, Ändern und Löschen von Benutzern entfällt durch automatisierte Schnittstellen (Provisionierung).
- **Nutzerkomfort:** nahtloses Single Sign-On (SSO) – perspektivisch auch über Behörden- und Ländergrenzen hinweg.

Da uns aktuell viele Anfragen erreichen, planen wir derzeit unsere Onboarding-Kapazitäten und die Priorisierung unserer Rollout-Roadmap. Um Ihre fachlichen und architektonischen Anforderungen exakt zu verstehen und verbindlich Ressourcen für den Integrations-Support zu reservieren, bitten wir Sie, den beiliegenden Anforderungssteckbrief auszufüllen.

Gerne unterstützen wir Sie oder Ihren technischen Dienstleister beim Ausfüllen auch vorab in einer kurzen Videokonferenz.

**Bitte senden Sie uns den ausgefüllten Steckbrief bis zum [Datum eintragen] an [E-Mail-Adresse EIM-Team] zurück**, damit wir Ihr Verfahren in unserer Ressourcenplanung entsprechend priorisieren können.

Mit besten Grüßen
**[Ihr Name]**
*Projektleitung Enterprise Identity Management*
