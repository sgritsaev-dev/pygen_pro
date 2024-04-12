import re

result = re.split(r'(\w+)\1', 're pypy py rere re')

print(result)