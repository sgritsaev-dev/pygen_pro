from collections import Counter

def mini():
    newline={}
    for el in sorted(data.most_common()[-1:-(list(data.values()).count(min(data.values())))-1:-1]):
        newline[el[0]]=el[1]
    return (list(newline.items()))

def maxi():
    newline={}
    for el in sorted(data.most_common()[0:(list(data.values()).count(max(data.values())))]):
        newline[el[0]]=el[1]
    return (list(newline.items()))

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')
data.min_values = mini
data.max_values = maxi
data['t'] += 1
print(data.min_values())
print(data.max_values())