def get_digits(number: int | float) -> list:
    return list(int(el) for el in str(number))


print(get_digits(1342))
