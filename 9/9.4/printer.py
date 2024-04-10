old_print = print

def print(*args, **kwargs):
    caps = tuple(c.upper() if isinstance(c, str) else c for c in args)
    if kwargs:
        kwargs['end']=kwargs['end'].upper()
        kwargs['sep']=kwargs['sep'].upper()
        return old_print(*caps, sep=kwargs['sep'], end=kwargs['end'])
    else:
        return old_print(*caps)
    

words = ('black', 'white', 'grey', 'black-1', 'white-1', 'python')
print(*words, sep=' to ', end=' LOVE')
