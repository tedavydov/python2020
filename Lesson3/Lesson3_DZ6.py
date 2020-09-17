def int_func(*us_str):
    tmp_list = []
    try:
        for el in us_str:
            tmp_str = str(el)
            flag_lat = True
            for x in tmp_str:
                # if ord(tmp_str[0]) > 128:
                if ord(x) > 128:
                    flag_lat = False
            if flag_lat:
                tmp_str = tmp_str.title()
            else:
                print(f"Используйте пожалуйста для слова {tmp_str} латинские буквы в нижнем регистре !")
            tmp_list.append(tmp_str)
    except:
        print("Ошибка ввода !")
    return tmp_list


# print("ВНИМАНИЕ :Используйте пожалуйста латинские буквы в нижнем регистре !")
run_prog = True
while run_prog:
    in_list = input("Введите слова через пробел : ").split()
    res_list = []
    if in_list:
        res_list = int_func(*in_list)
        for el in in_list:
            if el == 'q':
                print('Завершение программы')
                run_prog = False
                break
        print(str(res_list).strip("[]',").replace("', '"," "))
    else:
        print('Всего хорошего !')
        run_prog = False
