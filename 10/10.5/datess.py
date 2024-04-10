from datetime import *
def dates(start, count=None):
    value=-1
    if count:
        for i in range(count):
            yield date.fromordinal(datetime.toordinal(start)+i)
    else:
        while True:
            try:
                value+=1
                yield date.fromordinal(datetime.toordinal(start)+value)
            except:
                return
            
# TEST_6:
generator = dates(date(9999, 1, 7))

for _ in range(348):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

try:
   print(next(generator))
except StopIteration:
    print('Error')