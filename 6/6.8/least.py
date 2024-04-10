from collections import Counter
line = Counter(input().lower().split())
newline=[]
for el in sorted(line.most_common()[-1:-(list(line.values()).count(min(line.values())))-1:-1]):
    newline.append(el[0])
print(*newline, sep=', ')