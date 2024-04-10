from itertools import filterfalse as ff

def first_true(it, predicate):
    try:
        return list(filter(predicate, it))[0]
    except:
        pass

numbers = iter([1, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200])

print(first_true(numbers, lambda num: num > 10))