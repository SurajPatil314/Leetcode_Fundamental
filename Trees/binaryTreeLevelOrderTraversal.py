"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        else:
            a = []
            q1 = []
            q2 = []
            q1.append(root)
            b = []
            while (len(q1) != 0 or len(q2) != 0):
                b = []
                while (len(q1) != 0):
                    root = q1.pop(0)
                    b.append(root.val)
                    if root.left != None:
                        q2.append(root.left)
                    if root.right != None:
                        q2.append(root.right)
                if (len(b) > 0):
                    a.append(b)
                b = []
                while (len(q2) != 0):
                    root = q2.pop(0)
                    b.append(root.val)
                    if root.left != None:
                        q1.append(root.left)
                    if root.right != None:
                        q1.append(root.right)
                if (len(b) > 0):
                    a.append(b)
                b = []

            return a

