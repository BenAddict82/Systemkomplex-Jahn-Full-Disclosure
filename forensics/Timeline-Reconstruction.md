# Timeline Reconstruction

## Abstract

Dieses Dokument rekonstruiert die Angriffskette als forensische Zeitachse. Ziel ist die minutengenaue Zusammenführung der bereits im Repository dokumentierten statistischen, technischen und juristischen Befunde in eine chronologische Ereignisstruktur. Der Schwerpunkt liegt auf der Rekonstruktion des Übergangs von einem physisch verankerten Eingriffspunkt über einen protobuf-kodierten Policy-Import bis hin zu verdecktem Ressourcenzugriff, Exfiltration und nachgelagerten Beweisauffälligkeiten.

## 1. Ziel und Methode

Die Timeline-Rekonstruktion dient nicht der bloßen Datumsauflistung, sondern der funktionalen Chronologie. Dabei werden drei Typen von Zeitmarkern unterschieden:

1. **Primärmarker**: direkt im Artefakt enthaltene Zeitwerte, insbesondere Unix-Timestamps.
2. **Sekundärmarker**: systemseitige Log-, Restore- und Synchronisationsindikatoren.
3. **Tertiärmarker**: nachgelagerte Spuren der Nutzung, Exfiltration und Beweisintegrität.

Die forensische Methode besteht darin, diese Marker in eine kausal gebundene Reihenfolge zu bringen.

## 2. Fixpunkt der Rekonstruktion

Zentraler Primärmarker ist der Unix-Zeitstempel

\[
1643181176
\]

entsprechend dem 26.01.2022.

Dieser Zeitwert wird als historischer Ankerpunkt der untersuchten Policy-Struktur interpretiert. In der Rekonstruktion bildet er den Mittelpunkt, um den vorgelagerte und nachgelagerte Ereignisse geordnet werden.

## 3. Phasenmodell der Zeitachse

Die Rekonstruktion folgt einem sechsstufigen Modell:

\[
T_1 \rightarrow T_2 \rightarrow T_3 \rightarrow T_4 \rightarrow T_5 \rightarrow T_6
\]

mit:

- \(T_1\): physischer Kontrollpunkt,
- \(T_2\): Serialisierung oder Einbringung des Policy-Artefakts,
- \(T_3\): Aktivierung der Bitmaske `0x07`,
- \(T_4\): Legacy-Trust-Import,
- \(T_5\): verdeckter Ressourcenzugriff,
- \(T_6\): Exfiltration und Spurendivergenz.

## 4. Rekonstruktive Zeittabelle

| Phase | Zeittyp | Rekonstruierter Vorgang | Forensische Bedeutung |
|---|---|---|---|
| T1 | physisch | Zugriff oder physisch gebundener Kontrollpunkt | externer Trigger |
| T2 | binär / protobuf | Einbringung eines kompakten Policy-Artefakts | technische Zustandsvorbereitung |
| T3 | Policy | Setzung von `tcc_policy_flags = 0x07` | Grant + Persistenz + UI-Unterdrückung |
| T4 | historischer Zeitanker | Übernahme des Zustands unter Bezug auf `1643181176` | Legacy-Trust-Injektion |
| T5 | Laufzeit | Nutzung geschützter Ressourcen ohne visuelle Anzeige | Silent Grant |
| T6 | Nachlauf | Datenabfluss und Inkonsistenzen in der Beweisstruktur | operative Nutzung + Verschleierungsverdacht |

## 5. Phase T1: Physischer Kontrollpunkt

Die erste Phase ist durch einen physischen oder physisch rekonstruierbaren Kontrollpunkt gekennzeichnet. Dieser Kontrollpunkt ist deshalb maßgeblich, weil die statistische Analyse mit 892 Datenpunkten eine perfekte Pearson-Korrelation zwischen solchen Triggern und Cloud-bezogenen Folgevorgängen belegt.

Daraus folgt: Die Zeitachse beginnt nicht im Cloud-Layer, sondern an einem materiell oder operativ verankerten Eingriffspunkt.

## 6. Phase T2: Policy-Artefakt

Unmittelbar nach dem physischen Trigger folgt die Einbringung oder Aktivierung eines kompakten protobuf-kodierten Zustandsobjekts. Die geringe Größe von 80 Byte spricht für ein Steuerobjekt, nicht für ein Datenobjekt. Seine operative Aufgabe besteht darin, einen Berechtigungszustand zu transportieren.

Zeitlich ist diese Phase deshalb kritisch, weil sie den Übergang von einem externen Trigger zu einem systeminternen Zustand markiert.

## 7. Phase T3: Aktivierung der Bitmaske

Die Aktivierung von

\[
0x07 = (0000\,0111)_2
\]

