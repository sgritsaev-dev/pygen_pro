from random import randint

class RandomNumbers():

    def __init__(self, left, right, numbers) -> None:
        RandomNumbers.left, RandomNumbers.right = left, right
        RandomNumbers.numbers = numbers
        RandomNumbers.counter=-1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.counter+=1
        if self.counter==self.numbers:
            raise StopIteration
        return randint(self.left, self.right)
    
iterator = RandomNumbers(1, 100, 5)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))