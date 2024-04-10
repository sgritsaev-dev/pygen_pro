import csv
from collections import Counter

with open('C:/VS code pets/edu/pygen_prof/6/6.8/name_log.csv', encoding='utf-8') as csv_file:
    rows = list(csv.reader(csv_file))
    del rows[0]
    f_rows = list(map(lambda x: x[1], rows))
    for el in Counter(sorted(f_rows)).items():
        print(f'{el[0]}: {el[1]}')