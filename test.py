num=int(input())
for i in range(num):
    inp=input()
    inp1=inp.replace('-','')
    check=1
    for j in inp1:
        if j not in ['1','2','3','4','5','6','7','8','9','0']:
            check=0
            break
    if len(inp1)!=16:
        check=0
    elif inp1[0] not in ['4','5','6']:
        check=0
    elif '-' in inp:
        for j in inp.split('-'):
            if len(j)!=4:
                check=0
                break
    for j in range(len(inp1)-3):
        if inp1[j]==inp1[j+1] and inp1[j]==inp1[j+2] and inp1[j]==inp1[j+3]:
            check=0
            break
    if check==1:
        print('Valid')
    else: print('Invalid')