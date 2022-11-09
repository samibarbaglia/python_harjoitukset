# Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris
# -vitsin käyttäjälle. Käytä seuravalla sivulla esiteltävää rajapintaa:
# https://api.chucknorris.io/. Käyttäjälle on näytettävä pelkkä vitsin teksti.
import requests
url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)

try:
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json()
        print(f"\n{joke['value']}")
    else:
        print(f'ERROR: {response.status_code}')
except requests.exceptions.RequestException as e:
    print(f"Pieleen meni! {e}")
