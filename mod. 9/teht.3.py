# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa
# parametrinaan tuntimäärän. Metodi kasvattaa kuljettua matkaa sen
# verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä
# edennyt. Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
# Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan
# lukemaan 2090 km.

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
        elif self.current_speed + speed_change > 0:
            self.current_speed = self.top_speed

    def travel(self, aika):
        distance = self.travelled + (self.current_speed * aika)
        self.travelled = distance


someCar = Car('ABC-123', 142)
otherCar = Car('LOL-420', 69)

someCar.accelerate(30)
someCar.travel(1.5)
someCar.print_info()
someCar.accelerate(60)
someCar.travel(2)

someCar.print_info()