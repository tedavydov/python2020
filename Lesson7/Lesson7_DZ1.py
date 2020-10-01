class Matrix:
    def __init__(self, mx):
        self.correct = True
        if mx:
            if isinstance(mx, list):
                self.__row = 0
                self.__col = 0
                for el in mx:
                    if isinstance(el, list):
                        if not self.__row: self.__col = len(el)
                        if self.__col and self.__col == len(el):
                            self.__row += 1
                        else:
                            self.correct = False
                            print(f"Matrix.__init__ = ERROR : Неправильная размерность матрицы в строке {self.__row + 1}")
                            break
                        for x in el:
                            if not isinstance(x, int):
                                self.correct = False
                                print("Matrix.__init__ = ERROR : Матрица должна состоять из целых чисел [int]")
                                break
            else:
                self.correct = False
                print("Matrix.__init__ = ERROR : Матрица должна быть задана как список [ списков[int], , , ]")
        else:
            self.correct = False
        if self.correct:
            self.matrix = mx
            print(f"Matrix.__init__ = Ok : Создан объект матрицы {self.matrix}")

    def __str__(self):
        str_tmp = ""
        for el in self.matrix:
            str_tmp += "\n"
            for x in el:
                str_tmp += f"{str(x):<4}  "
        return str_tmp

    def __add__(self, mx):
        tmp_row = []
        tmp_mx = []
        try:
            if self.__col == mx.__col and self.__row == mx.__row:
                for row_n in range(self.__row):
                    for col_n in range(self.__col):
                        tmp_row.append(self.matrix[row_n][col_n] + mx.matrix[row_n][col_n])
                    tmp_mx.append(tmp_row)
                    tmp_row = []
            else:
                print(f"Matrix.__add__ = ERROR : Можно складывать только матрицы одинаковой размерности : "
                      f"{self.__row}/{self.__col} не соответствует {mx.__row}/{mx.__col}")
        except:
            print(f"Matrix.__add__ = ERROR : Некорректный экземпляр матрицы : {mx}")
        return Matrix(tmp_mx)


print("=" * 10, "тестирование инициализации матриц", "=" * 20)
a = Matrix([[2, 3], [3, 4], [5, 6]])
b = Matrix([[2, "w"], [3, 4], [5, 6]])
c = Matrix([[2, 3], [3, 3, 4], [5, 6]])
d = Matrix([[2, 3], [3, 4], [3, 5, 6]])
e = Matrix([[7, 1], [2, 2], [1, 9]])
f = Matrix([[7, 8, 1], [1, 2, 2], [1, 4, 9], [7, 3, 1]])

print()
print("=" * 10, "человеческий вывод матриц", "=" * 28)
print(f"Задана матрица 'a' (размерность {a._Matrix__row}/{a._Matrix__col}):\n", a, "\n")
print(f"Задана матрица 'e' (размерность {e._Matrix__row}/{e._Matrix__col}):\n", e, "\n")
print(f"Задана матрица 'f' (размерность {f._Matrix__row}/{f._Matrix__col}):\n", f, "\n")

print()
print("=" * 10, "тестирование сложения матриц", "=" * 25)
print(a, "\n   + ", e, f"\n\nрезультат сложения матриц 'a' и 'e' : \n{a + e}", "\n")

print()
print("=" * 10, "тестирование ошибочного сложения матриц", "=" * 25)
x = (a + f)
print(a, "\n   + ", f,
      f"\n\nрезультат сложения матриц 'a' и 'f' : \n{x}" if x.correct else "\n\nэти матрицы нельзя суммировать !")
