# Project Goals and Requirements

As already stated in the overview Pirate tries to create a solution for monitoring Arduino projects.
The primary use case is sending and receiving of data. In addition the remote Monitoring 

The overall Goals are defined below. Further and more specific requirements can be found in each components section.

## User Stories
* As a User I want to be able to see the status of my project in realtime on a graph.
* As a User I want to be able to download the shown graph data.
* As a User I want to be able to influence the variables/parameters directly without reflashing the Arduino.
* As a User I want to be able to access the the dashboard from "anywhere".
* When controlling a project from a remote location I as a User want to view a live feed of the project to monitor the actual influence my action have.
* As a User I want to easily be able to set up this solution.

# Functional Requirements

Parameter ändern
Der Benutzer verbindet sich mit Webseite
Die Webseite gibt Benutzer Überblick über Projekte
Der Benutzer wählt ein Projekt aus
Die Webseite stellt den Status des Projektes dar
Der Benutzer ändert einen Wert
Die Webseite leitet die Wertänderung weiter

Parameter abfragen
Der Benutzer verbindet sich mit Webseite
Die Webseite gibt Benutzer Überblick über Projekte
Der Benutzer wählt ein Projekt aus
Die Webseite stellt den Status des Projektes dar
Der Benutzer kann die Werte im Status auslesen

Liveübertragung ansehen
Der Benutzer verbindet sich mit Webseite
Die Webseite gibt Benutzer Überblick über Projekte
Der Benutzer wählt ein Projekt aus
Die Webseite stellt den Status des Projektes dar
Der Benutzer kann die Kameraübertragung aktivieren
Die Webseite stellt die Kameraübertragung dar

Zeitlichen Ablauf des Status einsehen
Der Benutzer verbindet sich mit Webseite
Die Webseite gibt Benutzer Überblick über Projekte
Der Benutzer wählt ein Projekt aus
Die Webseite stellt den Status des Projektes dar
Der Benutzer kann Statusansicht auf zeitlichen Verlauf umstellen
Die Webseite beginnt den zeitlichen Verlauf des Status bereitzustellen

## Non-Functional Requirements
Frontend muss 3h stabil funktionieren ( während eines Praktikums )
24/7 Bereitschaft sollte gewährleistet sein
Verzögerungszeit der gesamten Übertragung darf nicht länger als 2 Sekunden sein
Es muss unter LTE Verhältnissen laufen und für ausreichend befunden werden von Auftraggeber
Remotezugriff muss auf andere RProjekte adaptierbar sein
Es müssen mehrere RProjekte gleichzeitig unterstützt werden
Die Gesamtabgabe soll mit mindestens einem funktionsfähigen RProjekt erfolgen
Zugriff muss über eine Website erfolgen können
Zum Abgabezeitpunkt muss die aktuelle Version von Chrome und Firefox unterstützt werden
Zeitlicher Verlauf der Parameter und Istwerte muss dargestellt werden und exportierbar sein
Schnittstellen die in der Architekturplanung festgelegt werden, müssen nach Spezifikation implementiert sein
Dokumentation muss von Auftraggeber abgenommen worden sein
Optionale Nichtfunktionale Anforderungen
Zweites eingerichtetes funktionsfähiges RProjekt


<!-- perhaps a "solutions" section where links to how we solved the problems are linked? -->