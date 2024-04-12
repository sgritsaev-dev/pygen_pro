name = input()
try:
    with open(name, encoding='utf-8') as file:
        print(file.read())
except:
    print('Файл не найден')