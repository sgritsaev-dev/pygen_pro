fun = input()
arguments = list(map(int, input().split()))
res = list()
for i in range(arguments[0], arguments[1]+1):
    x=i
    res.append(eval(fun))
print(f'''Минимальное значение функции {fun} на отрезке [{arguments[0]}, {arguments[1]}] равно {min(res)}
Максимальное значение функции {fun} на отрезке [{arguments[0]}, {arguments[1]}] равно {max(res)}''')



