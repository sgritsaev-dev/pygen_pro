def recursive_sum(nested_lists):
    total=0
    if len(nested_lists)==0:
        return 0
    for el in nested_lists:
        if isinstance(el, int):
            total+=el
        else:
            total+=recursive_sum(el)
    return total

        
my_list = [1, [4, 4], 2, [1, [2, 10]]]

print(recursive_sum(my_list))