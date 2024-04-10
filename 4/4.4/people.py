import json
with open('C:/VS code pets/edu/pygen_prof/4.3/people.json', 'r', encoding='utf-8') as people_json:
    people = json.load(people_json)
    nulles={}
    for el in people:
        for key in el.keys():
            nulles[key]=None
    for el in people:
        for item in nulles:
            if item not in el:
                el[item] = el.get(item, None)

    with open('C:/VS code pets/edu/pygen_prof/4.3/updated_people.json', 'w', encoding='utf-8', newline='') as updated_people:
        json.dump(people, updated_people)