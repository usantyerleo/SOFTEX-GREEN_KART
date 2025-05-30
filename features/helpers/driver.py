_driver = None

def set_driver(instance):
    global _driver
    _driver = instance

def get_driver():
    if _driver is None:
        raise RuntimeError("Driver não foi inicializado!")
    return _driver
