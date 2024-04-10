def filter_names(names, ignore_char, max_names):
    counter=0
    no_digits = (el for el in names if all(c.isalpha() for c in el))
    ignored = (el for el in no_digits if el[0].lower()!=ignore_char.lower())
    for el in ignored:
        if counter<max_names:
            counter+=1
            yield el
            
    

data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 'D', 3))