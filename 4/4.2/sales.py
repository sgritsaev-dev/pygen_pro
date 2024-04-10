import csv

with open('C:/VS code pets/edu/pygen_prof/4.2/sales.csv', 'r', encoding='utf-8') as sales:
    rows = csv.DictReader(sales, delimiter=';')
    rows_x=list(filter(lambda x: int(x['old_price'])>int(x['new_price']), rows))
    for row in rows_x:
        print(row['name'])
    