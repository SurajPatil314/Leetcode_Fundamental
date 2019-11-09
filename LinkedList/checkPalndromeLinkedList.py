"""
Given a singly linked list, determine if it is a palindrome.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        temp2 = head3
        temp = []
        i = 0
        while (temp2 != None):
            temp.append(temp2.val)
            temp2 = temp2.next

        print(temp)

        if len(temp) < 2:
            return True

        r = q = int(len(temp) / 2)
        if len(temp) % 2 == 1:
            while (q > 0):
                if (temp[q - 1] != temp[r + 1]):
                    return False
                q = q - 1
                r = r + 1
        else:
            print(q)
            while (q > 0):
                if (temp[q - 1] != temp[r]):
                    return False
                q = q - 1
                r = r + 1

        return True