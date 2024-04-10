import itertools as it
from collections import Counter

def ranges(iterable):
    pairs = it.pairwise(iterable)
    groups = it.groupby(pairs, key=lambda x: x[1]-x[0]==1)
    res = []
    for key, value in groups:
        tumple = []
        if key==True:
            nums = Counter(it.chain.from_iterable(value))
            for key, value in nums.items():
                if value==1:
                    tumple.append(key)
            res.append(tuple(tumple))
        if key==False:
            nums = Counter(it.chain.from_iterable(value))
            for key, value in nums.items():
                print(key, value)
                res.append((key, key))
    chainik = list(it.chain.from_iterable(res))
    for el in chainik:
        if chainik.count(el)==3:
            chainik.remove(el)
            chainik.remove(el)
    finish=[]
    for i in range(1, len(chainik), 2):
        tun=(chainik[i-1], chainik[i])
        finish.append(tun)
    return finish


numbers = [0, 2, 3, 4, 7, 8, 10, 12, 13, 15]

print(ranges(numbers))