def my_func(x1, x2, x3):
    tmp_tup = (x1, x2, x3)
    is_dec = True
    sum_x = 0
    con_x = ""
    min = x1
    for x in tmp_tup[1:]:
        if x < min:
            min = x
    for x in tmp_tup:
        if x != min:
            try:
                sum_x = sum_x + float(x)
            except:
                is_dec = False
                con_x = con_x + x
    if is_dec:
        return sum_x
    else:
        return con_x

print(my_func(100.4, 20.7, 50))
print(my_func("wwa_", "waa__", "wbb"))
