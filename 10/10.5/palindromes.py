def palindromes():
    start = 0
    while True:
        start+=1
        if str(start)==str(start)[::-1]:
            yield start

generator = palindromes()
numbers = [next(generator) for _ in range(30)]

print(*numbers)