from random import randint


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.vals = []
        while head:
            self.vals.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        indx = randint(0, len(self.vals) - 1)
        return self.vals[indx]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
