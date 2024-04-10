def is_greater(lists, number):
    return any(sum(el)>number for el in lists)

data = [[-3, 4, 0, 1], [1, 1, -4], [0, 0], [9, 0]]

print(is_greater(data, 10))