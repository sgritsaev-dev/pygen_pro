from collections import Counter, defaultdict
mydic = Counter(map(len, input().split()))
print(mydic)
for el in sorted(mydic.items(), key=lambda item: item[1]):
    print(f'Слов длины {el[0]}: {el[1]}')
