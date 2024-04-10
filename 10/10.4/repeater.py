class Repeater:
    def __init__(self, text):
        Repeater.text = text

    def __iter__(self):
        return self

    def __next__(self):
        return self.text
    
geek = Repeater('geek')

print(next(geek))
print(next(geek))
print(next(geek))