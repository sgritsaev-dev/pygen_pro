def alternating_sequence(count=None):
    value = 1
    if count:
        for i in range(value, count+1):
            if i%2:
                yield i 
            else:
                yield -i
    else:
        while True:
            if value%2:
                yield value 
            else:
                yield -value
            value+=1


generator = alternating_sequence(10)

print(*generator)

generator = alternating_sequence()

print(next(generator))
print(next(generator))