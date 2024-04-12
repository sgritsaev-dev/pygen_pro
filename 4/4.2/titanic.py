import csv
with open('C:/Python_education/Codes/pygen_pro/4.2/titanic.csv', 'r', encoding='UTF-8') as titanic:
    men=[]
    women=[]
    rows = csv.DictReader(titanic, delimiter=';')
    survivers_under18 = list(filter(lambda x: x['survived']=='1' and float(x['age'])<18.0, list(rows)))
    for el in survivers_under18:
        if el['sex']=='female':
            women.append(el)
        else:
            men.append(el)
    for el in men:
        print(el['name'])
    for el in women:
        print(el['name'])
    
    
    # for row in rows:
    #     del row['adm_area']
    #     del row['location']
    #     spots[row['district']] = spots.get(row['district'], 0) + int(row['number_of_access_points'])
    # spots = dict(sorted(spots.items(), key=lambda x: (-x[1], x[0])))
    # for el in spots:
    #     print(f'{el}: {spots[el]}')