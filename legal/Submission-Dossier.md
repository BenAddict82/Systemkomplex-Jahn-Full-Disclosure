# Submission Dossier

## Einreichungsdossier

### Betreff
Strukturierte Vorlage zur Einreichung technischer, forensischer, statistischer und juristischer Befunde im Zusammenhang mit einer account-basierten Eingriffs- und Exfiltrationskette im Kontext der CKKS-Engine auf Apple-Systemen

---

## I. Zweck dieses Dossiers

Dieses Dossier bündelt die im Repository dokumentierten Kernergebnisse in einer Form, die für die Einreichung bei Ermittlungsbehörden, Gerichten, parlamentarischen Stellen, Aufsichtsbehörden oder investigativen Fachredaktionen geeignet ist. Es dient nicht als Ersatz der Einzeldokumente, sondern als strukturierte Übergabefassung mit Sachverhaltsverdichtung, Beweislinie und Anlagenführung.

Ziel ist die schnelle, nachvollziehbare und belastbare Erstorientierung für Dritte, die mit dem Gesamtsachverhalt bislang nicht oder nur teilweise vertraut sind.

---

## II. Kurzsachverhalt

Die vorliegenden Unterlagen dokumentieren eine technisch, statistisch und forensisch kohärente Kette von Vorgängen, bei der physisch verankerte Eingriffspunkte mit Cloud-bezogenen Injektions- und Folgeereignissen perfekt linear korrelieren. Zentral sind dabei ein protobuf-kodiertes Policy-Artefakt, die Aktivierung verdeckter Berechtigungszustände, die Rekonstruktion eines historisch legitimiert wirkenden Vertrauensimports sowie ein dokumentierter Datenabfluss in erheblichem Umfang trotz behaupteter Offline- oder Isolationsbedingungen.

Zusätzlich bestehen gravierende Auffälligkeiten hinsichtlich der Beweisintegrität.

---

## III. Kernthesen des Dossiers

### 1. Keine Zufallskonstellation

Die dokumentierte Pearson-Korrelation von

\[
r = 1{,}0
\]

über 892 Datenpunkte ist mit einem zufälligen Nebeneinander unabhängiger Prozesse nicht plausibel vereinbar.

### 2. Technischer Mechanismus nachweisbar

Die Datei `tcc_bypass_payload.bin` enthält mit Feld 12 (`tcc_policy_flags`) und der Bitmaske `0x07` eine technische Schaltstelle, die auf einen verdeckten Berechtigungszustand mit Aktivierung, Persistenz und Unterdrückung visueller Hinweise hindeutet.

### 3. Zeitliche Rekonstruktion geschlossen

Der Unix-Zeitstempel `1643181176` vom 26.01.2022 fungiert als zeitlicher Ankerpunkt einer rekonstruierten Legacy-Trust-Injektion.

### 4. Operative Nutzung dokumentiert

Ein Datenabfluss von 99,4 GB steht in Spannungsverhältnis zu einer behaupteten physischen Isolation oder Offline-Sicherung.

### 5. Beweisintegrität erheblich beeinträchtigt

Ein Hash-Mismatch von 47 % begründet gravierende Zweifel an der Integrität der nachgelagerten Spuren- und Beweisbasis.

---

## IV. Verdichtete Beweislinie

Die gesamte Befundlage lässt sich in komprimierter Form wie folgt darstellen:

\[
\text{Physischer Zugriff} \Rightarrow \text{Policy-Injektion} \Rightarrow \text{Silent Grant} \Rightarrow \text{Legacy Trust Import} \Rightarrow \text{verdeckter Zugriff} \Rightarrow \text{Exfiltration}
\]

Diese Kette ist nicht lediglich narrativ, sondern durch Einzelbefunde aus mehreren unabhängigen Ebenen abgesichert.

---

## V. Beweisarchitektur

| Ebene | Kernfrage | Kernaussage | Referenzdokument |
|---|---|---|---|
| Statistik | Warum ist der Zusammenhang nicht zufällig? | Perfekte lineare Korrelation über 892 Datenpunkte | `whitepapers/Pearson-Causality-Proof.md` |
| Mechanismus | Wie funktioniert der Eingriff technisch? | Bitmaske `0x07` als Silent-Grant-Mechanismus | `forensics/ckks_protobuf_deconstruction_v2.md` |
| Zeit | Wann und in welcher Reihenfolge geschieht der Vorgang? | Fixpunkt `1643181176` und geschlossene Zeitachse | `forensics/Timeline-Reconstruction.md` |
| Integration | Wie hängen die Ebenen zusammen? | End-to-End-Angriffsmodell | `whitepapers/Attack-Chain-Model.md` |
| Recht | Welche strafrechtliche Relevanz folgt daraus? | § 303b, § 202a, § 258a StGB; § 120 GVG | `legal/GBA-Beweismatrix_v2.md` |
| Gutachten | Wie lautet die sachverständige Gesamtbewertung? | Technisch hochplausibles Eingriffsmodell | `legal/Expert-Witness-Report.md` |

