input_string = input("Введите ряд значений, разделяя из пробелами :  ")
input_list = input_string.split()
print("Теперь сравните два получившихся списка :")
print(input_list)

list_len = len(input_list)
for i in range(list_len):
    if i < (list_len - 1):
        if (i % 2) == 0:
            s1 = input_list[i+1]
            input_list.pop(i+1)
            input_list.insert(i,s1)
print(input_list)
