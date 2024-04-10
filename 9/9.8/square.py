import functools
def square(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        return func(*args, **kwargs)**2
    return inner