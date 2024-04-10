from zipfile import ZipFile
import json
filenames=[]
names=[]
def is_correct_json(file):
    try:
        backs = json.load(file)
        return backs
    except:
        return False

with ZipFile('edu/pygen_prof/4/4.5/data.zip') as data:
    for el in data.infolist():
        if el.is_dir()==False and el.filename.split('.')[-1]=='json':
            filenames.append(el.filename)
    data.extractall('C:/VS code pets/edu/pygen_prof/4/4.5/arsenal_extract')
for name in filenames:
    with open('C:/VS code pets/edu/pygen_prof/4/4.5/arsenal_extract/'+name, encoding='utf-8') as file:
        try:
            x = is_correct_json(file)
            if x['team']=='Arsenal':
                names.append({'first_name':x['first_name'],'last_name':x['last_name']})

        except:
            False
sorted_names = sorted(names, key=lambda x: (x['first_name'], x['last_name']))
for el in sorted_names:
    print(el['first_name'], el['last_name'])
