def reverse_args(func):
    def inner(*args, **kwargs):
        return func(*reversed(args), **dict(reversed(kwargs.items())))
    return inner


@reverse_args
def concat(a, b, c=5):
    return a + b + c


print(concat('apple', 'cherry', 'melon'))
