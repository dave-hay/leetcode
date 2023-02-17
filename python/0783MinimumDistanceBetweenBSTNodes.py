# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        inorderNodes = []

        def inorderTraversal(node):
            if not node:
                return

            inorderTraversal(node.left)
            inorderNodes.append(node.val)
            inorderTraversal(node.right)

        inorderTraversal(root)

        minDist = float("inf")
        for i in range(1, len(inorderNodes)):
            minDist = min(minDist, inorderNodes[i] - inorderNodes[i - 1])
        return minDist
