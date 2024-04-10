from collections import Counter, defaultdict
import json
import csv
Big_D = Counter()
total=0
for i in range(1,5):
    name = f'C:/VS code pets/edu/pygen_prof/6/6.8/quarter{i}.csv'
    quater = f'q{i}'
    d = f'd{i}'
    with open(name, encoding='utf-8') as file:
        quater= list(csv.reader(file))
        d= defaultdict(int)
        del quater[0]
        for line in quater:
            d[line[0]]=int(line[1])+int(line[2])+int(line[3])
        Big_D+=d
with open('C:/VS code pets/edu/pygen_prof/6/6.8/prices.json', encoding='utf-8') as pr_json:
    prices = json.load(pr_json)
    for el in prices:
        total+=prices[el]*Big_D[el]
print(total)
    
