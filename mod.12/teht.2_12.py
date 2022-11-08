# Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa
# sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina. Perehdy
# rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on
# tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
# Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.

# SB KOMMENTTI: en saanut API-avainta toimimaan, tein niin paljon kuin pystyin ilman

import requests

user_location = input("Input location: ")
API = '38235476ebbabe664db40d4f8b5f076f'
url = "https://api.openweathermap.org/geo/1.0/direct?q=" \
      + user_location + "&limit={1}&appid=" \
      "{38235476ebbabe664db40d4f8b5f076f}&lang={fi}"

response = requests.get(url)
r2 = response.json()
print(f"{r2['lat']['lon']}")
# API = '38235476ebbabe664db40d4f8b5f076f'
lat = r2['lat']
lon = r2['lon']

url_2 = (f"https://api.openweathermap.org/data/2.5/weather?lat={lat}"
         f"&lon={lon}&appid={API}&units=metric")

try:
    answer = requests.get(url_2)
    if answer.status_code == 200:
        json_answer = answer.json()
        print(json_answer[0]['weather.description']['main.temp'])
except requests.exceptions.RequestException as e:
    print('Hakua ei voitu suorittaa')
