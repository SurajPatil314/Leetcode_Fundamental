"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).sss
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if not root:
            return True
        else:
            return checksymmetry(root.left, root.right)


def checksymmetry(rleft, rright) -> bool:
    if (rleft == None and rright == None):
        return True
    elif (rleft != None and rright != None):
        return (rleft.val == rright.val and checksymmetry(rleft.left, rright.right) and checksymmetry(rleft.right,
                                                                                                      rright.left))
    else:
        return False
