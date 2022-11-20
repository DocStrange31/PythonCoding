import os

fpath=input(r"Enter File Path:")

files=os.scandir(fpath)
lfile=[]
ldir=[]

for x in files:
    if x.is_dir():
        ldir.append(x.path)
    else:
        lfile.append(x.path)

for ab in ldir:
    for a in os.scandir(ab):
        if a.is_dir():
            ldir.append(a.path)
        else:
            lfile.append(a.path)

b=(".mp4",".mov",".mkv",".avi")
print("The Following are Movie Files found in given Directory:")
for y in lfile:
    if y.endswith(b):
        print(y)