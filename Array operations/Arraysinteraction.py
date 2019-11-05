"""
Given two arrays, write a function to compute their intersection.
"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        ans = []

        for i in nums1:
            if i in nums2:
                nums2.remove(i)
                ans.append(i)

        return ans