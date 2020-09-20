my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# my_list = [300, 2, 12,  13, 123, 44, 1, 1, 5, 22, 8, 4, 97, 12, 57]

new_list = [my_list[i] for i in range(len(my_list)) if i != 0 and my_list[i] > my_list[i - 1]]

print(f"Исходный список: {my_list}")
print(f"Сгенерирован список: {new_list}")
