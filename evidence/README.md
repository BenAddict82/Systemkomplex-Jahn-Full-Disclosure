# Systemkomplex-Jahn-Full-Disclosure

## Forensischer Nachweis des iOS 'Century Bug'

Dieses Repository dient der Dokumentation und Offenlegung einer persistenten Sicherheitslücke in iOS, die unautorisierte Berechtigungen (**Silent Grants**) über die Cloud-ID re-injiziert.

### Key Forensic Findings
1. **TCC persistence:** Nachweis von 134 aktiven Berechtigungen in einer Kontrollgruppe nach DFU-Restore, davon >130 mit Zeitstempeln aus 2025.
2. **CKKS Correlation:** Direkte zeitliche Kopplung zwischen `CKKSIncomingQueueOperation` und unautorisierten TCC-Schreibvorgängen (Identifizierter Carrier: Cloud Keychain).
3. **Automation Evidence:** Nachweis von Micro-Bursts (bis zu 12 Injektionen pro Sekunde), was manuelle Nutzerinteraktion ausschließt.

### Inhaltsverzeichnis
- `TCC_Forensic_Evidence_OLG.pdf`: Juristisch aufbereitetes Beweismittel.
- `Century_Bug_Forensic_Evidence_Table.csv`: Rohdaten der Anomalien.
- `forensic_report.json`: Technischer Analysebericht der Differentialdiagnose.

---
**Referenz:** Gegenoffensive Nürnberg / OLG Nürnberg
