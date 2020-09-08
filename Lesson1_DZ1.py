temp_str = "стр"
temp_int = 7
temp_usr = input("Угадайте что я написал ! Введите что-нибудь .. ")
if temp_usr == temp_str:
    print("УРА ! Вы угадали строку : ", temp_str)
    # temp_int2 = int(temp_usr)
    # print("int(temp_usr) : ", type(int(temp_usr))) # ValueError: invalid literal for int() ..
    # print ("temp_int : ", type(temp_int))
    # print("temp_str : ", type(temp_str))
    # print("temp_usr : ", type(temp_usr))
# elif int(temp_usr) == temp_int:  # ValueError: invalid literal for int() ..
#     print("Вы угадали число : ", temp_int)
else:
    print("Вы не угадали.")

