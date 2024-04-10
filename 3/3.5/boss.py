from datetime import *

def choose_plural(amount, declensions):
    if amount%10==1 and not amount%100==11:
        return f'{amount} {declensions[0]}'
    elif amount%10 in (2,3,4) and not amount%100 in (12,13,14):
        return f'{amount} {declensions[1]}'
    else:
        return f'{amount} {declensions[2]}'
d = ['день','дня','дней']
h = ['час','часа','часов']
m = ['минута','минуты','минут']
def counter(x, y):
    release = datetime.strptime(x, '%d.%m.%Y %H:%M')
    today = datetime.strptime(y, '%d.%m.%Y %H:%M')
    diff = release-today
    string = 'До выхода курса осталось: '
    if diff.days>=0:
        if diff.days>=1:
            string+=choose_plural(diff.days, d)
            if diff.seconds>=3600:
                string+= ' и '+choose_plural(diff.seconds//3600, h)
            return string
        elif diff.days<1:
            if diff.seconds>=3600:
                string+= choose_plural(diff.seconds//3600, h)
                if diff.seconds%3600>=60:
                    string+= ' и '+choose_plural(diff.seconds%3600//60, m)
                return string
            elif diff.seconds%3600>=60:
                string+= choose_plural(diff.seconds%3600//60, m)
                return string
            else:
                return 'Курс уже вышел!'
    else:
        return 'Курс уже вышел!'

x = '08.11.2022 12:00'
y = input()

print(counter(x, y))