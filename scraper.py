import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL cible
URL = "https://quotes.toscrape.com/"

# Envoyer la requête
response = requests.get(URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Récupérer les citations et auteurs
    quotes = soup.find_all("div", class_="quote")

    data = []
    for i, quote in enumerate(quotes):
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        data.append({"id": i + 1, "quote": text, "author": author})

    # Sauvegarder dans un fichier CSV
    df = pd.DataFrame(data)
    df.to_csv("quotes.csv", index=False, encoding="utf-8")

    print("✅ Fichier 'quotes.csv' généré avec succès.")
else:
    print(f"❌ Erreur HTTP : {response.status_code}")
