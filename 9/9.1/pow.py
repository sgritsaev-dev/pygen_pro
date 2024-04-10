def my_pow(number):
    total=0
    for el in enumerate(str(number)):
        total+=pow(int(el[1]), el[0]+1)
    return total
    
print(my_pow(123))