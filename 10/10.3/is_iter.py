def is_iterable(iterable):
    try:
        check = iter(iterable)
        return True
    except:
        return False
    
objects = [(1, 13), 7.0004, [1, 2, 3]]

for obj in objects:
    print(is_iterable(obj))