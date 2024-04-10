def convert(text):
    upper=0
    lower=0
    result=''
    for c in text:
        if c.isalpha():
            if c.islower():
                lower+=1
            if c.isupper():
                upper+=1
        result+=c
    if lower>=upper:
        result = result.lower()
    else:
        result = result.upper()
    return result

print(convert('PUFUFdfFDSDKNFDSgdfgfd31415!'))