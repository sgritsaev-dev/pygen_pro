from collections import Counter

def scrabble(symbols, word):
    x = Counter(symbols.lower())
    y = Counter(word.lower())
    x.subtract(y)
    return not any(-x)

print(scrabble('bbbbbeeeeegggggggeeeeeekkkkkii', 'Beegeekiyi'))