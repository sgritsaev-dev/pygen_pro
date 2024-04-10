import itertools as it

def ncycles(iterable, times):
    return it.chain.from_iterable(it.tee(iterable, times))

print(*ncycles([1, 2, 3, 4], 3))