from collections import Counter

def unique(iterable):
    yield from Counter(iterable)


numbers = [1, 2, 2, 3, 4, 5, 5, 5, 10]

print(*unique(numbers))