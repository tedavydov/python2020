rus_list = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять"]
try:
    src_file = open("text_5-4_source.txt", "r", encoding="utf-8")
    res_file = open("text_5-4_result.txt", "w", encoding="utf-8")
    try:
        for line in src_file:
            text, spl, num = line.split()
            print(f"{rus_list[int(num) - 1]:<10} {spl} {num:>10}", file=res_file)
    except:
        print('Ошибка чтения файла, программа завершена !')
    finally:
        src_file.close()
        res_file.close()
except:
    print('Ошибка открытия файла')
