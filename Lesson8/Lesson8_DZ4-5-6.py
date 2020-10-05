class StockRoom:
    # общий учет оборудования по категориям на всех складах (обобщенные типы оборудования)
    __quantity = {"OfficeEquipment": 0, "Printer": 0, "Scanner": 0, "Xerox": 0, "Laptop": 0, "NoName": 0}

    def __init__(self, address=""):
        self.address = address

        # учет оборудования на конкретном складе по партиям (конкретные модификации оборудования)
        self.__equipments = {}

    @property
    def inventory(self):
        '''Полная инвентаризация по всем складам,
           выдает отчет по наличию оборудования ..
        '''
        res = "=" * 10 + "Полная инвентаризация оборудования : " + "=" * 13 + "\n"
        res += "=" * 5 + f"  Склад  '{self.address}' : " + "=" * 20 + "\n"
        for eq in self.__equipments.keys():
            res += f"{str(eq):<50} на складе:{str(self.__equipments[eq]):>3} ед." + \
                   f"   всего на складах {eq.type:>7}:{str(self.__quantity[eq.type]):>3} ед.\n"
        return res

    @staticmethod
    def __count_validation(count):
        '''Проверяет переданный параметр количества оборудования,
           выдает целое число - корректное количество единиц оборудования ..
        '''
        if isinstance(count, str):
            count_val = 1
        elif isinstance(count, int):
            count_val = count
        elif isinstance(count, float):
            count_val = int(count)
        else:
            count_val = 1
        return count_val

    @staticmethod
    def __type_validation(eq, lst=None):
        '''Проверяет ведется ли учет данного оборудования,
           и выдает корректный строковый тип оборудования.
           передать :
                     eq - класс или строчный тип офисного оборудования
          [Options] lst - эталонный список строковых типов оборудования
        '''
        if lst is None:
            lst = ["OfficeEquipment", "Printer", "Scanner", "Xerox", "Laptop", "NoName"]
        eq_type = "NoName"
        if isinstance(eq, str) and eq in lst:
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
        return eq_type

    @classmethod
    def __quantity_accounting(cls, eq_type, count, add_flag=False):
        '''Общий учет оборудования по категориям на всех складах (обобщенные типы оборудования)
           передать :
                     eq_type - строчный тип офисного оборудования
        '''

        count_val = cls.__count_validation(count)
        if add_flag:  # =========== поступление ==================
            cls.__quantity[eq_type] += count_val
            return cls.__quantity[eq_type]
        else:  # ================== списание =====================
            if cls.__quantity[eq_type] == 0:
                return 0
            elif cls.__quantity[eq_type] >= count_val:
                cls.__quantity[eq_type] -= count_val
                return cls.__quantity[eq_type]
            else:
                return cls.__quantity[eq_type]

    def __equipment_accounting(self, eq, count, add_flag=False):
        '''Учет оборудования на конкретном складе по партиям (конкретные модификации оборудования)
           передать :
                     eq - класс офисного оборудования
              или :  eq - строчный тип офисного оборудования (упрощ. при списании на баланс подразделения)
        '''
        count_val = self.__count_validation(count)
        if add_flag:  # =========== поступление ===========
            eq_curr = self.__equipments.get(eq)
            if eq_curr is None:
                self.__equipments[eq] = count_val
            else:
                self.__equipments[eq] = eq_curr + count_val
            return self.__equipments[eq]
        else:  # ================== списание ===============
            lambda_eq = lambda eq_curr, count_val: ([0, False] if (eq_curr is None) else (
                [(eq_curr - count_val), True] if eq_curr >= count_val else [eq_curr, False]))
            if isinstance(eq, str):
                for el in self.__equipments.keys():
                    eq_curr = self.__equipments.get(el)
                    tmp = lambda_eq(eq_curr, count_val)
                    if el.type == eq and tmp[1]:
                        self.__equipments[el] = tmp[0]
                        return tmp[0]
                return 0
            else:
                eq_curr = self.__equipments.get(eq)
                tmp = lambda_eq(eq_curr, count_val)
                if tmp[1]:
                    self.__equipments[eq] = tmp[0]
                return tmp[0]

    def __exist_eq_all(self, eq_type, count):
        '''Проверка возможности списания (наличия) данного типа оборудования по всем складам
           передать :
                    eq_type - строчный тип офисного оборудования
                    count   - количество запрашиваемого оборудования
        '''
        eq_type_val = self.__type_validation(eq_type, self.__quantity.keys())
        if StockRoom.__quantity[eq_type_val] >= self.__count_validation(count):
            return True
        return False

    def __exist_eq_curr(self, eq_type, count):
        '''Проверка возможности списания (наличия) данного типа оборудования по данному складу
           передать :
                    eq_type - строчный тип офисного оборудования
                    count   - количество запрашиваемого оборудования
        '''
        count_val = self.__count_validation(count)
        eq_type_val = self.__type_validation(eq_type, self.__quantity.keys())
        if isinstance(eq_type, str):
            for el in self.__equipments.keys():
                if (el.type == eq_type_val) and (self.__equipments.get(el) >= count_val):
                    return True
        return False

    def income(self, equipment, count=1):
        '''Приемка на склад нового оборудовния
           передать :
                     equipment - класс офисного оборудования
        '''
        eq_count = self.__equipment_accounting(equipment, count, True)
        eq_type = self.__type_validation(equipment, self.__quantity.keys())
        print(f"Принято на склад '{self.address}' : {count} ед. оборудования '{eq_type}'\n"
              f"Теперь на складе {eq_count} ед. оборудования {equipment}")
        print(f"Всего на складах {StockRoom.__quantity_accounting(eq_type, count, True)}  ед. "
              f"оборудования '{eq_type}'")

    def delivery(self, eq_type, count=1, subdivision="Main Office"):
        '''Передача оборудования в подразделения компании
           передать :
                     eq_type - строчный тип офисного оборудования
        '''
        if self.__exist_eq_curr(eq_type, count):
            eq_count = self.__equipment_accounting(eq_type, count)
            if self.__exist_eq_all(eq_type, count):
                q_count = StockRoom.__quantity_accounting(eq_type, count)
            else:
                q_count = 0
            print(
                f"В подразделение '{subdivision}' передано {count} ед. оборудования '{eq_type}' со склада '{self.address}\n"
                f"на складе '{self.address}' осталось {eq_count} ед. обоудования этого типа.\n"
                f"Всего на складах осталось {q_count} ед. обоудования этого типа")
        else:
            print(f"На складе '{self.address}' не осталось оборудования '{eq_type}'")
            if self.__exist_eq_all(eq_type, count):
                print(f"Запросите оборудование '{eq_type}' с другого склада")


