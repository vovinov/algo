from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


a = TreeNode(5)
b = TreeNode(4)
c = TreeNode(8)
d = TreeNode(11)
e = TreeNode(13)
f = TreeNode(4)
g = TreeNode(7)
h = TreeNode(2)
i = TreeNode(1)
n = TreeNode()
a.left = b
a.right = c
b.left = d
b.right = n
c.left = e
c.right = f
d.left = g
d.right = h
f.left = n
f.right = i


def bfs(root):
    if root is None:
        return []

    queue = deque([root])
    elems = []
    while queue:
        current = queue.popleft()
        elems.append(current.val)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return elems


print(bfs(a))


def hasPathSum(root, targetSum: int) -> bool:

    def dfs(node, cur_sum):
        if not node:
            return False

        cur_sum += node.val
        if not node.left and not node.right:
            return cur_sum == targetSum

        return dfs(node.left, cur_sum) or dfs(node.right, cur_sum)

    return dfs(root, 0)


# [5,4,8,11,null,13,4,7,2,null,null,null,1] 22
print(hasPathSum(a, 22))
