class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node = Node('root', Node('left', Node('left.left')), Node('right'))
b=''
def ser(x):
    global b
    b+=x.val+' '
    if x.left!=None and x.right!=None:
        ser(x.left)
        ser(x.right)
    elif x.left==None and x.right!=None:
        b+='# '
        ser(x.right)
    elif x.left!=None and x.right==None:
        ser(x.left)
        b+='# '
    else:
        b+='# # '

c='root left left.left # # right # root #'
def deser(data):
    global obj
    l1=data.split()
    obj=Node(l1[0])
    l1.pop(0)

    def recur(x):
        if len(l1):
            value = l1[0]
            l1.pop(0)
            if value == '#':
                pass
            else:
                x = Node(value)
                print(x.val)
                recur(x.left)
                recur(x.right)
    recur(obj)


deser(c)
ser(obj)
print(b)






