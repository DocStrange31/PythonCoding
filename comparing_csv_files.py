fpath1=input(r'Enter File Path of First CSV File:')
fpath2=input(r'Enter File Path of Second CSV FIle:')
d1={}
d2={}
with open(fpath1,'r') as myfile1:
    for line in myfile1:
        l1=line.split(',')
        d1[str(l1[0])]=str(l1[1])

with open(fpath2,'r') as myfile2:
    for line in myfile2:
        l1 = line.split(',')
        d2[str(l1[0])] = str(l1[1])

mod=[]
new=[]
delete=[]
for x in d1:
    if x in d2 and d1[x]!=d2[x]:
        mod.append(x)
    elif x not in d2:
        delete.append(x)
for x in d2:
    if x not in d1:
        new.append(x)

print('Modified Values:')
for x in mod:
    str=(x+': '+(d1[x])[:len(d1[x])-1]+' to '+d2[x])
    print(str)

print('New Values:')
for x in new:
    print(x+': '+d2[x])
print('\nDeleted Values:')
for x in delete:
    print(x+': '+d1[x])