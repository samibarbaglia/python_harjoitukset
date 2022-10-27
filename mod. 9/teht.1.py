# Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus,
# huippunopeus, tämänhetkinen nopeus ja kuljettu matka. Kirjoita
# luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua
# parametreina saatuihin arvoihin. Uuden auton nopeus ja kuljetut matka
# on asetettava automaattisesti nollaksi. Kirjoita pääohjelma, jossa luot
# uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h). Tulosta
# pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class Car:
    def __init__(self, plate, top_speed):
        self.plate = plate
        self.top_speed = top_speed
        self.travelled = 0
        self.current_speed = 0

    def print_info(self):
        print(f'\nAuton {self.plate} huippunopeus on {self.top_speed} km/h.'
              f'\nTämänhetkinen nopeus: {self.current_speed} km/h, '
              f'kuljettu matka: {self.travelled} km.')


someCar = Car('ABC-123', 142)
otherCar = Car('DEF-456', 150)

someCar.print_info()
otherCar.print_info()