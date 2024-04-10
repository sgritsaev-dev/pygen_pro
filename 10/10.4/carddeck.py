class CardDeck():
    def __init__(self) -> None:
        CardDeck.keys=["пик", "треф", "бубен", "червей"]
        CardDeck.values=["2","3","4","5","6","7","8","9","10","валет", "дама", "король", "туз"]
        CardDeck.key_counter = 0
        CardDeck.value_counter = -1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.value_counter+=1
        if self.value_counter==len(self.values):
            self.value_counter=0
            self.key_counter+=1
        if self.key_counter==4:
            raise StopIteration
        return f'{self.values[self.value_counter]} {self.keys[self.key_counter]}'
    
cards = CardDeck()

print(*cards)
