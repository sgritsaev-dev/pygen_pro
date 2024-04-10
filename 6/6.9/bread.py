from collections import ChainMap, Counter       
total=0
bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

food = ChainMap(bread, meat, sauce, vegetables, toppings)
order = Counter(input().split(','))
maxlen=max(list(map(len, order)))
for el in order:
    total+=order[el]*food[el]
for el in sorted(order.items()):
    print(f'{el[0].ljust(maxlen)} x {el[1]}')
print('-'*max(len(f'{el[0].ljust(maxlen)} x {el[1]}'), len(f'ИТОГ: {total}р')))
print(f'ИТОГ: {total}р')