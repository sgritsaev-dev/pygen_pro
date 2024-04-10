from collections import OrderedDict
rev=OrderedDict()
data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
truefalse = [False, True]*(len(data)//2)
for el in truefalse:
    key, value = data.popitem(last=el)
    rev[key] = value
    
print(rev)