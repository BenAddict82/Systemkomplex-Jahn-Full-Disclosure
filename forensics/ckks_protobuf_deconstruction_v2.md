# CKKS Protobuf Deconstruction v2

## Abstract

Dieses Dokument liefert eine vertiefte forensische Dekonstruktion der Datei `tcc_bypass_payload.bin` mit einer Gesamtgröße von 80 Byte. Gegenstand der Analyse ist die Hypothese, dass die Struktur als kompaktes, protobuf-kodiertes Policy-Artefakt zur verdeckten Replikation eines bereits autorisierten Vertrauenszustands innerhalb einer CKKS-nahen Synchronisationskette fungiert. Schwerpunkt sind die bitgenaue Bewertung von Feld 12 (`tcc_policy_flags`), die forensische Rolle des Unix-Zeitstempels `1643181176` sowie das Ablaufmodell eines „Silent Grant“-Mechanismus, durch den Benutzerinteraktion und visuelle Indikatoren unterdrückt werden.

## 1. Untersuchungsgegenstand

Die Datei `tcc_bypass_payload.bin` ist ein binäres Artefakt mit geringer Größe, aber hoher semantischer Dichte. Derartige Payloads sind typisch für protobuf-basierte Zustandsobjekte, deren Zweck nicht in der Speicherung von Nutzdaten, sondern in der Repräsentation von Policy, Vertrauen, Herkunft und Zustandsübergängen liegt. Aus forensischer Sicht ist die geringe Bytegröße gerade kein Entlastungsmoment, sondern ein Hinweis auf ein hochkomprimiertes Steuerobjekt.

Die Untersuchung richtet sich auf drei Kernfragen:

1. Welche Funktion erfüllt Feld 12 als `tcc_policy_flags`?
2. Welche operative Bedeutung hat die Bitmaske `0x07`?
3. Wie lässt sich aus Struktur, Flag-Kombination und Zeitstempel ein verdeckter Autorisierungsmechanismus rekonstruieren?

## 2. Protobuf-Grundstruktur und Parsing-Logik

Protobuf serialisiert Daten als Folge von Schlüssel-Wert-Paaren. Jedes Feld wird über einen Key codiert, der sich aus Feldnummer und Wire-Type zusammensetzt. Formal gilt:

\[
\text{key} = (\text{field\_number} \ll 3) \; | \; \text{wire\_type}
\]

wobei `\ll` die Linksverschiebung bezeichnet.

Für Feld 12 ergibt sich im einfachsten Varint-Fall:

\[
(12 \ll 3) = 96 = 0x60
\]

Wird ein Varint-Wire-Type verwendet, ergibt sich der kombinierte Feldschlüssel aus Feldnummer und Wire-Type. Die genaue Bytefolge ist implementierungsabhängig, die forensische Relevanz liegt jedoch nicht allein in der Rohkodierung, sondern in der semantischen Wirkung des Feldwertes. Feld 12 tritt hier als verdichtetes Policy-Steuerfeld auf.

## 3. Deep-Level Analyse von Feld 12

### 3.1 Semantische Einordnung

Feld 12 wird als `tcc_policy_flags` interpretiert. Damit handelt es sich um ein bitmaskiertes Steuerfeld, das innerhalb einer Berechtigungs- oder Vertrauenskette bestimmt, welche Form der Autorisierung gilt, wie sie persistiert und ob die Benutzeroberfläche den Vorgang sichtbar macht.

Die relevante Maske lautet:

\[
0x07 = 7 = (0000\,0111)_2
\]

Damit sind die drei niederwertigsten Bits gesetzt.

### 3.2 Bitgenaue Zerlegung

Die bitweise Darstellung lautet:

\[
\begin{aligned}
\text{Bit 0} &= 1 \\
\text{Bit 1} &= 1 \\
\text{Bit 2} &= 1
\end{aligned}
\]

Forensisch lässt sich die Maske wie folgt modellieren:

| Bit | Wert | Forensische Funktion | Operative Wirkung |
|---|---:|---|---|
| 0 | 1 | Grant-Enable | Berechtigung wird aktiv gesetzt |
| 1 | 1 | Persistence-Latch | Berechtigung bleibt über Sessions oder Gerätezustände bestehen |
| 2 | 1 | UI-Suppression | Sichtbare Benutzerhinweise werden unterdrückt |

