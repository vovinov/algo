"""
Given the root of a binary tree, check whether
it is a mirror of itself (i.e., symmetric around its center).
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Ex 1
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(2)
d = TreeNode(3)
e = TreeNode(4)
f = TreeNode(4)
g = TreeNode(3)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g


def isSymmetric(root):

    q = deque([root])

    while q:
        level = []
        for _ in range(len(q)):

            cur = q.popleft()

            level.append(cur.val if cur else None)

            if cur:
                q.append(cur.left)
                q.append(cur.right)

        if len(level) > 1:
            n = len(level)

            if level[: n // 2] != level[n // 2 :][::-1]:
                return False

    return True


print(isSymmetric(a))  # [1, 2, 2, 3, 4, 4, 3]
# print(isSymmetric([1, 2, 2, None, 3, None, 3]))
