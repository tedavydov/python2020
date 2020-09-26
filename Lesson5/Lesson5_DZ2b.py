import my_file as mfile

file_name = "text_5-2.txt"
try:
    string_count = 0
    words_count = 0
    for line in mfile.read(file_name):
        string_count += 1
        words_count_line = len(line.split())
        words_count = words_count + words_count_line
        print(f"строка {string_count} содержит {words_count_line} слов;")
    print(f"Файл {file_name} содержит {string_count} строк, и {words_count} слов.")
except:
    print('Ошибка обработки файла, программа завершена !')
