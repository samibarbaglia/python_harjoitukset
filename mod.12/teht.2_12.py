# Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa
# sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina. Perehdy
# rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on
# tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
# Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.

import requests

user_location = input("Input location: ")
API = '38235476ebbabe664db40d4f8b5f076f'
url = f"https://api.openweathermap.org/data/2.5/weather?&appid=" \
      f"{API}&q={user_location}&units=metric&lang=fi"
print(url)
response = requests.get(url)
# print(f"{response.status_code}")

try:
    if response.status_code == 200:
        json_response = response.json()
        temp = json_response['main']['temp']
        description = json_response['weather'][0]['description']
        country = json_response['sys']['country']
        print(f"\n{user_location}, {country}:\n"
              f"- Lämpötila: {temp:0.2f} celcius\n"
              f"- Sää: {description}")
    elif response.status_code == 404:
        print(f"Hakua ei voitu suorittaa [ERROR {response.status_code}]")
except requests.exceptions.RequestException as e:
    print(f'Hakua ei voitu suorittaa [ERROR {e}]')