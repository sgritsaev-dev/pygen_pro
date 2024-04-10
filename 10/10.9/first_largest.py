from itertools import takewhile as tw

def largest(iterable, n):
    res = map(lambda x: None if x<n else x, iterable)
    i=-1
    for el in res:
        i+=1
        if el!=None:
            yield i
def first_largest(iterable, n):
    try:
        return next(largest(iterable, n))
    except:
        return -1
    

numbers = [10, 2, 14, 7, 7, 18, 20]

print(first_largest(numbers, 11))