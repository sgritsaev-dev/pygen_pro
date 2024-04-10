def flatten(nested_list):
    for el in nested_list:
        if isinstance(el, int):
            yield el
        else:
            yield from flatten(el)

generator = flatten([[1, 2], [[3]], [[4], 5]])

print(*generator)
