from time import *
def get_the_fastest_func(funcs, arg):
    timetable = {}
    for el in funcs:
        start = perf_counter()
        result = el(arg)
        end = perf_counter()
        timetable.setdefault((end-start), el)
    return timetable
        
import calendar
from datetime import *
def get_all_mondays1(y):
    all_list=[]
    data = date(year=y, month=1, day=1)
    while data!= date(year=y+1, month=1, day=1):
        all_list.append(data)
        data+=timedelta(days=1)
    mondays = list(filter(lambda x: x.isoweekday()==1, all_list))
    return (mondays)

def get_all_mondays(year):
    mondays = []
    for month in range(1, 13):
        for week in calendar.monthcalendar(year, month):
            monday = week[0]
            if monday:
                mondays.append(date(year, month, monday))
    return mondays

print(get_the_fastest_func([get_all_mondays, get_all_mondays1], 1999))