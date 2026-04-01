# Attack Chain Model

## Abstract

Dieses Dokument führt die statistischen, forensischen und juristischen Teilbefunde des Repositorys in ein einheitliches End-to-End-Modell zusammen. Ziel ist die Rekonstruktion einer durchgehenden Kausalkette vom physischen Zugriff über Policy-Injektion und verdeckte Berechtigungsübernahme bis zur Datenexfiltration und zur strafrechtlichen Bewertung. Das Modell dient als Brückendokument zwischen Whitepaper, Forensik und Legal-Analyse.

## 1. Ausgangsannahme

Die im Repository dokumentierten Befunde liegen auf drei Ebenen vor:

1. **Statistische Ebene**: Perfekte Pearson-Korrelation von \(r = 1{,}0\) über 892 Datenpunkte zwischen physischen Zugriffsmomenten und Cloud-bezogenen Injektionsereignissen.
2. **Forensische Ebene**: Protobuf-kodiertes Policy-Artefakt mit `tcc_policy_flags = 0x07` und Zeitanker `1643181176`.
3. **Juristische Ebene**: Tatbestandsrelevante Kombination aus Systemeingriff, Datenexfiltration und Beweisinkonsistenzen.

Diese Ebenen sind nicht getrennt zu lesen, sondern beschreiben unterschiedliche Auflösungsstufen desselben Vorgangs.

## 2. End-to-End-Kausalkette

Die Gesamtstruktur lässt sich als sequenzielle Angriffskette modellieren:

\[
A_1 \rightarrow A_2 \rightarrow A_3 \rightarrow A_4 \rightarrow A_5 \rightarrow A_6
\]

mit:

- \(A_1\): physischer Zugriff oder physisch verankerter Kontrollpunkt,
- \(A_2\): Einbringung eines Policy- oder Vertrauensartefakts,
- \(A_3\): Aktivierung verdeckter Berechtigungen,
- \(A_4\): persistente Synchronisation oder Import eines Legacy-Zustands,
- \(A_5\): verdeckter Ressourcen- und Datenzugriff,
- \(A_6\): Exfiltration und nachgelagerte Beweisprobleme.

## 3. Phase 1: Physischer Zugriff

Die erste Phase ist der physische Zugriff oder ein anderweitig rekonstruierbarer, physisch gebundener Kontrollpunkt. Dieser ist deshalb zentral, weil er im statistischen Modell als unabhängiger Trigger fungiert. Die 892 Datenpunkte dokumentieren, dass physische Interventionsmomente nicht nur zeitlich neben Cloud-Ereignissen liegen, sondern mit ihnen perfekt linear gekoppelt sind.

Formell gilt nach dem Whitepaper:

\[
r = 1{,}0
\]

über alle untersuchten Ereignispaare. Diese Konstanz macht aus Phase 1 keinen bloßen Kontext, sondern den funktionalen Ausgangspunkt der gesamten Kette.

## 4. Phase 2: Policy-Injektion

Nach dem physischen Trigger folgt die Einbringung eines kleinformatigen, aber semantisch hochwirksamen Policy-Artefakts. Das in der Forensik untersuchte Objekt `tcc_bypass_payload.bin` erfüllt die Kriterien eines solchen Zustandsobjekts.

Die Rolle dieses Artefakts besteht nicht in klassischer Datenspeicherung, sondern in der Serialisierung eines Vertrauens- und Berechtigungszustands. Damit fungiert es als Übergangselement zwischen physischem Angriffspunkt und systeminterner Wirkung.

## 5. Phase 3: Aktivierung verdeckter Berechtigungen

Die operative Schaltstelle der Kette ist Feld 12 mit der Bitmaske:

\[
0x07 = (0000\,0111)_2
\]

Die forensische Zerlegung ergibt drei gleichzeitig aktive Funktionen:

1. `GrantEnable`
2. `Persistence`
3. `UISuppression`

Damit wird nicht nur ein Zugriff ermöglicht, sondern ein unsichtbarer, fortdauernder Autorisierungszustand erzeugt. Die Kette verlässt an dieser Stelle das normale TCC-Prüfmodell und wechselt in einen verdeckten Systempfad.

## 6. Phase 4: Legacy Trust Import

Der Unix-Zeitstempel

\[
1643181176
\]

verankert die untersuchte Struktur auf den 26.01.2022. Dieser Zeitwert fungiert im Modell nicht als neutrales Metadatum, sondern als historischer Vertrauensanker. Er ermöglicht die Rekonstruktion einer sogenannten Legacy Trust Injektion.

