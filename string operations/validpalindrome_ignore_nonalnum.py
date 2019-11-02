"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        li = []
        for q in s:
            if q.isalnum():
                if q.isalpha():
                    li.append(q.lower())
                else:
                    li.append(q)

        i1 = 0
        i2 = len(li) - 1

        while (i1 < i2):
            if li[i1] != li[i2]:
                return False

            i1 = i1 + 1
            i2 = i2 - 1

        return True



