import random


# Чтение данных из файла
def file_read(file):
    with open(file, "r", encoding="utf-8") as txt_file:
        try:
            for line in txt_file:
                yield line
        except:
            print(f'Ошибка чтения файла {file}, программа завершена !')


# Запись данных в файл
def file_write_spl(new_str, *spl):
    f_name = new_str
    spl_new = str(spl[0])
    with open(f_name, "w", encoding="utf-8") as txt_file:
        while new_str:
            new_str = yield
            if new_str:
                if spl:
                    print(new_str, end=spl_new, file=txt_file)
                else:
                    print(new_str, file=txt_file)


def gen_tab_list(file_input):
    # добавить проверку одинаковой размерности строк
    table_list = []
    if isinstance(file_input, str):
        try:
            for line in file_read(file_input):
                xline = line.strip('\ufeff').strip('\n').strip(" ")
                if xline != "":
                    tmpx = []
                    tmp = xline.split(',')
                    for x in tmp:
                        tmpx.append(x.strip(" "))
                    table_list.append(tmpx)
            # print(table_list)
            return table_list
        except:
            print(f'gen_tab_list({file_input}) : Ошибка обработки шаблона списка !')
    else:
        print(f'gen_tab_list({file_input}) : ERROR - передайте имя файла - как строку !')


def gen_templ(file_input):
    # без проверки одинаковой размерности строк
    # добавляет в начале списка служебные поля
    # [0] - id
    # [1] - sn
    # [2] - host
    #     - если найдено поле с одним из этих заголовков,
    #     то в соответствующую строку помещается его индекс,
    #     иначе остается пустая строка !!!
    # При дальнейше доработке скрипта,
    # нужно также изменять связанные функции использующие этот тип списка !!!!
    table_list = []
    null_flag = True
    if isinstance(file_input, str):
        try:
            for line in file_read(file_input):
                xline = line.strip('\ufeff').strip('\n').strip(" ")
                if xline != "":
                    tmpx = []
                    tmp = xline.split(',')
                    for x in tmp:
                        tmpx.append(x.strip(" "))
                    if null_flag:  # добавляет в начале списка служебные поля
                        x0 = ''
                        x1 = ''
                        x2 = ''
                        for ex in range(len(tmpx)):
                            if tmpx[ex] == 'id':
                                x0 = ex
                            elif tmpx[ex] == 'sn':
                                x1 = ex
                            elif tmpx[ex] == 'host':
                                x2 = ex
                        table_list.append(x0)  # == table_list[0]
                        table_list.append(x1)  # == table_list[1]
                        table_list.append(x2)  # == table_list[2]
                        null_flag = False
                        # служебные поля - добавлены
                        # заголовок таблицы будет в строке table_list[3]
                        #  данные - со строки table_list[4] ..
                    table_list.append(tmpx)
            # print(table_list)
            return table_list
        except:
            print(f'gen_templ({file_input}) : Ошибка обработки шаблона !')
    else:
        print(f'gen_templ({file_input}) : ERROR - передайте имя файла - как строку !')


def gen_tab_dict(file_input, key=0, val=1):
    max_idx = 1
    if key != 0 or val != 1:
        max_idx = max(key, val)
    table_dict = {}
    if isinstance(file_input, str):
        try:
            line_num = 0
            for line in file_read(file_input):
                line_num += 1
                tmp = line.strip('\ufeff').strip('\n').strip(" ").split(',')
                if len(tmp) >= max_idx + 1:
                    table_dict[tmp[key].strip(" ")] = tmp[val].strip(" ")
                else:
                    print(f'gen_tab_dict({file_input}) : Ошибка в [{line_num}] строке файла'
                          f' - мало параметров для элемента словаря !')
            return table_dict
        except:
            print(f'gen_tab_dict({file_input}) : Ошибка обработки шаблона словаря в строке ({line_num}) !')
    else:
        print(f'gen_tab_dict({file_input}) : ERROR - передайте имя файла - как строку !')


