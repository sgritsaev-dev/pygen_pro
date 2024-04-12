import csv
def csv_columns(filename):
    with open(filename,'r', encoding='utf-8') as file:
        rows = csv.DictReader(file)
        d={}
        for row in rows:
            for key, value in row.items():
                d[key] = d.get(key, []) + [value]
        return d

csv_columns('C:/Python_education/Codes/pygen_pro/4.2/test.csv')