from itertools import dropwhile as dw

def drop_while_negative(iterable):
    return dw(lambda x: x<0, iterable)

iterator = iter([-3, -2, -1, 0, 1, 2, 3, -4, -5, -6])

print(*drop_while_negative(iterator))