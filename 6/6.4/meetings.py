import csv
from datetime import *
from collections import namedtuple 
meetings = namedtuple('meetings', ['surname', 'name', 'meeting_date', 'meeting_time'])
with open('C:/VS code pets/edu/pygen_prof/6/6.4/meetings.csv', 'r', encoding='utf-8') as data:
    reader = csv.DictReader(data)
    timetable = list(meetings._make(el.values()) for el in reader)
    sorted_table = sorted(timetable, key=lambda x: datetime.strptime(x.meeting_date+x.meeting_time, '%d.%m.%Y%H:%M'))
    for el in sorted_table:
        print(el.surname, el.name)