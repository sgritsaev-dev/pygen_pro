class Square():
    def __init__(self, length):
        Square.length = length
        Square.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.length:
            self.counter += 1
            return self.counter**2
        else:
            raise StopIteration


squares = Square(10)

print(list(squares))
