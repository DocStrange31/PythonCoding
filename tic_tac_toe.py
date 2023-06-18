game=[[0,0,0],
      [0,0,0],
      [0,0,0]]

def checkhorizontal(game):
    check=0
    for row in game:
        if row[0] and row[1] and row[2] and row[0]==row[1] and row[1]==row[2]:
            check=row[0]
            return check
    return check

def checkvertical(game):
    check=0
    for i in range(3):
        temp=game[0][i]
        for j in range(3):
            if game[j][i] and game[j][i]==temp:
                check=temp
            else:
                check=0
                break
        if check>0:
            break
    return check

def checkdiagonal(game):
    check1=1
    check2=1
    temp1 = game[0][0]
    temp2 = game[0][2]
    for i in range(3):
        if check1==0:
            break
        for j in range(3):
            if i == j:
                if game[i][j] == temp1:
                    check1 = temp1
                else:
                    check1=0
                    break
    for i in range(3):
        if check2==0:
            break
        for j in range(3):
            if i+j== 2:
                if game[i][j] == temp2:
                    check2 = temp2
                else:
                    check2=0
                    break
    if check1>check2:
        check=check1
    elif check1<check2:
        check=check2
    else:
        check=check1
    return check

def checkwin(game):
    x=checkvertical(game)
    y=checkhorizontal(game)
    z=checkdiagonal(game)
    if x==1 or y==1 or z==1:
        return 1
    elif x==2 or y==2 or z==2:
        return 2
    else:
        return 0

def checkdraw(game):
    check=1
    for i in range(3):
        for j in range(3):
            if game[i][j]==0:
                check=0
                return check
    return check

def printgame(game):
    for i in range(3):
        for j in range(3):
            if game[i][j]==1:
                print("o ",end="")
            elif game[i][j]==2:
                print("x ",end="")
            elif game[i][j]==0:
                print("  ",end="")
            if j==2:
                continue
            print('|',end="")
        if i==2:
            continue
        print("\n--+--+--")
    return

count=0
while(1):
    count+=1
    k=count%2
    printgame(game)
    if k==0:
        print("\no",end="")
    else:
        print("\nx",end="")
    print("'s Turn. Enter Position (1-9).")
    x=int(input())-1
    if x>8:
        print("Please Enter Number between 1 and 9")
        count-=1
        continue
    elif x<0:
        print("Please Enter Number between 1 and 9")
        count -= 1
        continue
    y=x//3
    z=x%3
    if k==0:
        if game[y][z]==0:
            game[y][z]=1
        else:
            print(f"Position {x+1} is already filled")
            count-=1
            continue
    else:
        if game[y][z]==0:
            game[y][z]=2
        else:
            print(f"Position {x+1} is already filled")
            count-=1
            continue
    if checkwin(game) > 0 or checkdraw(game) > 0:
        break
printgame(game)
if checkwin(game)==1:
    print("\no Won")
elif checkwin(game)==2:
    print("\nx Won")
elif checkdraw(game)==1:
    print("\nDraw")