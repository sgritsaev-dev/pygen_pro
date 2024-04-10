from datetime import *
dt_raw = input().split()
data = list(map(lambda x: datetime.strptime(x, '%d.%m.%Y'), dt_raw))
print(data)
gap = []
for i in range (len(data)):
    try:
        x = data[i]-data[i-1]
        gap.append(x)
    except:
        continue
print(gap)
# data = datetime.strptime(input(), '%d.%m.%Y')
# print(datetime.strftime(data, '%d.%m.%Y'))
# for i in range (2,11):
#     data = data + timedelta(days=i)
#     print(datetime.strftime(data, '%d.%m.%Y'))