import csv
with open('C:/Python_education/Codes/pygen_pro/4.2/data.csv', 'r', encoding='UTF-8') as data:
    rows = csv.DictReader(data)
    dc=[]
    doms={}
    for row in rows:
        row['email'] = row['email'][row['email'].index('@')+1:]
        x = {}
        x.setdefault('domain', row['email'])
        dc.append(x)
    for el in dc:
        doms.setdefault(el['domain'], dc.count(el))
    s_doms = dict(sorted(doms.items(), key=lambda x: (x[1], x[0])))   
    with open('C:/Python_education/Codes/pygen_pro/4.2/domain_usage.csv', 'w', encoding='UTF-8', newline='') as usage:
        writer = csv.writer(usage)
        writer.writerow(['domain', 'count'])
        for el in s_doms.items():
            writer.writerow(el)
    print(doms, s_doms, sep='\n')