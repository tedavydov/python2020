try:
    txt_file = open("text_5-3.txt", "r", encoding="utf-8")
    try:
        persons_min = []
        persons_count = 0
        summ = 0
        limit = 20000
        for line in txt_file:
            persons_count += 1
            person_list = line.split()
            person_pay = float(person_list[1])
            summ += person_pay
            if person_pay < limit:
                persons_min.append(person_list)
        print(f"Средний оклад сотрудников перечисленных в {txt_file.name} "
              f"равен {summ / persons_count:.02f} руб.\n"
              f"При этом перечисленные ниже сотрудники имеют оклад менее {limit} руб. :")
        for el in persons_min:
            print(f"    {el[0]:<15} - оклад равен : {el[1]:>10} руб.")
    except:
        print('Ошибка чтения файла, программа завершена !')
    finally:
        txt_file.close()
except:
    print('Ошибка открытия файла')
