import functools

def add_attrs(**kwattrs):
    def decorator(func):
        for key, value in kwattrs.items():
            func.__dict__[key]=value
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator

@add_attrs(dj='bee', attr2='geek')
def beegeek():
    return 'beegeek'
    
print(beegeek.__dict__)
print(beegeek)