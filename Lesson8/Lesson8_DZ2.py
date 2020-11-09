class MyZeroException(Exception):
    def __init__(self, err):
        self.err = err


del_inp = input("Мы разделим 55 на целое число, которое вы введете : ")

try:
    inp_num = int(del_inp)
    if inp_num == 0:
        raise MyZeroException("на ноль делить нельзя !")
    else:
        print(f"результат = {55 / inp_num:.02f}")
except (ValueError, MyZeroException) as e:
    print(e)

