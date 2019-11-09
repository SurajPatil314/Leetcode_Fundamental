"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together
 the nodes of the first two lists.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = []
        temp1 = l1
        temp2 = l2

        i1 = 0
        i2 = 0
        while (temp1 != None):
            i1 = 1
            temp.append(temp1.val)
            temp1 = temp1.next

        while (temp2 != None):
            i2 = 1
            temp.append(temp2.val)
            temp2 = temp2.next

        temp.sort()

        if i1 == 1:
            temp3 = l1
        else:
            temp3 = l2
        print(temp)

        temp4 = temp3

        if len(temp) == 0:
            return None
        for i in temp:
            temp3.next = ListNode(i)
            temp3 = temp3.next

        return temp4.next