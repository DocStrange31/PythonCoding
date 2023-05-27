linenum=int(input("Enter Number of Lines:"))

z=linenum
a=1
b=2
str2=""
charnum=2*z-1
if z % 2 == 0:
    for d in range(int((charnum + 1) / 2 - 1)):
        str2 += str(b) + " "
        b += 2
    for x in range(int((charnum + 1) / 2)):
        str2 += str(b) + " "
        b -= 2
    print(str2)
if z % 2 != 0:
    for y in range(int((charnum + 1) / 2 - 1)):
        str2 += str(a) + " "
        a += 2
    for y in range(int((charnum + 1) / 2)):
        str2 += str(a) + " "
        a -= 2


for i in range(1,linenum+1):
    a=1
    b=2
    charnum=2*i-1
    str1=""
    spaces=(linenum+1)*2-2*i

    if i%2==0:
        str1 += " " * spaces
        for x in range(int((charnum+1)/2-1)):
            str1+=str(b)+" "
            b+=2
        for x in range(int((charnum+1)/2)):
            str1+=str(b)+" "
            b-=2
        str1 += " " * (spaces - 1)
        print(str1)
    if i%2!=0:
        str1 += " " * spaces
        for y in range(int((charnum+1)/2-1)):
            str1+=str(a)+" "
            a+=2
        for y in range(int((charnum+1)/2)):
            str1+=str(a)+" "
            a-=2
        str1 += " " * (spaces - 1)
        print(str1)

for j in range(linenum-1,0,-1):
    a=1
    b=2
    charnum = 2 * j - 1
    str1 = ""
    spaces = (linenum+1) * 2 - 2 * j
    if j % 2 == 0:
        str1 += " " * spaces
        for x in range(int((charnum + 1) / 2 - 1)):
            str1 += str(b) + " "
            b += 2
        for x in range(int((charnum + 1) / 2)):
            str1 += str(b) + " "
            b -= 2
        str1 += " " * (spaces-1)
        print(str1)
    if j % 2 != 0:
        str1 += " " * spaces
        for y in range(int((charnum + 1) / 2 - 1)):
            str1 += str(a) + " "
            a += 2
        for y in range(int((charnum + 1) / 2)):
            str1 += str(a) + " "
            a -= 2
        str1 += " " * (spaces-1)
        print(str1)