from . import BaseCheck
import pandas as pd
import re


class LastName(BaseCheck.Check):
    """Класс для проверок на соответствие строки домену 'Фамилия'"""

    def __init__(self):
        self.last_name = pd.read_csv(r'C:\Users\lassi\PycharmProjects\pythonProject\assets\last_name.csv')

    def check(self, data: str):
        if re.search(r'^[а-яА-ЯёЁ-]+', data) is None:
            return False

        for _ in range(len(self.last_name['names'])):
            if self.last_name['names'].iloc[_] in data:
                return True
