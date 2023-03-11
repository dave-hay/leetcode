# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Recursion + Conversion to Array
    time: O(n)  - build list +
    space: O(n) - list of vals n + list(log2 n)
    """

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return

        def buildTree(root, nums):
            if not root or not nums:
                return

            # if started with empty add it's own value? which is the half point
            mid = len(nums) // 2

            root.val = nums[mid]

            # make left and right children
            # check if any left values?
            root.left = buildTree(TreeNode(), nums[:mid])
            root.right = buildTree(TreeNode(), nums[mid + 1 :])

            return root

        # find middle
        ll = []
        node = head
        while node:
            ll.append(node.val)
            node = node.next

        res = buildTree(TreeNode(), ll)
        return res
