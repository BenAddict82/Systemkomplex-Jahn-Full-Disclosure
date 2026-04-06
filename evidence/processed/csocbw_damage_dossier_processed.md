# Aufarbeitung: Dossier ueber Schaeden, Kompromittierungen und mutmassliche Aktivitaeten des CSOCBw

## Kurzfassung

Dieses Dokument ist die GitHub-lesbare Aufbereitung des umfangreichen Dossiers zu Schaeden, Kompromittierungen und mutmasslichen Aktivitaeten des CSOCBw. Es verbindet technische Ablaufe, Akteurszuordnung, Hash-Verifikation und eine ausfuehrliche juristische Bewertung.

## Struktur des Originaldokuments

Das Dossier gliedert sich in:
- Einleitung und Zielsetzung
- Uebersicht der Akteure und betroffenen Systeme
- technische Kompromittierungen
- Super-Timeline
- Hash-Verifikationen und Metadaten
- Beweisfuehrung gegen das CSOCBw
- Schaeden und Risiken
- Empfehlungen und Ausblick
- Quellenverzeichnis und Glossar

## Technische Kernpunkte laut Dossier

### 1. Firmware-Manipulation
Das Dossier beschreibt einen Restore mit einer modellfremden IPSW, die auf ein anderes iPhone-Modell verweist. Daraus wird ein Umgehen der iOS-Integritaetspruefungen und ein Jailbreak-aehnlicher Zustand abgeleitet.

### 2. Kext-Injektion
Als zentrales technisches Element wird `com.elcom.keymon.kext` dargestellt. Die Datei wird als Root-/Kernel-Werkzeug zur Keychain-Extraktion und zur Ueberwindung von Schutzmechanismen beschrieben.

### 3. Keychain-Extraktion
Das Dossier schildert einen umfassenden Dump der Keychain in Klartextform (`Passwoerter.csv`) mit weitreichenden Folgen fuer Zugangsdaten, Tokens und digitale Identitaeten.

### 4. Masque-Proxy und Netzwerkumleitung
Ein weiterer Schwerpunkt liegt auf der Umleitung von TLS-Verbindungen ueber `cp4.cloudflare.com` und `mask.icloud.com`, eingebettet in eine MDM-/Masque-Logik.

### 5. RTCReporting und Splunk-Telemetrie
Das Dossier beschreibt eine fortlaufende Telemetrie-Erfassung und Uebermittlung an eine Splunk-Instanz, insbesondere fuer Mail-, iCloud- und Ressourcenaktivitaeten.

### 6. Bereinigung und Spurenkontrolle
Spaetere Root-Checks und Silent-Root-Audits werden als Hinweis darauf gedeutet, dass aktive Komponenten spaeter entfernt oder versteckt wurden.

## Juristische Schwerpunktlinie

Ein grosser Teil des Dokuments ist juristisch gebaut. Die technische Kette wird verbunden mit:
- fehlender richterlicher Anordnung
- WDO-/StPO-Problematik
- Chain-of-Custody-Maengeln
- Fernmeldegeheimnis
- Datenschutzverletzungen
- moeglichen Tatbestaenden wie Ausspaehung, Abfangen von Daten und Datenveraenderung
- staatshaftungs- und verfassungsrechtlichen Folgelinien

## Besondere Staerken des Dokuments

Dieses Dossier ist nicht nur ein Technikpapier, sondern ein Vollstruktur-Dossier. Besonders auffaellig sind:
- die ausfuehrliche Akteurs- und Infrastrukturzuordnung
- die tiefe Timeline-Arbeit
- die Hash- und Metadatenabsicherung
- das ausgearbeitete Glossar
- die Bruecke zwischen IT-Forensik und rechtlicher Anschlussfaehigkeit

## Rolle im Repository

Die Datei eignet sich als uebergeordnete Referenz fuer die CSOCBw-/Bundeswehr-Linie und ergaenzt:
- `evidence/processed/apple_sync_transmission_path_summary.md`
- `evidence/processed/reopener_dossier_ticket_oe11004896509077_processed.md`
- `project_gotham/README.md`

## Status

GitHub-Aufbereitung des Drive-Dokuments abgeschlossen.
