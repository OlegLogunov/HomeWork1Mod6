class Car:
    price = 1000000

    def horse_powers(self, horse_power):
        self.horse_power = horse_power
        print(f"Мощность автомобиля {self.horse_power} л.с.")
        return self.horse_power

class Nissan(Car):
    price = 1500000

    def horse_powers(self):
        print("У меня электромобиль Nissan")

class Kia(Car):
    price = 800000

    def horse_powers(self):
        print(f"Автомобиль KIA за {self.price} руб.")

auto = Car()
auto.horse_powers(175)

auto_nis = Nissan()
auto_nis.horse_powers()

auto_kia = Kia()
auto_kia.horse_powers()
