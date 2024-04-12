import functools

def returns(datatype):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if type(res)==datatype:
                return res
            else:
                raise TypeError
        return wrapper
    return decorator

@returns(int)
def add(a, b):
    return a + b

try:
    print(add('199', '1'))
except TypeError as e:
    print(type(e))

@returns(int)
def add(a, b):
    return a + b

print(add(10, 5))