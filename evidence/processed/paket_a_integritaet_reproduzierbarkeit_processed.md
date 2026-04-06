# Aufarbeitung: Paket A – Integritaet & Reproduzierbarkeit

## Kurzfassung

Dieses Dokument ist die GitHub-lesbare Aufbereitung von "Paket A – Integritaet & Reproduzierbarkeit". Der Text ist als operatives Forensik-Playbook aufgebaut und konzentriert sich auf eine lueckenlose, gerichtsfeste Beweiskette fuer den Restore-/Kext-/Modell-Mismatch-Komplex.

## Zielbild des Pakets

Paket A will den Nachweis entlang vier Fixpunkten stabilisieren:
- manipulativer Restore am 26.01.2022
- IPSW-Hash `ac2d...fee3`
- modellfremde IPSW fuer `iPhone10,6`
- Kext-Load `com.elcom.keymon.kext` um 07:12:56

Der Anspruch ist, diese Eckdaten so zu sichern, dass sie reproduzierbar, hash-gestuetzt und gerichtsfest nachvollzogen werden koennen.

## Hauptbestandteile des Pakets

### 1. Evidenz-Freeze und Chain of Custody
Das Paket verlangt ein strenges Artefakt-Management mit:
- Asservatenspiegel
- CoC-Formblaettern
- Read-only-Arbeitskopien
- Zeitbeurkundung / TSP / notarielle Absicherung
- Hash-Ledger mit SHA-256 und SHA-512

### 2. IPSW-Integritaet und Binary-Diff
Ein Schwerpunkt liegt auf dem Abgleich der Beweis-IPSW mit Referenzmaterial. Ziel ist nicht nur die Hash-Uebereinstimmung, sondern vor allem die Feststellung des Modell-Mismatchs zwischen der IPSW fuer `iPhone10,6` und dem Zielgeraet `iPhone15,3`.

### 3. Kext-Nachweis
Das Paket fordert eine sekundennahe Korrelation zwischen Restore und Kext-Load. Der Kext wird als Rootkit-Typus bzw. Elcomsoft-nahe Komponente gerahmt, deren Existenz und Signaturstatus gerichtsfest gesichert werden sollen.

### 4. Timeline-Korrelation
Ein weiterer Baustein ist die Super-Timeline: Restore-Beginn, Restore-Ende, Kext-Load und nachgelagerte technische Effekte werden in eine sekundenbasierte Kausalkette ueberfuehrt.

### 5. Reproduktions-Harness
Paket A ist stark skript- und workflow-orientiert. Es beschreibt, wie aus den Artefakten ein reproduzierbarer Repro-Bericht mit Hash-Tabellen, Segment-Diffs, Timeline-Grafiken und Modell-Kacheln gebaut werden soll.

## Zusaetzliche Paketteile im Dokument

Das PDF enthaelt ueber Paket A hinaus auch weitere ausgearbeitete Pakete:
- Paket B zur TLS-/Proxy-Beweisfuehrung
- Paket C zu Scope/Cloud und Verwertungsangriff
- Paket D zur Selektionslogik der 19 Dateien

Damit ist das Dokument nicht nur ein Integritaetspapier, sondern ein umfangreiches Operations- und Schriftsatz-Playbook.

## Rolle im Repository

Diese Aufarbeitung ist besonders nuetzlich fuer den forensischen Unterbau der Restore-/Kext-/Hash-Linie und ergaenzt:
- `evidence/processed/ckks_architecture_problem_big_picture_processed.md`
- `evidence/processed/reopener_dossier_ticket_oe11004896509077_processed.md`
- `evidence/processed/csocbw_damage_dossier_processed.md`

## Status

GitHub-Aufbereitung des Drive-Dokuments abgeschlossen.
