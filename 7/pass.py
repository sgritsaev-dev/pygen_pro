def is_good_password(string):
    return all((len(string)>=9, string!=string.upper(), string!=string.lower(), any(filter(str.isdigit, string))))

print(is_good_password('МойПарольСамыйЛучший111'))
print(is_good_password('мойпарольсамыйлучший'))