class OfficeEquipment:
    def __init__(self, length, width, height, weight):
        if self.__eq_validation(length, width, height, weight):
            self.length = length
            self.width = width
            self.height = height
            self.weight = weight
            if self.type is None: self.type = "OfficeEquipment"
        else:
            self.type = "NoName"

    def __str__(self):
        type_str = self.type
        if not ((self.length is None) or (self.width is None) or (self.height is None) or (self.weight is None)):
            type_str += " (length:" + str(self.length) + " width:" + str(self.width) + \
                        " height:" + str(self.height) + " weight:" + str(self.weight) + ") "
        return type_str

    @staticmethod
    def __eq_validation(length, width, height, weight):
        flag = False
        if isinstance(length, int) and isinstance(width, int) and isinstance(height, int) and (
                isinstance(weight, int) or isinstance(weight, float)):
            flag = True
        return flag


class Printer(OfficeEquipment):
    def __init__(self, length, width, height, weight, type, color=False):
        self.type = "Printer"
        super().__init__(length, width, height, weight)
        if isinstance(type, str):
            self.type_f = self.type + type
        self.color = color


class Scanner(OfficeEquipment):
    def __init__(self, length, width, height, weight, color=False):
        self.type = "Scanner"
        super().__init__(length, width, height, weight)
        self.color = color


class Xerox(OfficeEquipment):
    def __init__(self, length, width, height, weight, mfu=False):
        self.type = "Xerox"
        super().__init__(length, width, height, weight)
        self.mfu = mfu


class Laptop(OfficeEquipment):
    def __init__(self, length, width, height, weight, screen):
        self.type = "Laptop"
        super().__init__(length, width, height, weight)
        self.screen = screen


stock1 = StockRoom("Moscow")
stock2 = StockRoom("Yaroslavl")

print("=" * 10, "Поступление оргтехники на склад : ", "=" * 25)
stock1.income(Printer(40, 40, 40, 35, "Laser", True), 4)
print("=" * 10)
stock1.income(Printer(33, 45, 20, 5, "Jet"), 2)
print("=" * 10)
stock2.income(Printer(40, 55, 22, 15, "Jet", True))
print("=" * 10)
stock1.income(Xerox(50, 55, 50, 40, True), 2)
print("=" * 10)
stock2.income(Scanner(25, 35, 10, 2, True), 3)
print("=" * 10)
stock1.income(Laptop(30, 20, 5, 1, 14))
print("=" * 10)

print()
print("=" * 10, "Передача оргтехники в подразделения компании : ", "=" * 13)
print()
stock1.delivery("Printer", 1, "Yaroslavl Office")
print()
stock2.delivery("Laptop", 1, "Yaroslavl Office")
print()
stock2.delivery("Scanner", 1, "Yaroslavl Office")
print()
stock1.delivery("Scanner", 1, "Moscow Office")

print()
print(stock1.inventory)
print(stock2.inventory)
