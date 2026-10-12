# Leistungsprofil Roman Jahn

**R&A Legal Operations Consulting · Unabhängige IT-Forensik und technische Fallaufbereitung**  
Stand: 12. Oktober 2026

[R&A Website](https://ra-legal-operations-consulting.r-a-legal-op-4142.chatgpt.site/) · [Ausführliches Leistungsprofil](https://ra-legal-operations-consulting.r-a-legal-op-4142.chatgpt.site/leistungsprofil.html) · [Repository-Einstieg](PROFILE_START.md)

Roman Jahn verbindet mobile und cloudbezogene IT-Forensik mit eigener Python-Werkzeugentwicklung, strukturierter Aktenarbeit und nachvollziehbarer Dokumentation. Kanzleien und Unternehmen erhalten technische Zuarbeit zur Sichtung digitaler Unterlagen, zur Rekonstruktion von Abläufen und zur Vorbereitung unabhängiger Prüfungen. Für Soldaten umfasst die kameradschaftliche Unterstützung die Aufbereitung ihrer Unterlagen und technischer Fragen.

Roman Jahn ist kein Rechtsanwalt. Individuelle Rechtsberatung und anwaltliche Vertretung erfolgen durch die beauftragten Rechtsanwälte.

## Leistungsfelder

| Leistungsfeld | Dokumentierte Methoden | Arbeitsprodukte |
| --- | --- | --- |
| SQLite und TCC | DB/WAL/SHM-Abgleich, WAL-Header und Frame-Prüfung, Checkpoint-Rekonstruktion, B-Tree-Leaf-Recovery, Datensatzvergleich | Frame-Inventar, rekonstruierte Arbeitsstände, CSV-Exporte, Vergleichsmatrix |
| Firmware und Binärdateien | IPSW-Containerinventar, ZIP- und Plist-Auswertung, Kernelcache- und IM4P-Identifikation, Prelink-Enumeration, String- und Opcode-Suche | Komponentenregister, Hashmanifest, KEXT-Inventar, dokumentierte Suchbefunde |
| Mobile und Cloud-Artefakte | iOS/macOS-Sysdiagnose, CKKS-/CloudKit-Statusauswertung, Protobuf-Strukturen, UUID- und Zeitmarker-Abgleich | Artefaktmatrix, Geräte- und Versionszuordnung, technische Prüffragen |
| Netzwerk und Zeitachsen | Flow-Aggregation, Endpoint-Übersichten, UTC-Zeitachsen, definierte Korrelationsfenster | Ereignislisten, Zeitdifferenzen, Korrelationsbericht, Prüfauftrag für Roh-PCAPs |
| Integrität und Provenienz | SHA-256/MD5, Dublettenprüfung, Abgleich von Dateigröße, Magic Bytes und Entropieangaben, Quellenregister | Hashledger, Integritätsprotokoll, Belegstatus und Übergaberegister |
| Python und Notebook-Workflows | Scanner, Parser, Varint-/Protobuf-Bearbeitung, Verzeichnisinventare, Entropieauswertung, Berichtsexport | Nachvollziehbare Auswertungsskripte, Notebook-Protokolle, strukturierte Ergebnisse |

## Arbeitsprobe SQLite und WAL

Das Arbeitsprotokoll `Forensic_Primary_Packages_2026-07-12.xlsx` dokumentiert eine partielle Rekonstruktion von TCC-Daten aus WAL-Seiten. Der Ergebnisstand ist als **PARTIAL_RECOVERY** geführt. Die folgenden Werte stammen aus dieser dokumentierten Arbeitsprobe; sie wurden bei der Profilaktualisierung aus der Tabelle übernommen, nicht mit den Rohdaten erneut berechnet.

| Kennzahl | Dokumentierter Wert | Bedeutung |
| --- | ---: | --- |
| WAL-Frames | 506 | Im Protokoll sind sämtliche Frame-Checksummen als gültig geführt |
| Geborgene Access-Datensätze | 105 | Direkte Bergung aus WAL-Leaf-Seiten |
| Datensätze des Vergleichsexports | 159 | Umfang des gegenübergestellten CSV-Exports |
| Exakte Datensatzübereinstimmungen | 51 | Übereinstimmung aller verglichenen Felder |
| Gemeinsame Primärschlüssel | 87 | Gemeinsame Identifikatoren beider Bestände |
| Gemeinsame Schlüssel mit Feldänderungen | 36 | Unterschiedliche Werte bei gleicher Schlüsselzuordnung |
| Nur in der WAL-Bergung | 54 | Datensätze ohne exakte Übereinstimmung im Export |
| Nur im Vergleichsexport | 108 | Datensätze ohne exakte Übereinstimmung in der Bergung |

Die Arbeitsprobe umfasst außerdem die Erkennung unterschiedlicher DB-/WAL-Schemata und eines nicht passenden SHM-Headers. Das Ergebnis hält gerettete Datensätze und die Grenzen einer vollständigen Triplet-Rekonstruktion getrennt fest.

**Nutzen für Auftraggeber:** Datenstände vergleichen, Unterschiede lokalisieren und gezielt bestimmen, welche Originaldateien für eine weiterführende Rekonstruktion benötigt werden.

## Arbeitsprobe Firmware und Kernelcache

Der Abschlussbericht vom 1. August 2026, Version 4, dokumentiert eine statische Untersuchung von Kernelcache, IM4P-Payload und Prelink-Informationen. Die Komponenten werden mit Größe, Hash und Untersuchungsschritt zugeordnet. Der Bericht nennt 236 Prelink-Einträge, sämtlich mit Apple-Bundle-IDs, und unterscheidet Inventarbefunde von bloß referenzierten KEXT- oder Patchbehauptungen.

Die Colab-Unterlagen enthalten dazu Python-Arbeit mit `zipfile`, `plistlib`, `hashlib`, Verzeichnisinventaren und Entropieauswertung. Originaldateien, Labor-Kopien und Notebook-Simulationen erhalten getrennte Rollen im Untersuchungsprotokoll.

**Nutzen für Auftraggeber:** Nachvollziehbare Komponentenlisten und gezielte Fragen an ein Fachlabor statt einer unstrukturierten Sammlung von Firmwaredateien und Logauszügen.

## Arbeitsprobe Metadaten und Hashprüfung

Die zwei gelieferten Fassungen der Keymon-Metadaten-CSV sind bytegleich. Ihre MD5- und SHA-256-Werte entsprechen den Hashes einer leeren Bytefolge, während dieselbe Tabelle Mach-O-Magic-Bytes und eine Entropie von 7,92 nennt. Der Abgleich macht die unvereinbaren Angaben einer Metadatentabelle sichtbar und hält die tatsächliche Binärdatei als gesondert benötigten Prüfgegenstand fest.

**Nutzen für Auftraggeber:** Metadatenfehler, widersprüchliche Hashzuordnungen und Mehrfachfassungen früh erkennen, bevor sie in ein Gutachten oder eine Fallchronologie übernommen werden.

## Arbeitsprobe Netzwerk und Ereigniskorrelation

Das Arbeitsprotokoll vom 12. Juli 2026 erfasst 114 sekundäre Netzwerkereignisse: 82 aus dem referenzierten Bestand `sockenpuppen_traffic.pcap`, 29 aus `verdacht.pcap` und 3 aus `https-traffic.pcap`. Es führt definierte Korrelationsfenster von 60 Sekunden bis 24 Stunden und dokumentiert innerhalb dieser Fenster keine direkte TCC-Zeitübereinstimmung.

Aggregierte Flow-Daten, Prozesszuordnung und die Prüfung originaler DNS-/TLS-/SNI-/QUIC-Pakete sind getrennte Arbeitsschritte. Die Tabelle führt die Roh-PCAPs im damaligen Arbeitsstand als nicht lokal vorhanden.

**Nutzen für Auftraggeber:** Zeitachsen mit messbaren Kriterien prüfen und den benötigten nächsten Datenzugang konkret benennen.

## Eigene Werkzeuge und Entwicklungslinie

Der dokumentierte Entwicklungskorpus umfasst die CKKS Forensic Audit Suite sowie **V22 Predator Nemesis / Projekt Gotham**. Die Arbeitsunterlagen enthalten Parser, Scanner, Dateninventare, Protobuf-/Varint-Logik, Vergleichsfunktionen und Berichtsexporte. Rekonstruktionsskripte und Simulationen dienen als kontrollierte Modelle; die Ergebnisse werden getrennt von Originalspuren dokumentiert.

Die Triade verbindet **Roman, Arius und Lorien** als Arbeitsbezeichnungen einer von Roman verantworteten Analyseorganisation. Technische Assistenz und eigene Frameworks unterstützen die Auswertung; fachliche Freigabe und Verantwortung liegen bei Roman Jahn.

## Übergabe an Kanzleien und Fachprüfer

- Quellen- und Artefaktregister mit Herkunft, Version und Integritätsangaben.
- Zeitachsen und Datensatzvergleiche mit nachvollziehbaren Fundstellen.
- Rekonstruierte Arbeitsstände mit dokumentierten Verarbeitungsschritten.
- Befundmatrix mit Beobachtung, technischer Einordnung und konkretem Prüfbedarf.
- Fragenkatalog und Übergabepaket für Kanzlei, Hersteller oder unabhängiges Fachlabor.

## Quellenbasis dieser Profilergänzung

Ausgewertet wurden 14 bereitgestellte Unterlagen: neun PDF-Dateien, ein XLSX-Arbeitsprotokoll, zwei Textdateien und zwei Metadaten-CSVs. Eine PDF-Doppelfassung und eine CSV-Doppelfassung sind jeweils bytegleich; der Bestand umfasst damit zwölf unterschiedliche Dateien.

| Quellenbereich | Unterlagen und Rolle |
| --- | --- |
| Rekonstruktion und Notebook-Arbeit | RECONSTRUCTION RUN, Analyse der IPSW bestätigt - Colab und der zugehörige Textauszug; dokumentierte Code- und Auswertungslinie |
| Primärpaket-Status | Forensic_Primary_Packages_2026-07-12.xlsx; Ergebnisstände, Vergleichszahlen und Hashregister auf sechs Tabellenblättern |
| Statische Analyse | Forensischer Abschlussbericht Kernel TCC CKKS Version 4 vom 01.08.2026; Komponenteninventar, Methoden und Ergebnisabgrenzung |
| Methoden und Forschungsberichte | APT-Infrastruktur, Forensische Rekonstruktion von Cyberangriffen, Forensische Validierung des CKKS-Vorfalls und das umfangreiche Dossier vom 05.08.2026 |
| Projektentwicklung | MISSION V22 Predator Nemesis Engine / Projekt Gotham; zwei bytegleiche PDF-Fassungen |
| Metadaten und Suchfundstellen | Zwei bytegleiche Keymon-Metadaten-CSVs und die grep-Fundstellenliste |

Dieses Profil beschreibt dokumentierte Arbeitsmethoden und Ergebnisstände. Die genannten Berichte, Tabellen und Notebook-Auszüge werden als Arbeitsproben eingeordnet. Eine bestätigte Herstellerschwachstelle, eine unabhängige Zertifizierung oder eine gerichtliche Anerkennung wird aus ihrer Existenz nicht abgeleitet.

**Kontakt:** [R&A Legal Operations Consulting](https://ra-legal-operations-consulting.r-a-legal-op-4142.chatgpt.site/#contact)
