"""
Reverse a singly linked list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        temp = []
        temp5 = head
        while (head != None):
            temp.append(head.val)
            head = head.next

        i = 0
        print(len(temp))

        if len(temp) == 0:
            return None
        temp8 = temp5
        while (len(temp) > 0):
            print("qq")
            temp8.next = ListNode(temp.pop())
            temp8 = temp8.next

        return temp5.next