def table_write(table_name, input, output):
    table_list = []
    if isinstance(input, str):
        # Чтение данных для таблицы
        table_list = gen_tab_list(input)
    elif isinstance(input, list):
        table_list = input
    else:
        print(f'table_write ERROR ! ошибка входных данных : input = {input}')

    # запись SQL-кода наполнения таблицы в файл
    try:
        if isinstance(output, str):
            gen_file = file_write_spl(output, '\n')  # ссылка на генератор
            try:
                next(gen_file)  # инициализация генератора
                # заполнение таблицы
                end = len(table_list)
                for i in range(end):
                    if (i != 0):
                        tmp_str = '('
                        end_next = len(table_list[i])
                        for j in range(end_next):
                            tmp_str += "'"
                            tmp_str += table_list[i][j]
                            if j != (end_next - 1):
                                tmp_str += "', "
                            else:
                                tmp_str += "'"
                        if i != (end - 1):
                            # все строки кроме последней
                            tmp_str += '),'
                        else:  # последняя строка
                            tmp_str += ');'
                        gen_file.send(tmp_str)
                    else:
                        # заголовок запроса (поля таблицы)
                        tmp_str = f'INSERT INTO {table_name} ('
                        end_next = len(table_list[0])
                        for j in range(end_next):
                            tmp_str += "`"
                            tmp_str += table_list[0][j]
                            if j != (end_next - 1):
                                tmp_str += "`, "
                            else:
                                tmp_str += "`"
                        tmp_str += ') VALUES '
                        gen_file.send(tmp_str)
            except:
                print(f'table_write: Ошибка генерации SQL-кода для {table_name}')
            finally:  # нужно чтобы прекратить генерацию и освободить файл для чтения
                gen_file.send("")  # ошибка StopIteration
        else:
            return table_list
    except:
        print(f'table_write: завершена генерация и запись SQL-кода '
              f'для {table_name}')  # заглушка == ошибка StopIteration


def genegate_sn(sn_templ):
    dec = '1234567890'  # len(dec) =  10
    chars_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # len(chars_up) =  26
    tmp_str = ''
    if isinstance(sn_templ, str):
        for ch in sn_templ:
            if ch == '0':
                tmp_str += dec[random.randint(0, len(dec) - 1)]
            elif ch == 'o':
                tmp_str += chars_up[random.randint(0, len(chars_up) - 1)]
            else:
                tmp_str += ch
        return tmp_str
    elif isinstance(sn_templ, list):
        return sn_templ[random.randint(0, len(sn_templ) - 1)]


def genegate_host(host_templ):
    chars_def = '-_abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'  # len(chars_all) =  63
    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'  # len(chars) =  51
    dec = '1234567890'  # len(dec) =  10
    # chars_full = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'  # len(chars_full) =  74
    # chars_all = '-_@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'  # len(chars_all) =  64
    # chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'  # len(chars) =  51
    # chars_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # len(chars_up) =  26
    tmp_str = ''
    if isinstance(host_templ, str):
        for ch in host_templ:
            if ch == '!':
                tmp_str += dec[random.randint(0, len(dec) - 1)]
            elif ch == '?':
                tmp_str += chars[random.randint(0, len(chars) - 1)]
            elif ch == '*':
                for x in range(random.randint(1, 11)):
                    tmp_str += chars_def[random.randint(0, len(chars_def) - 1)]
            else:
                tmp_str += ch
        return tmp_str
    elif isinstance(host_templ, list):
        return host_templ[random.randint(0, len(host_templ) - 1)]


