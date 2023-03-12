# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getLen(node):
            if not node:
                return 0

            left = getLen(node.left)
            right = getLen(node.right)

            self.res = max(self.res, left + right)

            return max(left, right) + 1

        getLen(root)
        return self.res
