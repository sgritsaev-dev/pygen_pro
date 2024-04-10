import csv
import json
with open('C:/VS code pets/edu/pygen_prof/4/4.4/students.json', 'r', encoding='UTF-8') as students_json:
    students = json.load(students_json)
    filtered_students = list(filter(lambda x: x['age']>=18 and x['progress']>=75, students))
    mapped_students = list(map(lambda x: {'name':x['name'],'phone':x['phone']}, filtered_students))
    sorted_students = sorted(mapped_students, key=lambda x: x['name'])
    with open('C:/VS code pets/edu/pygen_prof/4/4.4/data.csv', 'w', encoding='utf-8', newline='') as data:
        writer = csv.DictWriter(data, fieldnames=['name', 'phone'])
        writer.writeheader()
        for row in sorted_students:
            writer.writerow(row)
        