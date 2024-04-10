import functools


def returns_string(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, str):
            return (res)
        else:
            raise TypeError
    return inner
