# Enter your code here. Read input from STDIN. Print output to STDOUT
inp1=input().split()
inp2=input().split()
l1=[]
for i in inp1:
    for j in inp2:
        l1.append((int(i),int(j)))
print(str(l1))
