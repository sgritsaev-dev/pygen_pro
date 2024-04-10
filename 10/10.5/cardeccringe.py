def card_deck(suit):
    keys=["пик", "треф", "бубен", "червей"]
    keys.remove(suit)
    values=["2","3","4","5","6","7","8","9","10","валет", "дама", "король", "туз"]
    key_counter = 0
    value_counter = -1
    while True:
        value_counter+=1
        if value_counter>=len(values):
            value_counter=0
            key_counter+=1
        if key_counter==3:
            key_counter=0
        yield f'{values[value_counter]} {keys[key_counter]}'
    

generator = card_deck('треф')
cards = [next(generator) for _ in range(43)]

print(*cards)