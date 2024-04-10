from itertools import combinations as cb


wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

cache = {1:(100,), 2:(50, 50)}

res=set()

for i in range(1, 16):
    if i not in cache:
        for el in cb(wallet, i):
            if sum(el)==100:
                res.add(el)
    else:
        res.add(cache[i])
print(len(res))