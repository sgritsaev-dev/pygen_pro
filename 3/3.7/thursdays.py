from calendar import *
from datetime import *
def get_thursdays(y):
    all_list=[]
    data = date(year=y, month=1, day=1)
    while data!= date(year=y+1, month=1, day=1):
        all_list.append(data)
        data+=timedelta(days=1)
    thursdays = list(filter(lambda x: x.isoweekday()==4, all_list))
    third=[]
    for i in range (1,13):
        counter = 0 
        for el in thursdays:
            if el.month==i:
                counter+=1
            if counter==3:
                third.append(el.strftime('%d.%m.%Y'))
    print(*third, sep='\n')
        
        
x = int(input())
get_thursdays(x)
