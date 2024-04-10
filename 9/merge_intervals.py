def merge(list_of_lists):
    ss = sorted(list_of_lists, key=lambda x: (x[0], x[1]))
    new_ss=[]
    new_ss.append(ss[0])
    for i in range(1, len(ss)):
        if ss[i][1]>=new_ss[-1][1]:
            if ss[i][0]<=new_ss[-1][1]:
                new_ss[-1][1]=ss[i][1]
            elif ss[i][0]>new_ss[-1][1]:
                new_ss.append(ss[i])
    return new_ss



print(merge([[1,2],[3,6],[8,10],[15,18], [3,7], [3,10], [4,5]]))
print(merge([[1,4],[4,5]]))

#num from 1 to 10000