# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        """
        val(left)(right)
        only left can have empty? by itself
        if both empty: no parenthesis
        if only right: empty, full
        if only left: left, n/a
        self, left, right
        """

        def trav(node):
            if not node:
                return

            res = f"{node.val}"
            l = trav(node.left)
            r = trav(node.right)
            if l and r:
                res += f"({l})" + f"({r})"
            elif l and not r:
                res += f"({l})"
            elif r and not l:
                res += "()" + f"({r})"

            return res

        return trav(root)
