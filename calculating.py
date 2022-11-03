names = {'err': 'Заполните все поля'}


def calculating(km, cons, prc, peoples, money):
    if not data_check([km, cons, prc, peoples]):
        return names['err']
    res = do_calculating(float(km), float(cons), float(prc), int(peoples))
    if peoples == '1':
        return f'С вас {res["money"]} {money}\nПотрачено {res["liters"]} л.'
    else:
        return f'С каждого по {res["money"]} {money}\nПотрачено {res["liters"]} л.'


def data_check(lst):
    for item in lst:
        if not item:
            return False
    return True


def do_calculating(km: float, cons: float, prc: float, peoples: int):
    liters = cons * (0.01 * km)
    res = liters * prc
    res = int(res/peoples)
    return {'money': res, 'liters': round(liters, 1)}
