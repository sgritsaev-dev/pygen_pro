def is_palindrome(word):
    if len(word)<=1:
        return True
    elif word[0]!=word[-1]:
        return False
    return is_palindrome(word[1:-1])
print(is_palindrome('level'))
