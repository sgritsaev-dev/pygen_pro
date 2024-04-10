import sys
total=0
spisok=[]
lines = sys.stdin()
for line in lines:
    try:
        total+=line
    except:
        spisok.append(line)
print(total)
print(spisok)