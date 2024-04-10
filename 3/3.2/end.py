from datetime import date
counter=0
x = 0

while x!='end':
    x = input()
    xx = x.split('.')
    try:
        datex = date(day=int(xx[0]), month=int(xx[1]), year=int(xx[2]))
        counter+=1
        print('Корректная')
    except:
        print('Некорректная')
print(counter)