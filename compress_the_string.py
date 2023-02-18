inp=input()
l1=[]
str1=''
c=0
for i in inp:
    c+=1
    if c==1:
        str1+=i
        if len(inp)==1:
            l1.append(str1)
    else:
        if i==str1[len(str1)-1]:
            str1+=i
            if len(inp)==c:
                l1.append(str1)
        else:
            l1.append(str1)
            str1=i
            if len(inp)==c:
                l1.append(str1)
for i in l1:
    print((len(i),int(i[0])),end=' ')