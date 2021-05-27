def most_frequent(word):
    l = list(word)
    d = {}
    for i in l:
        if i in d:
            d[i]+= 1
        else:
            d[i]=1
    d1 = d.values()
    des1  = sorted(d1, reverse= True)
    print(des1)
    for i in des1:
        for k,v in d.items():
            if v==i: print(k, '=', v)
word = str(input('please enter a string: '))
most_frequent(word)
