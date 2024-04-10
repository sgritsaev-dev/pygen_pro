def reverse(sequence):
    for i in range (-1, -len(sequence)-1,-1):
        yield sequence[i]


generator = reverse('beegeek')

print(type(generator))
print(*generator)