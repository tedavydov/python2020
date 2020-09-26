try:
    txt_file = open("text_5-2.txt", "r", encoding="utf-8")
    try:
        string_count = 0
        words_count = 0
        for line in txt_file:
            string_count += 1
            words_count_line = len(line.split())
            words_count = words_count + words_count_line
            print(f"строка {string_count} содержит {words_count_line} слов;")
        print(f"Файл {txt_file.name} содержит {string_count} строк, и {words_count} слов.")
    except:
        print('Ошибка чтения файла, программа завершена !')
    finally:
        txt_file.close()
except:
    print('Ошибка открытия файла')
