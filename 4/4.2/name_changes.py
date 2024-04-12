import csv
from datetime import *
with open('C:/Python_education/Codes/pygen_pro/4.2/name_log.csv', 'r', encoding='UTF-8') as name_log:
    rows = csv.DictReader(name_log)
    new={}
    rows_sorted = sorted(list(rows), key= lambda x: datetime.strptime(x['dtime'], '%d/%m/%Y %H:%M'), reverse=True)
    for row in rows_sorted:
        new.setdefault(row['email'], list(row.values()))
        sorted_new = dict(sorted(new.items(), key=lambda item: item[0]))
    with open('C:/Python_education/Codes/pygen_pro/4.2/new_name_log.csv', 'w', encoding='UTF-8', newline='') as new_name_log:
        writer = csv.writer(new_name_log)
        writer.writerow(['username','email','dtime'])
        for row in sorted_new:
            writer.writerow(sorted_new[row])