# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.root = ListNode()  # will return self.root.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        # we'll set one list to be the 'head'

        while len(lists) > 1:
            mergedList = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedList.append(self.mergeList(l1, l2))
            lists = mergedList

        return lists[0]

    def mergeList(self, a, b):
        res = ListNode()
        node = res

        while a and b:
            aVal = a.val
            bVal = b.val

            if aVal > bVal:
                # cur takes space
                node.next = b
                b = b.next
            else:
                node.next = a
                a = a.next
            node = node.next

        while b:
            node.next = b
            b = b.next
            node = node.next
        while a:
            node.next = a
            a = a.next
            node = node.next

        return res.next
