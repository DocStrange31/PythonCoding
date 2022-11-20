import os

fpath=input(r"Enter File Path:")
find=input("Enter File Extension after '.' :")
files=os.scandir(fpath)
lfile=[]
ldir=[]

for x in files:
    if x.is_dir():
        ldir.append(x.path)
    else:
        lfile.append(x.name)

for ab in ldir:
    for a in os.scandir(ab):
        if a.is_dir():
            ldir.append(a.path)
        else:
            lfile.append(a.name)

search=0
for t in lfile:
    if t.endswith("."+find):
        search+=1

print("Total Number of Files with Given Extension = "+str(search))
