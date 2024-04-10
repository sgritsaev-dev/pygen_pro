from collections import Counter
import sys
data = [line.strip().split() for line in sys.stdin]
cc = Counter(data)
print(cc)