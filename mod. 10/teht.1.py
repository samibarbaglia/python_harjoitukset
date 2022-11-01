# Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman
# ja ylimmän kerroksen numeron. Hissillä on metodit siirry_kerrokseen,
# kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5),
# metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa,
# että hissi päätyy viidenteen kerrokseen. Viimeksi mainitut metodit ajavat
# hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa
# hissi sen jälkeen on. Testaa luokkaa siten, että teet pääohjelmassa hissin ja
# käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

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
        self.target = kerros

        while self.current != self.target:
            if self.current > kerros:
                Lift.move_down(self)

            elif self.current < kerros:
                Lift.move_up(self)

            elif self.current == self.target:
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