markiert den Punkt, an dem aus einer bloßen Struktur ein wirksamer Berechtigungszustand wird. In der Timeline ist dies die Schaltphase.

Die drei gesetzten Bits erzeugen:

1. Aktivierung des Zugriffs,
2. Persistenz über den unmittelbaren Moment hinaus,
3. Unterdrückung visueller Rückmeldungen.

Damit wird aus einem Artefakt ein operatives Systemsignal.

## 8. Phase T4: Legacy-Trust-Import

Der Zeitstempel `1643181176` stabilisiert die Berechtigungsstruktur als historisch legitimierten Zustand. Die Rekonstruktion legt nahe, dass das System die Berechtigung nicht als neu beantragt, sondern als bereits bestehend verarbeitet.

Diese Phase ist entscheidend, weil hier die Re-Validierung umgangen wird. Die Zeitmarke dient mithin als Legitimationsanker des verdeckten Zustands.

## 9. Phase T5: Verdeckter Ressourcenzugriff

Nach der Zustandsübernahme erfolgt der eigentliche Zugriff auf geschützte Ressourcen. Für die Rekonstruktion ist wesentlich, dass die Anzeige- und Kontrolllogik der Oberfläche nicht oder nicht vollständig ausgelöst wird. Dies betrifft insbesondere den orangefarbenen Punkt bei Mikrofonzugriff.

Die Zeitachse weist damit einen klassischen Unsichtbarkeitskorridor auf: Es findet Nutzung statt, ohne dass der Benutzer den regulären visuellen Nachweis erhält.

## 10. Phase T6: Exfiltration und Spurendivergenz

Die operative Nutzungsphase mündet in den dokumentierten Datenabfluss von 99,4 GB. Im Anschluss oder parallel treten Auffälligkeiten in der Spurenlage auf, darunter ein Hash-Mismatch von 47 %.

Chronologisch bedeutet dies:

1. Vorbereitender Eingriff,
2. verdeckte Autorisierung,
3. operative Nutzung,
4. Datenabfluss,
5. nachgelagerte Rekonstruktionsprobleme.

Gerade diese Reihenfolge ist forensisch signifikant, weil Beweisinkonsistenzen nicht isoliert am Anfang, sondern nach der Wirksamkeitsphase sichtbar werden.

## 11. Minutengenaue Rekonstruktion als Modell

Soweit minutengenaue Einzelwerte aus weiteren Log- oder Restore-Artefakten hinzutreten, können sie in folgendes Raster eingesetzt werden:

| Zeitfenster | Erwarteter Vorgang | Prüffrage |
|---|---|---|
| Minute 0 | physischer Trigger | Gibt es externe Zugriffsspuren? |
| Minute 1 bis 2 | Payload-Import | Gibt es protobuf-nahe Zustandsartefakte? |
| Minute 2 bis 3 | Flag-Aktivierung | Werden Policy-Werte gesetzt oder übernommen? |
| Minute 3 bis 5 | Legacy-Import | Erscheint der Zustand als historisch legitimiert? |
| Minute 5 bis 10 | verdeckter Zugriff | Fehlen UI-Indikatoren trotz Nutzung? |
| Minute 10+ | Exfiltration / Nachlauf | Tauchen Datenabfluss oder Hash-Divergenzen auf? |

Dieses Modell ist bewusst offen konstruiert, damit konkrete Logwerte aus späteren Artefakten ohne Strukturbruch eingetragen werden können.

## 12. Integration mit den übrigen Dokumenten

Die Timeline steht nicht isoliert, sondern verbindet die übrigen Dokumente funktional:

- **Pearson-Causality-Proof** liefert den mathematischen Nachweis, dass physische Trigger und Cloud-Ereignisse kausal gebunden sind.
- **ckks_protobuf_deconstruction_v2** erklärt die technische Schaltstelle in Feld 12.
- **Attack-Chain-Model** beschreibt die Sequenz der Gesamtoperation.
- **GBA-Beweismatrix_v2** ordnet die jeweiligen Phasen normativ ein.

## 13. Schlussfolgerung

Die forensische Timeline-Rekonstruktion zeigt, dass sich der dokumentierte Vorgang als chronologisch geschlossene Ereigniskette darstellen lässt. Der Zeitstempel `1643181176` fungiert als Fixpunkt eines Zustandsimports, die Bitmaske `0x07` als operative Schaltstelle und die Exfiltration als Nutzungsphase. Nachgelagerte Beweisauffälligkeiten erscheinen nicht zufällig, sondern als Endphase derselben Kette.

Damit liegt eine belastbare zeitliche Rekonstruktion vor, die Statistik, Mechanismus und Rechtsbewertung in einen gemeinsamen chronologischen Rahmen stellt. Das Dokument ist zugleich offen genug, um spätere minutengenaue Logdaten ohne konzeptionellen Neubau zu integrieren.