import re
import sys
data = [line.strip() for line in sys.stdin]
counter=0
for el in data:
    if re.search(r'beegeek', el, flags=re.IGNORECASE):
        counter+=1
print(counter)