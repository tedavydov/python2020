my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# my_list = [300, 2, 12,  13, 123, 44, 1, 1, 5, 22, 8, 4, 97, 12, 57]

# mlist = [el for el in range(10, 20)]
# mlist = [el for el in my_list]
# print(f"сгенерирован список: {mlist}")

# new_list = [my_list[i] for i in range(len(my_list))]
# new_list = [my_list[i] for i in range(len(my_list)) if i != 0]
new_list = [my_list[i] for i in range(len(my_list)) if i != 0 and my_list[i] > my_list[i - 1]]

print(f"Исходный список: {my_list}")
print(f"Сгенерирован список: {new_list}")

# Непонятно почему то-же самое вчера не работало :
# похоже что то с набором текста и кодировками .. мистика ..

# и это не сработало :
new_list3 = [​my_list[i] for i in range(len(my_list)) if i != 0 and ​my_list[i] > ​my_list[i-1]]

# Это не сработало :
# new_list2 = [​el for el in my_list if my_list.index(el) != 0 and el > my_list[my_list.index(el) - 1]]
# new_list1 = [​el for el in my_list if my_list.index(el) != 0 and el > my_list[my_list.index(el) - 1]]

print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list3}")

