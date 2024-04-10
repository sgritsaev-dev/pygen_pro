from datetime import *
workers={}
workers_raw = [input().split() for _ in range (int(input()))]
for el in workers_raw:
    workers.setdefault(f'{el[0]} {el[1]}', datetime.strptime(el[2], '%d.%m.%Y'))
x = min(workers.values())
if list(workers.values()).count(x)==1:
    for i, j in workers.items():
        if j==x: 
            print(x.strftime('%d.%m.%Y'), i)
else:
    print(x.strftime('%d.%m.%Y'), list(workers.values()).count(x))