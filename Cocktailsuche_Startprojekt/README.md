# Cocktailsuche

Das Projekt fragt TheCocktailDB nach einem Cocktailnamen ab. Die grafische Oberfläche zeigt für jeden Treffer den Namen und die Zubereitung an.

## Start

Python ab Version 3.9 mit Tkinter installieren. Im Projektordner ausführen:

```shell
python -m pip install requests
python ui.py
```

Zum Ausprobieren `Margarita` eingeben und Enter drücken. Die Anfrage benötigt eine Internetverbindung. Mit `python cocktail_api.py` lässt sich dieselbe Suche direkt im Terminal testen.

## Aufbau und KI-Einsatz

Der ursprüngliche API-Aufruf aus unserem Skript steckt in der Funktion `suche_cocktails` in `cocktail_api.py`. Sie übergibt den Suchbegriff mit dem Parameter `s` und gibt die eingelesene JSON-Antwort zurück.

Die mit KI erstellte Oberfläche in `ui.py` ruft diese Funktion auf. Die ebenfalls mit KI ergänzte Funktion `rezeptansicht` geht die Treffer in `drinks` durch und zeigt den Namen sowie die deutsche oder, falls diese fehlt, die englische Zubereitung. Bei einer leeren Trefferliste erscheint eine Meldung.