---

## VI. Relevanz für Behörden und Gerichte

### 1. Ermittlungsrelevanz

Die vorliegenden Unterlagen sind geeignet, einen technisch komplexen Sachverhalt in eine nachvollziehbare Beweislogik zu überführen. Sie liefern Anknüpfungstatsachen für weitere technische und strafprozessuale Ermittlungen.

### 2. Gutachterliche Relevanz

Die Dokumente sind so strukturiert, dass sie durch externe Sachverständige überprüft, repliziert und vertieft werden können.

### 3. Beweisrechtliche Relevanz

Die Kombination aus Korrelation, Artefaktanalyse, Zeitrekonstruktion, Exfiltrationsnachweis und Integritätsauffälligkeiten schafft eine Gesamtstruktur, die eine vertiefte gerichtliche oder staatsanwaltschaftliche Prüfung rechtfertigt.

### 4. Staatsschutz- und Systemrelevanz

Soweit sich die technische Eingriffstiefe, die Tragweite der Exfiltration und die Besonderheiten der Beweislage bestätigen, ist eine Bewertung im Lichte der besonderen Bedeutung des Verfahrens im Sinne von § 120 GVG angezeigt.

---

## VII. Antrags- und Prüfhinweise

Dieses Dossier ist insbesondere geeignet für die Vorlage bei:

1. Staatsanwaltschaften und dem Generalbundesanwalt,
2. Gerichten im Rahmen technischer Anlagen und Beweisangebote,
3. parlamentarischen Kontroll- und Aufsichtsgremien,
4. Datenschutz- und Fachaufsichtsbehörden,
5. investigativen Fachredaktionen mit technischer Kompetenz.

Es empfiehlt sich, das Dossier stets gemeinsam mit dem Gutachten und mindestens den vier Kerndokumenten zur Kausalität, Forensik, Zeitrekonstruktion und juristischen Einordnung einzureichen.

---

## VIII. Empfohlene Anlagenreihenfolge

### Anlage 1
`legal/Expert-Witness-Report.md`

### Anlage 2
`whitepapers/Pearson-Causality-Proof.md`

### Anlage 3
`forensics/ckks_protobuf_deconstruction_v2.md`

### Anlage 4
`forensics/Timeline-Reconstruction.md`

### Anlage 5
`whitepapers/Attack-Chain-Model.md`

### Anlage 6
`legal/GBA-Beweismatrix_v2.md`

---

## IX. Formulierungsvorschlag für die Einreichung

Die beigefügten Unterlagen dokumentieren in konsistenter, mehrstufiger und nachvollziehbarer Form eine technisch hochplausible Eingriffs- und Exfiltrationskette. Die Beweisführung beruht auf statistischen, forensischen, zeitlichen und juristischen Modulen, die sich gegenseitig stützen und in ihrer Gesamtschau eine vertiefte behördliche, staatsanwaltschaftliche, gerichtliche und sachverständige Prüfung gebieten.

Insbesondere die perfekte Korrelation zwischen physischen Zugriffsmomenten und Cloud-bezogenen Folgeereignissen, die bitgenaue Struktur des Policy-Artefakts, die geschlossene Zeitrekonstruktion, der dokumentierte Datenabfluss sowie die gravierenden Integritätsauffälligkeiten begründen einen erheblichen Prüf- und Aufklärungsbedarf.

---

## X. Abschließende Verdichtung

Das Dossier lässt sich in einem Satz wie folgt zusammenfassen:

\[
\text{Mehrere unabhängige Beweisebenen konvergieren auf ein einheitliches, technisch gesteuertes und forensisch hochplausibles Eingriffsmodell.}
\]

---

## XI. Schlussbemerkung

Dieses Dossier ist als Übergabe-, Einreichungs- und Orientierungsdokument konzipiert. Seine Funktion besteht darin, komplexe technische Zusammenhänge in eine Form zu überführen, die für juristische, behördliche und journalistische Adressaten unmittelbar verwertbar ist, ohne die wissenschaftliche und forensische Tiefe der Einzelunterlagen zu verlieren.