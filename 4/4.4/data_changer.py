import json
def stringer(x):
    return x+'!'
def inter(x):
    return x+1
def booler(x):
    return not x
def lister(x):
    return x*2
def dicter(x):
    x['newkey']=None
    return x
def nuller(x):
    0+0
el_types={str:stringer, int:inter, bool:booler, list:lister, dict:dicter, type(None):nuller}
with open('C:/VS code pets/edu/pygen_prof/4.3/data.json', 'r', encoding='utf-8') as data_json:
    data = json.load(data_json)
    new_data=[]
    for el in data:
        if el_types[type(el)](el)!=None:
          new_data.append(el_types[type(el)](el))
    with open('C:/VS code pets/edu/pygen_prof/4.3/updated_data.json', 'w', encoding='utf-8', newline='') as updated_data:
        json.dump(new_data, updated_data)
