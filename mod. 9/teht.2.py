# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi,
# joka saa parametrinaan nopeuden muutoksen (km/h). Jos nopeuden
# muutos on negatiivinen, auto hidastaa. Metodin on muutettava
# auto-olion nopeus-ominaisuuden arvoa. Auton nopeus ei saa kasvaa
# huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. Jatka
# pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten
# +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus. Tee sitten
# hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
# Kuljettua matkaa ei tarvitse vielä päivittää.

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

    def accelerate(self, speed_change):
        if 0 < self.current_speed + speed_change <= self.top_speed:
            self.current_speed = self.current_speed + speed_change
        elif self.current_speed + speed_change <= 0:
            self.current_speed = 0
        elif self.current_speed + speed_change > self.top_speed:
            self.current_speed = self.top_speed


someCar = Car('ABC-123', 142)

someCar.accelerate(30)
someCar.accelerate(70)
someCar.accelerate(50)
someCar.print_info()
someCar.accelerate(-200)
someCar.print_info()
someCar.accelerate(30)
someCar.print_info()
