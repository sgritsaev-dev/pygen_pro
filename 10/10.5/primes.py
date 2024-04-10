def spliter_amount(x):
    spisok=[]
    for i in range(1, x+1):
        if x%i==0:
            spisok.append(i)
    return len(spisok)
def primes(left, right):
    for j in range(left, right+1):
        if spliter_amount(j)==2:
            yield j

generator = primes(1, 15)

print(*generator)

generator = primes(6, 36)
print(next(generator))
print(next(generator))
