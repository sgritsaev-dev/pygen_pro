import re

def abbreviate(phrase):
    x = re.finditer(r'([A-Z])|\b([a-zA-Z])', phrase)
    res=''
    for el in x:
        res+=(el.group()).upper()
    return res
print(abbreviate('javaScript object notation'))
