def numbers_sum(elem):
    '''Принимает список и возвращает сумму его чисел (int, float),
игнорируя нечисловые объекты. 0 - если в списке чисел нет.'''
    return sum(filter(lambda x: isinstance(x, int) or isinstance(x, float), elem))

print(numbers_sum([ '2', 'five']))