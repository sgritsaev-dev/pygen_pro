from collections import ChainMap

def get_all_values(chainmap, key):
    res = set()
    for el in chainmap.maps:
        for k in el:
            if k==key:
                res.add(el[k])
    return res



chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
print(chainmap.maps)
result = get_all_values(chainmap, 'name')

print(*sorted(result))