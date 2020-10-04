class StockRoom:
    def __init__(self, address):
        self.address = address
        self.equipments = []
        self.quantity = {"OfficeEquipment": 0, "Printer": 0, "Scanner": 0, "Xerox": 0, "Laptop": 0, "NoName": 0}

    def acceptance(self, equipment):
        eq_type = "NoName"
        if isinstance(equipment, Printer):
            eq_type = "Printer"
        elif isinstance(equipment, Scanner):
            eq_type = "Scanner"
        elif isinstance(equipment, Xerox):
            eq_type = "Xerox"
        elif isinstance(equipment, Laptop):
            eq_type = "Laptop"
        elif isinstance(equipment, OfficeEquipment):
            eq_type = "OfficeEquipment"

        self.equipments.append({"Type": eq_type, "Equipment": equipment})
        self.quantity[eq_type] += 1
        print(f"Оборудование {eq_type} принято на склад '{self.address}'")

    def delivery(self, eq, subdivision="Main Office"):
        eq_type = "NoName"
        if isinstance(eq, str):
            eq_type = eq
        elif isinstance(eq, Printer):
            eq_type = "Printer"
        elif isinstance(eq, Scanner):
            eq_type = "Scanner"
        elif isinstance(eq, Xerox):
            eq_type = "Xerox"
        elif isinstance(eq, Laptop):
            eq_type = "Laptop"
        elif isinstance(eq, OfficeEquipment):
            eq_type = "OfficeEquipment"
        flag = False
        if eq_type in self.quantity.keys():
            for x in range(len(self.equipments)):
                if self.equipments[x]["Type"] == eq_type:
                    self.equipments.pop(x)
                    self.quantity[eq_type] -= 1
                    print(f"{eq_type} передан в {subdivision}\n"
                          f"на складе '{self.address}' осталось {self.quantity[eq_type]} ед. обоудования этого типа")
                    flag = True
                    break

        if not flag:
            print(f"на складе '{self.address}' не осталось оборудования типа {eq_type}")


class OfficeEquipment:
    def __init__(self, length, width, height, weight):
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight


class Printer(OfficeEquipment):
    def __init__(self, length, width, height, weight, type, color=False):
        super().__init__(length, width, height, weight)
        self.type = type
        self.color = color


class Scanner(OfficeEquipment):
    def __init__(self, length, width, height, weight, color=False):
        super().__init__(length, width, height, weight)
        self.color = color


class Xerox(OfficeEquipment):
    def __init__(self, length, width, height, weight, mfu=False):
        super().__init__(length, width, height, weight)
        self.mfu = mfu


class Laptop(OfficeEquipment):
    def __init__(self, length, width, height, weight, screen):
        super().__init__(length, width, height, weight)
        self.screen = screen

stock1 = StockRoom("Moscow")
stock2 = StockRoom("Yaroslavl")

print("=" * 10, "Поступление оргтехники на склад : ", "=" * 25)
stock1.acceptance(Printer(40, 40, 40, 35, "Laser", True))
stock1.acceptance(Printer(33, 45, 20, 5, "Jet"))
stock2.acceptance(Printer(40, 55, 22, 15, "Jet", True))
stock1.acceptance(Xerox(50, 55, 50, 40, True))
stock2.acceptance(Scanner(25, 35, 10, 2, True))
stock1.acceptance(Laptop(30, 20, 5, 1, 14))

print()
print("=" * 10, "Передача оргтехники в подразделения компании : ", "=" * 13)
print()
stock1.delivery("Printer", "Yaroslavl Office")
print()
stock2.delivery("Laptop", "Yaroslavl Office")
print()
stock2.delivery("Scanner", "Yaroslavl Office")
print()
stock1.delivery("Scanner", "Moscow Office")
