temp_str = "строка для проверки"
temp_int = 7
temp_usr = input("Угадайте что я написал ! Введите что-нибудь .. ")
if temp_usr == temp_str:
    print("УРА ! Вы угадали строку : ", temp_str)
elif temp_usr == temp_int:
    print("Вы угадали число : ", temp_int)
else:
    print("Вы не угадали.")

