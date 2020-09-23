import my_file as mfile


def fu(xx):
    tmp = []
    for x in (el for el in range(1, xx, 3)):
        yield x


file_name = "text_5-5b_nums.txt"
file_name0 = "text_5-5_nums.txt"
try:
    try:
        gen_file = mfile.write_spl(file_name, " ")  # ссылка на генератор
        # gen_file = mfile.write(file_name)  # ссылка на генератор = переделал метод
        next(gen_file)  # инициализация генератора
        for el in fu(20):
            gen_file.send(f'{el}')
    except:
        print('Ошибка генерации файла')
    finally:  # нужно чтобы прекратить генерацию и освободить файл для чтения
        gen_file.send("")  # ошибка StopIteration
except:
    print('генерация файла')  # заглушка == ошибка StopIteration

try:
    # with open(file_name) as num_file:
    summ = 0
    # for line in num_file:
    for line in mfile.read(file_name):
        tmp_list = map(int, line.split())
        for num in tmp_list:
            summ += num
    print(summ)
except:
    print('Ошибка обработки файла, программа завершена !')
