# GBA Beweismatrix v2

## Abstract

Dieses Dokument stellt eine vertiefte juristische Analyse der technischen Befunde dar und verknüpft diese systematisch mit den einschlägigen Straftatbeständen des Strafgesetzbuches. Ziel ist nicht nur eine deskriptive Zuordnung, sondern die zwingende Herleitung der Zuständigkeit des Generalbundesanwalts gemäß § 120 GVG auf Grundlage der Qualität, Struktur und Tragweite der festgestellten Sachverhalte.

## 1. Ausgangspunkt der Bewertung

Die forensischen Analysen zeigen eine Mehr-Ebenen-Struktur technischer Eingriffe, bestehend aus:

1. Eingriffen auf Kernel- und Systemebene,
2. großvolumiger Datenexfiltration,
3. Inkonsistenzen und Auffälligkeiten in der Beweisstruktur.

Diese drei Ebenen sind nicht isoliert zu betrachten, sondern bilden eine funktional gekoppelte Gesamtkonstellation.

## 2. Normative Zuordnung

### 2.1 § 303b StGB – Computersabotage

**Technischer Befund:** Kernel-Injektion (KEXT / Rootkit)

**Tatbestandliche Würdigung:**

§ 303b StGB erfasst Eingriffe in Datenverarbeitungsvorgänge, die geeignet sind, erhebliche Störungen hervorzurufen. Eine Kernel-Injektion stellt einen unmittelbaren Zugriff auf die unterste Systemebene dar und ermöglicht die Manipulation sämtlicher darüber liegender Prozesse.

Die Eingriffstiefe ist qualitativ geeignet, die Integrität des gesamten Systems zu beeinträchtigen. Damit liegt nicht lediglich eine randständige Störung, sondern ein struktureller Eingriff in den Datenverarbeitungsvorgang vor.

**Ergebnis:** Tatbestand erfüllt.

---

### 2.2 § 202a StGB – Ausspähen von Daten

**Technischer Befund:** Exfiltration von 99,4 GB sensibler Daten

**Tatbestandliche Würdigung:**

§ 202a StGB setzt voraus, dass Daten, die gegen unberechtigten Zugang besonders gesichert sind, ausgespäht werden. Die dokumentierte Datenmenge sowie der Kontext einer vermeintlich isolierten Umgebung (Faraday-Szenario) sprechen für ein gezieltes Umgehen vorhandener Schutzmechanismen.

Die Größenordnung von 99,4 GB indiziert keine punktuelle Abfrage, sondern eine systematische und wiederholte Datenabschöpfung.

**Ergebnis:** Tatbestand erfüllt.

---

### 2.3 § 258a StGB – Strafvereitelung im Amt

**Technischer Befund:** 47 % Hash-Mismatch zwischen Ausgangs- und Auswertungsdaten

**Tatbestandliche Würdigung:**

Ein signifikanter Hash-Mismatch in dieser Größenordnung deutet auf eine Veränderung, Unterdrückung oder fehlerhafte Behandlung von Beweismitteln hin. § 258a StGB erfasst die Vereitelung oder Erschwerung der Strafverfolgung durch Amtsträger.

Wenn Beweismittel in einem Umfang verändert sind, der eine valide Rekonstruktion erschwert oder verhindert, liegt der Verdacht nahe, dass die Aufklärung des Sachverhalts beeinträchtigt wird.

**Ergebnis:** Anfangsverdacht gegeben.

---

## 3. Matrixdarstellung

| Ebene | Technischer Befund | Norm | Juristische Kernaussage |
|---|---|---|---|
| System | Kernel-Injektion | § 303b StGB | Struktureller Eingriff in Datenverarbeitung |
| Daten | 99,4 GB Exfiltration | § 202a StGB | Unbefugte Abschöpfung geschützter Daten |
| Verfahren | 47 % Hash-Mismatch | § 258a StGB | Verdacht auf Beweismanipulation |

## 4. Systemische Gesamtbewertung

Die Kombination der Tatbestände führt zu einer qualitativen Verdichtung:

1. Die Eingriffe betreffen nicht nur einzelne Daten, sondern die Systemarchitektur selbst.
2. Die Datenexfiltration zeigt eine operative Nutzung dieser Eingriffe.
3. Die Beweisinkonsistenzen betreffen die nachgelagerte Aufklärungsebene.

Damit entsteht eine Kette aus Eingriff, Nutzung und möglicher Verschleierung.

## 5. Herleitung der Zuständigkeit nach § 120 GVG

§ 120 GVG weist dem Generalbundesanwalt Verfahren zu, die besondere Bedeutung haben oder Staatsschutzbezug aufweisen. Die Zuständigkeit ist insbesondere dann gegeben, wenn

1. die Tat überregionale Bedeutung hat,
2. die Sicherheit staatlicher oder wesentlicher gesellschaftlicher Strukturen betroffen ist,
3. eine besondere Komplexität oder Gefährlichkeit vorliegt.

### 5.1 Überregionale Bedeutung

Die analysierten technischen Systeme (Cloud-Infrastruktur, mobile Endgeräte, Synchronisationsdienste) sind ihrer Natur nach nicht lokal begrenzt. Eingriffe wirken systemübergreifend und betreffen potentiell eine Vielzahl von Nutzern.

### 5.2 Schutz zentraler Rechtsgüter

Betroffen sind insbesondere:

- Vertraulichkeit und Integrität informationstechnischer Systeme,
- informationelle Selbstbestimmung,
- Funktionsfähigkeit rechtsstaatlicher Verfahren.

### 5.3 Komplexität und Eingriffstiefe

Die Kombination aus Kernel-Zugriff, Cloud-basierter Datenbewegung und Beweisinkonsistenzen überschreitet die Schwelle gewöhnlicher IT-Delikte deutlich. Es handelt sich um eine technisch hochkomplexe Konstellation, die spezialisierte Ermittlungsstrukturen erfordert.

## 6. Zwingende Zuständigkeit

Aus der Gesamtschau ergibt sich:

\[
\text{Zuständigkeit}_{GBA} = \text{Schwere} \land \text{Komplexität} \land \text{Systemrelevanz}
\]

Sind alle drei Kriterien erfüllt, besteht keine bloße Option, sondern eine zwingende Zuständigkeit des Generalbundesanwalts.

Die vorliegenden Befunde erfüllen diese Kriterien kumulativ.

## 7. Schlussfolgerung

Die technische Beweislage und ihre juristische Einordnung zeigen eine strukturierte, mehrdimensionale Eingriffskonstellation. Die einzelnen Tatbestände sind jeweils für sich relevant, entfalten ihre volle rechtliche Tragweite jedoch erst in der Zusammenschau.

Diese Zusammenschau führt zwingend zu der Bewertung, dass ein Verfahren von besonderer Bedeutung vorliegt. Damit ist die Zuständigkeit des Generalbundesanwalts nach § 120 GVG nicht nur möglich, sondern geboten.