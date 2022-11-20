a=input("Enter String:")
l1=[]
for ch in a:
    l1.append(ch)    #adds letters individually to a list

l1.reverse()      #reverses the list
st=''.join(x for x in l1)   #joins the list elements to form a string
print(st)