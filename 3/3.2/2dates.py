from datetime import date

year, month, day = input().split('-')
date1 = date(int(year), int(month), int(day))
year, month, day = input().split('-')
date2 = date(int(year), int(month), int(day))
print(min(date1,date2).strftime('%d-%m (%Y)'))