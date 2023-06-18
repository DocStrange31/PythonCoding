def permute(s, l, r):
    if l == r:
        print("".join(s))
    else:
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l]  # swap characters
            permute(s, l + 1, r)     # recursive call
            s[l], s[i] = s[i], s[l]  # swap back characters

# Driver code
string = input()
n = len(string) 
s = list(string)
permute(s, 0, n-1) #l=0 ,r=2