import sys
import json
data = json.loads(sys.stdin.read())
for key, value in data.items():
    if type(value)==list:
        print(f'{key}: {", ".join(value)}')
    else:
            print(f'{key}: {value}')