def merge_the_tools(string, k):
    l1=[]
    l2=[]
    for i in range(int(len(string)/k)):
        l1.append(string[i*k:(i+1)*k])
    for i in l1:
        temp=''
        for j in i:
            if j not in temp:
                temp+=j
        l2.append(temp)
    for i in l2:
        print(i)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)