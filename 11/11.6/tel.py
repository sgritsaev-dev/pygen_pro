from re import match
import sys
data = [line.strip() for line in sys.stdin]
for el in data:
    telmatch = match(
        r"(?P<country_code>\d+)([ -]){1}(?P<city_code>\d+)(\2){1}(?P<number>\d+)", el)
    print(
        f'''Код страны: {
            telmatch.group('country_code')}, Код города: {
            telmatch.group('city_code')}, Номер: {
                telmatch.group('number')}''')
