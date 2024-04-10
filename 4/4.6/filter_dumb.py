import pickle
def tryer(x, f):
    try:
        return type(f(x))==type(x)
    except:
        return False
def filter_dump(filename, objects, typename):
    new_objects = list(filter(lambda x: tryer(x, typename), objects))
    with open(filename, 'wb') as file:
        pickle.dump(new_objects, file)

