from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        # if even lvl r->l if odd l->r
        def zz(node, lvl):
            if not node:
                return
            if len(res) == lvl:
                d = deque()
                d.append(node.val)
                res.append(d)
            elif lvl % 2 == 0:
                res[lvl].append(node.val)
            else:
                res[lvl].appendleft(node.val)

            nxtLvl = lvl + 1
            zz(node.left, nxtLvl)
            zz(node.right, nxtLvl)

        zz(root, 0)
        return res
