def my_del(dig1, dig2):
    result = 0
    try:
        result = dig1 / dig2
    except ZeroDivisionError:
        print('Вы ошиблись делить на "0" нельзя !')
    return result

print("Здравствуйте ! Это программа деления двух чисел.\n"
      + "Для завершения программы введите 'q' ")
run_prog = True
while run_prog:
    in_list = input("Введите два числа через пробел : ").split()
    def_list = []
    try:
        for el in in_list:
            if el == 'q' or el == '':
                run_prog = False
            else:
                def_list.append(float(el))
        if len(def_list) == 2:
            print(my_del(def_list[0], def_list[1]))
        else:
            print('Вы ошиблись!\n Введите два числа, или символ "q" для выхода из программы !')
    except:
        print('Вы ошиблись. \n Нужно ввести два числа, или символ "q" для выхода из программы !')
else:  # run_prog == False
    print("Программа завершена")
