def exception_decorator(func):
    def inner(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return (res, 'Функция выполнилась без ошибок')
        except:
            return (None, 'При вызове функции произошла ошибка')
    return inner

@exception_decorator
def f(x):
    return x**2 + 2*x + 1
    
print(f(7))

sum = exception_decorator(sum)

print(sum(['199', '1', 187]))
