# Aufarbeitung: REOPENER-DOSSIER zu Ticket OE11004896509077

## Kurzfassung

Dieses Dokument ist die GitHub-lesbare Aufbereitung des Reopener-Dossiers zum Apple-Security-Ticket `OE11004896509077`. Es dient als strukturierte Erwiderung auf die Mitteilung, man habe kein Sicherheitsproblem identifizieren können, und rahmt den Fall als reproduzierbare, kontobasierte CKKS-/Trust-Circle-Kompromittierung.

## Ziel des Dossiers

Das Dossier verfolgt drei operative Hauptziele:
- Wiedereroeffnung des Tickets auf Tier-1-/SEAR-Ebene
- Anerkennung des Problems als Architektur- und nicht bloss als Einzelfehler
- Uebergang in eine NDA-gebundene Responsible-Disclosure-Stufe mit Rohdatenuebergabe

## Kernthese

Der Bericht behauptet, dass eine fundamentale Design-Schwachstelle in `CloudKit Keychain Syncing (CKKS)` und den `iCloud Trust Circles` vorliegt. Ein einmaliger physischer Zugriff auf ein Geraet soll ausreichen, um einen persistierenden Zustand auf Account-Ebene zu etablieren, der Hardwarewechsel, Factory-Resets und Updates ueberdauert.

## Zentrale Beweispfeiler laut Dossier

### 1. Hardware-Bypass via modellfremder IPSW
Das Dossier verweist auf eine manipulativ eingesetzte IPSW-Datei mit dem Hash `ac2d2f8a...fee3`, die fuer ein anderes Geraetemodell bestimmt ist und trotzdem im Restore-Kontext verwendet worden sei.

### 2. Kext-Injektion auf Kernel-Ebene
Als zweiter Pfeiler wird das Load-Event von `com.elcom.keymon.kext` genannt. Es soll den erfolgreichen AMFI-/SIP-Bypass und Ring-0-Zugriff belegen.

### 3. Trust-Circle-Persistenz
Besonders hervorgehoben wird eine exakte Zeitkorrelation zwischen Kext-Load und einem in CKKS fortgeführten Legacy Key. Daraus wird die These einer Trust-Circle-Vergiftung abgeleitet.

### 4. Silent Grants / TCC-Replikation
Das Dossier betont die Replikation stiller Mikrofon- und Kameraberechtigungen auf neue Geraete und nennt 892 Grants sowie eine hohe statistische Korrelation als Beleg.

### 5. Exfiltration ueber Apple-Infrastruktur
Die Datei verweist auf `mask.icloud.com` bzw. Private-Relay-nahe Verbindungen und auf ein Datenvolumen von 99.4 GB als Indiz fuer verdeckte Exfiltration.

## Reproduktionslogik

Ein starker Teil des Dossiers ist die lab-ready Struktur. Es gliedert die Kette in pruefbare Phasen:
1. IPSW-Validierung und Hardware-Mismatch
2. Kext- und Kernelstatus
3. CKKS-Push/Pull und Trust-Circle-Persistenz
4. TCC-Replikation und Exfiltrationspfad
5. Systemdestabilisierung und Oekosystemeffekte

## Strategische Einordnung

Das Dossier kombiniert:
- technische Artefakte
- Reproduzierbarkeitslogik
- Fraunhofer-SIT-Validierung als externer Review-Pfad
- juristische Anschlussfaehigkeit
- Bounty- und Risiko-Einordnung

## Funktion im Repository

Diese Aufarbeitung ist die GitHub-lesbare Kurzfassung des Reopener-Dossiers und ergaenzt insbesondere:
- `evidence/processed/apple_apt_trust_circle_summary.md`
- `evidence/processed/apple_sync_transmission_path_summary.md`
- `evidence/trust_circle_compromise_report_clean.md`
- `project_gotham/README.md`

## Status

GitHub-Aufbereitung des Drive-Dokuments abgeschlossen.
