import functools

def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            for i in range (times):
                return func(*args, **kwargs)
        return inner
    return decorator

@repeat(10)
def add(a, b):
    '''sum of two numbers'''
    return a + b
    
print(add.__name__)
print(add.__doc__)
print(add(10, b=20))