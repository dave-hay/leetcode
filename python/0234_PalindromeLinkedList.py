# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True

        dummy = ListNode(0, head)
        slow, fast = dummy.next, dummy.next.next

        # find middle
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        half = slow.next
        slow.next = None

        # reverse
        prev = None

        while half:
            nxt = half.next
            half.next = prev
            prev = half
            half = nxt

        # compare values
        f, s = dummy.next, prev

        while f and s:
            if f.val != s.val:
                return False
            f = f.next
            s = s.next

        return True
