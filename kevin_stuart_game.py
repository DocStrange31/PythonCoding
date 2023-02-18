def minion_game(string):
    # your code goes here
    stlen=0
    vow='AEIOU'
    kevin={}
    stuart={}
    while stlen<len(string):
        for i in range(len(string)):
            if i+stlen+1<=len(string):
                if (string[i:i+stlen+1])[0] in vow:
                    if string[i:i+stlen+1] in kevin:
                        kevin[string[i:i+stlen+1]]+=1
                    else:
                        kevin[string[i:i+stlen+1]]=1
                else:
                    if (string[i:i+stlen+1]) in stuart:
                        stuart[string[i:i+stlen+1]]+=1
                    else:
                        stuart[string[i:i+stlen+1]]=1
        stlen+=1
    l1=list(stuart.values())
    l2=list(kevin.values())
    stuscore=0
    kevscore=0
    for i in l1:
        stuscore+=i
    for i in l2:
        kevscore+=i
    if stuscore>kevscore:
        print('Stuart '+str(stuscore))
    elif kevscore>stuscore:
        print('Kevin '+str(kevscore))
    else:
        print('Draw')
if __name__ == '__main__':
    s = input()
    minion_game(s)