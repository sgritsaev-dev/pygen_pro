def convert(n):
    return tuple([bin(n).replace('0b',''), oct(n).replace('0o',''), (hex(n).replace('0x', '')).upper()])

print(convert(15))