from collections import namedtuple
import itertools as it

Item = namedtuple('Item', ['name', 'mass', 'price'])

max_mass = 500

items = [Item('Обручальное кольцо', 7, 49_000),
         Item('Мобильный телефон', 200, 110_000),
         Item('Ноутбук', 2000, 150_000),
         Item('Ручка Паркер', 20, 37_000),
         Item('Статуэтка Оскар', 4000, 28_000),
         Item('Наушники', 150, 11_000),
         Item('Гитара', 1500, 32_000),
         Item('Золотая монета', 8, 140_000),
         Item('Фотоаппарат', 720, 79_000),
         Item('Лимитированные кроссовки', 300, 80_000)]

res=set()

for i in range(1, 11):
    for el in it.combinations(items, i):
        if sum(map(lambda x: x.mass, el))<=max_mass:
            res.add(el)

def sumer(tumpel):
    total=0
    for el in tumpel:
        total+=el.price
    return total
try:
    sres = max(res, key=sumer)
    if len(sres)>=1:
        for el in sorted(sres, key=lambda x: x.name):
            print(el.name)
except:
    print('Рюкзак собрать не удастся')
    


