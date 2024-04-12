import functools

def prefix(string, to_the_end=False):
    @functools.wraps
    def decorator(func):
        def wrapper(*args, **kwargs):
            if to_the_end:
                res=func(*args, **kwargs)+string
            else:
                res=string+func(*args, **kwargs)
        return wrapper
    return decorator