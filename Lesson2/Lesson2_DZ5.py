rating = [33, 12, 7]  # добавил стартовый рейтинг по условию задачи
# rating = []  # код работает и с пустым начальным рейтингом

num = 0
num_str = " "
while num_str:  # пока не введена пустая строка
    num_str = input("Сколько вы набрали очков ?  ")
    if num_str:
        num = int(num_str)
    else:
        print("Спасибо ! Вы хорошо играли !")
        break
    i = 0
    j = 0
    rating_len = len(rating)
    if rating_len < 1:  # если список (пока) пустой
        rating.append(num)  # вставим новый элемент в конец списка
    else:  # список уже не пустой
        for el in rating:  # получим индекс для вставки элемента
            if num <= el:
                j = i + 1
            i += 1
        rating.insert(j, num)  # вставим новый элемент по индексу

    # сформируем вывод списка с выделением места нового элемента
    print("Ваше \033[31m" + "место\033[0m " + "в рейтинге : [", end="")
    i = 0
    for el in rating:
        if i != j:
            print(f"{rating[i]}", end="")
        else:
            print("\033[31m" + f"{rating[j]}" + "\033[0m", end="")  # выделение цветом
            # print(f"({rating[j]})", end="") # выделение скобками
        if i < rating_len:
            print(", ", end="")
        else:
            print("", end="")
        i += 1
    print("]")

# print(rating)
