def print_given(*args, **kwargs):
    for el in args:
        print(el, type(el))
    sorted_kwargs = dict(sorted(kwargs.items(), key=lambda item: item[0]))
    for el in sorted_kwargs:
        print(el, sorted_kwargs[el], type(sorted_kwargs[el]))

print_given()
print_given(1, [1, 2, 3], 'three', two=2)
print_given(b=2, d=4, c=3, a=1)