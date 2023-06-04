from . import BaseCheck
import pandas as pd
import re


class FirstName(BaseCheck.Check):
    """Класс для проверок на соответствие строки домену 'Имя'"""

    def __init__(self):
        self.first_name_male = pd.read_csv(r'C:\Users\lassi\PycharmProjects\pythonProject\assets\first_name_male.csv')
        self.first_name_female = pd.read_csv(r'C:\Users\lassi\PycharmProjects\pythonProject\assets\first_name_female.csv')

    def check(self, data: str):
        if re.search(r'^[а-яА-ЯёЁ-]+', data) is None:
            return False

        male_first_name = self.first_name_male.loc[self.first_name_male['names'].str.contains(data, case=False)]
        female_first_name = self.first_name_female.loc[self.first_name_female['names'].str.contains(data, case=False)]
        if not male_first_name.empty or not female_first_name.empty:
            return True
