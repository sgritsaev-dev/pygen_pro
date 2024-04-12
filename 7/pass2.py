import sys

class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass

def is_good_password(string):
    if not len(string)>=9:
        raise LengthError
    elif not (string!=string.upper() and string!=string.lower()):
        raise LetterError
    elif not any(filter(str.isdigit, string)):
        raise DigitError
    else:
        return True
    
for el in sys.stdin:
    try:
        print(is_good_password(el))
    except Exception as err:
        print(type(err))