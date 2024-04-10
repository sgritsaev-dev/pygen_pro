import copy


def sort_priority(values, group):
    head = []
    nums = copy.deepcopy(values)
    values.clear()
    for el in sorted(list(group)):
        if el in nums:
            head.append(el)
            nums.remove(el)
    values.extend(head + sorted(nums))


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {5, 7, 2, 3}
sort_priority(numbers, group)

print(numbers)


[2, 3, 5, 7, 1, 4, 6, 8]
