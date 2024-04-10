from itertools import dropwhile as dw

def drop_this(it, obj):
    return dw(lambda x: x==obj, it)

numbers = [0, 0, 0, 1, 2, 3]

print(*drop_this(numbers, 0))