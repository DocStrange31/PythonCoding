import random

num=int(input('Enter Number of Characters:'))
str1='abcdefghijklmnopqrstuvwxyz'
str2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
str3='1234567890'
str4='!@#$%^&*()_'
ch=[1,2,3,4]
pwd=''
while len(pwd)<num:
    k=random.choice(ch)
    if k==1:
        pwd+=random.choice(str1)
    elif k==2:
        pwd += random.choice(str2)
    elif k==3:
        pwd += random.choice(str3)
    else:
        pwd += random.choice(str4)
print('Your Randomly Generated Password is:')
print(pwd)