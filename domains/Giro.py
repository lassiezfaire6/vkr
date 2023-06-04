from . import BaseCheck
import pandas as pd
import re


class Giro(BaseCheck.Check):
    """Класс для проверок на соответствие строки домену 'Расчётный счёт'"""

    def __init__(self):
        self.giro_1_5 = pd.read_csv(r'C:\Users\lassi\PycharmProjects\pythonProject\assets\giro_1_5.csv')
        self.giro_6_8 = pd.read_csv(r'C:\Users\lassi\PycharmProjects\pythonProject\assets\giro_6_8.csv')

    def check(self, data: str):
        if re.search(r'\d{20}', data) is None:
            return False

        check_flag = 0
        raw_data = list(map(int, data))

        for _ in self.giro_1_5['code']:
            s = [str(integer) for integer in raw_data[0:5]]
            a_string = int("".join(s))
            if a_string == _:
                check_flag += 1

        for _ in self.giro_6_8['code']:
            s = [str(integer) for integer in raw_data[5:8]]
            a_string = int("".join(s))
            if a_string == _:
                check_flag += 1

        if check_flag == 2:
            return True
