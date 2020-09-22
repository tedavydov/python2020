try:
    txt_file = open("text_5-1.txt", "w", encoding="utf-8")
    try:
        print("Введенный вами текст будет записан в файл\nНачните ввод текста :\n")
        input_flag = True
        while input_flag:
            in_str = input()
            if in_str:
                print(in_str, file=txt_file)
            else:
                print('Текст записан в файл text_5-1.txt')
                input_flag = False
    except:
        print('Ошибка записи в файл, программа завершена !')
    finally:
        txt_file.close()
except:
    print('Ошибка открытия файла на запись')
