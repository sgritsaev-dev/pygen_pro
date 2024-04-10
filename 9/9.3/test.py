print(bool(0.0))

print(bool({}))	

print(bool([]))	

print(bool('False'))	

print(bool({0: False}))	

print(bool(None))	

print(bool(False))	

print(bool(True))	

print(bool(set()))	

print(bool(0))	

print(bool(()))	

print(bool([0, 0, 0]))	

print(bool(''))


positive = [1, 2, 3, 4, 5]
negative = [-1, -2, -3]
combined = [1, 2, -3, 4]

result = map(lambda a, b, c: a + b + c, positive, negative, combined)

print(*result)

numbers = filter(lambda x: x > 0, [-3, -2, -1, 0, 1, 2, 3])

if 1 in numbers:
    print('bee')
if 1 in numbers:
    print('geek')