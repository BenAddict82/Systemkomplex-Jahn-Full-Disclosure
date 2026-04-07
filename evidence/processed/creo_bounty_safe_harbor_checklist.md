# CREO Bounty Safe Harbor Checklist

## Zweck

Diese Datei definiert die Mindestvoraussetzungen fuer jede rechtlich saubere und dokumentierbare Sicherheitspruefung im CREO-Kontext.

Sie beantwortet nicht die Frage, wie ein System technisch angegriffen werden koennte. Sie beantwortet die Frage, welche Freigaben, Klarstellungen und Programmbedingungen vor jeder ernsthaften Bounty-Arbeit schriftlich vorliegen muessen.

---

## 1. Programmbestaetigung

Vor Beginn jeder Pruefung muss schriftlich bestaetigt sein:
1. dass tatsaechlich ein aktives Bug-Bounty- oder Responsible-Disclosure-Programm besteht
2. welcher offizielle Kontaktweg gilt
3. wer fuer Annahme, Triage und Verguetung verantwortlich ist

---

## 2. Scope-Klaerung

Schriftlich zu klaeren sind:
1. welche Produktversionen erfasst sind
2. ob nur Testumgebungen oder auch spaetere Live-Versionen umfasst sind
3. welche Plattformen umfasst sind
4. ob Build-Artefakte, Binaries oder Demo-Versionen bereitgestellt werden
5. ob Plugin-, DAO-, SEP-, DPN- oder Abuse-/Support-Funktionen im Scope liegen

---

## 3. Safe Harbor

Es braucht eine ausdrueckliche schriftliche Zusage, dass regelkonforme Forschung innerhalb des freigegebenen Scopes:
1. keine Strafanzeige ausloest
2. keine zivilrechtlichen Schritte nach sich zieht
3. nicht als unbefugter Zugriff gewertet wird
4. nicht wegen Vertrags- oder AGB-Verletzung verfolgt wird, sofern die freigegebenen Regeln eingehalten werden

---

## 4. Erlaubte Methodik

Schriftlich festzulegen ist:
1. welche Testarten erlaubt sind
2. ob Reverse Engineering erlaubt ist
3. ob Binary-Analyse erlaubt ist
4. ob Traffic-Analyse in freigegebenen Testumgebungen erlaubt ist
5. ob Demo-, Test- oder Audit-Builds bereitgestellt werden
6. welche Handlungen ausdruecklich ausgeschlossen sind

---

## 5. Beweisstandard

Vorher zu klaeren ist:
1. welches Format ein gueltiger Bericht haben muss
2. welche Reproduzierbarkeit gefordert ist
3. ob Screenshots, Hashes, Logs oder Videos zulaessig sind
4. ob ein minimales Proof-of-Concept ohne produktive Auswirkung verlangt wird
5. wie Severity und Impact eingeordnet werden

---

## 6. Reward-Rahmen

Zu klaeren ist:
1. ob eine feste Reward-Matrix existiert
2. ob es Obergrenzen pro Severity gibt
3. ob es Ausschlussgruende gibt
4. ob Dubletten, bekannte Probleme oder Out-of-Scope-Funde nicht bezahlt werden
5. ob eine konkret garantierte Hoechstpraemie schriftlich bestaetigt wird

---

## 7. Disclosure-Regeln

Es muss vorab dokumentiert sein:
1. ob oeffentliche Kommunikation vor Fix verboten ist
2. wann eine koordinierte Veroeffentlichung erlaubt ist
3. ob Embargo-Fristen gelten
4. wie auf Streit ueber Severity oder Reward reagiert wird

---

## 8. Dokumentationspflicht

Jede weitere Arbeit sollte erst beginnen, wenn folgende Unterlagen lokal und im Repository sauber abgelegt sind:
1. Programmanfrage
2. Scope-Antwort
3. Safe-Harbor-Bestaetigung
4. Reward-Regeln
5. Disclosure-Regeln
6. interne Claim-vs-Proof-Matrix

---

## Fazit

Ohne diese schriftlichen Punkte ist CREO aus Bounty-Sicht kein belastbar abgesichertes Forschungsziel, sondern ein Risiko. Der erste technische Schritt ist deshalb nicht Forschung, sondern Programmklaerung.
