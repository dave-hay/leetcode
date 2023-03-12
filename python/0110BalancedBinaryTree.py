# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    dfs left and right
    """

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node, height):
            # once at bottom get it's height
            if not node:
                return height

            # each call inc height
            height += 1
            left = dfs(node.left, height)
            right = dfs(node.right, height)

            # if either have returned False, return False
            if not left or not right:
                return False

            # if eithers height diff greater than 1, return False
            if abs(left - right) > 1:
                return False

            # if ok return max height
            return max(left, right)

        return bool(dfs(root, 0))
