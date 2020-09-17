def st_func(x, y):
    res = 0
    exp = 0
    try:
        num = float(x)
        exp = int(y)
    except:
        print("Некорректные аргументы функции")
        return -1
    if num < 0:
        print("Первый аргумент должен быть действительным положительным числом")
    elif exp > 0:
        print("Второй аргумент должен быть отрицательным целым числом")
    else:
        res = num ** exp
    return res


def my_func(x, y):
    res = 1
    exp = 0
    try:
        num = float(x)
        exp = int(y)
    except:
        print("Некорректные аргументы функции")
        return -1
    if num < 0:
        print("Первый аргумент должен быть действительным положительным числом")
    elif exp > 0:
        print("Второй аргумент должен быть отрицательным целым числом")
    else:
        for i in range(abs(exp)):
            res = res * num
        res = 1 / res
    return res


print(my_func(100.4, 20.7))
print(my_func("wwa_", "waa__"))
print(st_func("wwa_", "waa__"))
print(st_func(100, 2))
print("=" * 50)

print(st_func(10, -2))
print(my_func(10, -2))
print("-" * 50)
print(st_func(1, -15))
print(my_func(1, -15))
print("-" * 50)
print(st_func(10, -55))
print(my_func(10, -55))
print("-" * 50)
print(st_func(10, -10))
print(my_func(10, -10))
