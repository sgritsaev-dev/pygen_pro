def get_min_max(data):
    spisok = list()
    if data:
        spisok.append(data.index(min(data)))
        spisok.append(data.index(max(data)))
        return tuple(spisok)
        
    
# INPUT DATA:

# TEST_1:
data = [2, 3, 8, 1, 7]

print(get_min_max(data))

# TEST_2:
data = [1, 1, 2, 3, 8, 8]

print(get_min_max(data))

# TEST_3:
data = [9]

print(get_min_max(data))

# TEST_4:
data = []

print(get_min_max(data))

# TEST_5:
data = [9, 9, 9, 9, 9]

print(get_min_max(data))

# TEST_6:
data = list(range(1, 101))

print(get_min_max(data))

# TEST_7:
data = list(range(1, 101))[::-1]

print(get_min_max(data))

# TEST_8:
data = [-86, -51, 33, -23, 40, 96, 19, -65, 26, 12, -93, 68, 82, 47, -58, -37, -100, 5, 75, 54, -79, -72, -2, 61, -16, -9, 89, -44, -30]

print(get_min_max(data))

# TEST_9:
data = [-86, -51, 33, -23, 40, 96, 19, -65, 26, 12, -93, 68, 82, 47, -58, -37, -100, 5, 75, 54, -79, -72, -2, 61, -16, -9, 89, -44, -30, -100, 96, -100, 1, 2, -99, 96]

print(get_min_max(data))