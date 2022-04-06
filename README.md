# Wetterstation-Raspberry-Pi

In diesem Projekt wird eine Wetterstation, bestehend aus einem Raspberry Pi 3 entwickelt.

Aktueller Stand:

Die aktuelle Version beinhaltet sowohl ein Thermometer, als auch ein Hygrometer. Zusätzlich ist eine Kamera und ein photosensitiver Widerstand verbaut.
Die Daten der Sensoren und das Bild der Kamera werden auf Kopfdruck in einer GUI dargestellt und können durchgehend manuell aktualisiert werden. Die Photozelle wird im Programm ausgewertet und entscheidet, ob es Sonnig, leicht bewölkt oder bewölkt ist. Bei kompletter Dunkelheit wird eine Sonnenfinsternis ausgegeben. Diesen Wetterstand sieht man ebenfalls auf der GUI.
Zusätzlich wird unter dem Kamerabild das Datum, der Wochentag und die aktuelle Zeit zum Zeitpunkt der Aktualisierung ausgegeben.

Mögliche Ziele:

In Zunkunft soll einerseits zusätzlich der aktuelle Sonnenauf- und Untergang ausgegeben werden, welcher auch die Wetterprognosen der Photozelle beeinflusst (Sonnenfinsternis oder Nacht). Die Daten des Auf- und Untergangs sollen automatisch aus dem Internet gezogen werden und dementsprechend je nach Datum variieren.

Andererseits soll eventuell ein Webserver eingerichtet werden, sodass man durch das Aufrufen der Domain die GUI bspw. auf seinem Handy sehen und bedienen kann.
