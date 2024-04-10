from itertools import islice

def take_nth(iterable, n):
    try:
        return  next(islice(iterable, n, n))
    except:
        return None