stat= 'THE DAY IS A'
invaly="INVALID YEAR. PLEASE PROVIDE VALID YEAR"
invalm="INVALID MONTH.PLEASE PROVIDE VALID MONTH"
invald="INVALID DATE. PLEASE PROVIDE VALID DATE"
print('DAY CALCULATOR')
print('PLEASE PROVIDE DATE WITHIN 31/12/9999')
print('ENTER DESIRED DATE')
k=int(input('DATE OF THE MONTH: '))
if k>31 or k<1:
    print(invald)
else:
    m=int(input('MONTH: '))
    if m<1 or m>12:
        print(invalm)
    else:
        y=input('YEAR: ')
        if len(y)>4:
            print("PLEASE PROVIDE YEAR WITHIN 0-9999")
        elif int(y)<1 :
            print(invaly)
        elif m==2 and int(y)%4==0 and k>29:
            print(invald)
        elif int(y)%4>0 and m==2 and k>28:
            print(invald)
        elif m==4 and k>30 or m==6 and k>30 or m==9 and k>30 or m==11 and k>30:
            print(invald)
        else:
            list=list()
            for ch in y:
                val=int(ch)
                list.append(val)
            C=10*list[0]+list[1]
            D=10*list[2]+list[3]
            if m>2:
                m=m-2
            else:
                m=m+10
            if m>10:
                (D)=(D-1)
            f=k+((13*m-1)//5)+D+(D//4)+(C//4)-2*C
            if f>=7 or f<0:
                f=(f%7)
            if f==0:
                print(stat +' SUNDAY')
            if f==1:
                print(stat +' MONDAY')
            if f==2:
                print(stat +' TUESDAY')
            if f==3:
                print(stat +' WEDNESDAY')
            if f==4:
                print(stat +' THURSDAY')
            if f==5:
                print(stat +' FRIDAY')
            if f==6:
                print(stat +' SATURDAY')
        
   

