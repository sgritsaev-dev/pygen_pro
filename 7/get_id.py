def get_id(names, name):
    total = 0
    if isinstance(name, str):
        if name[0].isupper() and name[0].isalpha():
            total+=1
            for el in name[1:]:
                if el.isalpha() and el.islower():
                    total+=1
        if total==len(name):
            return len(names)+1
        else:
            raise ValueError('Имя не является корректным')
    else:
        raise TypeError('Имя не является строкой')
    
# TEST_1:
names = ['Timur', 'Anri', 'Dima']
name = 'Arthur'

print(get_id(names, name))

# TEST_2:
names = ['Timur', 'Anri', 'Dima', 'Arthur']
name = 'Ruslan1337'

try:
    print(get_id(names, name))
except ValueError as e:
    print(e)

# TEST_3:
names = ['Timur', 'Anri', 'Dima', 'Arthur', 'Ruslan']
name = ['E', 'd', 'u', 'a', 'r', 'd']

try:
    print(get_id(names, name))
except TypeError as e:
    print(e)

# TEST_4:
names = ['Timur', 'Anri', 'Dima', 'Arthur']
name = 'ruslan'

try:
    print(get_id(names, name))
except ValueError as e:
    print(e)

# TEST_5:
names = ['Timur', 'Anri', 'Dima', 'Arthur']
name = 'RuSlan'

try:
    print(get_id(names, name))
except ValueError as e:
    print(e)

# TEST_6:
names = ['Timur', 'Anri', 'Dima', 'Arthur']
name = '123Ruslan'

try:
    print(get_id(names, name))
except ValueError as e:
    print(e)

# TEST_7:
names = ['Timur', 'Anri', 'Dima', 'Arthur', 'Ruslan']
name = False

try:
    print(get_id(names, name))
except TypeError as e:
    print(e)

# TEST_8:
names = ['Timur', 'Anri', 'Dima', 'Arthur', 'Ruslan']
name = 69

try:
    print(get_id(names, name))
except TypeError as e:
    print(e)

# TEST_9:
names = ['Timur', 'Anri', 'Dima', 'Arthur', 'Ruslan']
name = ['Roman']

try:
    print(get_id(names, name))
except TypeError as e:
    print(e)

# TEST_10:
names = []
name = 'Arthur'

print(get_id(names, name))

# TEST_11:
names = ['Timur']
name = 'Arthur'

print(get_id(names, name))

# TEST_12:
names = ['Timur', 'Anri', 'Dima', 'Roma', 'Gvido', 'Rosy', 'Soslan', 'Natasha', 'Arthur']
name = 'Arthur'

print(get_id(names, name))

# TEST_13:
names = ['Timur', 'Timur', 'Timur', 'Timur', 'Timur']
name = 'Timur'

print(get_id(names, name))