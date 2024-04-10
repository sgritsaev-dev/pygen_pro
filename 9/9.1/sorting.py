string=[]
string.extend(input())
lowers=[]
uppers=[]
odds=[]
evens=[]
for x in string:
    if x.isdigit():
        if int(x) % 2 == 1:
            odds.append(x)
        else:
            evens.append(x)
    elif x.islower():
        lowers.append(x)
    else:
        uppers.append(x)
print(*sorted(lowers), *sorted(uppers), *sorted(odds), *sorted(evens), sep='')