def genegate_table(table_templ_file, row_count=10):
    # считывание шаблона таблицы из файла правил для генерации
    table_templ = gen_tab_list(table_templ_file)
    # =====================================================================
    # блок инициализации переменных для корректной области видимости в коде
    table = []
    table_gen = []
    table_src = []
    gen_type = ''
    dct = {}
    lst = []
    # =====================================================================
    if (len(table_templ) >= 3):
        # копирование 'шапки' в целевую таблицу == table[0]
        table.append(table_templ[0])
        # копирование правил генерации таблицы
        table_gen = table_templ[1]  # список видов генерации
        table_src = table_templ[2]  # список шаблонов генерации
    if (len(table_templ) >= 5):
        if table_templ[3][0] == 'dict':
            dct = gen_tab_dict(table_templ[4][0])
            gen_type = 'dict'
        elif table_templ[3][0] == 'list':
            lst = gen_templ(table_templ[4][0])
            gen_type = 'list'
            # ==================================
            # --- ДОПОЛНИТЕЛЬНО ----------------
            # для (нереальной :-) ситуации когда
            # в четвертой строке файла ***_pattern.txt
            # задан список 'list' ,
            # НО в третьей строке файла ***_pattern.txt
            # оставили метки 'dict' (ну случаи бывают разные :-)
            dict_idx = 0
            dict_idx_list = []
            for el in table_src:  # поиск 'dict'
                if el == 'dict':
                    dict_idx_list.append(dict_idx)
                dict_idx += 1
            if len(dict_idx_list) >= 2:
                dct = gen_tab_dict(table_templ[4][0])
            # см.выше ..
            # table_src = table_templ[2]  # список шаблонов генерации
            # +++ желательно реализовать через str.find('dict')
            # dict(key):dict(val) - задание номеров полей в  ***_pattern.txt
            # это позволит реализовать более сложные варианты генерации таблиц ..
            # ==================================
    clm_count = len(table[0])
    rand_el = 0
    if (len(table_gen) == clm_count) and (len(table_src) == clm_count):
        for row in range(1, row_count + 1):
            row_tmp = []
            if gen_type == 'dict':
                # для каждой строки выбираем рандомный элемент шаблонного словаря
                rand_el = random.randint(1, len(dct) - 1)
            elif gen_type == 'list':
                # print(f'len(lst) = {len(lst)}')
                # print(f'len(dct) = {len(dct)}')
                rand_el = random.randint(4, len(lst) - 4)
            for clm in range(clm_count):
                tmp_cl = 'NULL'  # по умолч. = пустое поле в строке целевой таблицы
                src = table_src[clm].split('/')
                cnt = len(src)  # число строковых элементов шаблона
                if cnt == 1:  # генерация диапазона из заданного файла (строка src[0] = имя файла)
                    # =========================================================================
                    # генерация ID-шников (для внешних ключей)
                    if table_gen[clm] == "gen_id":
                        # =====================================================================
                        # генерация ID-шников по заданному словарю
                        # выбираются айдишники из списка ключей словаря,
                        # словарь рекомендуется задавать в файле ***_templates.txt
                        # --- ВНИМАНИЕ !!! ---------------------------------------
                        # словарь позволяет быстро найти соответствие айдишника
                        # и связанного с ним поля ,
                        # НО связать можно только одно поле !!!
                        # поэтому в третьей строке файла ***_pattern.txt
                        # можно задать только две метки 'dict'
                        # для айдишника и для связанного поля !!!!
                        if table_src[clm] == 'dict':
                            tmp_cl = list(dct.keys())[rand_el]
                        # =====================================================================
                        # генерация ID-шников по заданному списку
                        # выбираются айдишники из нулевой колонки шаблонного списка,
                        # список рекомендуется задавать в файле ***_templates.txt
                        # --- !!! -----------------------------------------------
                        # список позволяет связать с айдишником есколько полей !
                        elif table_src[clm] == 'list':
                            if lst[0] != '':
                                tmp_cl = lst[rand_el][lst[0]]
                            else:  # если по ошибке или намеренно задан пустой текст
                                tmp_cl = rand_el
                        # =====================================================================
                        # генерация ID-шников по заданному шаблону
                        # шаблон задается в соответствующем поле
                        # третьей строки файла ***_pattern.txt
                        # --- ВНИМАНИЕ !!! -----------------------
                        # при неправильно заданном шаблоне
                        # можно нарушить связность внешних ключей
                        else:
                            tmp_cl = genegate_host(table_src[clm])
                    # =========================================================================
                    # генерация серийных номеров оборудования
                    elif table_gen[clm] == "gen_sn":
                        # =====================================================================
                        # см.выше пояснения .. (генерация ID-шников по заданному словарю)
                        if table_src[clm] == 'dict':
                            # print(rand_el)
                            # print(dct.values())
                            # print(list(dct.values())[rand_el])
                            tmp_cl = genegate_sn(list(dct.values())[rand_el])
                        # =====================================================================
                        # см.выше пояснения .. (генерация ID-шников по заданному списку)
                        elif table_src[clm] == 'list':
                            if lst[1] != '':
                                tmp_cl = lst[rand_el][lst[1]]
                            else:  # если по ошибке или намеренно задан пустой текст
                                tmp_cl = rand_el
                        # =====================================================================
                        # генерация серийников по заданному шаблону
                        # шаблон задается в соответствующем поле
                        # третьей строки файла ***_pattern.txt
                        else:
                            tmp_cl = genegate_host(table_src[clm])
                    # =========================================================================
                    # генерация сетевых имен (хостов) оборудования
                    # также по этой схеме можно генерировать другой рандомный текст(словарь)
                    elif table_gen[clm] == "gen_ht":
                        # =====================================================================
                        # см.выше пояснения .. (генерация ID-шников по заданному словарю)
                        if table_src[clm] == 'dict':
                            tmp_cl = genegate_sn(list(dct.values())[rand_el])
                        # =====================================================================
                        # см.выше пояснения .. (генерация ID-шников по заданному списку)
                        elif table_src[clm] == 'list':
                            if lst[2] != '':
                                tmp_cl = lst[rand_el][lst[2]]
                            else:  # если по ошибке или намеренно задан пустой текст
                                tmp_cl = genegate_host(table_src[clm])
                        # =====================================================================
                        # генерация хостов по заданному шаблону
                        # шаблон задается в соответствующем поле
                        # третьей строки файла ***_pattern.txt
                        else:
                            tmp_cl = genegate_host(table_src[clm])
                # =========================================================================
                # генерация случайного числа в заданных рамках (от/до)
                # диапазон задается в соответствующем поле
                # третьей строки файла ***_pattern.txt
                elif cnt == 2 and table_gen[clm] != "gen_ht":
                    tmp_cl = random.randint(int(src[0]), int(src[1]))
                # =========================================================================
                else:  # генерация диапазона из заданного списка (разделитель '/')
                    # шаблон списка задается в соответствующем поле
                    # третьей строки файла ***_pattern.txt
                    tmp_cl = src[random.randint(0, cnt - 1)]
                row_tmp.append(tmp_cl)  # добавляем сгенерированное значение в строку
            if len(row_tmp) == len(table[0]):  # добавляем сгенерированную строку
                table.append(row_tmp)
    return table


