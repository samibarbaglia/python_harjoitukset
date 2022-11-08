# Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa
# sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina. Perehdy
# rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on
# tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
# Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.

import json

# SB KOMMENTTI: en saanut API-avainta toimimaan, tein niin paljon kuin pystyin ilman

import requests

user_location = input("Input location: ")
API = '38235476ebbabe664db40d4f8b5f076f'
url = f"https://api.openweathermap.org/geo/2.5/direct?q={user_location}&appid=38235476ebbabe664db40d4f8b5f076f"
answer = requests.get(url)
print(f"{answer.status_code}")

try:
    if answer.status_code == 200:
        json_answer = answer.json()
        print(json_answer[0]['weather.description']['main.temp'])
except requests.exceptions.RequestException as e:
    print('Hakua ei voitu suorittaa')
