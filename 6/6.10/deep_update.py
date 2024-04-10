from collections import ChainMap

def deep_update(chainmap, key, value):
    new_map=[]
    if key not in chainmap:
        chainmap.maps[0].setdefault(key, value)
    elif key in chainmap:
        for el in chainmap.maps:
            if key in el:
                el[key]=value
    for el in chainmap.maps:
        new_map.append(el)
    chainmap.maps.clear()
    for el in new_map:
        chainmap.maps.append(el)
    return None

chainmap = ChainMap({'name': 'Tanya'}, {'name': 'Arthur'}, {'name': 'Timur'})

deep_update(chainmap, 'name', 'Dima')

print(chainmap)