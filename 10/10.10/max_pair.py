import itertools as it

def max_pair(iterable):
    return max(map(sum, it.pairwise(iterable)))

# TEST_1:
print(max_pair([1, 8, 2, 4, 3]))

# TEST_2:
iterator = iter([1, 2, 3, 4, 5])

print(max_pair(iterator))

# TEST_3:
iterator = iter([0, 0, 0, 0, 0, 0, 0, 0, 0])

print(max_pair(iterator))

# TEST_4:
iterator = iter([10, 11])

print(max_pair(iterator))

# TEST_5:
iterator = iter([5, 6, 4, 3, 2, 2])

print(max_pair(iterator))