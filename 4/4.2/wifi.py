import csv
with open('C:/Python_education/Codes/pygen_pro/4.2/wifi.csv', 'r', encoding='UTF-8') as wifi:
    spots={}
    for row in csv.DictReader(wifi, delimiter=';'):
        del row['adm_area']
        del row['location']
        spots[row['district']] = spots.get(row['district'], 0) + int(row['number_of_access_points'])
    spots = dict(sorted(spots.items(), key=lambda x: (-x[1], x[0])))
    for el in spots:
        print(f'{el}: {spots[el]}')