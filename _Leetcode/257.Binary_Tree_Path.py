class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(5)

a.left = b
a.right = c
b.right = d

# ["1->2->5","1->3"]


def binaryTreePaths(root):
    paths = []

    def dfs(root, path):

        path += str(root.val) + "->"

        if not root.left and not root.right:
            paths.append(path[:-2])

        if root.left:
            dfs(root.left, path)
        if root.right:
            dfs(root.right, path)

    dfs(a, "")

    return paths


print(binaryTreePaths(a))
