import re

text = input()
i = input()

x = re.findall(fr'\B{i}\B', text)
print(len(x))