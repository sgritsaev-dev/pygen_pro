import sys
spisok=[int(el.strip()) for el in sys.stdin]
new_spisok=spisok[:spisok.index(0)]
def printer(list_, length):
    def counter(start):
        if start<length:
            print(f'Элемент {start}: {list_[start]}')
            counter(start+1)
    counter(0)
    
printer(reversed(spisok), len(spisok))