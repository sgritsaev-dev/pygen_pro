def type_checker(type, *args, **kwargs):
    return not (all(list(map(lambda x: isinstance(x, type), args))) and all(
        list(map(lambda x: isinstance(x, type), kwargs.values()))))


def value_checker(*args, **kwargs):
    return not (all(list(map(lambda x: x > 0, args))) and all(
        list(map(lambda x: x > 0, kwargs.values()))))


def takes_positive(func):
    def inner(*args, **kwargs):
        if type_checker(int, *args, **kwargs):
            raise TypeError
        elif value_checker(*args, **kwargs):
            raise ValueError
        else:
            return func(*args, **kwargs)
    return inner


# TEST_1:
@takes_positive
def positive_sum(*args):
    return sum(args)


print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# TEST_2:


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
except Exception as err:
    print(type(err))

# TEST_3:


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum('10', 20, 10))
except Exception as err:
    print(type(err))

# TEST_4:


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(10, 20, 16, 18, '10'))
except Exception as err:
    print(type(err))

# TEST_5:


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(10, 20, '16', 18, '10'))
except Exception as err:
    print(type(err))

# TEST_6:


@takes_positive
def positive_sum(*args):
    return sum(args)


print(positive_sum(*range(10, 100)))

# TEST_7:


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(3, 2, 1, -8, 1, 2, 3))
except Exception as err:
    print(type(err))

# TEST_8:


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(*range(100, -1, -1)))
except Exception as err:
    print(type(err))

# TEST_9:


@takes_positive
def positive_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep=4))

# TEST_10:


@takes_positive
def positive_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


try:
    print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep=-40))
except Exception as err:
    print(type(err))

# TEST_11:


@takes_positive
def positive_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


try:
    print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep='40'))
except Exception as err:
    print(type(err))

# TEST_12:


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(11, 20.7, 10))
except Exception as err:
    print(type(err))

# TEST_13:


@takes_positive
def power(a, n):
    return a**n


try:
    print(power(a="3", n="2"))
except Exception as err:
    print(type(err))
