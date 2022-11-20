str=input("Enter Values for List:")
l1=str.split(',')                        # user input

a=0
while a==0:                      # loops the program until the original list is unchanged after the iteration
    l2=list(l1)                  # records list before program begins
    for x in range(len(l1)):
        if x<len(l1)-1:
            first = l1[x]
            second = l1[x+1]
            if first > second:
                l1[x]=second
                l1[x+1]=first   # for each pair of values in list, if first value is greater than second, it swaps the values

    if l1==l2:
        a=1                     # checks if the recorded list is same as the list after the for loop, if not the list
                                # undergoes another iteration and if it is the same, loop is ended
print("List after Bubble Sort:")
print(l1)