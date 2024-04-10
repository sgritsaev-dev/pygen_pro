from functools import lru_cache
import sys

@lru_cache
def alpha(word):
    res = ''.join(el for el in sorted(word))
    return res

for word in sys.stdin:
    print(alpha(word.strip()))
