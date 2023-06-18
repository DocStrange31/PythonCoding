fpath=input("Enter File Path:")
l1=[]
with open(fpath,"r") as myfile:
    for line in myfile:
        l1.extend(line.split())
a=input("Enter word to be counted:")
print(l1.count(a))