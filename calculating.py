def calculating(km, cons, prc, peoples):
    if not data_check([km, cons, prc, peoples]):
        return 'Заполните все поля'
    return 'Все ок!'


def data_check(lst):
    for item in lst:
        if not item:
            return False
    return True
