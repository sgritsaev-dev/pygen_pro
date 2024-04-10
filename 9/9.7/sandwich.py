def sandwich(func):
    def inner(*args, **kwargs):
        print('---- Верхний ломтик хлеба ----')
        res = func(*args, **kwargs)
        print('---- Нижний ломтик хлеба ----')
        return res
    return inner


@sandwich
def add_ingredients(ingredients):
    print(' | '.join(ingredients))


add_ingredients(['томат', 'салат', 'сыр', 'бекон'])
