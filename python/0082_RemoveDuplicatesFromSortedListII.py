# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(-1)
        dummy.next = cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur and cur.next and cur.val == cur.next.val:
                    cur = cur.next
                cur = cur.next
                prev.next = cur
            else:
                prev = prev.next
                cur = cur.next

        return dummy.next
