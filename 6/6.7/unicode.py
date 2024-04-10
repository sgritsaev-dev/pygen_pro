from collections import Counter

files = input().split(',')
max_len=0
for el in files:
    if len(el)>max_len:
        max_len=len(el)
for el in sorted(Counter(files)):
    total=0
    word = Counter(el)
    for letter in word:
        if letter!=' ':
            total+=(word[letter]*ord(letter))
    print(f'{el.ljust(max_len)}: {total} UC x {Counter(files)[el]} = {total*Counter(files)[el]} UC')