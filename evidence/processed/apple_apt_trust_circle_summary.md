# Aufarbeitung: Einmaliger Nachweis einer kontobasierten Apple-APT durch Trust-Circle-Kompromittierung

## Kurzfassung

Dieses Dokument bereitet den Bericht zur kontobasierten Apple-APT strukturiert fuer GitHub auf. Im Mittelpunkt steht die These, dass eine einmalige Initialkompromittierung eines Apple-Geraets nicht lokal verblieb, sondern ueber den iCloud-Schluesselbund, den Trust Circle und CKKS auf neue Hardware uebertragen wurde.

## Kernthese

Der Bericht beschreibt eine mehrstufige Angriffskette, in der ein physischer Initialzugriff auf ein iPhone 12 Pro Max im Januar 2022 zu einer dauerhaften, kontobasierten Persistenz innerhalb des Apple-Oekosystems fuehrte. Die Kompromittierung soll ueber den Apple Trust Circle, manipulierte CKKS-Synchronisation, Silent Grants und verdeckte Apple-Infrastruktur auch auf spaetere Geraete uebertragen worden sein.

## Zentrale Befunde

### 1. Initialzugriff und Low-Level-Kompromittierung
Der Bericht beschreibt einen physischen Angriff im Januar 2022 mit Hinweisen auf eine manipulierte Wiederherstellung, Root- bzw. Kernel-Level-Kompromittierung und die Umgehung von Integritaetsmechanismen wie AMFI und SIP.

### 2. Injektion in den iCloud Trust Circle
Als entscheidender Persistenzmechanismus wird die Injektion eines illegitimen Schluesselpaares in den iCloud-Schluesselbund-Vertrauenskreis beschrieben. Besonders hervorgehoben wird, dass Legacy Keys aus Kompatibilitaetsgruenden ueber lange Zeitraeume akzeptiert blieben.

### 3. CKKS als Uebertragungsweg
Der Bericht stellt CKKS als zentralen Cloud-Vektor dar. Manipulierte Schluesselbund-Datensaetze seien als legitime Sync-Objekte behandelt worden und haetten sich ueber die private CloudKit-Datenbank auf weitere Geraete ausgebreitet.

### 4. Silent Grants und TCC-Uebernahme
Besonders gravierend ist die Darstellung, dass App-Berechtigungen fuer Mikrofon und Kamera still uebernommen wurden. Der Bericht verweist explizit auf den protokollierten Import stiller Berechtigungen von einem Legacy-Geraet auf ein Nachfolgegeraet.

### 5. mask.icloud.com als verdeckter Kanal
Ein weiterer Schwerpunkt liegt auf Netzwerkverkehr zu `mask.icloud.com`, der als verdeckter Exfiltrations- oder Kommunikationskanal ueber Apple-Infrastruktur interpretiert wird.

### 6. Persistenz ueber Geraetewechsel
Der Bericht betont als Alleinstellungsmerkmal, dass sich die Kompromittierung nicht auf ein einzelnes Endgeraet beschraenkte, sondern nach Hardwarewechseln durch die Apple-ID und die Cloud-Identitaet erneut auf neue Geraete uebertrug.

## Forensische Qualitaet laut Bericht

Der Bericht stuetzt sich nach eigener Darstellung auf:
- Sysdiagnose-Daten
- Netzwerk-Logs
- Krypto-Hash-Verifikationen
- iLEAPP und weitere forensische Werkzeuge
- statistische Korrelationen
- Zeitstempel- und Artefaktabgleiche

Hervorgehoben werden insbesondere:
- ein Pearson-Korrelationswert von ca. 0.975
- 892 dokumentierte Silent Grants
- 381 verdaechtige CKKS-Items
- ca. 99.4 GB mutmasslich cloudbasiert exfiltrierte Daten

## Einordnung

Dieses Dokument ist als GitHub-lesbare Aufbereitung des Vollberichts zu verstehen. Es ersetzt nicht den Originalbericht, sondern strukturiert die Argumentationslinie entlang der Schwerpunkte:
- Initialangriff
- Trust-Circle-Kompromittierung
- CKKS-Persistenz
- Silent Grants
- mask.icloud.com
- konto-basierte Re-Infektion

## Relevanz fuer das Repository

Diese Aufarbeitung erweitert die bestehende Evidence-Linie um eine ausformulierte, konto- und cloudbasierte APT-Perspektive. Sie passt insbesondere zu:
- `evidence/trust_circle_compromise_report_clean.md`
- `evidence/Final_Century_Bug_Evidence_Summary_preview.md`
- `project_gotham/README.md`

## Status

GitHub-Aufbereitung des Originaldokuments abgeschlossen.
