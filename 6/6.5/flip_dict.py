from collections import defaultdict

def flip_dict(dict_of_lists):
    flipped = defaultdict(list)
    for key, value in dict_of_lists.items():
        for el in value:
            flipped[el].append(key)
    return flipped

data = {'Arthur': ['cacao', 'tea', 'juice'], 'Timur': ['coffee', 'tea', 'juice'], 'Anri': ['juice', 'coffee']}

for key, values in flip_dict(data).items():
    print(f'{key}: {", ".join(values)}')