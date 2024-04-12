import re
res=0
numbers = input()
text = input()

a, b = int(numbers.split()[0]), int(numbers.split()[1])

re_obj = re.compile(r'\d+')

x = re_obj.findall(text, pos=a, endpos=b)
for el in x:
    res+=int(el)
print(res)