# ================================================
# Чтение шаблонов таблиц и генерация списка данных
# ================================================
# ПОЯСНЕНИЯ :
# Предусмотренно несколько вариантов задания шаблонов для генерации таблиц
# 1) Общий ПАТТЕРН таблицы :
#   задается в файле table-name_pattern.txt
#   позволяет перечислить простые варианты генерации
#   для каждого поля таблицы через запятую
# НАПРИМЕР :
#   aa/bb/cc - строковый шаблон - значения разделены слэшем '/'
#
#   01/02/03 - числовой шаблон - значения разделены слэшем '/'
#
#   01/55 - шаблон от/до - значения генерируются в заданном диапазоне
#
#   FOC0000o00o - шаблон серийного номера
#              (0 - заменяется на цифру, o - заменяется на латинский символ, остальное без изменений ..)
#
#   host??*123!!!!0* - шаблон сетевого имени
#              (! - заменяется на цифру ,
#               ? - заменяется на латинский символ ,
#               * - заменяется на группу латинских символов и цифр включая '-' и '_' ,
#                   остальное без изменений .. )
#
# 2) Дополнительный набор ШАБЛОНОВ таблицы :
#   задается в файле table-name_templates.txt
#   позволяет перечислить сложные варианты генерации
#   для каждого поля таблицы может быть задан список шаблонов
# НАПРИМЕР :
#   A) Если нужен список только для одного поля (SN) то лучше использовать словарь.
#     Тогда в четвертой строке записывается 'dict' ,
#     а в пятой строке - имя файла для генерации словаря.
#     Поля для которых используется словарь - помечают в третьей строке также 'dict' ,
#     при этом обязательно одно из полей должно быть помечено как 'id' в первой строке ,
#     - это поле используется как айдишник для внешнего ключа таблицы ,
#     второе поле выбирается из поддерживаемых типов генерации :
#     - на данный момент это 'sn' для серийников и 'host' для сетевых имен
#
#   B) Если нужен список только для нескольких полей - то лучше использовать тип списка.
#     Тогда в четвертой строке записывается 'list' ,
#     а в пятой строке - имя файла для генерации списка.
#     Поля для которых используется список - помечают в третьей строке также 'list' ,
#     при этом обязательно одно из полей должно быть помечено как 'id' в первой строке ,
#     - это поле используется как айдишник для внешнего ключа таблицы ,
#     остальные поля выбираются из поддерживаемых типов генерации :
#     - на данный момент это 'sn' для серийников и 'host' для сетевых имен
#
#   Не задействованные в сложной генерации (A/B) поля
#      - задаются простыми шаблонами в главном ПАТТЕРНЕ (см.п.1)
#      в третьей строке через запятую ..
#
#   Первая строка ПАТТЕРНА - это заголовки полей
#
#   Вторая строка ПАТТЕРНА - это тип генерации :
#      == 'gen_sn' , 'gen_ht' , 'gen_id'
#
#   Третья строка ПАТТЕРНА - это простые шаблоны генерации ,
#      либо отсылка к сложному шаблону 'dict' или 'list' для каждого поля.
#
#   Четвертая строка ПАТТЕРНА - это тип сложного шаблона 'dict' или 'list' .
#   Пятая строка ПАТТЕРНА - это имя файла сложного шаблона .
#    - эти строки могут не указываться при генерации только по простым шаблонам !
#
# ================================================


# =====================================
# Основной код скрипта :
# =====================================

# генерация кода таблиц из текстовых файлов
# (поля и данные, разделенные запятыми, первая строка - заголовки полей)
table_write("eq_types", "DB-Fill_00_eq_types.txt", "eq_types.sql")

# # Чтение шаблонов из подготовленного файла
# table_eq_types = gen_tab_list("DB-Fill_00_eq_types.txt")
# # генерация кода таблиц из текстовых файлов
# # (поля и данные, разделенные запятыми, первая строка - заголовки полей)
# table_write("eq_types", table_eq_types, "xxx_eq_types.sql")
# # table_write("equipments", table_eq, "xxx_eq.sql")

# считывание шаблона таблицы из файлов правил для генерации
table__tmp = genegate_table("DB-Fill_01_equipments_pattern.txt", 100)
table_write("equipments", table__tmp, "equipments.sql")
