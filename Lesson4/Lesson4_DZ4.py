my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# my_list = [2, 3, 2, 7, 7, 7, 23, 24, 25, 1, 44, 44, 3, 2, 10, 7, 3, 4, 11]

new_list = [el for el in my_list if my_list.count(el) == 1]

print(f"Исходный список: {my_list}")
print(f"Сгенерирован список: {new_list}")
