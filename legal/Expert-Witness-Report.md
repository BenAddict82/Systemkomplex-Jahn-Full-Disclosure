# Expert Witness Report

## Technisches Sachverständigengutachten

### Betreff
Forensische, statistische und technische Begutachtung einer account-basierten Eingriffs- und Exfiltrationskette im Kontext der CKKS-Engine auf Apple-Systemen

---

## I. Gutachtenauftrag

Gegenstand dieses Gutachtens ist die sachverständige Bewertung der im Repository dokumentierten technischen, statistischen und zeitlichen Befunde. Ziel ist die Beantwortung der Frage, ob die vorliegenden Artefakte, Korrelationen und Rekonstruktionen mit einem zufälligen, regulären oder benignen Systemverhalten vereinbar sind oder ob sie auf eine funktional gekoppelte Eingriffs- und Exfiltrationskette hindeuten.

Das Gutachten ist so strukturiert, dass es sowohl als technische Anlage in einem gerichtlichen oder behördlichen Verfahren als auch als Grundlage für weitere beweisrechtliche und gutachterliche Vertiefungen verwendet werden kann.

---

## II. Untersuchungsgrundlagen

Die Begutachtung stützt sich auf die im Repository dokumentierten Kernbefunde, insbesondere auf folgende Module:

1. mathematische Auswertung der Pearson-Korrelation,
2. forensische Dekonstruktion der Datei `tcc_bypass_payload.bin`,
3. rekonstruktive Zeitachsenanalyse,
4. systemische Modellierung der Angriffskette,
5. juristische Beweismatrix.

Diese Module werden nicht isoliert behandelt, sondern als komplementäre Beweisbausteine eines einheitlichen technischen Geschehens gewürdigt.

---

## III. Methodisches Vorgehen

Die gutachterliche Bewertung erfolgt nach einem Mehr-Ebenen-Ansatz:

### 1. Statistische Plausibilitätsprüfung

Es wird geprüft, ob die dokumentierte Korrelation zwischen physischen Zugriffsmomenten und Cloud-bezogenen Ereignissen zufällig erklärbar ist.

### 2. Forensische Artefaktanalyse

Es wird untersucht, welche technische Funktion dem 80-Byte-Artefakt `tcc_bypass_payload.bin` zukommt und welche operative Bedeutung Feld 12 mit der Bitmaske `0x07` besitzt.

### 3. Rekonstruktive Chronologie

Die dokumentierten Primär-, Sekundär- und Tertiärmarker werden in eine zeitliche Kausalkette gebracht, um die Reihenfolge der mutmaßlichen Eingriffe zu bestimmen.

### 4. Systemische Gesamtbewertung

Abschließend wird geprüft, ob die Einzelbefunde zusammen ein geschlossenes Funktionsmodell ergeben.

---

## IV. Festgestellte Befunde

## 1. Statistischer Befund

Die Auswertung von 892 Datenpunkten ergab eine Pearson-Korrelation von

\[
r = 1{,}0
\]

zwischen physischen Eingriffs- oder Kontrollpunkten und Cloud-bezogenen Injektions- oder Folgeereignissen.

### Gutachterliche Würdigung

Ein perfekter Korrelationswert über eine derart große Zahl von Datenpunkten ist unter realen technischen Bedingungen außergewöhnlich. Praktische Systeme unterliegen regelmäßig Messrauschen, Laufzeitabweichungen, Synchronisationslatenzen, Clock-Drift und heterogenen Prozessdynamiken. Ein exakt idealer lineare Zusammenhang ist daher regelmäßig nur dann zu erwarten, wenn eine funktionale Bindung zwischen den verglichenen Ereignisreihen besteht.

Der statistische Befund spricht damit mit hoher Evidenz gegen ein zufälliges Nebeneinander unabhängiger Prozesse.

---

## 2. Forensischer Befund zum Policy-Artefakt

Bei der Datei `tcc_bypass_payload.bin` handelt es sich um ein kompaktes, protobuf-kodiertes Steuerartefakt mit einer Größe von 80 Byte. Von besonderer Bedeutung ist Feld 12 (`tcc_policy_flags`) mit dem Wert:

