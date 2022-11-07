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

    def move_to_floor(self, kerros):

        while self.current != kerros:
            if self.current > kerros:
                Lift.move_down(self)

            elif self.current < kerros:
                Lift.move_up(self)

            elif self.current == kerros:
                print(f"Hissi on jo kerroksessa {self.current}.")

    def print_info(self):
        print(f"\nAlin kerros on {self.lowest}.")
        print(f"Ylin kerros on {self.highest}.")
        print(f"Hissin nykyinen kerros on {self.current}.\n")


Elevator = Lift(1, 10)

Elevator.move_to_floor(random.randint(1, 10))
Elevator.print_info()

Elevator.move_to_floor(1)
Elevator.print_info()
