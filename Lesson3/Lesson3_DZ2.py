param_s = {1: "имя", 2: "фамилия", 3: "год рождения", 4: "город проживания", 5: "email", 6: "телефон"}


def in_param(user, **kwargs):
    """ Это функция учета характеристик пользователей
        здесь :
            user - словарь с характеристиками
            **kwargs - набор(распакованный словарь) характеристик в виде пар : ключ = значение
    """
    global param_s
    for el in kwargs.items():  # блок добавления параметров
        try:  # если ключ не числовой ( и при прочих ошибках ключа .. )
            tmp = param_s.values()
            if el[0] in tmp:  # параметр по значению в словаре
                ind = list(tmp).index(el[0]) + 1
                user[param_s.get(ind)] = el[1]
            elif int(el[0]) in param_s.keys():  # параметр по номеру ключа
                user[param_s.get(int(el[0]))] = el[1]
            else:  # добавить новый параметр c числовым ключем ?
                sel = input(f'Вы хотите добавить характеристику с номером {el[0]} ? y/n  ')
                if sel == "y":
                    user[param_s.setdefault(int(el[0]))] = el[1]
                else:
                    print(f'Характеристика {el[0]} не добавлена .. ')
        except:
            user[el[0]] = el[1]
            print(f'Мы добавили новую характеристику {el[0]} !')
            # print(f'Вы ошиблись при задании характеристики {el[0]}, увы мы не смогли ее добавить .. ')
    return user


print('Это программа учета характеристик для пользователей')
print(f'Вы можете выбрать характеристику из списка : \n{param_s},\n   '
      + 'или добавить новую характеристику (или введите символ "q" для выхода из программы)')
print("*" * 85)
user_tmp = {}
user_tmp["ник"] = input("Введите ник (короткое имя) пользователя : ")
params_set = {}
run_prog = True
while run_prog:
    in_list = input("Введите характеристику (можно номер) и её значение через пробел : ").split()
    if len(in_list) == 2:
        params_set[in_list[0]] = in_list[1]
    elif not in_list or in_list[0] == 'q':
        print("Программа завершена")
        run_prog = False
    else:  # введена НЕ пара (параметр, значение)
        print('Вы ошиблись c вводом параметра!')

print(in_param(user_tmp, **params_set))
# print("DEBUG : " + ("=" * 20))
# print(user_tmp)
# print(params_set)
