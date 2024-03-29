"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        if not root:
            return True
        else:
            return checkvalidity(root, -4294967296, 4294967296)


def checkvalidity(root, mini, maxi) -> bool:
    if not root:
        return True
    if (root.val < mini or root.val > maxi):
        return False

    return ((checkvalidity(root.left, mini, root.val - 1)) and (checkvalidity(root.right, root.val + 1, maxi)))


