# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # BFS
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                res.append(level)
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []

    # Recursive DFS
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def trav(node, lvl):
            if not node:
                return

            # need to create new array
            if len(self.res) == lvl:
                self.res.append([node.val])
            else:
                self.res[lvl].append(node.val)
            trav(node.left, lvl + 1)
            trav(node.right, lvl + 1)

        trav(root, 0)
        return self.res
