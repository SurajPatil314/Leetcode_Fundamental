""""""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0

        depth = depthtree(root)

        return depth


def depthtree(root) -> int:
    if root == None:
        return 0
    else:
        ldepth = depthtree(root.left)
        rdepth = depthtree(root.right)

        if ldepth > rdepth:
            return ldepth + 1
        else:
            return rdepth + 1

