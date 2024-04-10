from functools import lru_cache
@lru_cache
def ways(number):
    if number<=3:
        return 1
    if number==4:
        return 2
    else:
        return ways(number-1)+ways(number-3)+ways(number-4)
print(ways(50))
# INPUT DATA:

# TEST_1:
print(ways(5))

# TEST_2:
print(ways(1))

# TEST_3:
print(ways(2))

# TEST_4:
print(ways(50))

# TEST_5:
print(ways(100))

# TEST_6:
print(ways(4))

# TEST_7:
print(ways(3))

# TEST_8:
print(ways(6))

# TEST_9:
print(ways(7))
    
