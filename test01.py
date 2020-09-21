from functools import reduce

my_list2 = [el for el in range(10, 25, 2)]

# для тестирования :
# my_list2 = [el for el in range(100, 121, 2)]
# my_list1 = [el for el in range(100, 121) if el % 2 == 0]

def my_sum(prev_el, el):
    return prev_el * el

print(reduce(my_sum, my_list2))

print(my_list2)
print(10 * 12 * 14 * 16 * 18 * 20 * 22 * 24)

# print(my_list)
# print(my_list1)
# print(my_list2)
