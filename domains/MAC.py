import re
from . import BaseCheck


class MAC(BaseCheck.Check):
    """Класс для проверок на соответствие строки домену 'MAC Адрес'"""

    def check(self, data: str):
        if re.search(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$', data) is None:
            return False
        else:
            return True
