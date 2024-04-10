from collections import Counter

files = input().split(',')
for el in sorted(Counter(files)):
    print(f'{el}: {Counter(files)[el]}')