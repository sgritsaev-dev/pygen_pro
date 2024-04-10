from collections import defaultdict

def wins(pairs):
    winline = defaultdict(set)
    for winner, loser in pairs:
        winline[winner].add(loser)
    return winline

result = wins([('Тимур', 'Артур'), ('Тимур', 'Дима'), ('Дима', 'Артур')])

for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))