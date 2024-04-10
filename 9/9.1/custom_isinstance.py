def custom_isinstance(objects, typeinfo):
    return len(list(filter(lambda x: isinstance(x, typeinfo), objects)))

numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, int))