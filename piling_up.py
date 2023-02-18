def cube(x):
    print(len(x))
    last=0
    while len(x):
        if last==0:
            if x[0]>x[len(x)-1]:
                last=x[0]
                x.pop(0)
            elif x[len(x)-1]>=x[0]:
                last=x[len(x)-1]
                x.pop()
        elif last!=0:
            if last>=x[len(x)-1] and x[len(x)-1]>x[0]:
                last=x[len(x)-1]
                x.pop()
            elif last>=x[0] and x[0]>=x[len(x)-1]:
                last=x[0]
                x.pop(0)
            elif last>=x[0] and last<x[len(x)-1]:
                last=x[0]
                x.pop(0)
            elif last>=x[len(x)-1] and last<x[0]:
                last=x[len(x)-1]
                x.pop()
            elif last<x[0] and last<x[len(x)-1]:
                return 'No'
                quit()

    if len(x)==0:
        return 'Yes'
        quit()

l1=[]
for i in range(int(input())):
    num=int(input())
    l1.append(cube(input().split()))
for i in l1:
    print(i)
