class Cell:
    def __init__(self, x):
        if x and isinstance(x, int):
            self.count = x
        else:
            self.count = 0
            print(f"Cell count ERROR {str(x)}")

    def __add__(self, cell):  # сложение клеток
        if cell and isinstance(cell, Cell):
            return Cell(int(self.count + cell.count))

    def __sub__(self, cell):  # вычитание клеток
        if cell and isinstance(cell, Cell):
            if self.count > cell.count:
                return Cell(int(self.count - cell.count))
            else:
                print(f"клетка {self.count} не больше {cell.count}")

    def __mul__(self, cell):  # умножение клеток
        if cell and isinstance(cell, Cell):
            return Cell(int(self.count * cell.count))

    def __truediv__(self, cell):  # деление клеток
        if cell and isinstance(cell, Cell):
            return Cell(int(self.count // cell.count))

    def __str__(self):
        return f"клетка размером {self.count} ячеек"

    def make_order(self, col):
        tmp_str = ""
        if col and isinstance(col, int):
            row = self.count // col
            row_end = self.count % col
            while row:
                tmp_str += ("*" * col) + "\n"
                row -= 1
            tmp_str += ("*" * row_end)
        else:
            print(f"Cell make_order ERROR {str(col)}")
        return tmp_str


cell_1 = Cell(23)
cell_2 = Cell(13)
cell_3 = Cell(17)
cell_4 = Cell(55)
cell_5 = Cell(41)

print(f"жили-были клетки :\n{cell_1}\n{cell_2}\n{cell_3}\n{cell_4}\n{cell_5}")

print()
print(f"клетка №1 сьела клетку №2 и получилась : {cell_1 + cell_2}")
print(f"клетка №3 укусила клетку №4 и ошиблась : {cell_3 - cell_4} не на ту напала !")
print(f"клетка №4 укусила клетку №5 и осталось : {cell_4 - cell_5} от клетки №4, а вот не надо кусаться !")
print(f"клетки №2 и №3 объединились, получилась : {cell_2 * cell_3}, все выиграли !")
print(f"клетки №4 и №1 подрались, получилась : {cell_4 / cell_1}, драться плохо !")

print()
print("Вот наши герои :")
print(f"обьединение клеток №2 и №3 :\n{(cell_2 * cell_3).make_order(50)}")
print(f"то что очталось от клеток №4 и №1 :\n{(cell_4 / cell_1).make_order(5)}")
print(f"и независимая клетка №5 :\n{cell_5.make_order(15)}")
