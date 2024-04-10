import itertools as it

def sum_of_digits(iterable):
    total=0
    for el in it.chain.from_iterable(map(str, iterable)):
        total+=int(el)
    return total





# TEST_1:
print(sum_of_digits([13, 20, 41, 2, 2, 5]))

# TEST_2:
print(sum_of_digits((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))

# TEST_3:
print(sum_of_digits([123456789]))

# TEST_4:
numbers = [10]*100