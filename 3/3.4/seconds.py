from datetime import *
params = input().split(':')
print(timedelta(hours=int(params[0]), minutes=int(params[1]), seconds=int(params[2])). seconds)
