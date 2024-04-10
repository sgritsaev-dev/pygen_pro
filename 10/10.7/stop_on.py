def stop_on(iterable, obj):
    for el in iterable:
        if el==obj:
            break
        yield el


    
    
    
numbers = [1, 2, 3, 4, 5]

print(*stop_on(numbers, 4))

iterator = iter('beegeek')

print(*stop_on(iterator, 'a'))