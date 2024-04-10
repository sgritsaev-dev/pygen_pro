from datetime import *
print((datetime.strptime(input(), '%H:%M:%S') + timedelta(seconds=int(input()))).strftime('%H:%M:%S'))
