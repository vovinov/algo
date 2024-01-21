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


def max_depth(root):
    if not root:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return 1 + max(left_depth, right_depth)


print(max_depth(a))



