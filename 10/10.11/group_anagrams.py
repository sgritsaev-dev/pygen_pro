import itertools as it
from collections import Counter

def group_anagrams(iterable):
    res = it.groupby(sorted(iterable, key=lambda x: sorted(Counter(x))), key=lambda x: Counter(x))
    result = [tuple(value) for key, value in res]
    return result