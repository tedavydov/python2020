class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        if name and isinstance(name, str):
            self.name = name
        else:
            print("Неправильно задан параметр name")
            self.name = "name"
        if surname and isinstance(surname, str):
            self.surname = surname
        else:
            print("Неправильно задан параметр surname")
            self.surname = "surname"
        if position and isinstance(position, str):
            self.position = position
        else:
            print("Неправильно задан параметр position")
            self.position = "position"
        if wage and bonus and (
                isinstance(wage, int) or isinstance(bonus, int) or
                isinstance(wage, float) or isinstance(bonus, float)):
            self._income = {"wage": wage, "bonus": bonus}
        else:
            print("Неправильно заданы параметры wage и bonus")
            self._income = {"wage": 1, "bonus": 1}


class Position(Worker):

    def get_full_name(self):
        print(f"Я {self.name} {self.surname}")

    def get_total_income(self):
        print(f"Мой доход с учетом премии {sum(self._income.values())} руб. на позиции {self.position}")


ivan = Position("Иван", "Иванов", "инженер", 20000, 10000)
ivan.get_full_name()
ivan.get_total_income()

igor = Position("Игорь", "Селиванов", "менеджер", 30000, 10000)
igor.get_full_name()
igor.get_total_income()
