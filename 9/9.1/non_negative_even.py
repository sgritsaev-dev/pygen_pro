def non_negative_even(numbers):
    return all(list(map(lambda x: x%2==0 and x>=0, numbers)))

print(non_negative_even([0, 2, 4, 8, 16, -1]))