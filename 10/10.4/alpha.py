class Alphabet():

    def __init__(self, language) -> None:
        Alphabet.language = language
        Alphabet.data = {'en': 'abcdefghijklmnopqrstuvwxyz', 'ru': 'абвгдежзийклмнопрстуфхцчшщъыьэюя'}
        Alphabet.counter = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.counter+=1
        if self.counter==len(self.data[self.language]):
            self.counter=0
        return self.data[self.language][self.counter]
    
en_alpha = Alphabet('en')

letters = [next(en_alpha) for _ in range(28)]

print(*letters)