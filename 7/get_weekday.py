def get_weekday(number):
    week = { 1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Суббота", 7: "Воскресенье"}
    if isinstance(number, int):
        if number in week.keys():
            return week[number]
        else:
            raise ValueError('Аргумент не принадлежит требуемому диапазону')
    else:
        raise TypeError('Аргумент не является целым числом')

try:
    print(get_weekday('dfgg'))
except TypeError as err:
    print(err)
    print(type(err))