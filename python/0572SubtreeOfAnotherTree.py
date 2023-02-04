# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # the ends have to be the same
        if not subRoot:
            return True
        if not root:
            return False

        if self.compare(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def compare(self, rt, srt):
        if not rt and not srt:
            return True
        if rt and srt and rt.val == srt.val:
            return self.compare(rt.left, srt.left) and self.compare(rt.right, srt.right)
        return False
