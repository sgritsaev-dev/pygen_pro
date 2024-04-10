import copy

data1 = [[1, 2, 3], [4, 5, 6]]
data2 = copy.deepcopy(data1)

data1[0].append(7)
data2[1].append(8)

print(id(data1), data1)
print(id(data2), data2)