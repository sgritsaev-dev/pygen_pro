from datetime import *
max_count=0
workers={}
birthdays=set()
workers_raw = [input().split() for _ in range (int(input()))]
for el in workers_raw:
    workers.setdefault(f'{el[0]} {el[1]}', datetime.strptime(el[2], '%d.%m.%Y'))
for el in workers.values():
    x = list(workers.values()).count(el)
    if x>max_count:
        max_count=x
for el in workers.values():
    if list(workers.values()).count(el)==max_count:
        birthdays.add(el)
bd = sorted(list(birthdays))
bd = list(map(lambda x: x.strftime('%d.%m.%Y'), bd))
print(*bd, sep='\n')

# if list(workers.values()).count(x)==1:
#     for i, j in workers.items():
#         if j==x: 
#             print(x.strftime('%d.%m.%Y'), i)
# else:
#     print(x.strftime('%d.%m.%Y'), list(workers.values()).count(x))