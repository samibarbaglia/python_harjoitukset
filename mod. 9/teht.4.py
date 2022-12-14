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
        elif self.current_speed + speed_change > self.top_speed:
            self.current_speed = self.top_speed
        return

    def travel(self, time):
        distance = self.travelled + (self.current_speed * time)
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
