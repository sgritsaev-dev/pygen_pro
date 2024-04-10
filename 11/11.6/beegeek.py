from re import fullmatch
import sys
data = [line.strip() for line in sys.stdin]
for el in data:
    telmatch = fullmatch(r"_\d+[A-Za-z]{0,}_{0,1}", el)
    if telmatch:
        print(True)
    else:
        print(False)
    