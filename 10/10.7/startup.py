import csv

with open('C:/VS code pets/edu/pygen_prof/10/10.7/data.csv', encoding='utf-8') as data:
    lines = csv.DictReader(data)
    res = sum(int(el['raisedAmt']) for el in lines if el['round']=='a')
    print(res)