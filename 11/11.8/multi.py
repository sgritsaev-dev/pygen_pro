import re

string = 'hello3(world)hi'

def multi(match_obj):
    x = re.match(r'\d+', match_obj.group(0))
    y = re.search(r'\((?P<word>\w+)\)', match_obj.group(0))
    return int(x.group(0))*y.group('word')
string = re.sub(r'\d+\(\w+\)', multi, string)
print(string)
