import os

fpath=input(r"Enter Folder Path:")
format=int(input(" Press 1 for Bytes \n Press 2 for KB \n Press 3 for MB \n Press 4 for GB \n Select Required File Size Unit: "))

files=os.scandir(fpath)  #lists all files and folders present in given root folder

dirsize={}             # will contain file sizes in dictionary format
ldir=[]                # will contain paths of all subdirectories in given directory
lfile=[]               # will contain names of all files in all subdirectories in given directory
ldirname=[]

ldir.append(fpath)     #Appends given Folder Path to ldir list

for entry in files:
    if entry.is_dir():
        if entry.path not in ldir:
            ldir.append(str(entry.path))      # if entry in 'files' list is folder, it's path is added to 'ldir' list if not already present
        if entry.name not in ldir:
            ldirname.append(str(entry.name))  # if entry in 'files' list is folder, it's name is added to 'ldirname' list if not already present

    elif entry.is_file():                     # if entry in 'files' list is file, it's name is added to 'lfile' list
        lfile.append(str(entry.name))

for xy in ldir:
    for ab in os.scandir(xy):
        if ab.is_dir():
            if ab.path not in ldir:
                ldir.append(ab.path)         # recursively adds all folder paths to 'ldir' list if not added already
            if ab.name not in ldirname:
                ldirname.append(ab.name)     # recursively adds all folder names to 'ldirname' list if not added already
        elif ab.is_file():
            lfile.append(ab.name)            # adds all file names to 'lfile' list if not added already

for t in ldir:
    dirsize[t]=0                             # adds folder paths as keys to dictionary and sets size as 0

for x in ldir:
    os.chdir(x)
    for y in lfile:
        if os.path.exists(os.path.abspath(y)):
            dirsize[x]+=os.path.getsize(y)      # file sizes are added to respective subdirectory's sizes in 'dirsize' dictionary
for u in ldir:
    os.chdir(u)
    for v in ldirname:
        if os.path.exists(os.path.abspath(v)):
            dirsize[u]+=dirsize[os.path.abspath(v)] # subdirectory's sizes are added to respective main directory's sizes
sizekb={}
sizemb={}
sizegb={}          #Dictionaries for various size units

for b in dirsize:
    sizekb[b]=(dirsize[b]/1024)

for kb in sizekb:
    sizemb[kb]=(sizekb[kb]/1024)

for mb in sizemb:
    sizegb[mb]=(sizemb[mb]/1024)

if format==1:               #Printing Directory Sizes
    print("\nThe Sizes of Directories in given Path are:")
    for d in dirsize:
        print(d+' = '+str(dirsize[d])+' Bytes')
elif format==2:
    print("\nThe Sizes of Directories in given Path are:")
    for e in sizekb:
        print(e+' = '+str(sizekb[e])+' KB')
elif format==3:
    print("\nThe Sizes of Directories in given Path are:")
    for f in sizemb:
        print(f+' = '+str(sizemb[f])+' MB')
elif format==4:
    print("\nThe Sizes of Directories in given Path are:")
    for g in sizemb:
        print(g+' = '+str(sizegb[g])+' GB')

elif format>4 or format<1:
    print("\nInvalid Key for Selecting Size Unit")