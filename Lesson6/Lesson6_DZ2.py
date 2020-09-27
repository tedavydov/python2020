class Road:

    def __init__(self, length, width):
        if isinstance(length, int) and isinstance(width, int):
            self._length = length
            self._width = width
        else:
            print("Неправильно заданы параметры")
            self._length = 0
            self._width = 0

    def weight(self, depth=1):
        if self._length and self._width:
            # формула: длина * ширина
            # * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см (= 25кг)
            # * число см толщины полотна
            return self._length * self._width * 25 * depth
        else:
            print("не заданы параметры для расчета")


r = Road(130, 20)  # создаем объект дороги длиной 130 м и шириной 20 м

print(r.weight(5), "кг")  # рассчитаем массу асфальта для покрытия толщиной 5 см
print(r.weight(), "кг")  # рассчитаем массу асфальта (по умолчанию покрытие толщиной 1 см)
