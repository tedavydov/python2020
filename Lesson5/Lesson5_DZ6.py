less_dict = {}
try:
    src_file = open("text_5-6_rus.txt", "r", encoding="utf-8")
    # src_file = open("text_5-6_src.txt", "r", encoding="utf-8")
    try:
        for line in src_file:
            summ = 0
            lesson, hours = line.split(":")
            hours_list = hours.split()
            for el in hours_list:
                if el != "-":
                    summ += int(el.split("(")[0])
            less_dict[lesson] = summ
    except:
        print('Ошибка обработки файла, программа завершена !')
    finally:
        src_file.close()
        print(less_dict)
except:
    print('Ошибка открытия файла')

