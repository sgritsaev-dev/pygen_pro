from itertools import product

systema = '0123456789ABCDEF'

n = int(input())
m = int(input())

for el in product(systema[:n], m):
    print(el, end=' ')
