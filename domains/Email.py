import re
from . import BaseCheck


class Email(BaseCheck.Check):
    """Класс для проверок на соответствие строки домену 'Адрес e-mail'"""

    def check(self, data: str):
        if re.search(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', data) is None:
            return False
        else:
            return True
