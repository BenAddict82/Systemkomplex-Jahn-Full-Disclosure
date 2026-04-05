# Evidence Overview

Dieses Verzeichnis buendelt die aktuell hochgeladenen Beweismittel zur Century-Bug- und TCC-Persistenz-Analyse.

## Kernaussagen

1. **TCC Persistence:** In der Kontrollgruppe wurden 134 aktive Berechtigungen nach DFU-Restore festgestellt, davon mehr als 130 mit Zeitstempeln aus 2025.
2. **CKKS Correlation:** Es besteht eine direkte zeitliche Kopplung zwischen `CKKSIncomingQueueOperation` und unautorisierten TCC-Schreibvorgaengen.
3. **Automation Evidence:** Micro-Bursts von bis zu 12 Injektionen pro Sekunde sprechen gegen manuelle Nutzerinteraktion.

## Enthaltene Dateien

- [Final_Century_Bug_Evidence_Summary_preview.md](Final_Century_Bug_Evidence_Summary_preview.md)
  - GitHub-lesbare Sofortvorschau der wichtigsten Befunde.
- [Final_Century_Bug_Evidence_Summary.pdf](Final_Century_Bug_Evidence_Summary.pdf)
  - Originales PDF-Beweismittel.
- [Century_Bug_Forensic_Evidence_Table.csv](Century_Bug_Forensic_Evidence_Table.csv)
  - Strukturierte Evidenztabelle zu Persistenz, Automatisierung, Kausalitaet und Kryptographie.
- [forensic_report.json](forensic_report.json)
  - Technischer Analysebericht mit Anomaliesummary und Gesamtbewertung.
- [upload_status.txt](upload_status.txt)
  - Sitzungsnotiz zu erfolgreich geschriebenen Artefakten.

## Empfohlene Lesereihenfolge

1. `Final_Century_Bug_Evidence_Summary_preview.md`
2. `Final_Century_Bug_Evidence_Summary.pdf`
3. `Century_Bug_Forensic_Evidence_Table.csv`
4. `forensic_report.json`

## Hinweis zur Anzeige

Die GitHub-integrierte PDF-Vorschau kann unzuverlaessig rendern. Deshalb ist die Markdown-Vorschau zusaetzlich enthalten, damit die Kernaussagen direkt im Repository sichtbar bleiben.

## Referenz

Gegenoffensive Nuernberg / OLG Nuernberg
