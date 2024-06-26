def power(degree):
    def inner(number):
        return number**degree
    return inner

# INPUT DATA:


# TEST_1:
square = power(2)
print(square(5))

# TEST_2:
print(power(3)(3))

# TEST_3:
result = power(4)(2)
print(result)

# TEST_4:
result = power(2)(4)
print(result)

# TEST_5:
result = power(0)(-1)
print(result)

# TEST_6:
result = power(-2)(2)
print(result)

# TEST_7:
result = power(-2)(0.25)
print(result)

# TEST_8:
result = power(17)(17)
print(result)

# TEST_9:
result = power(1)(-2948492393)
print(result)

# TEST_10:
result = power(2)(-2948492393)
print(result)
