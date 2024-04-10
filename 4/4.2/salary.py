import csv
with open('C:/VS code pets/edu/pygen_prof/4.2/salary_data.csv', encoding='utf-8') as salary:
    rows = list(csv.DictReader(salary, delimiter=';'))
    names=set()
    avg_salaries={}
    
    for row in rows:
        names.add(row['company_name'])
    for el in names:
        avg=0
        counter=0
        for row in rows:
            if row['company_name']==el:
                avg+=int(row['salary'])
                counter+=1
        avg_salaries.setdefault(el, avg/counter)
    srt_salaries = sorted(avg_salaries.items())
    final = sorted(srt_salaries, key=lambda x: x[1])
    for el in final:
        print(el[0])
