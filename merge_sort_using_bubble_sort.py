str=input("Enter List of Numbers for Sort:")
listin=str.split(',')

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
            a = 0
            while a == 0:  # loops the program until the original list is unchanged after the iteration
                l2 = list(x)  # records list before program begins
                for b in range(len(x)):
                    if b < len(x) - 1:
                        first = x[b]
                        second = x[b + 1]
                        if first > second:
                            x[b] = second
                            x[b + 1] = first
                if l2==x:
                    a=1

            if temp in listbr:
                listbr.remove(temp)

print(listbr[0])