from collections import Counter
line = Counter(input().lower().split())
newline=[]
for el in sorted(line.most_common()[0:(list(line.values()).count(max(line.values())))]):
    newline.append(el[0])
print(max(newline))