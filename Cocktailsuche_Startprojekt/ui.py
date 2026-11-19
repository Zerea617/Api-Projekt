import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


from requests import RequestException
from cocktail_api import suche_cocktails


def rezeptansicht(daten):
    if not daten["drinks"]:
        return "Keine Cocktails gefunden."

    rezepte = []
    for cocktail in daten["drinks"]:
        name = cocktail["strDrink"]
        anleitung = cocktail.get("strInstructionsDE") or cocktail.get("strInstructions")
        rezepte.append(name + "\n" + (anleitung or "Keine Zubereitung angegeben."))
    return "\n\n".join(rezepte)


def anzeigen(text):
    ausgabe.configure(state="normal")
    ausgabe.delete("1.0", "end")
    ausgabe.insert("1.0", text)
    ausgabe.configure(state="disabled")


def suchen(event=None):
    name = eingabe.get().strip()
    if not name:
        anzeigen("Gib einen Cocktailnamen ein.")
        return

    try:
        daten = suche_cocktails(name)
        anzeigen(rezeptansicht(daten))
    except RequestException:
        anzeigen("Die Anfrage ist fehlgeschlagen. Versuche es später erneut.")


fenster = tk.Tk()
fenster.title("Cocktailsuche")
rahmen = ttk.Frame(fenster, padding=12)
rahmen.pack(fill="both", expand=True)
ttk.Label(rahmen, text="Welchen Cocktail suchst du?").pack(anchor="w")
eingabe = ttk.Entry(rahmen)
eingabe.pack(fill="x", pady=5)
eingabe.bind("<Return>", suchen)
ttk.Button(rahmen, text="Rezept suchen", command=suchen).pack(anchor="w")
ausgabe = ScrolledText(rahmen, width=64, height=15, wrap="word", state="disabled")
ausgabe.pack(fill="both", expand=True, pady=8)
eingabe.focus_set()
fenster.mainloop()
