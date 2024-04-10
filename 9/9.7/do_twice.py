def do_twice(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return inner

print('TEST_1')
@do_twice
def beegeek():
    print('beegeek')
    
beegeek()

print('TEST_2')
@do_twice
def beegeek():
    print('beegeek')
    
print(beegeek())

print('TEST_3')
@do_twice
def beegeek():
    return 'beegeek'
    
print(beegeek())

print('TEST_4')
@do_twice
def beegeek():
    print('beegeek')
    
beegeek()
beegeek()
beegeek()

print('TEST_5')
@do_twice
def beegeek(a, b, sep):
    print(a + b + sep)
    
beegeek(1, 2, sep=10)

print('TEST_6')
@do_twice
def beegeek(*args, **kwargs):
    print('beegeek' * sum(args + tuple(kwargs.values())))
    
beegeek(1, 1, 1, sep=1, end=2, step=3)