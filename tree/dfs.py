class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f


def dfs(root):
    if root is None:
        return []

    stack = [root]
    elems = []
    while stack:
        current = stack.pop()
        elems.append(current.val)

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return elems




print(dfs(a))