from collections import Counter
total=0
booklist = Counter(input().split())
for i in range(int(input())):
    client = input().split()
    if booklist[client[0]]>0:
        booklist[client[0]]-=1
        total+=int(client[1])
print(total)