import requests


def suche_cocktails(name):
    antwort = requests.get(
        "https://www.thecocktaildb.com/api/json/v1/1/search.php",
        params={"s": name},
        timeout=10
    )
    antwort.raise_for_status()

    daten = antwort.json()
    return daten


if __name__ == "__main__":
    name = input("Welchen Cocktail suchst du? ")
    print(suche_cocktails(name))