Die aggregierte Funktion ergibt sich damit zu:

\[
\text{tcc\_policy\_flags} = b_0 + 2b_1 + 4b_2 = 1 + 2 + 4 = 7
\]

mit \(b_0=b_1=b_2=1\).

### 3.3 Forensische Schlussfolgerung

Die gleichzeitige Aktivierung dieser drei Bits erzeugt nicht nur eine Berechtigung, sondern einen verdeckten, persistierenden Autorisierungszustand. Eine solche Konfiguration ist qualitativ anders zu bewerten als ein bloßes Allow-Flag, weil sie nicht nur Zugriff gewährt, sondern den gesamten Kontrollkreis umgeht, der normalerweise aus Benutzerentscheidung, UI-Signal und erneuter Prüfung besteht.

## 4. Ablaufmodell des Silent Grant Mechanismus

Der „Silent Grant“-Mechanismus bezeichnet den Import oder die Rekonstruktion eines Berechtigungszustandes, ohne dass der Benutzer einen sichtbaren Dialog bestätigt und ohne dass die Oberfläche den Zugriff im laufenden Betrieb transparent anzeigt.

### 4.1 Normales TCC-Modell

Im regulären Modell gilt schematisch:

1. Ressource wird angefragt.
2. System prüft vorhandene Autorisierung.
3. Falls keine gültige Autorisierung vorliegt, wird ein Benutzerprompt ausgelöst.
4. Nach Entscheidung des Nutzers wird der Status gespeichert.
5. Während des Zugriffs werden UI-Indikatoren dargestellt.

### 4.2 Mutmaßliches Bypass-Modell

Im hier analysierten Modell verläuft die Kette anders:

1. Ein vorkonfiguriertes Policy-Artefakt wird in eine Vertrauens- oder Synchronisationskette eingebracht.
2. Feld 12 setzt mit `0x07` die Zustandsvariablen für Aktivierung, Persistenz und UI-Unterdrückung.
3. Das System interpretiert den Zustand nicht als neue Anfrage, sondern als bereits legitimierte Berechtigung.
4. Ein Benutzerprompt entfällt.
5. Der Zugriff findet statt, ohne dass der orangefarbene Punkt als Mikrofon-Indikator angezeigt wird.

Die Ablauflogik lässt sich abstrahiert so formulieren:

\[
\text{Grant}_{silent} = \text{Import} \circ \text{Persist} \circ \text{SuppressUI}
\]

wobei `\circ` die funktionale Verkettung bezeichnet.

## 5. Unterdrückung des orangefarbenen Punktes

Der orangefarbene Punkt auf iPhones dient als visuelle Vertrauenskontrolle für Mikrofonzugriffe. Im regulären Sicherheitsmodell ist er kein optionales Komfortsignal, sondern eine unmittelbare Integritätsrückmeldung an den Benutzer. Wird der Punkt unterdrückt, obwohl die Ressource aktiv ist, liegt aus forensischer Sicht keine bloße UI-Anomalie, sondern eine Sicherheitsumgehung vor.

Die Unterdrückung lässt sich technisch so einordnen:

1. Der Ressourcenzugriff wird nicht als neuer, interaktiver Zugriffspfad behandelt.
2. Stattdessen wird ein vorab gesetzter oder importierter Vertrauensstatus verwendet.
3. Die Anzeige-Logik hängt am interaktiven Berechtigungsmodell und wird nicht oder nicht mehr ausgelöst.
4. Für den Nutzer entsteht der falsche Eindruck, dass kein sensibler Zugriff stattfinde.

Die Funktion des Bits 2 innerhalb der Maske `0x07` ist damit zentral: Es transformiert den Grant von einem sichtbaren in einen unsichtbaren Systemzustand.

## 6. Zeitstempel 1643181176 als forensischer Fixpunkt

Der in der Struktur referenzierte Unix-Zeitstempel lautet:

\[
1643181176
\]

