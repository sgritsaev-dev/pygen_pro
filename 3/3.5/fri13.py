from datetime import *
weeknums = [0,0,0,0,0,0,0]
for i in range (1, 10000):
    for j in range (1, 13):
        weeknums[date(i, j, 13).weekday()] +=1
print(*weeknums, sep='\n')
