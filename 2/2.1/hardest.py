numbers = [7, 71, 72]
if numbers:
    maxint = 0
    for num in numbers:
        if num>maxint:
            maxint=num
    maxlen=len(str(maxint))
    numbers.sort(key=lambda x: str(x)*2, reverse=True)
    numberg = list(map(lambda x: str(x)*10, numbers))
    numberg.sort(reverse=True)
    print(numberg)
    for el in numbers:
        print(str(el)*10)
    biggest = int(''.join(str(number) for number in numbers))
    print(biggest)
else:
    print(-1)
    
