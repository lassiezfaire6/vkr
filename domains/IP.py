import re
from . import BaseCheck



class IP(BaseCheck.Check):
    """Класс для проверок на соответствие строки домену 'IP Адрес'"""

    def check(self, data: str):
        if re.search(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}', data) is None:
            return False
        else:
            return True