\[
0x07 = (0000\,0111)_2
\]

Die Bitzerlegung ergibt eine Kombination aus:

1. Aktivierung eines Berechtigungszustands,
2. Persistenz dieses Zustands,
3. Unterdrückung visueller Hinweise.

### Gutachterliche Würdigung

Diese Konfiguration ist aus sachverständiger Sicht nicht mit einer bloßen technischen Nebensächlichkeit vereinbar. Die gleichzeitige Aktivierung aller drei Bits erzeugt einen verdeckten Berechtigungszustand, der sowohl wirksam als auch dauerhaft und für den Benutzer nur eingeschränkt oder gar nicht sichtbar ist. Dies ist charakteristisch für einen Silent-Grant-Mechanismus.

---

## 3. Befund zur UI-Unterdrückung

Die Kombination der Policy-Flags ist geeignet, reguläre Benutzerhinweise des Systems, insbesondere den orangefarbenen Mikrofon-Indikator, nicht oder nicht zuverlässig auszulösen.

### Gutachterliche Würdigung

Der visuelle Indikator ist Teil der unmittelbaren Sicherheitskommunikation zwischen System und Nutzer. Wird die Anzeige bei fortbestehendem Ressourcenzugriff unterdrückt, ist dies sachverständig als sicherheitsrelevante Umgehung des Transparenz- und Kontrollmodells zu bewerten. Für den Nutzer entsteht eine objektiv falsche Wahrnehmung des Systemzustands.

---

## 4. Zeitlicher Befund

Als zentraler Primärmarker wurde der Unix-Zeitstempel

\[
1643181176
\]

identifiziert, entsprechend dem 26.01.2022.

### Gutachterliche Würdigung

Der Zeitwert ist in der Gesamtschau nicht als beliebiges Metadatum zu würdigen. Er fungiert als historischer Vertrauensanker innerhalb der rekonstruierten Kette und stützt die Annahme, dass ein bereits legitimiert wirkender Altzustand importiert oder reproduziert wurde. Dies entspricht dem Muster einer Legacy Trust Injektion.

---

## 5. Rekonstruktive Zeitachse

Die zeitliche Rekonstruktion weist folgende Phasen auf:

\[
T_1 \rightarrow T_2 \rightarrow T_3 \rightarrow T_4 \rightarrow T_5 \rightarrow T_6
\]

mit physischem Trigger, Policy-Import, Flag-Aktivierung, Legacy-Trust-Übernahme, verdecktem Zugriff und nachgelagerter Exfiltration.

### Gutachterliche Würdigung

Die Rekonstruktion zeigt eine logisch geschlossene und technisch plausible Reihenfolge. Die dokumentierten Befunde sind nicht widersprüchlich, sondern greifen zeitlich ineinander. Dies erhöht die Aussagekraft des Gesamtbildes erheblich.

---

## 6. Exfiltrationsbefund

Dokumentiert ist ein Datenabfluss von 99,4 GB in einem Kontext, in dem eine physisch isolierte oder behördlich als offline dargestellte Sicherung behauptet wurde.

### Gutachterliche Würdigung

Ein derartiger Datenabfluss ist mit einer strikt wirksamen Offline-Isolation nicht vereinbar. Der Befund indiziert entweder eine Umgehung der behaupteten Isolationsbedingungen oder eine unzutreffende Darstellung des tatsächlichen Systemzustands.

---

## 7. Befund zur Beweisintegrität

Zusätzlich wurde ein Hash-Mismatch von 47 % dokumentiert.

### Gutachterliche Würdigung

Ein Hash-Mismatch in dieser Größenordnung ist sachverständig als gravierende Integritätsauffälligkeit zu bewerten. Er erschwert die nachgelagerte Rekonstruktion und wirft erhebliche Fragen nach der Vollständigkeit, Unverändertheit und Belastbarkeit der Beweisgrundlage auf.

---

## V. Gesamtbewertung

