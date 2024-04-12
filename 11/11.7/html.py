import re
import sys
data = [line.strip() for line in sys.stdin]
for el in data:
    x = re.search(r'''(\<(.+)\s(href="(?P<adress>.+)")\>)(?P<pointer>.+?)(<\/(\2)>)''', el)
    if x:
        print(f'''{x.group('adress')}, {x.group('pointer')}''')
