class Car:

    def __init__(self, name, speed, color):
        self.is_police = False
        if name and isinstance(name, str):
            self.name = name
        else:
            print("Неправильно задан параметр name")
            self.name = "XXX"
        if speed and (isinstance(speed, int) or isinstance(speed, float)):
            self.speed = speed
        else:
            print("Неправильно задан параметр speed")
            self.speed = 0
        if color and isinstance(color, str):
            self.color = color
        else:
            print("Неправильно задан параметр color")
            self.color = "Белый"

    def go(self):
        if self.speed:
            print(f"{self.name} стартует со скоростью {self.speed} км/ч")
        else:
            print(f"{self.name} не может поехать")

    def show_speed(self):
        if self.speed:
            print(f"скорость {self.name} равна {self.speed} км/ч")
        else:
            print(f"{self.name} не едет")

    def stop(self):
        print(f"{self.name} больше не едет")

    def turn(self, direction):
        directions = ["север", "юг", "восток", "запад"]
        if direction and isinstance(direction, str):
            if direction in directions:
                print(f"{self.name} повернул на {direction}")
            else:
                print(f"{self.name} не может повернуть в направлении {direction}")


class TownCar(Car):

    def show_speed(self):
        if self.speed:
            if self.speed > 60:
                print(f"{self.name} превысил допустимую скорость на {self.speed - 60} км/ч")
            else:
                print(f"скорость {self.name} равна {self.speed} км/ч")
        else:
            print(f"{self.name} не едет")


class WorkCar(Car):

    def show_speed(self):
        if self.speed:
            if self.speed > 40:
                print(f"{self.name} превысил допустимую скорость на {self.speed - 40} км/ч")
            else:
                print(f"скорость {self.name} равна {self.speed} км/ч")
        else:
            print(f"{self.name} не едет")


class PoliceCar(Car):

    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)
        self.is_police = True


class SportCar(Car):

    def go(self, speed=None):
        if speed and (isinstance(speed, int) or isinstance(speed, float)):
            self.speed = speed
            print(f"{self.name} меняет скорость на {self.speed} км/ч")
        elif self.speed:
            print(f"{self.name} едет со скоростью {self.speed} км/ч")
        else:
            print(f"{self.name} не может ехать")


town = TownCar("Mazda", 65, "white")
town.go()
town.turn("назад")
town.turn("север")
town.show_speed()

sport = SportCar("Jaguar", 80, "red")
sport.go()
print("Police = ", sport.is_police)
sport.show_speed()
sport.go(45)
sport.show_speed()

police = PoliceCar("Police", 80, "blue")
work = WorkCar("BMW", 80, "black")
work.go()
police.go()
print("Police = ", police.is_police)
work.show_speed()
work.stop()
