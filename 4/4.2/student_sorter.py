import csv
with open('C:/Python_education/Codes/pygen_pro/4.2/student_counts.csv', 'r', encoding='UTF-8') as data:
    rows = csv.DictReader(data)
    new_rows=[]
    for row in rows:
        year = {'year':row.pop('year')}
        sorted_row = dict(sorted(list(row.items()), key=lambda x: (int(x[0].split('-')[0]), x[0].split('-')[1])))
        new_row=year|sorted_row
        new_rows.append(new_row)
        headers = list(new_row.keys())
    with open('C:/Python_education/Codes/pygen_pro/4.2/sorted_student_counts.csv', 'w', encoding='UTF-8', newline='') as sorted_data:
        writer = csv.DictWriter(sorted_data, fieldnames=headers)
        writer.writeheader()
        writer.writerows(new_rows)
