import csv
import json
from datetime import *
with open('C:/VS code pets/edu/pygen_prof/4/4.4/pools.json', 'r', encoding='UTF-8') as pools_json:
    pools = json.load(pools_json)
    filtered_pools = list(filter(lambda x: (datetime.strptime(x["WorkingHoursSummer"]['Понедельник'].split('-')[0], '%H:%M')-datetime.strptime('10:00', '%H:%M'))<=timedelta(hours=0) and (datetime.strptime(x["WorkingHoursSummer"]['Понедельник'].split('-')[1], '%H:%M')-datetime.strptime('12:00', '%H:%M'))>=timedelta(hours=0), pools))
    sorted_pools = sorted(filtered_pools, key=lambda x: (x["DimensionsSummer"]["Length"], x["DimensionsSummer"]["Width"]))
    print(f'''{sorted_pools[-1]["DimensionsSummer"]["Length"]}x{sorted_pools[-1]["DimensionsSummer"]["Width"]}\n{sorted_pools[-1]["Address"]}''')