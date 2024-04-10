def upper(func):
    def inner(*args, **kwargs):
        new_args = (el.upper() if type(el) == str else el for el in args)
        new_kwargs = {
            key: value.upper() if type(value) == str else value for key,
            value in kwargs.items()}
        res = func(*new_args, **new_kwargs)
        return res
    return inner


print = upper(print)
print('hi1', 'there', 1, end='5')
