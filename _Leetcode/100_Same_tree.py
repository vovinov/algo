#  Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


a1 = TreeNode(1)
b1 = TreeNode(2)
a2 = TreeNode(1)
b2 = TreeNode(2)

a1.left = b1
a2.right = b2


def isSameTree(p, q):

    if not p and not q:
        return True

    if not p or not q:
        return False

    return (
        p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    )


print(isSameTree(a1, a2))
