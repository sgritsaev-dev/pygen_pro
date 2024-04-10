import pickle
truf ={False:'Контрольные суммы не совпадают', True:'Контрольные суммы совпадают'}
def tryer(x, f):
    try:
        return type(f(x))==type(x)
    except:
        return False
name = 'C:/VS code pets/edu/pygen_prof/4/4.6/data.pkl'
with open(name, 'rb') as file:
    object = pickle.load(file)
    total=0
    if type(object)==list:
        oo=list(filter(lambda x: tryer(x, int), object))
        total=min(oo)*max(oo)
    elif type(object)==dict:
        o=list(object.keys())
        oo=list(filter(lambda x: tryer(x, int), o))
        total+=sum(oo)
    x = int(input())
    print(truf[total==x])