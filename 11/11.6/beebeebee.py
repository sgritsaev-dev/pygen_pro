import re
import sys
data = [line.strip() for line in sys.stdin]
counter=0
for el in data:
    if re.fullmatch(r"^beegeek$", el):
        counter+=2
    elif re.fullmatch(r"^beegeek.*beegeek$", el):
        counter+=3
    elif re.search(r"^beegeek", el) or re.search(r"beegeek$", el):
        counter+=2
    elif re.search(r"beegeek", el):
        counter+=1
print(counter)
