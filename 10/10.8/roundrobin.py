import itertools as it

def roundrobin(*args):
    for el in it.zip_longest(*args, fillvalue='mazafaka'):
        if 'mazafaka' in el:
            el=list(el)
            try:
                for i in range(1000):
                    el.pop(el.index('mazafaka'))
            except:
                pass
        yield from el

print(*roundrobin('abc', 'd', 'ef'))