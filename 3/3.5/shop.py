from datetime import *
schedule = {
    'Mon': {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    'Tue': {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    'Wed': {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    'Thu': {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    'Fri': {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    'Sat': {'start': timedelta(hours=10), 'end': timedelta(hours=18)},
    'Sun': {'start': timedelta(hours=10), 'end': timedelta(hours=18)}
    }
input_data = datetime.strptime(input(), '%d.%m.%Y %H:%M')
for el in schedule:
    if input_data.strftime('%a')==el:
        input_delta = timedelta(hours=input_data.hour, minutes=input_data.minute)
        timeleft = schedule[el]['end'] - input_delta
        work_mins = schedule[el]['start'].seconds//60
        if (schedule[el]['start'].seconds//60)<=(input_delta.seconds//60)<=(schedule[el]['end'].seconds//60):
            print(timeleft.seconds//60)
        else:
            print('Магазин не работает')