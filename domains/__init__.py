import glob
from os.path import dirname, basename, isfile, join
import importlib


def get_class_names():
    modules = glob.glob(join(dirname(__file__), "*.py"))
    module_list = [basename(f)[:-3] for f in modules if isfile(f)
                   and not f.endswith('__init__.py')]
    return module_list


__all__ = get_class_names()

gbl = globals()
for _ in __all__:
    moduleToImport = 'domains.' + _
    gbl[moduleToImport] = importlib.import_module(moduleToImport)
