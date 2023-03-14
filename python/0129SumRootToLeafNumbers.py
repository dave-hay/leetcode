# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    """
    intuitive
        dfs(num), append self move down, if end add to total
    haxor
        res[lvl] = cur * number of children
    """

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, val) -> int:
            if not node:
                return 0
            # dont count twice if no l or r
            val += str(node.val)
            if node and not node.left and not node.right:
                return int(val)
            left, right = 0, 0

            if node.right:
                right = dfs(node.right, val)
            if node.left:
                left = dfs(node.left, val)

            return left + right

        return dfs(root, "")
