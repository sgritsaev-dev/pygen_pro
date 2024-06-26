class Xrange():

    def __init__(self, start, end, step=1) -> None:
        Xrange.start = start
        Xrange.end = end
        Xrange.step = step
        if any((isinstance(start, float), isinstance(
                end, float), isinstance(step, float))):
            start = float(start)
            end = float(end)
            step = float(step)
        Xrange.flag = Xrange.start - Xrange.step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            self.flag += self.step
            if self.flag >= self.end:
                raise StopIteration
            return self.flag
        if self.start > self.end:
            self.flag += self.step
            if self.flag <= self.end:
                raise StopIteration
            return self.flag

# INPUT DATA:


# TEST_1:
evens = Xrange(0, 10, 2)

print(*evens)

# TEST_2:
xrange = Xrange(0, 3, 0.5)

print(*xrange, sep='; ')

# TEST_3:
xrange = Xrange(10, 1, -1)

print(*xrange)

# TEST_4:
xrange = Xrange(5, 10)

print(*xrange)

# TEST_5:
xrange = Xrange(-20, 12, 4)

print(*xrange)

# TEST_6:
xrange = Xrange(-50, -10, 5)

print(*xrange)

# TEST_7:
xrange = Xrange(-50, -49)

print(*xrange)

# TEST_8:
xrange = Xrange(-50, -48, 2)

print(*xrange)

# TEST_9:
xrange = Xrange(100, 101)

print(*xrange)

# TEST_10:
xrange = Xrange(0, 1)

print(*xrange)

# TEST_11:
xrange = Xrange(-1, 0)

print(*xrange)

# TEST_12:
xrange = Xrange(200, 202, 2)

print(*xrange)

# TEST_13:
xrange = Xrange(24, 89, 13)

print(list(xrange))

# TEST_14:
xrange = Xrange(100, 10, -1)

print(list(xrange))

# TEST_15:
xrange = Xrange(10, -21, -6)

print(list(xrange))

# TEST_16:
xrange = Xrange(1, 0, -1)

print(list(xrange))

# TEST_17:
xrange = Xrange(0, -1, -1)

print(list(xrange))

# TEST_18:
xrange = Xrange(5, 50, 1.5)

print(list(xrange))

# TEST_19:
xrange = Xrange(5, 48.5, 1.5)

print(tuple(xrange))

# TEST_20:
xrange = Xrange(5, 48.51, 1.5)

print(tuple(xrange))

# TEST_21:
xrange = Xrange(5.0, 56, 2.0)

print(tuple(xrange))

# TEST_22:
xrange = Xrange(5.1, 55, 1.1)

print(tuple(xrange))

# TEST_23:
xrange = Xrange(5.1, 55.8, 1.1)

print(tuple(xrange))

# TEST_24:
xrange = Xrange(5.9, 44, 3)

print(tuple(xrange))

# TEST_25:
xrange = Xrange(32.9, 99.9, 4.5)

print(*xrange)

# TEST_26:
xrange = Xrange(100.1, 13.7, -3.8)

print(*xrange)

# TEST_27:
xrange = Xrange(100.1, -18.7, -5.6)

print(*xrange)

# TEST_28:
xrange = Xrange(1.0, 0.0, -1.0)

print(*xrange)

# TEST_29:
xrange = Xrange(0.0, 1.0)

print(*xrange)

# TEST_30:
xrange = Xrange(0, 1.0)

print(*xrange)

# TEST_31:
xrange = Xrange(-10, 20)

print(*xrange)

# TEST_32:
xrange = Xrange(-20, 13, 4)

print(*xrange)

# TEST_33:
xrange = Xrange(1, 5)

next(xrange)
next(xrange)
next(xrange)
next(xrange)

try:
    next(xrange)
except StopIteration:
    print('Error')

# TEST_34:
xrange = Xrange(5, 1, -1)

next(xrange)
next(xrange)
next(xrange)
next(xrange)

try:
    next(xrange)
except StopIteration:
    print('Error')
