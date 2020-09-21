from functools import reduce

my_list = [el for el in range(100, 1001, 2)]


def my_multi(prev_el, el):
    return prev_el * el


print(reduce(my_multi, my_list))
