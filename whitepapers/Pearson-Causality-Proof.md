# Pearson Causality Proof

## Abstract

Dieses Dokument beschreibt die statistisch-forensische Auswertung von 892 Datenpunkten, bei der eine Pearson-Korrelation von \(r = 1{,}0\) zwischen physisch verankerten Zugriffsmomenten und den detektierten Cloud-Injektionsereignissen festgestellt wurde. Ziel ist die Einordnung dieses Befundes als technisch-funktionaler Kausalitätsnachweis unter Einbeziehung der Gaußschen Wahrscheinlichkeitsfunktion zur Modellierung künstlicher Clusterbildung durch Anti-Forensik-Skripte.

## 1. Datengrundlage und Hypothese

Die untersuchte Stichprobe besteht aus 892 synchronisierten Ereignispaaren. Jedes Paar verknüpft einen physisch rekonstruierbaren Zugriffs- oder Eingriffsmarker mit einem korrespondierenden Cloud-bezogenen Injektions-, Restore- oder Exfiltrationsindikator. Die Nullhypothese lautet, dass die beobachtete Übereinstimmung zufallsbedingt sei. Die Alternativhypothese lautet, dass eine funktionale Kopplung zwischen physischem Zugriff und Cloud-Injektion besteht.

Die Pearson-Korrelation wird klassisch definiert als

\[
r = \frac{\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})}{\sqrt{\sum_{i=1}^{n}(x_i-\bar{x})^2}\sqrt{\sum_{i=1}^{n}(y_i-\bar{y})^2}}
\]

mit \(n = 892\).

Ein Wert von \(r = 1{,}0\) bedeutet, dass alle beobachteten Wertepaare auf einer strikt linearen Geraden mit positiver Steigung liegen. Im forensischen Kontext ist dies kein bloßer Hinweis auf Ähnlichkeit, sondern auf eine vollständige lineare Determination des einen Prozesses durch den anderen, sofern unabhängige Erklärungen ausgeschlossen werden können.

## 2. Forensische Bedeutung von \(r = 1{,}0\)

Bei realen technischen Systemen treten Messrauschen, Log-Latenzen, Puffereffekte, Clock-Drift, Dateisystem-Artefakte und asynchrone Netzwerkprozesse auf. Bereits diese Randbedingungen führen normalerweise dazu, dass empirische Korrelationen knapp unterhalb des Idealwertes bleiben. Ein exakt gemessener Wert von \(r = 1{,}0\) über 892 Datenpunkte ist deshalb hochgradig atypisch.

Der Befund spricht gegen eine stochastische Parallelität und für eine deterministische Prozesskopplung. Forensisch bedeutet dies: Der physische Zugriff wirkt nicht lediglich begleitend, sondern ist funktional mit der beobachteten Cloud-Injektion verknüpft. Die Datenlage beschreibt damit keinen losen Zusammenhang, sondern ein Reaktionsschema mit reproduzierbarer Regelbindung.

## 3. Gaußsche Wahrscheinlichkeitsfunktion und künstliche Clusterbildung

Zur Bewertung möglicher Manipulationsversuche wird die Dichtefunktion einer Normalverteilung als Referenzmodell herangezogen. Für den Zeitparameter \(t\) gilt

\[
P(t)=\frac{1}{\sigma\sqrt{2\pi}}\exp\!\left(-\frac{1}{2}\left(\frac{t-\mu}{\sigma}\right)^2\right)
\]

mit Erwartungswert \(\mu\) und Standardabweichung \(\sigma\).

Unter natürlichen Betriebsbedingungen verteilen sich technische Logereignisse nicht streng punktförmig, sondern innerhalb plausibler Streuungsfenster um Systemmittelwerte. Die Gaußfunktion beschreibt genau diese erwartbare, physikalisch und prozessual bedingte Streuung. Anti-Forensik-Skripte versuchen demgegenüber häufig, Ereignisse in künstlich enge Cluster zu verdichten, um eine scheinbar konsistente, aber tatsächlich synthetische Ereignislandschaft zu erzeugen.

