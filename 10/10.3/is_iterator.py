def is_iterator(iterable):
    try:
        return iterable==iter(iterable)
    except:
        return False
    
