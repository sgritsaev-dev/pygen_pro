def is_power(n):
    if n<2:
        if n==1:
            return True
        else:
            return False
    return is_power(n/2)
print(is_power(513))