class DictItemsIterator():
    def __init__(self, data) -> None:
        DictItemsIterator.data = data
        DictItemsIterator.list = [el for el in data]
        DictItemsIterator.counter = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.counter+=1
        if self.counter==len(self.list):
            raise StopIteration
        try:
            return self.list[self.counter], self.data[self.list[self.counter]]
        except IndexError:
            raise StopIteration




data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}

pairs = DictItemsIterator(data)

print(tuple(pairs))

try:
    print(next(pairs))
except StopIteration:
    print('Error')