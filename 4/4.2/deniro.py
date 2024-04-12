import csv
with open('C:/Python_education/Codes/pygen_pro/4.2/deniro.csv', 'r+', encoding='UTF-8') as deniro:
    rows = csv.reader(deniro)
    number = int(input())-1
    sorted_rows = sorted(rows, key=lambda x: int(x[number]) if x[number].isdigit() else x[number])
    
    for row in sorted_rows:
        print(*row,sep=',')