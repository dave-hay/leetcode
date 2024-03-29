# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dive(node):
            if not node:
                return 0
            l = dive(node.left)
            r = dive(node.right)

            return max(l, r) + 1

        return dive(root)
