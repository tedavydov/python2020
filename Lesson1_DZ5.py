vyr = float(input("Введите значение выручки фирмы "))
izd = float(input("Введите значение издержек фирмы "))

rent = 1
rent_str = ""
result = ""
if vyr > izd:
    result = "прибыль"
    rent = (vyr - izd) / vyr
    rent_str = f"рентабельность равна {rent:.4f}"
elif vyr < izd:
    result = "убыток"
else:
    result = "хм .. а не видно пока результатов - товарищи !"

print(f"Результат работы вашей фирмы : {result}, а {rent_str}")

if rent != 1:
    sotr_count = int(input("А введите-ка количество сотрудников вашей фирмы "))
    if sotr_count <= 0:
        print("Да вы никак обнуть нас хотите ?")
    else:
        print(f"А ведь на каждого сотрудника вашей фирмы приходится : {((vyr - izd) / sotr_count):.0f} рублей прибыли !")

