def filter_anagrams(word, words):
    anagrams=[]
    for el in words:
        total = 0
        for c in el:
            if c not in word:
                break
            elif c in word:
                total+=1
        for c in word: 
            if c not in el:
                break
            elif c in el:
                total-=1
        if total==0:
            anagrams.append(el)
    return anagrams    

print(filter_anagrams('крона', ['кротко', 'укроп', 'норка']))