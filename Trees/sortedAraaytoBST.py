"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two
subtrees of every node never differ by more than 1.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        if len(nums) == 0:
            return None
        else:
            return constructBST(nums, 0, len(nums) - 1)


def constructBST(nums, mini, maxi) -> TreeNode:
    if mini <= maxi:
        mid = mini + (maxi-mini) // 2
        curr = TreeNode(nums[mid])
        curr.left = constructBST(nums, mini, mid - 1)
        curr.right = constructBST(nums, mid + 1, maxi)

        return curr

