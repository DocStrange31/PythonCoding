str=input("Enter List of Numbers for Sort:")
listin=str.split(',')
print(listin)


listbr=[]
for i in listin:
    i=int(i)
    listbr.append([i])

while len(listbr)!=1:
    for x in listbr:
        ind=listbr.index(x)
        if ind<len(listbr)-1:
            temp=listbr[ind + 1]
            x+=temp
            x.sort()
            if temp in listbr:
                listbr.remove(temp)
            print(listbr)
