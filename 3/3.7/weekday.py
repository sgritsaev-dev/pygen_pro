from datetime import *
data = datetime.strptime(input(), '%Y-%m-%d')
print(data.strftime('%A'))