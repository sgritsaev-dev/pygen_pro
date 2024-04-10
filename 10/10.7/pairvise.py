def pairwise(seq):
    seq = list(seq)
    seq_prev = list(seq[1:])
    seq_prev.append(None)
    yield from zip(seq, seq_prev)