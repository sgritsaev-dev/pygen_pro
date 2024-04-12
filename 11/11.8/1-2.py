import re

string = input()

string = re.sub(r'\b(\w)(\w)(\w*)\b', r'\2\1\3', string)
print(string)