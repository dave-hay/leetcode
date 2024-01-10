# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_distance = 0

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def traverse(node, start):
            d = 0

            if node is None:
                return d

            l = traverse(node.left, start)
            r = traverse(node.right, start)

            if node.val == start:
                self.max_distance = max(l, r)
                d = -1
            elif l >= 0 and r >= 0:
                d = max(l, r) + 1
            else:
                dist = abs(l) + abs(r)
                self.max_distance = max(self.max_distance, dist)
                d = min(l, r) - 1
            return d

        traverse(root, start)
        return self.max_distance
