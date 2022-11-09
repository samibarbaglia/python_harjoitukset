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
    def __init__(self, plate, top_speed, speed):
        self.plate = plate
        self.top_speed = top_speed
        self.travelled = 0
        self.speed = speed

    def print_info(self):
        print(f'Car [{self.plate}]: '
              f'\n- Top speed: {self.top_speed} km/h, travelled: {self.travelled} km.'
              f'\n- Current speed: {self.speed} km/h')

    def travel(self, hour):
        distance = self.travelled + (self.speed * hour)
        self.travelled = distance
        self.print_info()


class Electric(Car):
    def __init__(self, plate, top_speed, speed, battery):
        self.battery = battery
        super().__init__(plate, top_speed, speed)

    def travel(self, hour):
        super().travel(hour)
        print(f'- Max. battery: {self.battery} kWh.\n')


class Gas(Car):
    def __init__(self, plate, top_speed, speed, gasoline_l):
        self.gasoline_l = gasoline_l
        super().__init__(plate, top_speed, speed)

    def travel(self, hour):
        gas_per_l = 10 #1l pyörittää 10km
        gas_used = (self.speed / gas_per_l) * hour
        gas_left= self.gasoline_l - gas_used
        super().travel(hour)
        print(f'- Max. gasoline: {self.gasoline_l} l, USED: {gas_used:0.2f} l, LEFT: {gas_left:0.2f} l')


car = []
car.append(Electric('ABC-15', 180, random.randint(20, 180), 52.5))
car.append(Gas('ACD-123', 165, random.randint(20, 165), 32.3))

for c in car:
    c.travel(3)
