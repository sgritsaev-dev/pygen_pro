import functools

def strip_range(start, end, char='.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            new_res=''
            for i in range(len(res)):
                if i in range(start, end):
                    new_res+=char
                else:
                    new_res+=res[i]
            return new_res
        return wrapper
    return decorator
                





@strip_range(3, 20, '_')
def beegeek():
    return 'beegeek'
    
print(beegeek())