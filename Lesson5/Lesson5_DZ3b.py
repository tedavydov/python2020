import my_file as mfile

file_name = "text_5-3.txt"
try:
    persons_min = []
    persons_count = 0
    summ = 0
    limit = 20000
    for line in mfile.read(file_name):
        persons_count += 1
        person_list = line.split()
        person_pay = float(person_list[1])
        summ += person_pay
        if person_pay < limit:
            persons_min.append(person_list)
    print(f"Средний оклад сотрудников перечисленных в {file_name} "
          f"равен {summ / persons_count:.02f} руб.\n"
          f"При этом перечисленные ниже сотрудники имеют оклад менее {limit} руб. :")
    for el in persons_min:
        print(f"    {el[0]:<15} - оклад равен : {el[1]:>10} руб.")
except:
    print('Ошибка обработки файла, программа завершена !')
