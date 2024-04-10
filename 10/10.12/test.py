from itertools import combinations

numbers = range(26)

all_num_permutations = combinations(numbers, 2)
print(len(list(all_num_permutations)))
print(list(all_num_permutations))
print(len(list(all_num_permutations)))