import re

x = input()

if re.match(r'(^Здравствуйте)|(^Доброе утро)|(^Добрый день)|(^Добрый вечер)', x, flags=re.IGNORECASE):
    print(True)
else:
    print(False)