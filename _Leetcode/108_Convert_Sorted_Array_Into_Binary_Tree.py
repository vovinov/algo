class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums):

    def helper(l, r):

        if l <= r:

            mid = (l + r) // 2

            node = TreeNode(nums[mid])

            node.left = helper(l, mid - 1)
            node.right = helper(mid + 1, r)

            return node

    return helper(0, len(nums) - 1)


elems = []


def dfs(node):

    if not node:
        return

    elems.append(node.val)

    if node.left:
        dfs(node.left)

    if node.right:
        dfs(node.right)

    return elems


print(dfs(sortedArrayToBST([-10, -3, 0, 5, 9])))
