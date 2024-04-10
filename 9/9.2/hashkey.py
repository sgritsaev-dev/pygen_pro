def hash_as_key(data):
    dic = {}
    for el in data:
        if list(map(lambda x: hash(x), data)).count(hash(el))==1:
            dic[hash(el)]=el
        else:
            dic.setdefault(hash(el), []).append(el)
    return dic




data = [-1, -2, -3, -4, -5]

print(hash_as_key(data))

{1: 1, 2: 2, 3: 3, 4: 4, 5: [5, 5]}