from collections import ChainMap

def get_value(chainmap, key, from_left=True):
    if key in chainmap:
        if from_left:
            for el in chainmap.maps:
                if key in el:
                    return el[key]
        else:
            for el in list(reversed(chainmap.maps)):
                if key in el:
                    return el[key]
    else:
        return None
    








# INPUT DATA:

# TEST_1:
chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'name'))

# TEST_2:
chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'name', False))

# TEST_3:
chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'age'))

# TEST_4:
chainmap = ChainMap({'name': 'Arthur'})

print(get_value(chainmap, 'name', False))

# TEST_5:
chainmap = ChainMap({'age': 20}, {'city': 'Moscow'}, {'name': 'Anri', 'age': 20}, {'name': 'Timur', 'age': 29})

print(get_value(chainmap, 'name'))

# TEST_6:
chainmap = ChainMap({'age': 20}, {'city': 'Moscow'}, {'name': 'Anri', 'age': 20}, {'name': 'Timur', 'age': 29})

print(get_value(chainmap, 'age', False))