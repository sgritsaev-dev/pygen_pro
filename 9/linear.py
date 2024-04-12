def linear(nested_lists):
    total=[]
    if len(nested_lists)==0:
        return []
    for el in nested_lists:
        if isinstance(el, int):
            total.append(el)
        else:
            total.extend(linear(el))
    return total


my_list = [3, [4], [5, [6, [7, 8]]]]

print(linear(my_list))