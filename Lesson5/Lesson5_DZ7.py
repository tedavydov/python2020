import json

firm_list = []
firm_tmp = {}
firm_summ = 0
firm_count = 0
try:
    src_file = open("text_5-7_src.txt", "r", encoding="utf-8")
    try:
        for line in src_file:
            firm_name, firm_type, debit, credit = line.split()
            firm = firm_name + " " + firm_type
            summ = float(debit) - float(credit)
            firm_tmp[firm] = summ
            if summ > 0:
                firm_count += 1
                firm_summ += summ
    except:
        print('Ошибка обработки файла, программа завершена !')
    finally:
        src_file.close()
        firm_list.append(firm_tmp)
        if firm_count:
            firm_summ = firm_summ / firm_count
            summation = dict(average_profit=firm_summ)
            firm_list.append(summation)
        print(firm_list)
except:
    print('Ошибка открытия файла')
try:
    with open("less_5-7_firm-summ.json", "w", encoding="utf-8") as firm_json_file:
        json.dump(firm_list, firm_json_file, ensure_ascii=False, indent=4)
except:
    print('Ошибка записи JSON файла')
