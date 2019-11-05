"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(0, len(nums) - 1):
            temp = nums[i]
            q = target - nums[i]
            nums.remove(nums[i])
            if q in nums:
                ans.append(i)
                ans.append(nums.index(q) + 1)
                break
            else:
                nums.insert(i, temp)

        return ans
