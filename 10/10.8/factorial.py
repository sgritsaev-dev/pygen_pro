from math import factorial as F
from itertools import accumulate as ACC

def factorials(n):
    for i in range(1, n+1):
        yield F(i)

numbers = factorials(150)

print(*numbers)