import json

name = input()
try:
    with open(name, encoding='utf-8') as file:
        try:
            lines = json.dumps(file)
            print(file)
        except ValueError('Ошибка при десериализации') as v:
            print(v)
except FileNotFoundError('Файл не найден') as f:
    print(f)