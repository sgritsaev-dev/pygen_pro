from collections import defaultdict
from operator import itemgetter

data = [('Books', 1343), ('Books', 1166), ('Merch', 616), ('Courses', 966), ('Merch', 1145), ('Courses', 1061), ('Books', 848), ('Courses', 964), ('Tutorials', 832), ('Merch', 642), ('Books', 815), ('Tutorials', 1041), ('Books', 1218), ('Tutorials', 880), ('Books', 1003), ('Merch', 951), ('Books', 920), ('Merch', 729), ('Tutorials', 977), ('Books', 656)]
dick = defaultdict(int)
for el in data:
    dick[el[0]]+=el[1]
sorted_dick = dict(sorted(dick.items(), key=itemgetter(0)))
for el in sorted_dick:
    print(f'{el}: ${sorted_dick[el]}')