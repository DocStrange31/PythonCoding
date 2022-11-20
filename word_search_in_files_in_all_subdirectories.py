import os

fpath=input(r"Enter File Path:")
find=input("Enter String to be Searched:")
files=os.scandir(fpath)
lfile=[]        # list for file paths
ldir=[]         # list for folder paths
final=[]        # final list of file paths which contain given string

for x in files:
    if x.is_dir():
        ldir.append(x.path)            # adds paths of folders present in root folder
    else:
        lfile.append(x.path)           # adds paths of files present in root folder

for ab in ldir:
    for a in os.scandir(ab):
        if a.is_dir():
            ldir.append(a.path)        # adds paths of all subdirectories present in given folder
        else:
            lfile.append(a.path)       # adds paths of all files present in given folder

for entry in lfile:
    with open(entry,"r") as myfile:
        for line in myfile:
            if find in line:
                if entry not in final:
                    final.append(entry)  # opens each file and checks line by line if given string present

print("The Following Files Contain the Specified String:")
for y in final:
    print(os.path.basename(y))      # prints file name from file path