def txt_to_dict():
    with open('C:/VS code pets/edu/pygen_prof/10/10.7/planets.txt', encoding='utf-8') as planets:
        counter=0
        dic={}
        for el in planets:
            if not el.isspace():
                counter+=1
                dic[el.split(' = ')[0]]=(el.split(' = ')[1]).strip()
                if counter==4:
                    counter=0
                    yield dic
                    dic={}

planets = txt_to_dict()

print(next(planets))
print(next(planets))
print(next(planets))