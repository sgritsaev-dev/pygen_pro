def generator_square_polynom(a, b, c):
    def point(x):
        return a * (x**2) + b * x + c
    return point
