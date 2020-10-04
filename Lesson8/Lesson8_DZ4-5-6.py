class StockRoom:
    def __init__(self, x):
        self.x = x


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
