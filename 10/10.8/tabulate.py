import itertools as it

def tabulate(func):
    res = it.count(1, 1)
    yield from map(func, res)