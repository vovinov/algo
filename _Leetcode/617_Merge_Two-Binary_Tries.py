from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


a1 = TreeNode(1)
b1 = TreeNode(3)
c1 = TreeNode(2)
d1 = TreeNode(5)

a1.left = b1
a1.right = c1
b1.left = d1

a2 = TreeNode(2)
b2 = TreeNode(1)
c2 = TreeNode(3)
d2 = TreeNode(4)
e2 = TreeNode(7)

a2.left = b2
a2.right = c2
b2.right = d2
c2.right = e2


def mergeTrees(root1, root2):

    if not root1:
        return root2
    if not root2:
        return root1

    root1.val += root2.val

    root1.left = mergeTrees(root1.left, root2.left)
    root1.right = mergeTrees(root1.right, root2.right)

    return root1


print(mergeTrees(a1, a2))
# print(mergeTrees([1], [1, 2]))
