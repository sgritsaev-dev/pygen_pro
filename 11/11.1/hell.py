# INPUT DATA:

# TEST_1:
txt1 = 'Перезвони мне, пожалуйста: 7-919-667-21-19'

# TEST_2:
txt2 = 'Артур: +7-919-667-21-19, Анри: 7-hey-anri-anri, Тимур: 8-917-4864-1911'

# TEST_3:
txt3 = 'Тимур: 7-ddd-ddd-dd-dd, Сослан: 8-ddd-dddd-dddd, Артур: 7-123-123-11-22,,,, Дима: 8-123-123-11-22, Анри: 8-123-1231-1221...... Гвидо: 7-123-1231-1221, 7-123-13-181-22, 8-1237-131-1221'




txt = txt3
txt = txt.replace('.', ' ')
txt = txt.replace(',', ' ')
for el in txt.split():
    x = el.strip(', ').lstrip('+')
    if len(x)==15 and ((x.startswith('7-') and len(x.split('-'))==5) or (x.startswith('8-') and len(x.split('-'))==4)) and all(el.isdigit() for el in x.split('-')):
        xx = x.split('-')
        if (x.startswith('7-') and all((len(xx[1])==3, len(xx[2])==3,len(xx[3])==2, len(xx[4])==2))) or (x.startswith('8-') and all((len(xx[1])==3, len(xx[2])==4,len(xx[3])==4))):
            print(x)

