def to_binary(n):
    if n!=0:
        return bin(n)[2:]
    else:
        return 0

print(to_binary(256))