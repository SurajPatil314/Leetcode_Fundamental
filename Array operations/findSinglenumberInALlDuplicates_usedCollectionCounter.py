"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        for tuples in Counter(nums).items():
            if tuples[1] == 1:
                return tuples[0]
        return False
