from collections import deque

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


def bfs(root):
    if root is None:
        return []

    queue = deque([root])
    elems = []
    while queue:
        current = queue.popleft()
        elems.append(current.val)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return elems


print(bfs(a))