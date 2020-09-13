type_list = ["bool", "int", "float", "str", "bin", "oct", "hex", "list"]
my_list = [False, 1, 2.5, "str", 0b1011000111001, 0o22, 0x1C, [1, 3]]
us_list = []

us_el = bool(input("Введите логическое значение True/False "))
us_list.append(us_el)

us_el = int(input("Введите целое десятичное число  "))
us_list.append(us_el)

us_el = float(input("Введите вещественое число  "))
us_list.append(us_el)

us_el = input("Введите строку  ")
us_list.append(us_el)

us_el = input("Введите двоичное число  ")
us_el = bin(int(us_el, 2))
# print(f"{type(us_el)}  {us_el}")
us_list.append(us_el)

us_el = input("Введите восмеричное число  ")
us_el = oct(int(us_el, 8))
# print(f"{type(us_el)}  {us_el}")
us_list.append(us_el)

us_el = input("Введите шестнадцатеричное число  ")
us_el = hex(int(us_el, 16))
# print(f"{type(us_el)}  {us_el}")
us_list.append(us_el)

input_list = input("Введите ряд значений, разделяя из пробелами :  ").split()
us_list.append(input_list)

# не получилось добавить кортеж в список ..
# us_list.append(input("Введите несколько значений через запятую"))

print("У нас есть эталонный список значений : ")
print("list = [False, 1, 2.5, 'str', 0b1011000111001, 0o22, 0x1C, [1, 3]]")
print(f"в памяти он сохранился как : {my_list}")

print("Сравните введенные вами значения с нашим списком : ")
for us in us_list:
    index = us_list.index(us)
    type_my = str(type(my_list[index]))
    type_us = str(type(us))
    print(f"{type_list[index]:<7}=>  {str(us):>15} is {type_us:>16}"
          f"      example: {str(my_list[index]):>10} is {type_my:>16}")

# РЕЗУЛЬТАТ :
#
# 1) Если задать список в программе
#   то числовые переменные
#   автоматом приводятся к десятичной системе счисления
#   т.е. типам    'int'  и   'float'
#   например переменные "bin", "oct", "hex"
#   заданные как :    0b1011000111001, 0o22, 0x1C
#   приводятся к типу int
#
# 2) Если задать переменные преобразованием
#   из переменной типа  <class 'int'>
#   методами  "bin", "oct", "hex"
#   то получим строку - переменную типа <class 'str'>
#
