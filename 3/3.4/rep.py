from datetime import *
data={}
start = datetime.strptime(input(), '%H:%M')
stop = datetime.strptime(input(), '%H:%M')
while start<stop:
    data.setdefault(start.strftime('%H:%M'), (start+timedelta(minutes=45)).strftime('%H:%M'))
    start+=timedelta(minutes=55)
print(data)
print(start, stop)