def parse_ranges(text):
    args = (el for el in text.split(','))
    tumples = (tuple(el.split('-')) for el in args)
    ints = (tuple(map(int, x)) for x in tumples)
    rages = map(lambda x: range(x[0], x[1]+1), ints)
    for i in rages:
        yield from i
    


print(*parse_ranges('1-2,4-4,8-10'))