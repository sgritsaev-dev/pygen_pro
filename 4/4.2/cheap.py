import csv
with open('C:/Python_education/Codes/pygen_pro/4.2/prices.csv', 'r', encoding='UTF-8') as data:
    rows = csv.DictReader(data, delimiter=';')
    new_rows=[]
    sorted_rows = sorted(rows, key=lambda x: x['Магазин'])
    cheapest={}
    min_price=1000
    count=0
    for row in sorted_rows:
        shop = {'Магазин':row.pop('Магазин')}
        sorted_row = dict(sorted(list(row.items()), key=lambda x: (int(x[1]),x[0])))
        if int(list(sorted_row.values())[0])<min_price:
            min_price=int(list(sorted_row.values())[0])
        new_row=shop|sorted_row
        new_rows.append(new_row)
    for row in new_rows:
        if str(min_price) in list(row.values()):
            cheapest.setdefault(list(row.values())[0], list(row.keys())[1])
    sorted_cheapest = dict(sorted(cheapest.items(), key=lambda x: (x[1], x[0])))
    for el in sorted_cheapest:
        while count==0:
            print(f'{sorted_cheapest[el]}: {el}')
            count+=1

    
    