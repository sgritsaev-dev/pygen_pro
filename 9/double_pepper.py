def dict_travel(data, path=''):
    sorted_data = dict(sorted(data.items(), key=lambda x: x[0]))
    for k in sorted_data:
        if isinstance(sorted_data[k], (int, str)):
            print(f'{path}{k}: {data[k]}')
        else:
            dict_travel(sorted_data[k], path + f'{k}.')




# INPUT DATA:

# TEST_1:
data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}

dict_travel(data)

# TEST_2:
data = {'d': 1, 'b': {'c': 30, 'a': 10, 'b': 20}, 'a': 100}

dict_travel(data)

# TEST_3:
data = {'b': {'c': 30, 'a': 10, 'b': {'d': 40, 'e': 50}}}

dict_travel(data)

# TEST_4:
data = {'firstname': 'Alyson', 'lastname': 'Hannigan', 'birthday': {'day': 24, 'month': 'March', 'year': 1974}}

dict_travel(data)

# TEST_5:
data = {'firstname': 'Тимур', 'lastname': 'Гуев', 'birthdate': {'day': 10, 'month': 'October', 'year': 1993},'address': {'streetaddress': 'Часовая 25, кв. 127', 'city': {'region': 'Московская область', 'type': 'город', 'cityname': 'Москва'}, 'postalcode': '125315'}}

dict_travel(data)