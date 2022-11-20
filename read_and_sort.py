fpath=input("Enter File Path:")
l1=[]
with open(fpath, "r") as myfile:
    for line in myfile:
        l1.append(line)     #adds each line to a list

for x in l1:
    c=len(x)
    if "\n" in x:
        l1[l1.index(x)]=x[:c-1]         #removes the extra \n wherever present

l1.sort(reverse=True)    #sorts list in reverse order
for t in l1:
    print(t)