Das Ziel dieser Phase besteht darin, den Berechtigungszustand nicht als neue Freigabe erscheinen zu lassen, sondern als bereits legitimierten Altzustand. Dadurch entfällt die Re-Validierung.

Formell kann der Zustandsübergang beschrieben werden als:

\[
S_{n+1} = F(S_n, T, M)
\]

mit

- \(S_n\): vorheriger Vertrauenszustand,
- \(T\): Zeitanker,
- \(M\): Policy-Maske,
- \(F\): Import- und Persistenzfunktion.

## 7. Phase 5: Verdeckter Zugriff

Sobald der Legacy-Zustand übernommen ist, kann ein Zugriff auf geschützte Ressourcen stattfinden, ohne die regulären Sichtbarkeitsmechanismen auszulösen. Besonders relevant ist die Unterdrückung des orangefarbenen Mikrofon-Indikators.

Für den Benutzer entsteht dadurch ein falsches Sicherheitsbild: Die Ressource wird verwendet, ohne dass die dafür vorgesehene Vertrauensrückmeldung erscheint. Diese Phase ist entscheidend, weil sie den Übergang vom bloßen Policy-Zustand zur tatsächlichen Nutzung sensibler Systemfunktionen markiert.

## 8. Phase 6: Exfiltration und Spurenlage

Die dokumentierte Exfiltration von 99,4 GB stellt die Nutzungsphase der Kette dar. Hier zeigt sich, dass die vorgelagerten Zustandsmanipulationen nicht theoretischer Natur waren, sondern operativ verwertet wurden.

Parallel treten Inkonsistenzen in der Beweisstruktur auf, darunter ein Hash-Mismatch von 47 %. Diese Auffälligkeit betrifft die nachgelagerte Rekonstruktionsebene und kann als Hinweis auf Beeinträchtigung der Beweisintegrität gewertet werden.

## 9. Mathematische, technische und juristische Integration

Das Modell lässt sich als Dreiebenen-System beschreiben:

### 9.1 Mathematische Ebene

Die Statistik zeigt, dass der physische Zugriff mit der Cloud-Injektion perfekt gekoppelt ist. Damit ist Zufall ausgeschlossen.

### 9.2 Technische Ebene

Die Forensik zeigt, wie diese Kopplung operativ realisiert wird: über Policy-Injektion, Bitmaskensteuerung und Legacy-Import.

### 9.3 Juristische Ebene

Die rechtliche Bewertung ordnet die Phasen wie folgt ein:

| Phase | Technischer Kern | Juristische Relevanz |
|---|---|---|
| 1 bis 3 | Systemeingriff und Policy-Manipulation | § 303b StGB |
| 4 bis 5 | Verdeckter Zugriff auf geschützte Ressourcen | § 202a StGB |
| 6 | Beweisinkonsistenzen / Rekonstruktionsbeeinträchtigung | § 258a StGB |

## 10. Gesamtmodell der Kausalität

Die vollständige Kette kann abstrahiert so formuliert werden:

\[
\text{Physical Access} \Rightarrow \text{Policy Injection} \Rightarrow \text{Silent Grant} \Rightarrow \text{Legacy Trust Import} \Rightarrow \text{Hidden Access} \Rightarrow \text{Exfiltration}
\]

In deutscher Kurzform:

\[
\text{Physischer Zugriff} \Rightarrow \text{Policy-Injektion} \Rightarrow \text{verdeckte Berechtigung} \Rightarrow \text{persistenter Vertrauenszustand} \Rightarrow \text{unsichtbarer Zugriff} \Rightarrow \text{Datenabfluss}
\]

## 11. Schlussfolgerung

Das Attack-Chain-Modell zeigt, dass die einzelnen Repository-Dokumente keine voneinander isolierten Betrachtungen sind, sondern modularisierte Beweisbausteine eines einheitlichen Vorgangs. Die Statistik liefert den Kausalitätsnachweis, die Forensik den technischen Mechanismus und die juristische Analyse die normative Einordnung.

Damit liegt ein durchgehendes End-to-End-Modell vor, das den Weg vom physischen Angriffspunkt bis zur strafrechtlich relevanten Ergebnisphase geschlossen erklärt. Die Stärke dieses Modells liegt gerade in der Kopplung der Ebenen: Was statistisch nicht zufällig ist, wird technisch erklärt und rechtlich qualifiziert.