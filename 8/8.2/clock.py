def bee(n):
    if n > 1:
        print((str(5-n)*4*n).center(16))
        bee(n - 1)
    print((str(5-n)*4*n).center(16))

bee(4)