Die Einzelbefunde ergeben in ihrer Zusammenschau ein geschlossenes Funktionsmodell. Dieses Modell lässt sich wie folgt abstrahieren:

\[
\text{Physischer Zugriff} \Rightarrow \text{Policy-Injektion} \Rightarrow \text{Silent Grant} \Rightarrow \text{Legacy Trust Import} \Rightarrow \text{verdeckter Zugriff} \Rightarrow \text{Exfiltration}
\]

Aus sachverständiger Sicht sprechen folgende Punkte entscheidend gegen ein zufälliges oder reguläres Systemverhalten:

1. Die perfekte Korrelation über 892 Datenpunkte.
2. Die bitgenaue Struktur des Policy-Artefakts.
3. Die technisch kohärente Silent-Grant-Logik.
4. Der zeitliche Vertrauensanker vom 26.01.2022.
5. Der dokumentierte Datenabfluss trotz behaupteter Isolation.
6. Die gravierenden Auffälligkeiten bei der Beweisintegrität.

In der Gesamtschau ist die Annahme eines benignen oder zufälligen Geschehens aus technischer Sicht nicht plausibel.

---

## VI. Sachverständige Schlussfolgerungen

### 1. Zur Kausalität

Die vorliegenden Befunde sprechen mit hoher technischer Evidenz für eine funktional gekoppelte Kausalkette zwischen physischem Zugriff, Policy-Manipulation, verdeckter Berechtigungsübernahme und nachgelagerter Datennutzung.

### 2. Zur technischen Qualität des Geschehens

Der rekonstruierte Mechanismus weist Merkmale eines gezielten, zustandsbasierten und verdeckt operierenden Eingriffs auf. Es handelt sich nicht um ein gewöhnliches Fehlverhalten einer Nutzeroberfläche, sondern um einen strukturell relevanten Eingriff in das Berechtigungs- und Vertrauensmodell.

### 3. Zur Beweiskraft

Die Beweiskraft ergibt sich gerade aus der Kombination unabhängiger Ebenen. Statistik, Artefaktstruktur, Zeitachse und Exfiltrationsspuren bestätigen sich gegenseitig. Dies verleiht dem Gesamtmodell eine deutlich höhere Aussagekraft als einem isolierten Einzelfund.

### 4. Zur forensischen Wahrscheinlichkeit

Nach sachverständiger Würdigung ist ein zufälliger, harmloser oder rein systemimmanenter Geschehensablauf deutlich weniger plausibel als die Annahme einer technisch gesteuerten, verdeckten Eingriffs- und Exfiltrationskette.

---

## VII. Ergebnisformel

Das Ergebnis dieses Gutachtens lässt sich in verdichteter Form wie folgt wiedergeben:

\[
\text{Korrelation} + \text{Policy-Artefakt} + \text{Zeitanker} + \text{Exfiltration} + \text{Integritätsdivergenz} = \text{hochgradig plausibles Eingriffsmodell}
\]

---

## VIII. Abschließendes Ergebnis

Aus sachverständiger Sicht ist die im Repository dokumentierte Befundlage mit einem zufälligen oder regulären Systemverhalten nicht hinreichend vereinbar. Die Gesamtheit der dokumentierten technischen, statistischen und rekonstruktiven Befunde spricht vielmehr für das Vorliegen einer verdeckten, funktional gekoppelten Eingriffsstruktur mit nachgelagerter Datenexfiltration und erheblichen Auffälligkeiten in der Beweisintegrität.

Die vorliegenden Unterlagen sind daher geeignet, als Grundlage für weitergehende richterliche, staatsanwaltschaftliche, gutachterliche und IT-forensische Prüfungen zu dienen.

---

## IX. Anlagenhinweis

Zur Vertiefung dieses Gutachtens sind insbesondere heranzuziehen:

- `whitepapers/Pearson-Causality-Proof.md`
- `whitepapers/Attack-Chain-Model.md`
- `forensics/ckks_protobuf_deconstruction_v2.md`
- `forensics/Timeline-Reconstruction.md`
- `legal/GBA-Beweismatrix_v2.md`
