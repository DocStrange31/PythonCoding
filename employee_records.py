opt=int(input('Please Choose Required Action: \nPress 1 for Employee Registration\nPress 2 for Employee Search\nPress 3 to Erase all Employee Records\n'))
empa=open('employee.txt','a')
empr=open('employee.txt','r')
rownum=0
for line in empr:
    rownum+=1
if opt==1:
    l1=[]
    l1.append('EMP'+str(rownum+1))
    l1.append(input('Enter Employee Name: '))
    l1.append(input('Enter Employee Designation: '))
    l1.append(float(input('Enter Salary: ')))
    l1.append(input('Enter Employee Address: '))
    l1.append(input('Enter Employee Email ID: '))
    l1.append(int(input('Enter Employee Mobile Number: ')))
    l1.append(int(input('Enter Emergency Contact Number: ')))
    l1.append(input("Enter Employee's Parents' Name: "))
    l1.append(int(input("Enter Employee Parents' Mobile Number: ")))
    temp=str(l1)
    temp=temp.replace(',',' ').replace('[','').replace(']','').replace("'", "")
    if rownum>0:
        empa.write("\n"+temp)
    else:
        empa.write(temp)
    empa.close()
    print('\nUnique Employee ID for Registered Employee: EMP'+str(rownum+1))
elif opt==2:
    empid=input("Enter Employee ID: ")
    s=open('employee.txt','r')
    for line in s:
        if empid in line:
            l1=line.split()
            print('Employee ID: '+l1[0])
            print('Employee Name: '+l1[1])
            print('Employee Designation: '+l1[2])
            print('Salary: '+l1[3])
            print('Employee Address: '+l1[4])
            print('Employee Email ID: '+l1[5])
            print('Employee Mobile Number: '+l1[6])
            print('Emergency Contact Number: '+l1[7])
            print("Employee's Parental Name: "+l1[8])
            print("Employee Parents' Mobile Number: "+l1[9])
elif opt==3:
    d=open('employee.txt','w')
    d.write('')
    print('All Employee Records have been Erased')
