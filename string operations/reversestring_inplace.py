"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1)
 extra memory.

You may assume all the characters consist of printable ascii characters.
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i1 = 0
        i2 = len(s) - 1

        while (i1 < i2):
            i3 = s[i1]
            s[i1] = s[i2]
            s[i2] = i3

            i1 = i1 + 1
            i2 = i2 - 1


