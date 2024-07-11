"""
iven the root of a binary tree, return the postorder
traversal of its nodes' values.
"""


def postorderTraversal():

    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    # [1, null, 2, 3]

    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)

    a.right = b
    b.left = c

    res = []

    def helper(node):

        if node:
            helper(node.left)
            helper(node.right)
            res.append(node.val)

    helper(a)

    return res


print(postorderTraversal())
