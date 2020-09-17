def my_func(result=0, *args):
    try:
        for x in args:
            result += x
    except:
        print('Вы ошиблись - нужно вводить числа !')
    return result


print("Здравствуйте ! Это программа суммирования чисел.\n"
      + "Для завершения программы введите 'q' ")
summ = 0
run_prog = True
while run_prog:
    in_list = input("Введите числа через пробел : ").split()
    def_list = []
    if in_list:
        try:
            for el in in_list:
                if el == 'q':
                    print('Завершение программы с подсчетом суммы')
                    run_prog = False
                    break
                else:
                    def_list.append(float(el))
            summ = my_func(summ, *def_list)
            print(summ)
        except:
            print('Вы ошиблись, повторите ввод  !')
    else:
        print('Хорошо больше не будем считать')
        run_prog = False

# print(summ)
