def new_fact(n):
    fact = 1
    for x in range(1, n + 1):
        fact = fact * x
        yield fact


start = int(input("Введите целое число для старта : "))
for el in new_fact(start):
    print(el, end=" ")
