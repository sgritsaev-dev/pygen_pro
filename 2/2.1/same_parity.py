
def same_parity(numbers):
    parity_numbers=[]
    if len(numbers)>0:
        for el in numbers:
            x = numbers[0]
            if el%2==x%2:
                parity_numbers.append(el)
    return parity_numbers
print(same_parity([]))