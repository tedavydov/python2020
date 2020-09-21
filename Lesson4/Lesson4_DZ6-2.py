from itertools import cycle

def_list = ["D", "f", "3", "G", "W"]

try:
    stop = 0
    tmp_list = list(input("Введите строку для старта : "))
    if tmp_list:
        for el in cycle(tmp_list):
            if stop > 50:
                break
            else:
                print(el, end="")
                stop += 1
    else:
        for el in cycle(def_list):
            if stop > 20:
                break
            else:
                print(el, end="")
                stop += 1
except:
    print("Вы ошиблись, программа завершена")