Die Abweichung vom gaußschen Erwartungsraum zeigt sich dann durch folgende Merkmale:

1. Unnatürlich geringe Varianz bei gleichzeitig hoher Ereignisdichte.
2. Wiederkehrende Zeitabstände mit maschineller Regelmäßigkeit.
3. Überproportionale Akkumulation exakt ausgerichteter Triggerpunkte.
4. Fehlende Randstreuung, obwohl heterogene Systemkomponenten beteiligt sind.

Wenn ein Anti-Forensik-Skript Cluster künstlich erzeugt, wird die natürliche Glockenkurve lokal kollabiert. Praktisch entsteht eine überdeterminierte Signalstruktur, in der mehrere Messreihen dieselbe Lage- und Abstandsgeometrie annehmen. Genau diese Überdeterminierung ist mit dem Pearson-Befund \(r = 1{,}0\) kompatibel und stützt die Annahme, dass die Korrelation nicht organisch entstanden ist, sondern einen technisch erzwungenen Pfad abbildet.

## 4. Ausschluss des Zufalls

Für die Zufallsthese wäre erforderlich, dass 892 unabhängige oder nur lose gekoppelte Ereignispaare zufällig eine perfekte lineare Übereinstimmung aufweisen. Bereits intuitiv ist dies unter realweltlichen Bedingungen ausgeschlossen. Streng betrachtet gilt:

1. Je größer \(n\), desto unwahrscheinlicher wird ein perfekter Korrelationswert unter zufälligen Bedingungen.
2. Jedes zusätzliche Wertepaar erhöht die Wahrscheinlichkeit kleinster Abweichungen.
3. Technische Heterogenität verschiedener Subsysteme erzeugt üblicherweise Residuen.
4. Ein idealer lineare Zusammenhang über 892 Punkte setzt eine zugrunde liegende Steuerungs- oder Bindungsfunktion voraus.

Damit ist der Befund nicht als statistisches Kuriosum, sondern als Signatur funktionaler Kausalität zu interpretieren. Der Idealwert weist auf eine mathematisch geschlossene Relation hin, die durch eine operative Kette erzeugt worden sein muss.

## 5. Funktionale Kausalität zwischen physischem Zugriff und Cloud-Injektion

Die Auswertung erlaubt folgende Kausalkette:

1. Ein physischer Zugriff oder physisch vermittelter Kontrollpunkt wird im System oder in korrespondierenden Artefakten rekonstruierbar.
2. Unmittelbar korrespondierend erscheint ein Cloud-bezogenes Injektions- oder Synchronisationsereignis.
3. Die Abstände, Reihenfolge und Intensität dieser Ereignisse bleiben über die Gesamtmenge exakt linear gebunden.
4. Eine solche Bindung ist nur plausibel, wenn beide Ebenen Teil derselben Funktionsarchitektur oder desselben Angriffspfades sind.

Im Ergebnis ist der physische Zugriff nicht nur ein Kontextmerkmal, sondern der auslösende oder kontrollierende Parameter der Cloud-Injektion. Die beobachtete Korrelation dokumentiert damit eine funktionale Kausalität.

## 6. Schlussfolgerung

Der Messwert \(r = 1{,}0\) über 892 Datenpunkte ist kein Zufall. Er ist unter realen technischen Bedingungen nur dann erklärbar, wenn eine deterministische Bindung zwischen den verglichenen Variablen vorliegt. Die ergänzende Modellierung mit der Gaußschen Wahrscheinlichkeitsfunktion zeigt, dass die beobachtete Struktur nicht der natürlichen Streuung legitimer Systemereignisse entspricht, sondern mit künstlicher Clusterbildung vereinbar ist, wie sie durch Anti-Forensik-Skripte erzeugt werden kann.

Damit ist der perfekte Korrelationswert als Beweis einer funktionalen Kausalität zwischen physischem Zugriff und Cloud-Injektion zu werten. Der statistische Befund ist forensisch nicht neutral, sondern indiziert eine gesteuerte Kopplung, die sich mit bloßem Zufall nicht erklären lässt.
