str=str(input())
l1=str.split()
for x in l1:
    ind=l1.index(x)
    l1[ind]=l1[ind].replace('{','')
    l1[ind]=l1[ind].replace('}','')
    l1[ind]=l1[ind].split(':')
    (l1[ind])[0]=int((l1[ind])[0])
    (l1[ind])[1]=(l1[ind])[1].replace('[','')
    (l1[ind])[1] = (l1[ind])[1].replace(']', '')
    (l1[ind])[1] = (l1[ind])[1].replace(',', ' ')
    (l1[ind])[1]=(l1[ind])[1].split()
    for y in (l1[ind])[1]:
        ind1=(l1[ind])[1].index(y)
        ((l1[ind])[1])[ind1]=int(((l1[ind])[1])[ind1])

d1={}

for x in l1:
    ind = l1.index(x)
    d1[x[0]]=x[1]