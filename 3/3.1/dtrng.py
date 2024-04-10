from datetime import date
dates=[]
def get_date_range(start, end):
    for i in range (date.toordinal(start), date.toordinal(end)+1):
        dates.append(date.fromordinal(i))
    return dates
date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)

print(*get_date_range(date1, date2), sep='\n')