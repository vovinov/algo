
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

res = []


def minDepth(root: Optional[TreeNode]) -> int:
    
    res.append(root.val)
    print(res)

    if not root.left:
        res.append(None)
    else:
        minDepth(root.left)
    
    if not root.right:
        res.append(None)
    else:
        minDepth(root.right)




print(minDepth(a1))

