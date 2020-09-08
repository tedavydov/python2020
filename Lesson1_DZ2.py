user_secunds = input("Введите время в секундах ")

sec = int(user_secunds)
hh = sec // 3600
mm = (sec % 3600) // 60
ss = (sec % 3600) % 60

if hh < 10:
    hh = f"0{str(hh)}"
if mm < 10:
    mm = f"0{str(mm)}"
if ss < 10:
    ss = f"0{str(ss)}"

print (f"Вы ввели : {hh}:{mm}:{ss}")

