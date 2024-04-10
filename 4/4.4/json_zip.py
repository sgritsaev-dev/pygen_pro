import json
with open('C:/VS code pets/edu/pygen_prof/4.3/data1.json', 'r', encoding='utf-8') as data1_json, open('C:/VS code pets/edu/pygen_prof/4.3/data2.json', 'r', encoding='utf-8') as data2_json:
    data1, data2 = json.load(data1_json), json.load(data2_json)
    data1.update(data2)
    with open('C:/VS code pets/edu/pygen_prof/4.3/data_merge.json', 'w', encoding='utf-8', newline='') as merge:
        json.dump(data1, merge)
        
        