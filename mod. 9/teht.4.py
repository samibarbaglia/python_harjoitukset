# Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on
# ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista.
# Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja
# asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit: tunti_kuluu, joka
# toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet
# eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
# tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
# kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut
# vähintään kilpailun kokonaiskilometrimäärän.Kirjoita pääohjelma, joka luo 8000 kilometrin
# kilpailun nimeltä "Suuri romuralli". Luotavalle kilpailulle annetaan kymmenen auton lista
# samaan tapaan kuin aiemmassa tehtävässä. Pääohjelma simuloi kilpailun etenemistä kutsumalla
# toistorakenteessa aja tunti-metodia, jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla,
# onko kilpailu ohi. Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin
# välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.

import random


class Car:
    def __init__(self, plate, top_speed):
        self.plate = plate
        self.top_speed = top_speed
        self.travelled = 0
        self.current_speed = 0

    def print_info(self):
        print(f'\nAuton {self.plate} huippunopeus {self.top_speed} km/h.'
              f'\nHetkellinen nopeus {self.current_speed} km/h, '
              f'Kuljettu matka {self.travelled} km.')

    def accelerate(self, speed_change):
        if 0 < self.current_speed + speed_change <= self.top_speed:
            self.current_speed = self.current_speed + speed_change
        elif self.current_speed + speed_change <= 0:
            self.current_speed = 0
        elif self.current_speed + speed_change > 0:
            self.current_speed = self.top_speed
        return

    def travel(self, aika):
        distance = self.travelled + (self.current_speed * aika)
        self.travelled = distance


class Competition:

    def __init__(self, name, travelled_km):
        self.cars = []
        self.name = name
        self.travelled_km = travelled_km

    def game(self):
        # Luodaan autot (lisätään listaan)
        for i in range(10):
            self.cars.append(Car('ABC-' + str(i + 1), random.randint(100, 200)))

        # Ajetaan kilpailu, kunnes joku auto yli 10000
        stop = False
        while not stop:
            for car in self.cars:
                car.accelerate(random.randint(-10, 15))
                car.travel(1)
                if car.travelled >= 10000:
                    stop = True
                    break

        # Tulostetaan autojen tiedot
        for car in self.cars:
            car.print_info()


competition = Competition("romuralli", 8000)
competition.game()
