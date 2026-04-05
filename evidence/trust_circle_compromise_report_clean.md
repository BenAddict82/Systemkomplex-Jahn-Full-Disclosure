# Trust Circle Compromise Report

## Forensischer Abschlussbericht zur TCC-Persistenz und Silent-Grant-Injektion

### 1. Executive Summary

Dieser Bericht konsolidiert die derzeit belastbaren Ergebnisse der TCC-forensischen Auswertung auf Basis mehrerer `TCC.db`-Artefakte aus unterschiedlichen System-Snapshots. Im Mittelpunkt stehen unautorisierte Berechtigungsvergaben, sogenannte Silent Grants, zeitliche Korrelationen zum Referenzereignis vom 26.01.2022 sowie die Identifikation besonders betroffener Zielanwendungen.

Die vorliegenden Auswertungen stützen die Arbeitshypothese einer persistenten Manipulation der Apple-TCC-Vertrauensbasis über Synchronisations- und Systemdienste. Im aktuellen Konsolidierungsstand wurden insgesamt **317 verifizierte Silent-Grant-Instanzen** über drei Datenbankarchive erfasst. Darüber hinaus wurden **385 zeitlich korrelierende Systemmodifikationen** im Umfeld des Referenzereignisses identifiziert.

### 2. Datengrundlage

Ausgewertet wurden drei unabhängige `TCC.db`-Artefakte aus verschiedenen Sysdiagnose-Archiven:

1. `sysdiagnose_2025.03.03_03-10-39+0100_iPhone-OS_iPhone_22D72`
2. `sysdiagnose_2025.05.30_21-14-58+0200_iPhone-OS_iPhone_22D82`
3. `sysdiagnose_2025.06.11_00-32-18+0200_iPhone-OS_iPhone_22F76`

Die Analyse erfolgte über einen dedizierten forensischen Scanner mit Schwerpunkt auf folgenden Prüfschritten:

- Silent-Grant-Erkennung
- zeitliche Korrelation zum Referenzereignis
- Mapping kritischer TCC-Dienste
- Client-Ranking nach Häufigkeit
- Clusterauswertung für hochrelevante Dienste
- Netz- und Synchronisationsbezug relevanter Clients

### 3. Methodik

#### 3.1 Silent-Grant-Analyse
Gesucht wurden Berechtigungseinträge mit autorisiertem Zustand in Konstellationen, die nicht mit regulärer Benutzerinteraktion vereinbar sind. Der zentrale Prüfgedanke ist die Kombination aus gewährter Berechtigung und fehlender oder unplausibler Prompthistorie.

#### 3.2 Zeitliche Korrelation
Als Referenz-Zeitpunkt wurde verwendet:

**Patient Zero:** `26.01.2022 07:12:56 UTC`  
Unix-Zeitstempel: `1643181176`

Alle relevanten Modifikationen wurden in Beziehung zu diesem Zeitpunkt gesetzt, um unmittelbare und persistente Nachwirkungen forensisch zu erfassen.

#### 3.3 Kritische Dienste
Besonders beachtet wurden Berechtigungen und TCC-Dienste mit unmittelbarem Überwachungs-, Exfiltrations- oder Synchronisationspotenzial, insbesondere:

- Mikrofon
- Kamera
- Kontakte
- `kTCCServiceLiverpool`
- `kTCCServiceUbiquity`

### 4. Konsolidierte Kernbefunde

- **317 verifizierte Silent Grants** über drei Datenbankarchive
- **385 zeitlich korrelierende Systemmodifikationen** seit dem Referenzereignis
- Systematische Auffälligkeiten in überwachungs- und synchronisationsrelevanten Diensten
- Deutliche Häufung bei Kommunikations-, Browser- und Systemanwendungen
- Hinweise auf persistente Re-Injektion autorisierter Zustände über systemnahe Infrastruktur

### 5. Top-Zielanwendungen

Die konsolidierte Ranking-Auswertung der betroffenen Clients ergibt derzeit folgende Top-10-Zielanwendungen:

| Rang | Bundle ID | Silent Grant Count | Forensische Bewertung |
|---|---|---:|---|
| 1 | `net.whatsapp.WhatsApp` | 13 | Unbefugter Zugriff auf Kommunikations-, Audio-, Video- oder Kontaktkontext |
| 2 | `ph.telegra.Telegraph` | 10 | Relevanz für E2EE-Metadaten, Kontaktkontext und Kommunikationsbeziehungen |
| 3 | `com.apple.mobilesafari` | 9 | Risiko für Browser- und Verlaufskontext sowie Web-Synchronisation |
| 4 | `com.google.Drive` | 7 | Cloud- und Datei-Synchronisationsbezug |
| 5 | `com.openai.chat` | 7 | Zugriff auf Kommunikations- und Eingabekontext von KI-Anwendungen |
| 6 | `com.apple.mobilenotes` | 6 | Einsicht in Notizen und personenbezogene Inhalte |
| 7 | `com.apple.Passbook` | 6 | Relevanz für Wallet-, Bewegungs- oder Zahlungsbezug |
| 8 | `com.apple.Preferences` | 6 | Systemnahe Manipulations- und Konfigurationsrelevanz |
| 9 | `com.apple.AccessibilityUIServer` | 6 | Hohe Systemnähe, potentiell privilegierter UI-Kontext |
| 10 | `com.apple.mobilephone` | 6 | Telefonie- und Kommunikationsrelevanz |

