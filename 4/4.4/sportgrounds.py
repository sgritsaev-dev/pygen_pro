import csv
import json
with open('C:/VS code pets/edu/pygen_prof/4/4.4/playgrounds.csv', 'r', encoding='UTF-8') as grounds:
    spots={}
    for row in list(csv.reader(grounds, delimiter=';'))[1:]:
        spots.setdefault(row[1], {}).setdefault(row[2],[]).append(row[3])
    with open('C:/VS code pets/edu/pygen_prof/4/4.4/addresses.json', 'w', encoding='utf-8', newline='') as addresses:
        json.dump(spots, addresses, indent=3, ensure_ascii=False)
        