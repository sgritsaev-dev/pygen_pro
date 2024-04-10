import itertools
def zip_longest(*data, fill=None):
    return list(itertools.zip_longest(*data, fillvalue=fill))



print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))

