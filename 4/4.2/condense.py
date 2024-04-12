import csv
def condense_csv(filename, ID_name=0):
    with open(filename, 'r', encoding='UTF-8') as data:
        rows = csv.reader(data)
        items = {}
        for row in rows:
            for i in range (len(row)):
                if i==0 and row[i] not in items:
                    values={}
                    items.setdefault(row[i], values)
                if i%2==1 and row[i] not in values:
                    values.setdefault(row[i], row[i+1])
        with open('C:/Python_education/Codes/pygen_pro/4.2/condensed.csv', 'w', encoding='UTF-8', newline='') as condensed:
            writer = csv.writer(condensed)
            headers=[]
            headers.append(ID_name)
            for item in items:
                for el in items[item].keys():
                    if el not in headers:
                        headers.append(el)
            writer.writerow(headers)
            for item in items:
                line=[]
                line.append(item)
                for el in items[item].values():
                    line.append(el)
                writer.writerow(line)
            
            








condense_csv('C:/Python_education/Codes/pygen_pro/4.2/titanic_copy.csv', ID_name='item')