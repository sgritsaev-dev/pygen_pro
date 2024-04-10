from datetime import *
start = datetime.strptime(input(), '%d.%m.%Y')
end = datetime.strptime(input(), '%d.%m.%Y')
if (start.day+start.month)%2==0:
    start += timedelta(days=1)

for i in range (datetime.toordinal(start), datetime.toordinal(end)+1, 3):
    if datetime.fromordinal(i).isoweekday() not in (1,4):
        print(datetime.fromordinal(i).strftime('%d.%m.%Y'))
