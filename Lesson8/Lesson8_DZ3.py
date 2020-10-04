class MyNumException(Exception):
    '''Наше исключение будет сообщать что введены не числа ..'''

    def __init__(self, err):
        self.err = err


in_str = " "
in_nums = []
res_nums = []
while in_str:
    in_str = input("введите числа, разделяя их пробелами ('q' - выход) : ")
    if in_str == "q":
        print("ввод завершен")
        break
    in_list = in_str.split()
    in_nums.append(in_list)
    try:
        for el in in_list:
            try:
                res_nums.append(float(el))
            except ValueError:  # заменим системное исключение своим
                raise MyNumException(f"{el} - это не число !")
    except MyNumException as e:  # а потом (возможно в вызывающем коде) выведем свое исключение вместо системного
        print(e)

print()
print(f"вы ввели = {in_nums}")
print()
print(f"результат = {res_nums}")
