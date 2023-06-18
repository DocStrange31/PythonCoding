fpath1=input("Enter File Path of First File:")
fpath2=input("Enter File Path of Second File:")

l1=[]
with open(fpath1,"r") as myfile1:
    for line in myfile1:
        l1.append(line)               #adds each name in first file to list l1

l2=[]
with open(fpath2,"r") as myfile2:
    for line1 in myfile2:
        l2.append(line1)              #adds each name in second file to list l2

totallist=l1+l2
totallist.sort()                      #adds the two lists and sorts the final list

with open("final.txt","w") as finalfile:
    for x in totallist:
        finalfile.write(x)            #writes each element in the final list into a new file

print("The Names have been sorted and written into the file 'final.txt'")
