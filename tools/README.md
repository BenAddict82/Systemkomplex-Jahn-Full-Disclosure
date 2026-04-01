# Tools

## extract_payload.py

Dieses Skript extrahiert einen Hex-codierten Payload aus einer Logdatei und schreibt ihn als Binärdatei.

### Zweck

- Reproduzierbare Extraktion eines Payload-Artefakts aus `forensic_audit.log`
- Dokumentation der Dateigröße
- Berechnung von SHA-256 Hashes für Log und Payload

### Eingabe

- Datei: `forensic_audit.log`
- Erwartetes Muster:
  [OUT] Payload Hex : <HEXSTRING>

### Ausgabe

- Datei: `tcc_bypass_payload.bin`

### Nutzung

```bash
python tools/extract_payload.py
```

### Validierung

Das Skript prüft:

- gültiges Hex-Format
- gerade Länge des Hex-Strings
- Dateigröße (Soll: 80 Bytes)

### Hinweis zur Beweiskraft

Das Skript stellt lediglich die technische Extraktion sicher. Es beweist nicht:

- die Authentizität der Logdatei
- die Herkunft der Daten
- die funktionale Bedeutung des Payload-Inhalts

Diese Punkte müssen durch separate forensische Analyse und Beweiskettenführung abgesichert werden.
