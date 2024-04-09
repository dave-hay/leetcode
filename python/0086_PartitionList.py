# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_greater = ListNode()
        dummy_less = ListNode()

        g = dummy_greater
        l = dummy_less
        node = head

        while node:
            tmp = node.next
            node.next = None
            if node.val < x:
                l.next = node
                l = l.next
            else:
                g.next = node
                g = g.next

            node = tmp

        l.next = dummy_greater.next

        return dummy_less.next
