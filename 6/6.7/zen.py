from collections import Counter

with open('C:/VS code pets/edu/pygen_prof/6/6.7/pythonzen.txt', 'r', encoding='utf-8') as zen:
    lines = list(map(str.lower, filter(lambda x: x.isalpha(), zen.read())))
    for el in dict(sorted(Counter(lines).items())):
        print(f'{el}: {dict(sorted(Counter(lines).items()))[el]}')