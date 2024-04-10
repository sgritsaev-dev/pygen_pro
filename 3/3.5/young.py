from datetime import *
today = datetime.strptime(input(), '%d.%m.%Y')+timedelta(days=1)
workers={}
soon={}
workers_raw = [input().split() for _ in range (int(input()))]
for el in workers_raw:
    workers.setdefault(f'{el[0]} {el[1]}', datetime.strptime(el[2], '%d.%m.%Y'))
for name, day in workers.items():
    x = (datetime(day=day.day, month=day.month, year=today.year)-today).days
    if 0<x<7 or 358<x<365:
        soon.setdefault(name, day)
if soon:
    for name, day in soon.items():
        if day==max(soon.values()):
            print(name)
else:
    print('Дни рождения не планируются')