def polynom(x):
    res = x**2 + 1
    polynom.values.add(res)
    return res
polynom.values=set()

polynom(1)
polynom(2)
polynom(3)

print(*sorted(polynom.values))