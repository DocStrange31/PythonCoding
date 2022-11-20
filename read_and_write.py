def myfunction(fpath):
    with open(fpath,"r") as myfile:
        for line in myfile:
            if "\n" in line:
                line=line[:len(line)-1]
            print(line)            #reads each line in list and prints it after removing extra "\n"

path=input("Enter Required File's Path:")
myfunction(path)