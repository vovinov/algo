class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)

a1.right = a2
a2.left = a3


def inorderTraversal(root):

    ans = []
    stack = []

    cur = root

    while stack or cur:

        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        ans.append(cur.val)
        cur = cur.right

    return ans


print(inorderTraversal(a1))
