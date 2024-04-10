from re import fullmatch
import sys
data = [line.strip() for line in sys.stdin]
for el in data:
    telmatch = fullmatch(r"(\w+)\1", el)
    if telmatch:
        print(el)


