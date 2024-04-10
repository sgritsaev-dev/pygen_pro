from itertools import combinations_with_replacement
wallet = [100, 50, 20, 10, 5]
s = 0
for i in range(0,21):
    s += sum([1 for p in set(combinations_with_replacement(wallet, i)) if sum(p) ==100])
print(s)
