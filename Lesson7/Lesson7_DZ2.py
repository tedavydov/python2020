from abc import ABC, abstractmethod


class Apparel(ABC):
    def __init__(self, x):
        self._name = "Apparel"
        self._parameter_name = "Apparel parameter name"
        if x and (isinstance(x, int) or isinstance(x, float)):
            self.parameter = x
        else:
            self.parameter = 0
            self._parameter_name = f"Apparel parameter name = ERROR {str(x)}"
            print(self._parameter_name)

    def __str__(self):
        return f"{self._name} : {self._parameter_name} = {self.parameter}"

    @abstractmethod
    def consumption(self):
        return self.parameter


class Costume(Apparel):
    def __init__(self, x):
        super().__init__(x)
        self._name = "костюм"
        self._parameter_name = "рост"

    @property
    def consumption(self):
        return 2 * self.parameter + 0.3


class Coat(Apparel):
    def __init__(self, x):
        super().__init__(x)
        self._name = "пальто"
        self._parameter_name = "размер"

    @property
    def consumption(self):
        return self.parameter / 6.5 + 0.5


my_coat = Coat(2)
print(my_coat)
my_costume = Costume(5)
print(my_costume)

print()
print(f"Суммарный расход ткани :  {my_coat.consumption + my_costume.consumption:>5.02f} кв.метров")
