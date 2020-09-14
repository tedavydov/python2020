dict_of_months = {1 : "январь",2 : "февраль",3 : "март",4 : "апрель",5 : "май",6 : "июнь",7 : "июль",8 : "август",9 : "сентябрь",10 : "октябрь",11 : "ноябрь",12 : "декабрь"}
dict_of_seasons = {1 : "зима",2 : "весна",3 : "лето",4 : "осень"}
list_of_months = list(dict_of_months.values())
list_of_seasons = list(dict_of_seasons.values())
month_number = int(input("Введите номер месяца :  "))

season = 0
if month_number > 11:
    season = 1
    month_number = 12
elif month_number < 1:
    season = 1
    month_number = 1
elif month_number < 3:
    season = 1
elif month_number < 6:
    season = 2
elif month_number < 9:
    season = 3
else:
    season = 4

print(f"[список] Вы ввели месяц {list_of_months[month_number-1]}, это {list_of_seasons[season-1]} !")
print(f"[словарь] Вы ввели месяц {dict_of_months.get(month_number)}, это {dict_of_seasons.get(season)} !")
