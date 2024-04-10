from calendar import *
from datetime import *
def get_days_in_month(y, m):
    x = list(month_name).index(m)
    return [datetime(year=y, month=list(month_name).index(m), day=i) for i in range (1, monthrange(y, x)[1]+1)]

print(get_days_in_month(1982, 'January'))