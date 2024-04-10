def with_previous(seq):
    seq=list(seq)
    seq_prev = list(seq[:-1])
    seq_prev.insert(0, None)
    yield from zip(seq, seq_prev)


numbers = 'dsfdgdgd'

print(*with_previous(numbers))