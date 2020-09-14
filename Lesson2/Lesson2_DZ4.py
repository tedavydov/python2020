input_string = input("Введите строку из нескольких слов, разделённых пробелами :  ")
input_list = input_string.split()

print("Спасибо, вот ваши слова по порядку :")
num = 0
for word in input_list:
    num += 1
    print(f"{num} : {word[:10]}")
