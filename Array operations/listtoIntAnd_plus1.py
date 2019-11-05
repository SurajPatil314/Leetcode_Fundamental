"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array
contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans1 = 0
        p = len(digits) - 1
        for i in digits:
            ans1 = ans1 + i * 10 ** p
            p = p - 1

        print(ans1)

        ans1 = ans1 + 1
        ans2 = str(ans1)

        ans3 = []

        for i1 in ans2:
            ans3.append(str(i1))

        return ans3

