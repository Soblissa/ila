# Agentenkommunikation: Status & offene Fragen

**Stand:** 2026-03-31  
**Autor:** Cheko (ILA-Hauptagent)  
**Für:** Torsten

---

## Was heute getan wurde

### Infrastruktur
- Chekos Gateway läuft auf Port **19840**, bind: LAN → von außen erreichbar unter `147.93.120.51:19840`
- Gateway-Config um `remote.url` ergänzt: `http://147.93.120.51:19840`
- Neuer Operator-Token erzeugt (via `devices rotate`) mit Scopes `operator.read`, `operator.write`, `operator.admin`

### Erkenntnisse zur Serverstruktur
Auf dem Server laufen **drei** OpenClaw-Instanzen als separate Linux-Nutzer:
- `user1` → Cheko (Port 19840, öffentlich)
- `turyia` → Turiya (Port 19870, loopback)
- `user2` → weiterer Agent

### Was funktioniert
- Turiya erreicht Chekos Gateway technisch (`Connect: ok`)
- Gateway-Token ist korrekt für den Verbindungsaufbau

### Was nicht funktioniert
- Turiya bleibt bei `RPC: limited - missing scope: operator.read`
- `openclaw gateway probe` erzeugt keinen Pairing-Request (ist nur ein Test, kein Verbindungsaufbau)
- `openclaw devices list` zeigt nur das bereits vorhandene gepaarte Gerät — kein neuer Pending-Request von Turiya

---

## Analyse: Was fehlt

Das OpenClaw Device-Pairing-Modell ist auf **Endgeräte** ausgelegt (iOS, Android, macOS, headless Node). Für **Agent-zu-Agent-Kommunikation** zwischen zwei Gateway-Instanzen auf demselben Server gibt es in der Dokumentation keinen expliziten Weg über direktes Gateway-Pairing.

**Wahrscheinliche Lösung:** Agent-zu-Agent-Kommunikation in OpenClaw läuft über die **Sessions-Infrastruktur** (`sessions_send`, `sessions_spawn`) — nicht über direktes Gateway-Operator-Pairing.

---

## Offene Fragen für Torsten

1. **Wie kommunizieren zwei OpenClaw-Agenten auf demselben Server direkt miteinander?**  
   → Ist `sessions_send` mit `sessionKey` der richtige Weg, oder gibt es einen dedizierten Agent-zu-Agent-Kanal?

2. **Muss Turyias Gateway als "Remote-Gateway" in Chekos Config eingetragen werden?**  
   → Oder reicht es, wenn beide Agenten denselben `sessions`-Store kennen?

3. **Welcher Token-Typ muss Turiya haben, um als Operator auf Chekos Gateway zuzugreifen?**  
   → Gateway-Token reicht für Connect, aber nicht für `operator.read`. Was ist der fehlende Schritt?

4. **Kann Turiya als Node (nicht als Operator) an Chekos Gateway angebunden werden?**  
   → Das wäre technisch einfacher, aber semantisch falsch (Turiya ist kein Peripheriegerät).

---

## Empfehlung

Kurzfristig: Torsten prüft OpenClaw-Doku/Discord zum Thema **Multi-Agent auf demselben Server** — speziell `sessions_send` cross-agent.

Mittelfristig: Klarer Kommunikationskanal zwischen Turiya und Cheko definieren, damit Sarah nicht mehr als Copy-Paste-Brücke fungieren muss.

---

## Nächste Schritte

- [ ] Torsten klärt Multi-Agent-Kommunikation mit OpenClaw-Doku oder Community
- [ ] Sobald Lösung bekannt: Konfiguration anpassen und testen
- [ ] Danach: Plugin-Bau starten (Figma-Zugriff + Design-System-Analyse sind bereits fertig)
