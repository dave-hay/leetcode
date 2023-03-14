# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def path_sum(node) -> int:
            if not node:
                return 0

            left = path_sum(node.left)
            right = path_sum(node.right)

            curVal = node.val

            # can only add left and right if it is the root
            if left < 0 and right < 0:
                self.res = max(self.res, curVal)
                return curVal
            if left < 0:
                self.res = max(self.res, curVal + right)
                return node.val + right
            if right < 0:
                self.res = max(self.res, curVal + left)
                return node.val + left

            # so we have left and right
            # do both branches
            self.res = max(self.res, curVal + left + right)

            if left > right:
                return curVal + left
            else:
                return curVal + right

        path_sum(root)
        return self.res


# cleaner solution
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = [root.val]

        # return max path sum without split
        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute max path sum WITH split
            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]