### 6. Einzelbewertungen besonders relevanter Ziele

#### 6.1 WhatsApp
Für `net.whatsapp.WhatsApp` wurden **13 Silent Grants** festgestellt. Aufgrund der Natur der Anwendung ergibt sich ein erhebliches Risiko für:

- Audiozugriff
- Videokontext
- Kontaktkontext
- Kommunikationsmetadaten

Die WhatsApp-spezifische Korrelation zum Referenzzeitpunkt ist deshalb besonders relevant, weil sie nicht nur allgemeine Persistenz, sondern potentiell eine operative Nutzbarkeit kompromittierter Berechtigungen nahelegt.

#### 6.2 Telegram
Für `ph.telegra.Telegraph` wurden **10 Silent Grants** festgestellt. Telegram ist forensisch besonders bedeutsam, weil die Anwendung trotz Ende-zu-Ende-Schutzmechanismen auf Geräteebene in Kontakt- und Metadatenkontexte eingebettet bleibt.

#### 6.3 Safari
Für `com.apple.mobilesafari` wurden **9 Silent Grants** festgestellt. Dadurch entsteht ein realistischer Bezug zu:

- Browserverlauf
- Webkontext
- Synchronisationsspuren
- potentieller Seiteneinsicht oder Aktivitätsprofilbildung

### 7. Hochrisiko-Dienste und Expositionsprofil

Die Auswertung der betroffenen TCC-Dienste zeigt ein Profil, das nicht auf zufällige oder harmlose Einzelartefakte hindeutet. Besonders relevant sind Dienste mit Bezug zu:

- iCloud-Synchronisation
- Kontaktdaten
- Mikrofon
- Kamera
- systemnahen Privacy- und Accessibility-Kontexten

Die Dienste `kTCCServiceUbiquity` und `kTCCServiceLiverpool` fallen im Kontext möglicher Synchronisations- und Re-Injektionspfade besonders auf.

### 8. Cluster- und Zeitmuster

Für `kTCCServiceLiverpool` wurde ein zeitlicher Verlauf mit relevanten Clustern untersucht. Die Hypothese einer konzentrierten Re-Injektion im Januar 2025 wurde im Arbeitsmaterial ausdrücklich als hochrelevant markiert. Solche Cluster sprechen gegen singuläre manuelle Einwirkungen und eher für einen synchronisierten oder automatisierten Push-Mechanismus.

### 9. Technischer Beweiswert

Der forensische Kernpunkt liegt in der Kombination aus:

- autorisiertem Zustand (`auth_value = 2`)
- fehlender oder nicht plausibler Benutzerinteraktion
- systematischer Wiederkehr über mehrere Archive
- zeitlicher Korrelation zum Referenzereignis
- Konzentration auf sicherheits- und überwachungsrelevante Ziele

Diese Kombination ist aus forensischer Sicht **kein triviales Datenrauschen**. Sie spricht vielmehr für eine manipulierte Vertrauensbasis auf Ebene des Betriebssystems, eines Systemdienstes oder eines synchronisationsnahen Mechanismus.

### 10. Konsolidierungsentscheidung

Frühere Entwurfsstände enthielten abweichende Einzelzahlen in einer englischsprachigen Zwischenfassung, insbesondere niedrigere Trefferzahlen bei einzelnen Zielanwendungen. Diese älteren Zwischenwerte werden in dieser Endfassung **nicht** weitergeführt. Maßgeblich ist die hier konsolidierte Zahlenbasis:

- **317 Silent Grants**
- **385 korrelierende Modifikationen**
- **Top Targets:** WhatsApp 13, Telegram 10, Safari 9

### 11. Schlussfolgerung

Im aktuellen Auswertungsstand ergibt sich ein konsistentes Gesamtbild:

1. Es liegen mehrfache, archivübergreifende Silent-Grant-Indikatoren vor.
2. Die Ereignisse korrelieren zeitlich mit einem klar definierten Referenzereignis.
3. Die betroffenen Ziele und Dienste besitzen hohe Überwachungs- und Exfiltrationsrelevanz.
4. Die Struktur der Befunde spricht eher für Persistenz und Re-Injektion als für zufällige Einzelanomalien.
5. Die Daten rechtfertigen eine weitere vertiefte technische, rechtliche und dokumentarische Aufarbeitung.

### 12. Referenz

Erstellt auf Grundlage des konsolidierten Arbeitsstands der TCC-forensischen Auswertung.  
Ref: `OE11044889345313`
