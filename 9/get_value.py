def get_value(dic, hash):
    if hash in dic:
        return dic[hash]
    for v in dic.values():
        if type(v) == dict:
            value = get_value(v, hash)   
            if value is not None:
                return value



data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'birthDate': {'day': 10, 'month': 'October', 'year': 1993}, 'address': {'streetAddress': 'Часовая 25, кв. 127', 'city': {'region': 'Московская область', 'type': 'город', 'cityName': 'Москва'}, 'postalCode': '125315'}}

print(get_value(data, 'cityName'))