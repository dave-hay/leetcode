# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Time Complexity: O(n + m)
        Have to visit every node from each list
    Space Complexity: O(1)
        creating one new ListNode then redirecting pointers
    """

    def mergeTwoLists(self, list1, list2):
        base = ListNode()
        head = base

        # if both valid
        while list1 and list2:
            # compare vals
            v1 = list1.val
            v2 = list2.val

            if v1 > v2:
                head.next = list2
                list2 = list2.next
            else:
                head.next = list1
                list1 = list1.next

            head = head.next

        # only list1 valid
        while list1:
            head.next = list1
            list1 = list1.next
            head = head.next

        # only list2 valid
        while list2:
            head.next = list2
            list2 = list2.next
            head = head.next

        return base.next
