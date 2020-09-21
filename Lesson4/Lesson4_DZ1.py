from sys import argv


# path, w_time, w_rate, w_bonus = argv
def pay(msg, w_time, w_rate, w_bonus):
    print(f'{msg}: {int(w_time) * float(w_rate) + float(w_bonus)}')


while True:
    try:
        if len(argv) > 1:
            pay("Вы заработали", argv[1], argv[2], argv[3])
        else:
            inp_param = input("Введите через пробел выработку в часах, ставку в час и премию сотрудника:\n").split()
            pay("Заработок сотрудника составил", inp_param[0], inp_param[1], inp_param[2])
        break
    except:
        argv = []
        print('Повторите ввод параметров')
