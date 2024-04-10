import csv

with open('writing_test.csv', 'w', encoding='utf-8', newline='') as csv_file:
    fieldnames = ['first_col', 'second_col']
    values = ['value1', 'value2']
    # создаем writer объект и указываем названия столбцов
    writer = csv.writer(csv_file)
    # записываем первую строку с названиями столбцов
    writer.writerow(fieldnames)
    writer.writerow(values)