rating = [33, 12, 7]  # добавил стартовый рейтинг по условию задачи
# rating = []  # код работает и с пустым начальным рейтингом

num = 0
num_str = " "
while num_str:  # пока не введена пустая строка
    num_str = input("Сколько вы набрали очков ?  ")
    try:
        if num_str:
            num = int(num_str)
        else:
            print("Спасибо ! Вы хорошо играли !")
            break
    except:
        print("Вы ввели не целое число ! Игра окончена !")
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

    # ВЫВОД В F-СТРОКЕ
    # сформируем вывод списка с выделением места нового элемента
    # ( новый вариант с f-строкой и слайсом )
    if j == 0:
        print("Ваше \033[31m" + "место\033[0m " + "в рейтинге : ["
              + "\033[31m" + f"{rating[j]}" + "\033[0m"
              + f", {str(rating[1:]).strip('[]')}]")
        # print(f"DEBUG:  j == {j} (0)")
    elif j == rating_len:
        print("Ваше \033[31m" + "место\033[0m " + "в рейтинге : ["
              + f"{str(rating[:rating_len]).strip('[]')}, "
              + "\033[31m" + f"{rating[j]}" + "\033[0m]")
        # print(f"DEBUG: j == {j} (rating_len == {rating_len})")
    else:
        print("Ваше \033[31m" + "место\033[0m " + "в рейтинге : ["
              + f"{str(rating[:j]).strip('[]')}, "
              + "\033[31m" + f"{rating[j]}" + "\033[0m"
              + f", {str(rating[j + 1:]).strip('[]')}]")
    #     print(f"DEBUG: j == {j} in {rating_len}")
    #     print(str(rating[:j]))
    #     print(str(rating[j + 1:]))
    #     print("=" * 16)
    # print(f"DEBUG: rating == {rating}")
    # print("=" * 20)

    # # ВЫВОД В ЦИКЛЕ ПЕРЕБОРА
    # # сформируем вывод списка с выделением места нового элемента
    # # ( старый вариант с циклом перебора индексов .. )
    # print("Ваше \033[31m" + "место\033[0m " + "в рейтинге : [", end="")
    # i = 0
    # for el in rating:
    #     if i != j:
    #         print(f"{rating[i]}", end="")
    #     else:
    #         print("\033[31m" + f"{rating[j]}" + "\033[0m", end="")  # выделение цветом
    #         # print(f"({rating[j]})", end="") # выделение скобками
    #     if i < rating_len:
    #         print(", ", end="")
    #     else:
    #         print("", end="")
    #     i += 1
    # # print("]")
    # # print(f"DEBUG: rating == {rating}  j == {j} (rating_len == {rating_len})")
    # # print("=" * 20)
