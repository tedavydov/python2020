from itertools import count

try:
    for el in count(int(input("Введите целое число от 1 до 49 для старта : "))):
        if el > 50:
            print("Программа завершена")
            break
        else:
            print(el)
except:
    print("Вы ошиблись, программа завершена")
