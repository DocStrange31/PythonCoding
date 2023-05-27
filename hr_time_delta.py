t1=input()
t2=input()
t1=t1.split()
t2=t2.split()
print(t1,t2)
yrdiff=(int(t2[3])-int(t1[3]))*31557600
def mon(x):
    if x[2]=='Jan':
        x[2]=1
    elif x[2]=='Feb':
        x[2]=2
    elif x[2]=='Mar':
        x[2]=3
    elif x[2]=='Apr':
        x[2]=4
    elif x[2]=='May':
        x[2]=5
    elif x[2]=='Jun':
        x[2]=6
    elif x[2]=='Jul':
        x[2]=7
    elif x[2]=='Aug':
        x[2]=8
    elif x[2]=='Sep':
        x[2]=9
    elif x[2]=='Oct':
        x[2]=10
    elif x[2]=='Nov':
        x[2]=11
    elif x[2]=='Dec':
        x[2]=12
mon(t1)
mon(t2)
if t2[2]%2==0 and t1[2]%2!=0:
    mondiff=
daydiff=(int(t2[1])-int(t1[1]))*86400
