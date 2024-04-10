import csv
import json
with open('C:/VS code pets/edu/pygen_prof/4/4.4/food_services.json', 'r', encoding='UTF-8') as food_json:
    food = json.load(food_json)
    cartiers={}
    nets={}
    for row in food:
        cartiers[row['District']] = cartiers.get(row['District'], 0)+1
    sorted_cartiers = sorted(cartiers.items(), key=lambda item: item[1])
    print(f'{sorted_cartiers[-1][0]}: {sorted_cartiers[-1][1]}')
    filtered_food = list(filter(lambda x: x["IsNetObject"]=='да', food))
    for row in filtered_food:
        nets[row['OperatingCompany']] = nets.get(row['OperatingCompany'], 0)+1
    sorted_nets = sorted(nets.items(), key=lambda item: item[1])
    print(f'{sorted_nets[-1][0]}: {sorted_nets[-1][1]}')
    