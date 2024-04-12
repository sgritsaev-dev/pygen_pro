import re

i = input()
text = input()
eng=i[0:-2]+'se'
am=i[0:-2]+'ze'
x = re.findall(fr'(\b({am})\b)|(\b({eng})\b)', text, flags=re.IGNORECASE)
print(len(x))