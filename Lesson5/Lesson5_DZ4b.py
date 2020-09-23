import my_file as mfile

rus_list = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять"]

file_source_name = "text_5-4_source.txt"
file_result_name = "text_5-4b_result.txt"
wr_file = mfile.write(file_result_name)  # ссылка на генератор
next(wr_file)  # инициализация генератора
try:
    for line in mfile.read(file_source_name):
        text, spl, num = line.split()
        wr_file.send(f"{rus_list[int(num) - 1]:<10} {spl} {num:>10}")
        # print(f"{rus_list[int(num) - 1]:<10} {spl} {num:>10}")  # тест
except:
    print('Ошибка обработки файла, программа завершена !')
# finally:
#     wr_file.send("")  # ошибка StopIteration ( НО ! файл создал, добавил пустую 12-ю строку )
