# Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa
# sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina. Perehdy
# rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on
# tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
# Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.

import requests
user_location = input("Syötä paikkakunnan nimi: ")
url = "https://api.openweathermap.org/geo/1.0/direct?q=" \
      + user_location + "&limit={1}&appid=" \
      "{38235476ebbabe664db40d4f8b5f076f}"
response = requests.get(url).json()
print(f"{response}")
