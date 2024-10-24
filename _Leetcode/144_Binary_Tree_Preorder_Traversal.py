def preorderTraversal(root):

    ans = []

    def helper(node):
        if not node:
            return

        ans.append(node.val)

        if node.left:
            helper(node.left)
        if node.right:
            helper(node.right)

    helper(root)

    return ans
