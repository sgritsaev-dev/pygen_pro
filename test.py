import csv
counter=0
vins21 = set()
with open('V:/AutoEver/Outgoing/CCS/D_Demianov/4Sergey/20 - 21 transactions.csv', 'r+', encoding='utf-8') as file:
    data = csv.DictReader(file)
    for el in data:
        el['vin_id']=el['vin_id'].replace('CI_', '')
        vins21.add(el['vin_id'])