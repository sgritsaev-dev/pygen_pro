import itertools as it

def is_rising(iterable):
    for el in it.pairwise(iterable):
        if el[0]>=el[1]:
            return False
    return True

# TEST_1:
print(is_rising([1, 2, 3, 4, 5]))

# TEST_2:
iterator = iter([1, 1, 1, 2, 3, 4])

print(is_rising(iterator))

# TEST_3:
iterator = iter(list(range(100, 200)))

print(is_rising(iterator))

# TEST_4:
iterator = iter(list(range(200, 100, -1)))

print(is_rising(iterator))