from collections import OrderedDict

def custom_sort(ordered_dict, by_values=False):
    truefalse={False:0, True:1}
    new_dick = dict(sorted(ordered_dict.items(), key=lambda item: item[truefalse[by_values]]))
    ordered_dict.clear()
    for el in new_dick:
        ordered_dict[el]=new_dick[el]
    return ordered_dict

data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
custom_sort(data)

print(data)