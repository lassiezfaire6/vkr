from . import BaseCheck
import re


class Inn(BaseCheck.Check):
    """Класс для проверок на соответствие строки домену 'ИНН'"""

    def check(self, data: str):
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
