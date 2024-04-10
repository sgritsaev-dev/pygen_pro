def outer(x):
    y = 5
    z = 10

    def inner():
        nonlocal y
        y += 1
        z = 20
        print('x =', x)
        print('z =', z)
    inner()
    print('x =', x)
    print('y =', y)
    print('z =', z)


outer(5)
