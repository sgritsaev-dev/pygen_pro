from datetime import *
data = datetime.strptime(input(), '%d.%m.%Y')
print(datetime.strftime(data, '%d.%m.%Y'))
for i in range (2,11):
    data = data + timedelta(days=i)
    print(datetime.strftime(data, '%d.%m.%Y'))