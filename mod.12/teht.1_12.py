# Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris
# -vitsin käyttäjälle. Käytä seuravalla sivulla esiteltävää rajapintaa:
# https://api.chucknorris.io/. Käyttäjälle on näytettävä pelkkä vitsin teksti.
import requests

url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url).json()
print(f"\n{response['value']}")
