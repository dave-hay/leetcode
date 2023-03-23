# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
    1
 2     3
n n  4   5
    n n n n

serialize = 1,2,n,n,3,4,n,n,5,n,n
"""


class Codec:
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        preorder traversal
        """

        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0

        def dfs():
            # base case
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1  # move to next
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
