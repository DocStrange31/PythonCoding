a=input("Enter Desired String:")
l1=a.split()       #splits the string into words using <space> as indicator and adds it to a list
l2=[]
for x in l1:
    l2.append(x[::-1])   #each word is reversed and added to a second list
b=''
for ii in l2:
    b+=ii +' '      #the second list elements are joined using <space> in between each element
print(b)