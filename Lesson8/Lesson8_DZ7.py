class ComplexNum:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def __str__(self):
        if isinstance(self.__a, int) and isinstance(self.__b, int):
            return f"{self.__a} + {self.__b}i"
        else:
            if isinstance(self.__a, float):
                aa = f"{self.__a:.02f}"
            else:
                aa = self.__a
            if isinstance(self.__b, float):
                bb = f"{self.__b:.02f}"
            else:
                bb = self.__b
            return f"{aa} + {bb}i"

    def __add__(self, cpx2):  # сложение
        return ComplexNum(self.__a + cpx2.__a, self.__b + cpx2.__b)

    def __sub__(self, cpx2):  # вычитание
        return ComplexNum(self.__a - cpx2.__a, self.__b - cpx2.__b)

    def __mul__(self, cpx2):  # умножение
        tmp_a = (self.__a * cpx2.__a) - (self.__b * cpx2.__b)
        tmp_b = (self.__b * cpx2.__a) + (self.__a * cpx2.__b)
        return ComplexNum(tmp_a, tmp_b)

    def __truediv__(self, cpx2):  # деление
        tmp_a = (self.__a * cpx2.__a + self.__b * cpx2.__b) / (cpx2.__a * cpx2.__a + cpx2.__b * cpx2.__b)
        tmp_b = (self.__b * cpx2.__a - self.__a * cpx2.__b) / (cpx2.__a * cpx2.__a + cpx2.__b * cpx2.__b)
        return ComplexNum(tmp_a, tmp_b)


print("=" * 10, "Зададим комплексные числа : ", "=" * 13)
cpx1 = ComplexNum(3, 7)
cpx2 = ComplexNum(1, -4)
cpx3 = ComplexNum(12, 10)
cpx4 = ComplexNum(4, 8)
cpx5 = ComplexNum(9, 1)

print()
print("=" * 10, "Сложение комплексных чисел : ", "=" * 13)
print(f"({cpx1}) + ({cpx3}) = ({cpx1 + cpx3})")
print(f"({cpx4}) - ({cpx2}) = ({cpx4 + cpx2})")
print(f"({cpx2}) - ({cpx5}) = ({cpx2 + cpx5})")
print("=" * 10, "проверка : ", "=" * 13)
print(f"({cpx1}) + ({cpx3}) = {str(complex(3, 7) + complex(12, 10))}")
print(f"({cpx4}) - ({cpx2}) = {str(complex(4, 8) + complex(1, -4))}")
print(f"({cpx2}) - ({cpx5}) = {str(complex(1, -4) + complex(9, 1))}")


print()
print("=" * 10, "Умножение комплексных чисел : ", "=" * 13)
print(f"({cpx1}) * ({cpx3}) = ({cpx1 * cpx3})")
print(f"({cpx4}) * ({cpx2}) = ({cpx4 * cpx2})")
print("=" * 10, "проверка : ", "=" * 13)
print(f"({cpx1}) * ({cpx3}) = {str(complex(3, 7) * complex(12, 10))}")
print(f"({cpx4}) * ({cpx2}) = {str(complex(4, 8) * complex(1, -4))}")

print()
print("=" * 10, "Деление комплексных чисел : ", "=" * 13)
print(f"({cpx1}) / ({cpx3}) = ({cpx1 / cpx3})")
print(f"({cpx2}) / ({cpx5}) = ({cpx2 / cpx5})")
print("=" * 10, "проверка : ", "=" * 13)
print(f"({cpx1}) / ({cpx3}) = ({(complex(3, 7) / complex(12, 10)).real:.02f} + {(complex(3, 7) / complex(12, 10)).imag:.02f}j)")
print(f"({cpx2}) / ({cpx5}) = ({(complex(1, -4) / complex(9, 1)).real:.02f} + {(complex(1, -4) / complex(9, 1)).imag:.02f}j)")
