from datetime import *

def years_days(yy):
    for i in range(datetime.toordinal(date(year=yy, month=1, day=1)), datetime.toordinal(date(year=yy+1, month=1, day=1))):
        yield date.fromordinal(i)
