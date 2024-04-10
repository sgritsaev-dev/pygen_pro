import csv
import json
with open('C:/VS code pets/edu/pygen_prof/4/4.4/food_services.json', 'r', encoding='UTF-8') as food_json:
    food = json.load(food_json)
    types={}
    sorted_types={}
    for row in food:
        types.setdefault(row['TypeObject'], []).append(row)
    for el in types:
        sorted_types[el] = sorted(types[el], key=lambda x: x['SeatsCount'])
    for el in dict(sorted(sorted_types.items())):
        print(f'''{el}: {sorted_types[el][-1]['Name']}, {sorted_types[el][-1]['SeatsCount']}''')
    