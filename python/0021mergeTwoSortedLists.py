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

    def mergeTwoListsEst(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode()
        node = head

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        if list1:
            node.next = list1

        if list2:
            node.next = list2

        return head.next

    def mergeTwoListsEzr(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode()
        node = head

        while node:
            if list1 and list2:
                if list1.val < list2.val:
                    node.next = list1
                    list1 = list1.next
                else:
                    node.next = list2
                    list2 = list2.next
            elif list1:
                node.next = list1
                return head.next
            elif list2:
                node.next = list2
                return head.next

            node = node.next

        return head.next

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
