import functools


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        print(f'''TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}
TRACE: возвращаемое значение {func.__name__}(): {repr(value)}''')
        return value
    return wrapper


@trace
def beegeek():
    '''beegeek docs'''
    return 'beegeek'


print(beegeek())
print(beegeek.__name__)
print(beegeek.__doc__)
