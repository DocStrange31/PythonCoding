str=input("Enter elements of List seperated by ',':")
l1=str.split(',')
for x in l1:
    ind=l1.index(x)
    temp=x
    for y in range(ind+1,len(l1)):
        if l1[y]<temp:
            temp=l1[y]
    if temp!=x:
        l1[l1.index(temp)]=x
        l1[ind]=temp

print(l1)