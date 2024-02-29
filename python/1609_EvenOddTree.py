from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        lvl = 0

        while q:
            prv = None
            isEven = lvl % 2 == 0

            for _ in range(len(q)):
                node = q.popleft()
                curVal = node.val

                if isEven and curVal % 2 == 0 or not isEven and curVal % 2 == 1:
                    return False

                if prv:
                    # check the prev value rules
                    if isEven and curVal <= prv or not isEven and curVal >= prv:
                        return False

                prv = curVal

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            lvl += 1

        return True
