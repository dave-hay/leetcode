# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        dummy = ListNode(0, list1)
        node = dummy

        l1First = l1Last = None

        i = -1
        while node:
            if i == a - 1:
                l1First = node
            if i == b + 1:
                l1Last = node
            node = node.next
            i += 1

        l2Start = list2
        l2End = None

        l2 = list2

        while l2:
            if not l2.next:
                l2End = l2
            l2 = l2.next

        l1First.next = l2Start
        l2End.next = l1Last

        return dummy.next
