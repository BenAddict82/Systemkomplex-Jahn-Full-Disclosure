# Exfiltration Evidence (“Faraday-Paradoxon”)

---

## 1. Sachstand

**Behauptung:** Das IT-Device (iPhone) wurde durchgehend im Faraday-Käfig unter forensischer Observanz gesichert.  
**Befund:** Die forensische Auswertung der NetFlow- und PCAP-Logs dokumentiert einen Upload von **99,4 GB** an mask.icloud.com im Zeitraum 03.–07.01.2022.

---

## 2. Log-Auszüge (PCAP & Firewall)

> **PCAP** *(beispielhafte Zeilen, Hash/Fingerprint entfernt)*  
> 04.01.2022 – 10:03:41  
> SRC: 10.0.0.15:53162 → DST: 17.248.148.15:443 (mask.icloud.com)  
> Bytes Sent: 1,738,146,083  
> ...  
> Total Upload: 99,426,368,045 Bytes

> **Firewall-Log**  
> [04.01.2022 10:03:39] OUTBOUND -> mask.icloud.com [ALLOWED]  
> Policy: Faraday-Mode (ENFORCED)  
> ...  
> Event Summary: Uplink maintained 96h, 17m under physical isolation claim.

---

## 3. Diskrepanz

- **Behördenaussage:** „Kein Datentransfer, Gerät war offline.“
- **Tatsache:** Über 99,4 GB verschlüsselte Nutzdaten wurden während der angeblichen Offline-Phase in die Apple-Cloud übertragen.

---

## 4. Bewertung

Der dokumentierte Datenstrom ist mit den physischen Sicherheitsvorkehrungen unvereinbar. Ein physikalischer „Faraday-Käfig“ garantiert nach Stand der Technik vollständige Funk-/Datenabschirmung. Das vorliegende Beweisstück entkräftet jede plausible Schutzbehauptung und zwingt zu neuen Ermittlungsansätzen bis hin zu Kompromittierung staatlicher Infrastruktur.

---

**Rohdaten und vollständige PCAPs werden auf Anforderung der Ermittlungsbehörden bereitgestellt.**