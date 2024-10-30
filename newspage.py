import requests

# URL der Tagesschau API
url = "https://www.tagesschau.de/api2u/homepage/"

# Anfrage an die API senden
response = requests.get(url)


if response.status_code == 200:
        data = response.json()
        news = data.get('news', [])
else:
        news = f"Fehler beim Abrufen der Daten: {response.status_code}"
