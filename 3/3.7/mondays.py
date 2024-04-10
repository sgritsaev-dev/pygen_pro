from calendar import *
from datetime import *
def get_all_mondays(y):
    all_list=[]
    data = date(year=y, month=1, day=1)
    while data!= date(year=y+1, month=1, day=1):
        all_list.append(data)
        data+=timedelta(days=1)
    mondays = list(filter(lambda x: x.isoweekday()==1, all_list))
    return (mondays)
        
        

print(get_all_mondays(1982))