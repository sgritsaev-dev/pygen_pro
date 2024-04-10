from functools import lru_cache
class Fibonacci():
    def __init__(self) -> None:
        Fibonacci.first=1
        Fibonacci.second=0

    def __iter__(self):
        return self
    
    # @lru_cache
    def __next__(self):
        self.first, self.second = self.second, (self.first+self.second)
        return self.second


fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
