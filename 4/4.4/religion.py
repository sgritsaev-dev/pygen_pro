import json
with open('C:/VS code pets/edu/pygen_prof/4/4.4/countries.json', 'r', encoding='utf-8') as countries_json:
    countries = json.load(countries_json)
    new_countries={}
    for el in countries:
        el[el['religion']]=el['country']
        del el['country']
        del el['religion']
    for el in countries:
        for country in el:
            new_countries[country]=new_countries.get(country, [])+[el[country]]
    with open('C:/VS code pets/edu/pygen_prof/4/4.4/religions.json', 'w', encoding='utf-8', newline='') as religions:
        json.dump(new_countries, religions)