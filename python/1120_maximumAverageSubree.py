# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        res = float("-inf")

        def trav(node, values, count):
            nonlocal res
            if not node:
                return (0, 0)

            l_val, l_count = trav(node.left, values + node.val, count + 1)
            r_val, r_count = trav(node.right, values + node.val, count + 1)

            total_vals = node.val + l_val + r_val
            total_count = l_count + r_count + 1

            res = max((total_vals / total_count), res)

            return (total_vals, total_count)

        trav(root, 0, 0)

        return res
