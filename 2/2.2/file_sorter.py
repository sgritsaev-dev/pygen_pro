from math import *
files_list = []
size_file = {'B': 1, 'KB': 1024, 'MB': 1048576, 'GB': 1073741824}
with open('C:/VS code pets/edu/pygen_prof/2.2/files.txt', encoding='UTF-8') as files:
    files = files.readlines()
    for el in files:
        file = el.strip().split()
        files_list.append(file)
for el in files_list:
    el.append(el[0].replace(el[0][:el[0].index('.')], ''))
    el[1] = int(el[1])*size_file[el[2]]
    el[2] = 'B'
files_list.sort(key=lambda x: x[0])
files_list.sort(key=lambda x: x[3])
format = files_list[0][3]
total = 0
for el in files_list:
    if el[3]==format:
        print(el[0])
        total+=el[1]
    else:
        print('----------')
        if total >= size_file['GB']:
            print('Summary:', round(total/size_file['GB']), 'GB')
        elif total >= size_file['MB']:
            print('Summary:', round(total/size_file['MB']), 'MB')
        elif total >= size_file['KB']:
            print('Summary:', round(total/size_file['KB']), 'KB')
        else:
            print('Summary:', round(total/size_file['B']), 'B')
        print('\n'+el[0])
        total = 0
        format = el[3]
        total+=el[1]
print('----------')
if total >= size_file['GB']:
    print('Summary:', round(total/size_file['GB']), 'GB')
elif total >= size_file['MB']:
    print('Summary:', round(total/size_file['MB']), 'MB')
elif total >= size_file['KB']:
    print('Summary:', round(total/size_file['KB']), 'KB')
else:
    print('Summary:', round(total/size_file['B']), 'B')


