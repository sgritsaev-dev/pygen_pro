from datetime import *
data = datetime.strptime(input(), '%d.%m.%Y')
x = data + timedelta(days=1)
y = data - timedelta(days=1)
print(datetime.strftime(x, '%d.%m.%Y'))
print(datetime.strftime(y, '%d.%m.%Y'))
