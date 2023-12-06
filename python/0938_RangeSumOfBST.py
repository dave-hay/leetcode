# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
N is the number of nodes in the tree.

Time Complexity: O(N)
Space Complexity: O(N), required for the stack

"""


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def trav(node):
            if not node:
                return 0

            total = 0
            val = node.val

            if val <= high and val >= low:
                total += val
            if val > low:
                total += trav(node.left)
            if val < high:
                total += trav(node.right)

            return total

        return trav(root)
