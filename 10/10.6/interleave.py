def interleave(*seqs):
    return (i for el in zip(*seqs) for i in el)


numbers = [1, 2, 3]
squares = [1, 4, 9]
qubes = [1, 8, 27]

print(*interleave(numbers, squares, qubes))