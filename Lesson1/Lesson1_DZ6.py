start = int(input("Сколько пробежал спортсмен в первый день ? "))
stop = int(input("А сколько он хотел бы пробежать ? "))

result = start
days = 1
while result < stop:
    result = result * 1.1
    days += 1

print(f"А ведь ваш спортсмен достигнет желаемого результата на {days} день !")
