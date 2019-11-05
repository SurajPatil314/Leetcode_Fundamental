from collections import deque

"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        dq = deque(nums)
        lenn = len(nums)
        k %= lenn
        for i in range(k):
            last = dq.pop()
            dq.appendleft(last)

        for idx, n in enumerate(dq):
            nums[idx] = n