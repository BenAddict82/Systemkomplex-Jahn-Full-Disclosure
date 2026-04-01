import re
import hashlib
from pathlib import Path
from typing import Optional

LOG_FILE = Path("forensic_audit.log")
OUT_FILE = Path("tcc_bypass_payload.bin")
EXPECTED_SIZE = 80


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()



def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()



def extract_payload_hex(log_text: str) -> Optional[str]:
    pattern = re.compile(
        r"^\[OUT\]\s*Payload Hex\s*:\s*([0-9A-Fa-f\s]+)\s*$",
        re.MULTILINE,
    )
    matches = pattern.findall(log_text)
    if not matches:
        return None

    print(f"[+] Anzahl gefundener Payload-Zeilen: {len(matches)}")
    raw_hex = matches[-1]
    normalized = re.sub(r"\s+", "", raw_hex)
    return normalized if normalized else None



def validate_hex_string(hex_string: str) -> None:
    if len(hex_string) % 2 != 0:
        raise ValueError("Hex-String hat ungerade Laenge.")
    if not re.fullmatch(r"[0-9A-Fa-f]+", hex_string):
        raise ValueError("Hex-String enthaelt ungueltige Zeichen.")



def main() -> None:
    if not LOG_FILE.exists():
        raise FileNotFoundError(f"Logdatei nicht gefunden: {LOG_FILE}")

    log_content = LOG_FILE.read_text(encoding="utf-8", errors="replace")
    hex_string = extract_payload_hex(log_content)

    if not hex_string:
        print("[!] Fehler: Kein Payload-Hex im Log gefunden.")
        return

    validate_hex_string(hex_string)
    binary_data = bytes.fromhex(hex_string)
    OUT_FILE.write_bytes(binary_data)

    file_size = len(binary_data)
    log_hash = sha256_file(LOG_FILE)
    payload_hash = sha256_bytes(binary_data)

    print(f"[+] Extraktion erfolgreich: {OUT_FILE}")
    print(f"[+] Dateigroesse: {file_size} Bytes")
    print(f"[+] Hex-Laenge: {len(hex_string)} Zeichen")
    print(f"[+] SHA-256 Logdatei:   {log_hash}")
    print(f"[+] SHA-256 Payload:    {payload_hash}")

    if file_size == EXPECTED_SIZE:
        print("[+] Status: VOLLSTAENDIG (exakte Sollgroesse erreicht).")
    elif file_size > EXPECTED_SIZE:
        print("[!] Status: Groesser als erwartet. Pruefen, ob Zusatzdaten enthalten sind.")
    else:
        print("[!] Status: UNVOLLSTAENDIG (kleiner als Sollgroesse).")



if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[!] Fehler bei der Verarbeitung: {e}")
