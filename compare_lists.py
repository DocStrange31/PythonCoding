str=input('Enter Values of First List:')
l1=str.split(',')
str1=input('Enter Values of Second List:')
l2=str1.split(',')
for x in l1:
    ind=l1.index(x)
    l1[ind]=int(x)
for x in l2:
    ind=l2.index(x)
    l2[ind]=int(x)

com=[]
dif=[]
for x in l1:
    if x in l2:
        com.append(x)
    else:
        dif.append(x)
for x in l2:
    if x not in l1:
        dif.append(x)
print('Common Values are:')
for x in com:
    print(x)
print('Uncommon Values are:')
for x in dif:
    print(x)