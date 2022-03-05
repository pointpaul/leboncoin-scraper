# leboncoin-scraper

Un wrapper pour utiliser mon [API](https://rapidapi.com/mayliepaul/api/lbc-aio/). Scrapez Leboncoin en toute simplicité, sans proxies ni blocages Datadome.

# Utilisation

* récupérez votre X-RapidApi-Key sur [RapidAPI](https://rapidapi.com/mayliepaul/api/lbc-aio).
* Installer le module requests avec ```pip install requests```

Au premier lancement, le script vous demandera de rentrer votre X-RapidApi-Key et la sauvegardera.
Ensuite, vous pourrez récupérer les données depuis Leboncoin grâce a 3 fonctions:

* ```leboncoin.recherche(url)``` renvoie les annonces de votre lien de recherche,
* ```leboncoin.numéro(list_id)``` renvoie le numéro de téléphone d'une annonce, identifiée par son *list_id*,
* ```leboncoin.annonce(list_id)``` renvoie les informations d'une annonce.

# Contact

Vous pouvez me contacter sur Discord pour plus d'informations : .paul#7172