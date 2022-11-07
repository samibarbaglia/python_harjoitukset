import random


class Car:
    def __init__(self, plate, top_speed):
        self.plate = plate
        self.top_speed = top_speed
        self.travelled = 0
        self.current_speed = 0

    def print_info(self):
        print(f'\nCAR {self.plate} top speed: {self.top_speed} km/h.'
              f' Current {self.current_speed} km/h, '
              f'travelled {self.travelled} km.')

    def accelerate(self, speed_change):
        if 0 < self.current_speed + speed_change <= self.top_speed:
            self.current_speed = self.current_speed + speed_change
        elif self.current_speed + speed_change <= 0:
            self.current_speed = 0
        elif self.current_speed + speed_change > 0:
            self.current_speed = self.top_speed
        return

    def travel(self, time):
        distance = self.travelled + (self.current_speed * time)
        self.travelled = distance


class Competition:

    def __init__(self, name, distance):
        self.cars = []
        self.distance = distance
        self.name = name
        self.time = 0

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.travel(1)

    def game(self):
        for i in range(10):
            self.cars.append(Car('ABC-' + str(i + 1), random.randint(100, 200)))

        stop = False
        while not stop:
            print(f"\n-- [TUNTI {self.time + 1}] --")
            self.time = self.time + 1
            for car in self.cars:
                car.accelerate(random.randint(-10, 15))
                car.travel(1)
                Car.print_info(car)
                if car.travelled >= self.distance:
                    stop = True
                    print("\n\n-- [KILPAILUN TULOKSET] --")
                    break

        # Tulostetaan autojen tiedot
        for car in self.cars:
            car.print_info()


competition = Competition("Suuri romuralli", 8000)
print("TERVETULOA SUUREEN ROMURALLIIN!")
competition.game()
