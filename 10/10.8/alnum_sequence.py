import itertools as it
import string

def alnum_sequence():
    res = (elem for tuple in zip(it.count(1), string.ascii_uppercase) for elem in tuple)
    return it.cycle(res)

alnum = alnum_sequence()

print(*(next(alnum) for _ in range(555)))