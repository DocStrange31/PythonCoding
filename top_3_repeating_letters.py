    s = input()
    d1 = {}
    for i in s:
        if s.count(i) not in d1:
            d1[s.count(i)] = i
        elif s.count(i) in d1:
            if i not in d1[s.count(i)]:
                d1[s.count(i)] +=i
    l1 = d1.keys()
    l1 = list(l1)
    l1.sort(reverse=True)
    l2=[]
    for i in l1[:3]:
        if len(d1[i])==1:
            l2.append(d1[i]+' '+str(i))
        else:
            for k in sorted(d1[i]):
                l2.append(k+' '+str(i))
    for i in l2[:3]:
        print(i)