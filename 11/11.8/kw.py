from keyword import kwlist as kw
import re

string = input()
for el in kw:
    string = re.sub(fr'\b{el}\b', r'<kw>', string, flags=re.I)

print(string)