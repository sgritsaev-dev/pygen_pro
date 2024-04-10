from datetime import date
dates=[]
def saturdays_between_two_dates(date1, date2):
    if date1>date2:
        date1, date2 = date2, date1
        for i in range (date.toordinal(date1), date.toordinal(date2)+1):
            if date.fromordinal(i).isoweekday() == 6:
                dates.append(date.fromordinal(i))
    return len(dates)

date1 = date(2020, 7, 26)
date2 = date(2020, 7, 2)

print(saturdays_between_two_dates(date1, date2))