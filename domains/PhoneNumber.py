from . import BaseCheck
import pandas as pd
import re


class PhoneNumber(BaseCheck.Check):
    """Класс для проверок на соответствие строки домену 'Номер мобильного телефона'"""

    def __init__(self):
        self.phone_number = pd.read_csv(r'C:\Users\lassi\PycharmProjects\pythonProject\assets\phone_number.csv')

    def check(self, data: str):
        check_flag = 0

        if re.search(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', data) is not None:
            check_flag += 1

        empty_check = self.phone_number.loc[self.phone_number['code'].astype(str).str.contains(data[1:4], case=False)]
        if not empty_check.empty:
            check_flag += 1

        if check_flag == 2:
            return True