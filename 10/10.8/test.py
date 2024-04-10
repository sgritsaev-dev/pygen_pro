import time

s = ['/', 'Ъ', "T", 'Я']

symbols = s*10
while True:
    symbols = '\r' + symbols.pop() + ''.join(symbols)
    print(symbols, end='')
    symbols = list(symbols)[1:]
    time.sleep(0.1)