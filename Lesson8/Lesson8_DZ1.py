class Data:

    def __init__(self, data):
        if data and isinstance(data, str):
            self.__data_s = data

            # думаю что конвертация и валидация должны проводится сразу при создании обьекта
            # --------------------------------------------------------
            # так метод класса не получит данные инициализации объекта
            # self.__convert_to_num()
            # --------------------------------------------------------
            # метод класса должен получить данные инициализации объекта
            self.__convert_to_num(self)
            self.__date_validation(self)

        else:
            self.__data_s = ""
            print(f"ERROR: DATA is not a string ({str(data)})")

    def __str__(self):
        if self.__data_s:
            try:
                if self.__y and self.__m and self.__d:
                    return f"Date: {self.__y}/{self.__m}/{self.__d}"
                else:
                    return f"Date string: {str(self.__data_s)}"
            except:
                return f"Obj ERROR: wrong date format {str(self.__data_s)}"
        else:
            return "Obj ERROR: date not set"

    @classmethod
    def __convert_to_num(cls, obj):
        if obj.__data_s:
            try:
                if obj.__data_s.find(".") >= 0:
                    tmp = map(int, obj.__data_s.split("."))
                elif obj.__data_s.find("/") >= 0:
                    tmp = map(int, obj.__data_s.split("/"))
                elif obj.__data_s.find("-") >= 0:
                    tmp = map(int, obj.__data_s.split("-"))
                else:
                    tmp = map(int, obj.__data_s.split())
                obj.__y, obj.__m, obj.__d = tmp
            except:
                print(f"CONVERT ERROR: wrong date format ({str(obj.__data_s)})")
        else:
            print("CONVERT ERROR: date not set")

    @staticmethod
    def __date_validation(self_obj):
        try:
            if self_obj.__y:
                if self_obj.__y < 1900: self_obj.__y = 1900
                if self_obj.__y > 2020: self_obj.__y = 2020
                print(f"verified year = ({str(self_obj.__y)})")
            else:
                self_obj.__y = 1900
                print("VALIDATION ERROR: empty year !")
            if self_obj.__m:
                if self_obj.__m < 1: self_obj.__m = 1
                if self_obj.__m > 12: self_obj.__m = 12
                print(f"verified month = ({str(self_obj.__m)})")
            else:
                self_obj.__m = 1
                print("VALIDATION ERROR: empty month !")
            if self_obj.__d:
                if self_obj.__d < 1: self_obj.__d = 1
                if self_obj.__m in [1, 3, 5, 7, 8, 10, 12] and self_obj.__d > 31:
                    self_obj.__d = 31
                elif self_obj.__m == 2 and not (self_obj.__y / 4) and self_obj.__d > 29:
                    self_obj.__d = 29
                elif self_obj.__m == 2 and (self_obj.__y / 4) and self_obj.__d > 28:
                    self_obj.__d = 28
                elif self_obj.__d > 30:
                    self_obj.__d = 30
                print(f"verified day = ({str(self_obj.__d)})")
            else:
                self_obj.__d = 1
                print("VALIDATION ERROR: empty day !")
        except:
            print(f"VALIDATION ERROR: wrong date ({self_obj.__data_s})")


print("=" * 10, "зададим 1-ю дату (23)", "=" * 25)
date_1 = Data(23)
print("=" * 10, "зададим 2-ю дату (23/12/2021)", "=" * 25)
date_2 = Data("23/12/2021")
print("=" * 10, "зададим 3-ю дату (2020.2.0)", "=" * 25)
date_3 = Data("2020.2.0")
print("=" * 10, "зададим 4-ю дату (1020-09-31)", "=" * 25)
date_4 = Data("1020-09-31")
print("=" * 10, "зададим 5-ю дату (2001/13/05)", "=" * 25)
date_5 = Data("2001/13/05")

print()
print("=" * 10, "проверим что же мы насоздавали", "=" * 25)
print(f"1: {date_1}\n2: {date_2}\n3: {date_3}\n4: {date_4}\n5: {date_5}")
