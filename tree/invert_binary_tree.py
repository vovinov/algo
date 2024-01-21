class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a = Node(4)
b = Node(2)
c = Node(7)
d = Node(1)
e = Node(3)
f = Node(6)
h = Node(9)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = h


def invert_tree(root):
    if not root:
        return None

    root.left, root.right = root.right, root.left

    invert_tree(root.left)
    invert_tree(root.right)

    return root


print(invert_tree(a))