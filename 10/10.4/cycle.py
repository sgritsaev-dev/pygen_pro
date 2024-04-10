class Cycle():
    def __init__(self, data) -> None:
        Cycle.data = data
        Cycle.index=-1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.index+=1
        if self.index==len(self.data):
            self.index=0
        return self.data[self.index]
    
cycle = Cycle(range(100_000_000))

for _ in range(1000000000):
    print(next(cycle))
