import re

result = re.split(r'\s*[(?:|)(?:&)(?:and)(?:or)]\s*', input())

print(*result, sep=', ')