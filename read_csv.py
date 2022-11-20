fpath=input(r"Enter File Path:")
linenum=int(input("Enter Line Number:"))
index=int(input("Enter Required Position:"))
with open(fpath,'r') as myfile1:
    with open('write_csv.txt','w') as myfile2:
        count=0
        for line in myfile1:
            count+=1
            if count==linenum:
                myfile2.write(line[index])

print("Required Value has been written in a new file: write_csv.txt")