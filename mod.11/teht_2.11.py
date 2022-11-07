# Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton
# ominaisuutena on bensatankin koko litroina. Kirjoita aliluokille alustajat. Esimerkiksi
# sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin.
# Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman
# kapasiteettinsa. Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh)
# ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi
# nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.
import random


class Car:
    def __init__(self, plate, top_speed):
        self.plate = plate
        self.top_speed = top_speed
        self.travelled = 0

    def print_info(self):
        print(f'Top speed: {self.top_speed} km/h, '
              f'travelled {self.travelled} km.')

    def travel(self, time, speed):
        distance = self.travelled + (speed * time)
        self.travelled = distance
        print(f'{self.plate}, current speed: {speed} km/h')


class Electric(Car):
    def __init__(self, plate, top_speed, battery):
        self.battery = battery
        super().__init__(plate, top_speed)

    def travel(self, time, speed):
        super().travel(time, speed)
        super().print_info()
        print(f'Max. battery: {self.battery} kWh.\n')


class Gas(Car):
    def __init__(self, plate, top_speed, gasoline_l):
        self.gasoline_l = gasoline_l
        super().__init__(plate, top_speed)

    def travel(self, time, speed):
        super().travel(time, speed)
        super().print_info()
        print(f'Max. gasoline: {self.gasoline_l} l.\n')


car = []
car.append(Electric('ABC-15', 180, 52.5))
car.append(Gas('ACD-123', 165, 32.3))

for c in car:
    c.travel(3, random.randint(50, 100))
