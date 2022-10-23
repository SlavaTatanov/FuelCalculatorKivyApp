def calculating(km, cons, prc, peoples):
    if not data_check([km, cons, prc, peoples]):
        return 'Заполните все поля'
    return str(do_calculating(float(km), float(cons), float(prc), int(peoples)))


def data_check(lst):
    for item in lst:
        if not item:
            return False
    return True


def do_calculating(km: float, cons: float, prc: float, peoples: int):
    res = (prc*cons/100)*km
    res = int(res/peoples)
    return res
