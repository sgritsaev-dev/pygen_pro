import re

def normalize_whitespace(text):
    return re.sub(r'( ){1,}', r' ', text)

print(normalize_whitespace('AAAA                A                AAAA'))