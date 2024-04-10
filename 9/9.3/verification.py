import string

class NoLetterError(Exception):
    pass # в пароле нет ни одной буквы
class NoUpperError(Exception):
    pass # в пароле нет ни одной заглавной буквы
class NoLowerError(Exception):
    pass # в пароле нет ни одной строчной буквы
class NoDigitError(Exception):
    pass # в пароле нет ни одной цифры

def verification(login, password, success, failure):
    try: 
        if not any(filter(lambda x: x in string.ascii_letters, password)):
            raise NoLetterError('в пароле нет ни одной буквы')
        elif not any(filter(lambda x: x in string.ascii_uppercase, password)):
            raise NoUpperError('в пароле нет ни одной заглавной буквы')
        elif not any(filter(lambda x: x in string.ascii_lowercase, password)):
            raise NoLowerError('в пароле нет ни одной строчной буквы')
        elif not any(filter(lambda x: x in string.digits, password)):
            raise NoDigitError('в пароле нет ни одной цифры')
        else:
            success(login)
    except NoLetterError as nle:
        failure(login, nle)
    except NoUpperError as nue:
        failure(login, nue)
    except NoLowerError as nlwe:
        failure(login, nlwe)
    except NoDigitError as nde:
        failure(login, nde)

def success(login):
    print(f'Привет, {login}!')

def failure(login, text):
    print(f'{login}, попробуйте снова. Ошибка: {text}')

verification('timyrik20', 'Beegeek314', success, failure)
verification('timyrik20', '314', success, failure)
verification('timyrik20', 'beegeek314', success, failure)
verification('timyrik20', 'B314', success, failure)
verification('timyrik20', 'Beegeek', success, failure)
