import functools

class MaxRetriesException(Exception):
    pass

def retry(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except:
                    pass
            raise MaxRetriesException
        return wrapper
    return decorator

# INPUT DATA:

# TEST_1:
@retry(3)
def no_way():
    raise ValueError

try:
    no_way()
except Exception as e:
    print(type(e))

# TEST_2:
@retry(8)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 5:
        raise ValueError
    print('beegeek')

beegeek()

# TEST_3:
@retry(6)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 7:
        raise ValueError
    print('beegeek')

try:
    beegeek()
except Exception as e:
    print(type(e))

# TEST_4:
@retry(7)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 7:
        raise ValueError
    print('beegeek')

try:
    beegeek()
except Exception as e:
    print(type(e))

# TEST_5:
@retry(5)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 7:
        raise ValueError
    print('beegeek')

try:
    beegeek()
except Exception as e:
    print(type(e))

# TEST_6:
@retry(5)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 7:
        raise ValueError
    print('beegeek')

try:
    beegeek()
except Exception as e:
    print(type(e))

# TEST_7:
@retry(9)
def add(a, b):
    add.calls = add.__dict__.get('calls', 0) + 1
    if add.calls < 10:
        raise ValueError
    return a + b

try:
    print(add(10, 20))
except Exception as e:
    print(type(e))

# TEST_8:
@retry(10)
def add(a, b):
    add.calls = add.__dict__.get('calls', 0) + 1
    if add.calls < 10:
        raise ValueError
    return a + b

try:
    print(add(10, 30))
except Exception as e:
    print(type(e))

# TEST_9:
@retry(100)
def add(a, b):
    add.calls = add.__dict__.get('calls', 0) + 1
    if add.calls < 10:
        raise ValueError
    return a + b

try:
    print(add(40, 10))
except Exception as e:
    print(type(e))

# TEST_10:
@retry(1)
def add(a, b):
    add.calls = add.__dict__.get('calls', 0) + 1
    if add.calls < 10:
        raise ValueError
    return a + b

try:
    print(add(40, 20))
except Exception as e:
    print(type(e))

# TEST_11:
@retry(10)
def calculate(a, b, c):
    calculate.calls = calculate.__dict__.get('calls', 0) + 1
    if calculate.calls < 4:
        raise ValueError
    return a + b + c

try:
    print(calculate(1, 2, c=3))
except Exception as e:
    print(type(e))

# TEST_12:
@retry(3)
def calculate(a, b, c):
    calculate.calls = calculate.__dict__.get('calls', 0) + 1
    if calculate.calls < 4:
        raise ValueError
    return a + b + c

try:
    print(calculate(b=1, a=2, c=3))
except Exception as e:
    print(type(e))

# TEST_13:
@retry(4)
def calculate(a, b, c):
    calculate.calls = calculate.__dict__.get('calls', 0) + 1
    if calculate.calls < 4:
        raise ValueError
    return a + b + c

try:
    print(calculate(b=2, a=2, c=3))
except Exception as e:
    print(type(e))

# TEST_14:
@retry(99)
def calculate(a, b, c):
    calculate.calls = calculate.__dict__.get('calls', 0) + 1
    if calculate.calls < 4:
        raise ValueError
    return a + b + c

try:
    print(calculate(10, b=1, c=2))
except Exception as e:
    print(type(e))

# TEST_15:
@retry(99)
def calculate(a, b, c):
    """Calculate something"""
    calculate.calls = calculate.__dict__.get('calls', 0) + 1
    if calculate.calls < 4:
        raise ValueError
    return a + b + c

print(calculate.__name__)
print(calculate.__doc__)
try:
    print(calculate(2000, b=1, c=4))
except Exception as e:
    print(type(e))