

def add_to_list_in_dict(data, key, element):
    try:
        data[key].append(element)
    except:
        data[key] = [element]


# INPUT DATA:

# TEST_1:
data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
add_to_list_in_dict(data, 'b', 7)

print(data)

# TEST_2:
data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
add_to_list_in_dict(data, 'c', 7)

print(data)

# TEST_3:
data = {}
add_to_list_in_dict(data, 'c', 7)

print(data)

# TEST_4:
data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': []}
add_to_list_in_dict(data, 'c', 7)

print(data)

# TEST_5:
data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [4, 5, 6]}
add_to_list_in_dict(data, 'b', 'stepik')

print(data)

# TEST_6:
data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [4, 5, 6]}
add_to_list_in_dict(data, 'a', True)
add_to_list_in_dict(data, 'a', -90)
add_to_list_in_dict(data, 'b', False)
add_to_list_in_dict(data, 'b', 'beegeek')
add_to_list_in_dict(data, 'b', None)
add_to_list_in_dict(data, 'c', [])

print(data)

# TEST_7:
data = {'a': [1, 2, 3]}

add_to_list_in_dict(data, 'a', 1)
add_to_list_in_dict(data, 'a', 3)
add_to_list_in_dict(data, 'b', False)

print(data)