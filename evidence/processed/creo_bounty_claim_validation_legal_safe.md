# CREO Bounty Claim Validation: Legal-Safe Working Memo

## Zweck

Dieses Dokument dient der quellenbasierten und rechtlich defensiblen Einordnung oeffentlich behaupteter CREO-Sicherheitsmerkmale, des angekuendigten Bug-Bounty-/Responsible-Disclosure-Programms sowie der Grenzen zulaessiger Sicherheitsforschung.

Es ersetzt keine technische Exploit-Dokumentation und keine offensive Angriffsanleitung. Ziel ist vielmehr die Trennung zwischen:
- belastbar verifizierbaren oeffentlichen Aussagen
- derzeit nicht belastbar verifizierten Behauptungen
- realistischem, zulaessigem Bounty-Vorgehen
- rechtlich riskanten oder unzulaessigen Offensivhandlungen

---

## 1. Oeffentlich verifizierbare CREO-Aussagen

Nach den derzeit oeffentlich einsehbaren CREO-Quellen lassen sich insbesondere folgende Aussagen als vom Projekt selbst behauptet verifizieren:

- CREO ist laut eigener Website noch **nicht released** und **nicht public**.
- CREO bewirbt **AES-512**, **Cascade Encryption**, **Individual Encryption / IAE**, **SEP Network** und **Dedicated Private Network (DPN)** als Kernelemente.
- CREO macht sehr weitgehende Sicherheitsclaims wie **no master keys**, **no backdoors**, **no central servers**, **no message storage**, **no data collection** und **no surveillance**.
- Das Whitepaper beschreibt ein **permanentes Bug-Bounty-Programm** und **Responsible Disclosure**.
- Das Whitepaper nennt als Scope insbesondere kryptografische Fehler, Implementierungsfehler, Governance-Exploits und Abuse-Vektoren.
- Das Whitepaper nennt als Prozess: Acknowledgement innerhalb von 7 Tagen, Triage innerhalb von 30 Tagen und Release von Fixes innerhalb von 90 Tagen.
- Die Finanzierung moeglicher Bounties soll laut Whitepaper aus der **DAO Treasury** erfolgen.

---

## 2. Derzeit nicht belastbar verifizierte Punkte

Die folgende Behauptung ist in den geprueften offiziellen CREO-Quellen in dieser Form derzeit nicht belastbar als oeffentliche Zusage verifizierbar:

- eine konkret zugesagte oder garantiert auszahlbare **Einzelpraemie von 1.000.000 EUR oder USD** fuer einen bestimmten Fund

Solange hierzu keine klare, offizielle, schriftlich dokumentierte Programmbedingung vorliegt, darf ein solcher Betrag nur als **behaupteter Community- oder Marketing-Claim** behandelt werden, nicht als verifizierte Programmbedingung.

---

## 3. Fachliche Einordnung der Claims

Die derzeitige CREO-Kommunikation kombiniert:
- sehr starke Sicherheitsversprechen
- ein teilweise proprietaeres bzw. hybrides Open-/Closed-Source-Modell
- Verweise auf Audits und reproduzierbare Builds
- eine noch nicht oeffentlich verfuegbare Produktlage

Aus sicherheitstechnischer Sicht folgt daraus:
- Verifiziert sind primaer die **oeffentlichen Behauptungen**.
- Nicht verifiziert ist damit automatisch deren technische Richtigkeit.
- Fuer eine belastbare Bounty-Bewertung muessen Website-Claims, Whitepaper-Claims, reale Binaries, Build-Nachweise und Scope-Regeln getrennt betrachtet werden.

---

## 4. Realistisches und zulaessiges Bounty-Vorgehen

Ein rechtlich sauberes Vorgehen setzt zwingend voraus:

1. **Schriftliche Safe-Harbor-Bestaetigung**
   - ausdruecklich autorisierte Sicherheitsforschung
   - keine zivil- oder strafrechtlichen Schritte bei Scope-Einhaltung

2. **Klar definierter Scope**
   - welche Versionen getestet werden duerfen
   - welche Targets und Umgebungen erfasst sind
   - ob Reverse Engineering zulaessig ist
   - ob nur Testbuilds oder auch spaetere Produktivsysteme umfasst sind

3. **Klarer Reward-Rahmen**
   - Severity-Modell
   - Auszahlungsobergrenzen
   - Nachweisstandard
   - Ausschlussgruende

4. **Minimalinvasive und reproduzierbare Methodik**
   - Claim-vs-Proof-Pruefung
   - Audit-/Build-/Checksum-Validierung
   - Nachweis von Diskrepanzen zwischen behaupteten und real pruefbaren Eigenschaften
   - keine unautorisierten Zugriffe auf Nutzer-, Relay- oder Live-Systeme

---

## 5. Rechtlich riskante oder unzulaessige Offensivlinien

Nicht Bestandteil eines legalen Bounty-Vorgehens sind insbesondere ohne glasklare Autorisierung:

- Umgehung von Schutzmechanismen
- Exploit-Entwicklung
- Anti-Debug- oder Anti-Tamper-Bypass
- Speicher- oder Schluesselmaterial-Extraktion aus nicht autorisierten Targets
- Kernel-, TCC- oder Berechtigungs-Bypasses
- Angriffe auf Infrastruktur, Relay-Knoten, Produktivinstanzen oder Drittsysteme
- jede Form von Exfiltration oder versteckter Persistenz

---

## 6. Sinnvolle naechste Arbeitsprodukte im Repository

Fuer eine belastbare und rechtlich saubere Weiterarbeit sind insbesondere sinnvoll:

- `creo_claims_vs_proof_matrix.md`
- `creo_bounty_safe_harbor_checklist.md`
- `creo_responsible_disclosure_template.md`
- `creo_public_claims_evidence_map.md`

---

## 7. Arbeitsfazit

Der derzeit belastbare Stand lautet:

- CREO macht oeffentlich aussergewoehnlich starke Sicherheitsclaims.
- CREO kuendigt ein Responsible-Disclosure- und Bug-Bounty-Modell an.
- CREO ist laut Eigendarstellung noch nicht released bzw. nicht public.
- Eine konkrete, verifizierte, oeffentlich dokumentierte Einzelpraemie von 1.000.000 EUR/USD ist in den geprueften offiziellen Quellen derzeit nicht belastbar belegt.

Daraus folgt fuer das Repository:

Eine sachlich belastbare CREO-Linie muss auf **verifizierten Claims, Scope-Klaerung, Safe Harbor und reproduzierbarer Claim-Pruefung** beruhen – nicht auf offensiven Exploit- oder Infiltrationsnarrativen.
