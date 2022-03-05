import requests


class Scraper:
    def __init__(self, apikey):
        self.apikey = apikey

    def recherche(self, url):

        headers = {
            "x-rapidapi-host": "lbc-aio.p.rapidapi.com",
            "x-rapidapi-key": self.apikey,
        }

        response = requests.get(
            "https://lbc-aio.p.rapidapi.com/search",
            headers=headers,
            params={"url": url},
        )

        return response.json()

    def numéro(self, list_id):
        headers = {
            "x-rapidapi-host": "lbc-aio.p.rapidapi.com",
            "x-rapidapi-key": self.apikey,
        }

        response = requests.get(
            "https://lbc-aio.p.rapidapi.com/phone",
            headers=headers,
            params={"list_id": list_id},
        )

        return response.json()

    def annonce(self, list_id):
        headers = {
            "x-rapidapi-host": "lbc-aio.p.rapidapi.com",
            "x-rapidapi-key": self.apikey,
        }

        response = requests.get(
            "https://lbc-aio.p.rapidapi.com/listing",
            headers=headers,
            params={"list_id": list_id},
        )

        return response.json()

    def cookie(self):
        headers = {
            "x-rapidapi-host": "lbc-aio.p.rapidapi.com",
            "x-rapidapi-key": self.apikey,
        }

        response = requests.get(
            "https://lbc-aio.p.rapidapi.com/cookie", headers=headers
        )

        return response.json()
