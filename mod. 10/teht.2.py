#Tehtävät 2 ja 3

import random


class Lift:
    def __init__(self, lowest, highest):
        self.lowest = lowest
        self.highest = highest
        self.current = 0
        self.target = 0

    def move_up(self):
        self.current = self.current + 1
        print(f"Hissi liikkuu ylös kerrokseen {self.current}.")

    def move_down(self):
        self.current = self.current - 1
        print(f"Hissi liikkuu alas kerrokseen {self.current}.")

    def move_to_floor(self, floor):
        self.target = floor

        while self.current != self.target:
            if self.current > floor:
                Lift.move_down(self)

            elif self.current < floor:
                Lift.move_up(self)

            elif self.current == self.target:
                print(f"Hissi on jo kerroksessa {self.current}.")

    def print_info(self):
        print(f"\nAlin kerros on {self.lowest}.")
        print(f"Ylin kerros on {self.highest}.")
        print(f"Hissin nykyinen kerros on {self.current}.\n")

class Building:
    def __init__(self, lowest, highest, amount_lifts):
        self.lowest = lowest
        self.highest = highest
        self.lifts = amount_lifts
        self.lifts = []
        for i in range(amount_lifts):
            list_lift = Lift(lowest, highest)
            self.lifts.append(list_lift)

    def move_lift(self, index, floor):
        the_lift = self.lifts[index-1]
        the_lift.move_to_floor(floor)

    def fire_alarm(self):
        for i in range(len(self.lifts)):
            build_a.move_lift(i+1, 0)


Elevator = Lift(1, 10)

Elevator.move_to_floor(random.randint(1, 10))
Elevator.print_info()

Elevator.move_to_floor(1)
Elevator.print_info()

build_a = Building(1, 7, 2)
build_b = Building(0, 4, 1)

build_a.move_lift(2, 7)
build_a.fire_alarm()