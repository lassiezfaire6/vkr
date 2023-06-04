import pandas as pd
import re


def inn_check(data):
    if re.search(r'\d{10}', data) is None or re.search(r'\d{12}', data) is None:
        return False

    raw_data = list(map(int, data))  # конвертируем число в список чисел
    check_flag = 0  # введём счётчик количества пройденных проверок

    k = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]  # коэффициенты для расчёта по первой методике проверки
    check_num = 0
    summa = 0

    # рассмотрим ИНН для физлиц (10 чисел) - с одним контрольным числом
    if len(raw_data) == 10:
        for i in range(2, 11, 1):
            summa = summa + k[i] * raw_data[i - 2]  # воспользуемся алгоритмом рассчёта контрольного числа

        # необходимо учитывать варинт, когда остаток от деления суммы произведений будет равен 10: тогда контрольное
        # число будет нулём
        if summa % 11 != 10:
            check_num = summa % 11

        # если рассчитаное число совпадает с фактическим, то набор чисел проходит проверку
        if check_num == raw_data[-1]:
            check_flag += 1
        else:
            return False

    # рассмотрим ИНН для ИП и физлиц (12 чисел) - тогда контрольных числа будет два
    elif len(raw_data) == 12:
        for i in range(1, 11, 1):
            summa = summa + k[i] * raw_data[i - 1]
            # print(k[i], '*', raw_data[i-1], '=', k[i] * raw_data[i-1])
            # print('Итого сумма:', summa, 'остаток от деления на 11:', summa % 11)

        if summa % 11 != 10:
            check_num = summa % 11

        # если проверку не прошло даже первое контрольное число - дальше проверять нет смысла
        if check_num != raw_data[-2]:
            return False

        else:
            summa = 0
            check_num = 0

            for i in range(0, 11, 1):
                summa = summa + k[i] * raw_data[i]

            if summa % 11 != 10:
                check_num = summa % 11

            if check_num == raw_data[-1]:
                check_flag += 1
            else:
                return False

    else:
        return False

    # функция для проверки ИНН: если строка прошла обе проверки, это действительно ИНН
    if check_flag == 1:
        return True


def giro_check(data, giro_1_5, giro_6_8):
    if re.search(r'\d{20}', data) is None:
        return False

    check_flag = 0
    raw_data = list(map(int, data))

    for _ in giro_1_5['code']:
        s = [str(integer) for integer in raw_data[0:5]]
        a_string = int("".join(s))
        if a_string == _:
            check_flag += 1

    for _ in giro_6_8['code']:
        s = [str(integer) for integer in raw_data[5:8]]
        a_string = int("".join(s))
        if a_string == _:
            check_flag += 1

    if check_flag == 2:
        return True


def phone_number_check(data, phone_number):
    check_flag = 0

    if re.search(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', data) is not None:
        check_flag += 1

    empty_check = phone_number.loc[phone_number['code'].astype(str).str.contains(data[1:4], case=False)]
    if not empty_check.empty:
        check_flag += 1

    if check_flag == 2:
        return True


def first_name_check(data, first_name_male, first_name_female):
    if re.search(r'^[а-яА-ЯёЁ-]+', data) is None:
        return False

    male_first_name = first_name_male.loc[first_name_male['names'].str.contains(data, case=False)]
    female_first_name = first_name_female.loc[first_name_female['names'].str.contains(data, case=False)]
    if not male_first_name.empty or not female_first_name.empty:
        return True


def last_name_check(data, last_name):
    if re.search(r'^[а-яА-ЯёЁ-]+', data) is None:
        return False

    for _ in range(len(last_name['names'])):
        if last_name['names'].iloc[_] in data:
            return True


def email_check(data):
    if re.search(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', data) is None:
        return False
    else:
        return True


def ip_check(data):
    if re.search(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}', data) is None:
        return False
    else:
        return True


def mac_check(data):
    if re.search(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$', data) is None:
        return False
    else:
        return True


# gai_dictionary = pd.read_csv('gai_dictionary.csv', sep=';')

giro_1_5 = pd.read_csv(r'C:\Users\lassi\PycharmProjects\pythonProject\assets\giro_1_5.csv')
giro_6_8 = pd.read_csv(r'C:\Users\lassi\PycharmProjects\pythonProject\assets\giro_6_8.csv')

phone_number = pd.read_csv(r'C:\Users\lassi\PycharmProjects\pythonProject\assets\phone_number.csv')

first_name_male = pd.read_csv(r'C:\Users\lassi\PycharmProjects\pythonProject\assets\first_name_male.csv')
first_name_female = pd.read_csv(r'C:\Users\lassi\PycharmProjects\pythonProject\assets\first_name_female.csv')

last_name = pd.read_csv(r'C:\Users\lassi\PycharmProjects\pythonProject\assets\last_name.csv')

# input_data = '972700809600'  # ИНН
# input_data = '40432520900000007553'  # Расчетный счет
input_data = '89261085956'  # Номер телефона
# input_data = 'Диана'  # Имя
# input_data = 'Иванова' # Фамилия
# input_data = 'lygun.kirill@gmail.com'  # e-mail
# input_data = '46.138.171.157'  # IP-адрес
# input_data = 'A0-D7-68-30-26-E0'  # MAC-адрес

print('Вы ввели:', input_data)
if inn_check(input_data):
    print('Введённая строка - ИНН')
if giro_check(input_data, giro_1_5, giro_6_8):
    print('Введённая строка - расчётный счёт')
if phone_number_check(input_data, phone_number):
    print('Введённая строка - номер телефона')
if first_name_check(input_data, first_name_male, first_name_female):
    print('Введённая строка - имя')
if last_name_check(input_data, last_name):
    print('Введённая строка - фамилия')
if email_check(input_data):
    print('Введённая строка - адрес e-mail')
if ip_check(input_data):
    print('Введённая строка - IP-адрес')
if mac_check(input_data):
    print('Введённая строка - MAC-адрес')
