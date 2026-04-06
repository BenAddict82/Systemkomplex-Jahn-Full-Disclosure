# Aufarbeitung: TCC Forensic Evidence OLG

## Kurzfassung

Dieses Dokument bereitet die forensische Kurzanalyse der `TCC.db` fuer GitHub auf. Schwerpunkt ist die Diskrepanz zwischen lokalem DFU-Restore-Status und tatsaechlicher Berechtigungslage.

## Kernaussage

Die Datei argumentiert, dass trotz Bereinigung einer Kontrollgruppe weiterhin hunderte Berechtigungen und Anomalien im System sichtbar sind. Daraus wird eine Persistenz der Silent Grants ueber die Cloud-ID abgeleitet.

## Zentrale Metriken

### Kontrollgruppe (Clean)
- 134 Eintraege mit `auth_value = 2`
- 130 Zeitstempel-Anomalien aus 2025
- Primaer betroffene Dienste: `Ubiquity`, `Liverpool`
- Forensischer Status: anomal mit hoher Persistenz trotz DFU

### Zielgruppe (Infected)
- 97 Eintraege mit `auth_value = 2`
- 92 Zeitstempel-Anomalien
- Primaer betroffene Dienste: `Ubiquity`, `Liverpool`
- Forensischer Status: infiziert bzw. erwartungsgemaess kompromittiert

## Forensische Bewertung

Das Dokument wertet insbesondere die 130 Anomalien in der Clean-ID-Gruppe als Beweis fuer den sogenannten Century Bug. Die Grundthese lautet, dass Berechtigungen unautorisiert erneut injiziert werden und damit den lokalen Sicherheitsstatus des Betriebssystems umgehen.

## Bedeutung der Dienste

Die Dienste `Ubiquity` und `Liverpool` werden als primaere Schwerpunktdienste benannt. Innerhalb des Repository-Kontexts stehen sie fuer iCloud-/CloudKit-nahe und synchronisationsrelevante TCC-Strukturen.

## Funktion im Repository

Diese Aufbereitung ist das GitHub-lesbare Gegenstueck zum kompakten OLG-Kurzbeleg. Sie eignet sich als Bruecke zwischen:
- der tabellarischen Evidence-Ebene
- dem ausfuehrlichen Trust-Circle-/CKKS-Bericht
- der TCC-Persistenz-Linie im `evidence/`-Ordner

## Relevante Anschlussdateien

- `evidence/processed/final_century_bug_evidence_summary_processed.md`
- `evidence/trust_circle_compromise_report_clean.md`
- `evidence/top_10_targeted_apps.csv`

## Status

GitHub-Aufbereitung des Originaldokuments abgeschlossen.
