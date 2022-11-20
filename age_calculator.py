import datetime

invaly="INVALID YEAR. PLEASE PROVIDE VALID YEAR"
invalm="INVALID MONTH.PLEASE PROVIDE VALID MONTH"
invald="INVALID DATE. PLEASE PROVIDE VALID DATE"
invalhr="INVALID HOUR INPUT. PLEASE PROVIDE VALID HOUR OF THE DAY IN 24 HOUR FORMAT"
invalmin="INVALID MINUTE. PLEASE PROVIDE VALID MINUTE INPUT WITHIN 60"
d=int(input("Enter Required Date:"))
if d>31 or d<1:
    print(invald)
else:
    mon=int(input("Enter Required Month:"))
    if mon<1 or mon>12:
        print(invalm)
    else:
        y=int(input("Enter Required Year:"))
        if y<1 :
            print(invaly)
        elif mon==2 and y%4==0 and k>29:
            print(invald)
        elif y%4>0 and mon==2 and k>28:
            print(invald)
        elif mon==4 and k>30 or mon==6 and k>30 or mon==9 and k>30 or mon==11 and k>30:
            print(invald)
        else:
            h = int(input("Enter Hour of Required Time:"))
            if h>24 or h<0:
                print(invalhr)
            else:
                m = int(input("Enter Minute of Required Time:"))
                if m>60 or m<0:
                    print(invalmin)                         #ALL ABOVE LINES OF CODE ARE TO VERIFY IF THE DATE IS VALID
                else:
                    ts = (datetime.datetime.now() - datetime.datetime(y, mon, d, h, m,0)).total_seconds()
                                                                                         # total between now and given date calculated in seconds

                    totmin = (ts // 60)  # total time in minutes excluding remainder seconds
                    tothr = (totmin // 60)  # total time in hours excluding remainder minutes
                    totd = (tothr // 24)  # total time in days excluding remainder hours
                    toty = int(totd // 365)  # total time in years excluding remainder days
                    remd = int(totd % 365)  # Extra days
                    remhr = int(tothr % 24)  # Extra Hours
                    remmin = int(totmin % 60)  # Extra Minutes
                    remsec = int(ts % 60)  # Extra Seconds

                    print("Your Age as of now is :", toty, "Years,", remd, "Days,", remhr, "Hours,", remmin,
                          "Minutes and", remsec, "Seconds")

