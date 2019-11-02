"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:

        if (len(s) < 1):
            return -1

        if not s:
            return -1

        if len(s) == 1:
            return 0

        ah = {}

        for ch in s:
            if ch in ah:
                ah[ch] = ah[ch] + 1
            else:
                ah[ch] = 1

        for k in ah:
            if ah[k] == 1:
                result = s.find(k)
                return result

        return -1







