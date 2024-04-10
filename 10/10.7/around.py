def around(seq):
    seq = list(seq)
    seq_for = list(seq[1:])
    seq_for.append(None)
    seq_prev = list(seq[:-1])
    seq_prev.insert(0, None)
    yield from zip(seq_prev, seq, seq_for)

numbers = [1, 2, 3, 4, 5]

print(*around(numbers))