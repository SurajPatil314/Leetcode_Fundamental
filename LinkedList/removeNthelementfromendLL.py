"""
Given a linked list, remove the n-th node from the end of list and return its head.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        temp = head
        i = 0
        while (temp != None):
            temp = temp.next
            i = i + 1

        i = i - n
        i1 = 0
        temp = head

        if i == 0:
            head = head.next
            return head
        else:

            if n == 1:
                while (temp.next.next != None):
                    temp = temp.next

                temp.next = None
                return head

            while (i1 < i):
                temp = temp.next
                print(temp.val)
                i1 = i1 + 1

            temp.val = temp.next.val
            temp.next = temp.next.next

            return head