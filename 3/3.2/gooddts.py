from datetime import date

def print_good_dates(dates):
    dates.sort()
    for el in dates:
        if el.year==1992 and (el.month+el.day)==29:
            print(el.strftime('%B %d, %Y'))

dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)