import os

fpath=input("Enter File Path:")
search=input("Enter Word to be Found:")

files1=os.listdir(fpath)      #lists all files in a directory and adds it to 'files1' list
l1=[]
files=[]

for f in files1:
    if f.endswith(".txt"):
        files.append(f)       #filters files which are .txt


for x in files:
    with open(fpath+"/"+x,"r") as myfile:
        for line in myfile:
            if search in line:
                l1.append(x)
                print(x)         #checks if given string is present in the file, line by line
                                 #if file is present, name of the file is added to 'files' list

print("The given word is present in the following files:")
for x in l1:
    print(x)
print(l1)