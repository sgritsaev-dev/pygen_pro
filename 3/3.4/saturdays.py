from datetime import *
def num_of_sundays(year):
    y = int(input())
    counter=0
    for i in range (date(year=y, month=1, day=1).toordinal(), (date(year=y, month=12, day=31).toordinal())+1):
        if datetime.fromordinal(i).strftime('%w')=='0':
            counter+=1
    return counter