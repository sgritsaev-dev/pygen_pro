from datetime import datetime
def is_available_date(dates, some_date):
    booked_dates = []
    wanted_dates = []
    for el in dates:
        try:
            booked_dates.append(datetime.strptime(el, '%d.%m.%Y'))
        except:
            period = el.split('-')
            amount = datetime.strptime(period[1], '%d.%m.%Y').toordinal() - datetime.strptime(period[0], '%d.%m.%Y').toordinal()
            for i in range (amount+1):
                datex = datetime.strptime(period[0], '%d.%m.%Y').toordinal()+i
                booked_dates.append(datetime.fromordinal(datex))
    try:
        wanted_dates.append(datetime.strptime(some_date, '%d.%m.%Y'))
    except:
        period = some_date.split('-')
        amount = datetime.strptime(period[1], '%d.%m.%Y').toordinal() - datetime.strptime(period[0], '%d.%m.%Y').toordinal()
        for i in range (amount+1):
            datey = datetime.strptime(period[0], '%d.%m.%Y').toordinal()+i
            wanted_dates.append(datetime.fromordinal(datey))
    return not(bool(set(booked_dates) & set(wanted_dates)))
    

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))