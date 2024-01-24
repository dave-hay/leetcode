# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
palindrome
count freqencies
can have:
    - one or zero odd freqency count
    - remaining counts have to be even
---
recursive function
array dict to store frequency
when end reached check that 0 or 1 odd freqency
Time O(N):
    - Will need to check N nodes,
    - check function takes 9 so O(1)
Space (H):
    - call stack H will be height, for left leaning tree will be N
    - array will be O(1) space
"""


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def paths(node, counts):
            if not node:
                return 0

            counts[node.val - 1] += 1
            # check leaf nodes
            # check if freq passes
            res = 0
            if not node.left and not node.right:
                odds = 0
                for freq in counts:
                    odds += freq % 2
                res = 1 if odds < 2 else 0
            else:
                res = paths(node.left, counts) + paths(node.right, counts)

            # add to counts
            counts[node.val - 1] -= 1
            return res

        counts = [0 for _ in range(9)]
        return paths(root, counts)
