l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=[[9,8,7],[6,5,4],[3,2,1]]
l3=[]
for i in range(len(l1)):
    ltemp=[]
    for j in range(len(l1)):
        temp=0
        for k in range(len(l1)):
            temp+=l1[i][k]*l2[k][j]
        ltemp.append(temp)
    l3.append(ltemp)
for x in l3:
    print(x)