fpath1=input("Enter File Path for First File:")
fpath2=input("Enter File Path for Second File:")

l1=[]
l2=[]
with open(fpath1,"r") as myfile1:
    for line in myfile1:
        l1.append(line)          #adds each line of first file as an element to list l1

with open(fpath2,"r") as myfile2:
    for line1 in myfile2:
        l2.append(line1)         #adds each line of second file as an element to list l2

if l1==l2:                       #checks if two lists are the same
    print("The Two Files are the Same")
else:
    print("The Two Files are Different")