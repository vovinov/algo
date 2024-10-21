class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)

a.left = b
a.right = c
c.left = d
c.right = e


def sumOfLeftLeaves(root):

    summ = 0

    stack = [(root, None)]

    while stack:

        cur, is_left = stack.pop()

        if not cur.left and not cur.right and is_left:
            summ += cur.val

        if cur.left:
            stack.append((cur.left, 1))  # type: ignore
        if cur.right:
            stack.append((cur.right, 0))  # type: ignore

    return summ


print(sumOfLeftLeaves(a))
