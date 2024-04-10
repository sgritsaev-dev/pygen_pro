def nonempty_lines(name):
    with open (name, encoding='utf-8') as lines:
        no_empty = (el.strip() for el in lines if len(el)>0)
        no_long = (el if len(el)<=25 else '...' for el in no_empty)
        yield from no_long

lines = nonempty_lines('C:/VS code pets/edu/pygen_prof/10/10.7/data.csv')

print(next(lines))
print(next(lines))
print(next(lines))
print(next(lines))
print(next(lines))
print(next(lines))
print(next(lines))
print(next(lines))
print(next(lines))
print(next(lines))
print(next(lines))
print(next(lines))