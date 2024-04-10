from datetime import *
def fill_up_missing_dates(dates):
    dates = list(map(lambda x: datetime.strptime(x, '%d.%m.%Y'), dates))
    dates.sort()
    data = [dates[0]+timedelta(days=i) for i in range (0, (dates[-1] - dates[0]).days+1)]
    data = list(map(lambda x: x.strftime('%d.%m.%Y'), data))
    return data



dates = ['01.11.2021', '07.11.2021', '04.12.2021', '03.11.2021']

print(fill_up_missing_dates(dates))