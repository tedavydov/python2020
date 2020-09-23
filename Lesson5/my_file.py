def read(file_name):
    with open(file_name, "r", encoding="utf-8") as txt_file:
        try:
            for line in txt_file:
                yield line
        except:
            print(f'Ошибка чтения файла {file_name}, программа завершена !')


def write(new_str):
    file_name = new_str
    with open(file_name, "w", encoding="utf-8") as txt_file:
        # try:
        while new_str:
            new_str = yield
            if new_str:  # иначе ошибка StopIteration
                print(new_str, file=txt_file)
        # except:
        #     print(f'Ошибка записи файла {file_name}, программа завершена !')


def write_spl(new_str, *spl):
    file_name = new_str
    spl_new = str(spl[0])
    with open(file_name, "w", encoding="utf-8") as txt_file:
        while new_str:
            new_str = yield
            if new_str:
                if spl:
                    print(new_str, end=spl_new, file=txt_file)
                else:
                    print(new_str, file=txt_file)
