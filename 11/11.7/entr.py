import re

text = input()
i = input()

x = re.findall(fr'\b({i})\b', text)
print(len(x))