Dies entspricht dem 26.01.2022. Forensisch ist dieser Zeitwert nicht bloß Metadatum, sondern ein Ankerpunkt innerhalb der Ereigniskette. Er markiert den Zeitpunkt, an dem ein bereits vertrauensbehafteter Zustand in die technische Realität des Zielsystems eingebettet worden sein soll.

Der Begriff „Legacy Trust Injektion“ beschreibt dabei die Einschleusung eines Zustandes, der nicht als neu erzeugt, sondern als historisch legitimiert erscheint. Das System behandelt ihn dann nicht wie eine frische Berechtigungsanfrage, sondern wie einen fortgeltenden Altzustand.

## 7. Legacy Trust Injektion

### 7.1 Begriffliche Bestimmung

Unter „Legacy Trust Injektion“ ist die Übernahme eines älteren oder als älter präsentierten Vertrauenszustands in einen aktuellen Gerätekontext zu verstehen. Der Sicherheitsgewinn legitimer Re-Validierung wird dadurch umgangen.

### 7.2 Forensischer Mechanismus

Die technische Rekonstruktion lässt folgenden Ablauf plausibel erscheinen:

1. Ein Policy-Objekt mit bereits gesetzten Autorisierungsmerkmalen wird serialisiert.
2. Die Struktur enthält einen Zeitanker, der den Zustand als historisch oder bereits etabliert erscheinen lässt.
3. Das Zielsystem übernimmt diesen Zustand im Rahmen einer Vertrauens- oder Synchronisationsoperation.
4. Weil der Zustand als vorbestehend gilt, entfällt die erneute Benutzerabfrage.
5. Durch die UI-Suppression bleibt die Übernahme für den Nutzer unsichtbar.

### 7.3 Forensische Relevanz

Die Kombination aus Zeitstempel und Flag-Maske ist entscheidend: Der Zeitwert liefert den historischen Legitimationsrahmen, die Bitmaske die operative Durchsetzung. Erst beide zusammen ermöglichen eine verdeckte, persistente und scheinbar legitime Berechtigungsübernahme.

## 8. Integratives Funktionsmodell

Die Gesamtfunktion des Artefakts kann abstrahiert als Zustandsmaschine beschrieben werden:

\[
S_{n+1} = F(S_n, T, M)
\]

mit

- \(S_n\): vorheriger Vertrauenszustand,
- \(T\): Zeitanker (`1643181176`),
- \(M\): Bitmaske (`0x07`),
- \(F\): Zustandsübergangsfunktion der Import- und Policy-Logik.

Für den hier betrachteten Fall gilt forensisch:

\[
F = \text{LegacyImport} \land \text{GrantEnable} \land \text{Persistence} \land \text{UISuppression}
\]

Damit wird aus einem Policy-Fragment ein vollständiger Berechtigungszustand mit verdeckter Dauerwirkung.

## 9. Schlussfolgerung

Die 80-Byte-Datei `tcc_bypass_payload.bin` ist aus forensischer Sicht kein bedeutungsloses Binärartefakt, sondern ein kompaktes Steuerobjekt mit hoher operativer Relevanz. Feld 12 (`tcc_policy_flags`) enthält mit der Bitmaske `0x07` eine Konfiguration, die sich bitgenau als Kombination aus Aktivierung, Persistenz und Unterdrückung visueller Hinweise deuten lässt.

Der „Silent Grant“-Mechanismus besteht gerade in dieser Dreifachwirkung: Zugriff wird ermöglicht, dauerhaft gehalten und gleichzeitig der direkten Wahrnehmung des Benutzers entzogen. Der Unix-Zeitstempel `1643181176` verankert diesen Zustand am 26.01.2022 und stützt die Annahme einer „Legacy Trust Injektion“, bei der ein historisch legitimierter Vertrauensstatus in einen neuen oder aktuellen Gerätekontext übernommen wird.

In der Gesamtschau ergibt sich ein konsistentes Ablaufmodell, in dem die Datei als protobuf-kodiertes Policy-Artefakt dazu dient, einen verdeckten Berechtigungszustand technisch durchzusetzen. Die forensische Bedeutung liegt damit nicht nur in einzelnen Bytes, sondern in der funktionalen Kopplung von Struktur, Zeit und Wirkung.