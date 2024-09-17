from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


a1 = TreeNode(3)
b1 = TreeNode(9)
c1 = TreeNode(20)
d1 = TreeNode(15)
e1 = TreeNode(7)

a1.left = b1
a1.right = c1
c1.left = d1
c1.right = e1


def minDepth(root):

    if not root:
        return 0

    q = deque([(root, 1)])

    while q:

        cur, depth = q.popleft()

        if not cur.left and not cur.right:
            return depth

        if cur.left:
            q.append((cur.left, depth + 1))

        if cur.right:
            q.append((cur.left, depth + 1))


print(minDepth(a1))
