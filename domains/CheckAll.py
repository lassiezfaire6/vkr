from . import BaseCheck
import domains


class CheckAll:
    domains: dict[str, type[BaseCheck]]

    def __init__(self):
        self.domains = {
            "Inn": domains.Inn.Inn(),
            "Giro": domains.Giro.Giro()
    }

    def check(self, name: str, data: str):
        if name in self.domains:
            return self.domains[name].check(data)
        raise NotImplementedError()
