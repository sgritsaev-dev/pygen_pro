import itertools as it

words = sorted('hi never here my blue'.split())
for el, group in it.groupby(sorted(words, key=len), key=len):
    print(f'''{el} -> {(', '.join(word for word in group))}''')
