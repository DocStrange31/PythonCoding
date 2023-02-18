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
        b+='# '

def deser(data):
    l1=data.split()
    it = iter(l1)

    def recur():
        value = next(it)
        if value == '#':
            return None
        else:
            return Node(value, recur(), recur())
    return recur()

ser(node)
print(b)
s=deser(b)
print(s.left.val)




