import pickle
from collections import namedtuple
Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open('C:/VS code pets/edu/pygen_prof/6/6.4/data.pkl', 'rb') as data:
    lines = pickle.load(data)
    for line in lines:
        for key, value in Animal._asdict(line).items():
            print(f'{key}: {value}')
        print()