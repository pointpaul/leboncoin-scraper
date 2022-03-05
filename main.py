from helper import Scraper
from os import path

if not path.exists("./config.txt"):
    with open("./config.txt", "w") as f:
        f.write(input("Clé X_RapidAPI_Key: "))
else:
    X_RapidAPI_Key = open("./config.txt").read()
    print("X_RapidAPI_Key :", X_RapidAPI_Key)

leboncoin = Scraper(X_RapidAPI_Key)

# print(leboncoin.recherche("https://www.leboncoin.fr/recherche?category=2"))
# print(leboncoin.numéro(2126418487))
# print(leboncoin.annonce(2126418487))
# print(leboncoin.cookie())
